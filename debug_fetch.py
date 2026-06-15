import requests
from bs4 import BeautifulSoup


def fetch_page(key: str) -> BeautifulSoup:
    url = f"https://www.mql5.com/en/docs/python_metatrader5/mt5{key}_py"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_section(soup: BeautifulSoup, heading: str) -> str:
    # Find all h3 headings with the specified text
    headings = soup.find_all("h3")
    target_heading = None
    for h in headings:
        if h.get_text(strip=True) == heading:
            target_heading = h
            break

    if not target_heading:
        # Try h2 headings as well
        headings = soup.find_all("h2")
        for h in headings:
            if h.get_text(strip=True) == heading:
                target_heading = h
                break

    if not target_heading:
        print(f"Could not find heading: {heading}")
        return ""

    # Get all content until the next heading
    content = []
    for sibling in target_heading.next_siblings:
        if sibling.name in ["h2", "h3"]:
            break
        if sibling.name is not None:  # Skip text nodes that are just whitespace
            content.append(str(sibling))

    result = "".join(content).strip()
    print(f"Found content for {heading}: {result[:100]}...")
    return result


# Test with initialize function
soup = fetch_page("initialize")
print(
    "Page title:",
    soup.find("h1").get_text(strip=True) if soup.find("h1") else "No title",
)

# Check what headings are available
headings = soup.find_all(["h2", "h3"])
print("Available headings:")
for h in headings:
    print(f"  {h.name}: {h.get_text(strip=True)}")

# Try to extract sections
params = extract_section(soup, "Parameters")
example = extract_section(soup, "Example")

print("\nParameters section:")
print(params[:500] if params else "No parameters found")

print("\nExample section:")
print(example[:500] if example else "No example found")
