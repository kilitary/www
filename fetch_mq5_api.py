import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

FUNCTIONS = [
    "initialize",
    "shutdown",
    "version",
    "last_error",
    "account_info",
    "terminal_info",
    "symbols_total",
    "symbols_get",
    "symbol_info",
    "symbol_info_tick",
    "symbol_select",
    "market_book_add",
    "market_book_get",
    "market_book_release",
    "copy_rates_from",
    "copy_rates_from_pos",
    "copy_rates_range",
    "copy_ticks_from",
    "copy_ticks_range",
    "orders_total",
    "orders_get",
    "order_calc_margin",
    "order_calc_profit",
    "order_check",
    "order_send",
    "positions_total",
    "positions_get",
    "history_orders_total",
    "history_orders_get",
    "history_deals_total",
    "history_deals_get",
]

OUTPUT_FILE = Path("mq5_api.md")


def fetch_page(key: str) -> BeautifulSoup:
    url = f"https://www.mql5.com/en/docs/python_metatrader5/mt5{key}_py"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_section(soup: BeautifulSoup, heading: str) -> str:
    # Look for paragraphs with specific classes that contain the heading text
    paragraphs = soup.find_all("p")
    target_paragraph = None

    # Look for the heading in paragraphs with specific classes
    for p in paragraphs:
        if p.get_text(strip=True) == heading:
            target_paragraph = p
            break

    # If not found, try looking for paragraphs with BoldTitles class
    if not target_paragraph:
        for p in paragraphs:
            classes = p.get("class", [])
            if "p_BoldTitles" in classes and heading in p.get_text(strip=True):
                target_paragraph = p
                break

    if not target_paragraph:
        # Try finding any paragraph that contains the heading text
        for p in paragraphs:
            if heading in p.get_text(strip=True):
                target_paragraph = p
                break

    if not target_paragraph:
        return ""

    # Get all content until the next BoldTitles or similar heading
    content = []
    current = target_paragraph

    # Skip the heading itself
    current = current.find_next_sibling()

    while current:
        # Stop if we hit another heading
        if (
            current.name == "p"
            and current.get("class")
            and "p_BoldTitles" in current.get("class", [])
        ):
            break
        # Stop if we hit a heading with specific text
        if current.name == "h2" or current.name == "h3":
            break
        # Add the content
        content.append(str(current))
        current = current.find_next_sibling()

    return "".join(content).strip()


def clean_markdown(section: str) -> str:
    # Parse the section content to extract meaningful text
    soup = BeautifulSoup(section, "html.parser")

    # Extract text from different types of elements
    texts = []
    for element in soup.find_all():
        # Skip empty elements
        if not element.get_text(strip=True):
            continue

        # Handle different element types
        if element.name in ["p", "div", "span", "li", "td", "th", "code"]:
            text = element.get_text(strip=True)
            if text:
                texts.append(text)
        elif element.name in ["br", "hr"]:
            texts.append("\n")
        elif element.name == "table":
            # For tables, extract rows
            rows = element.find_all("tr")
            for row in rows:
                cells = row.find_all(["td", "th"])
                row_text = "  ".join([cell.get_text(strip=True) for cell in cells])
                if row_text:
                    texts.append(row_text)

    # Join texts and clean up extra whitespace
    content = "\n".join(texts)
    # Replace multiple newlines with double newline
    content = re.sub(r"\n\s*\n", "\n\n", content)
    return content.strip()


def process_function(func_name: str) -> str:
    key = func_name.replace("_", "")
    try:
        soup = fetch_page(key)
    except Exception as e:
        return f"## {func_name}\n\n*Failed to fetch documentation: {e}*\n"

    # Extract function description (first paragraph after the heading)
    description = ""
    heading = soup.find("h1")
    if heading:
        next_elem = heading.find_next("p")
        if next_elem:
            description = next_elem.get_text(strip=True)

    # Extract sections
    params = extract_section(soup, "Parameters")
    returns = extract_section(soup, "Return Value")
    example = extract_section(soup, "Example")

    md = [f"## {func_name}"]
    if description:
        md.append(f"\n{description}")

    if params:
        cleaned_params = clean_markdown(params)
        if cleaned_params:
            md.append("\n**Parameters**\n")
            md.append(cleaned_params)

    if returns:
        cleaned_returns = clean_markdown(returns)
        if cleaned_returns:
            md.append("\n**Return Value**\n")
            md.append(cleaned_returns)

    if example:
        cleaned_example = clean_markdown(example)
        if cleaned_example:
            md.append("\n**Example**\n")
            md.append(cleaned_example)

    md.append("\n---\n")
    return "\n".join(md)


def main():
    parts = []
    for fn in FUNCTIONS:
        parts.append(process_function(fn))
    content = "# MetaTrader5 Python API Documentation\n\n" + "\n".join(parts)
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"Wrote documentation for {len(FUNCTIONS)} functions to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
