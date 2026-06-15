import requests


def fetch_raw_page(key: str) -> str:
    url = f"https://www.mql5.com/en/docs/python_metatrader5/mt5{key}_py"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


# Test with initialize function
content = fetch_raw_page("initialize")

# Look for Parameters and Example in the raw content
print("Looking for 'Parameters' in content:")
if "Parameters" in content:
    start = content.find("Parameters")
    print(f"Found 'Parameters' at position {start}")
    print("Context around 'Parameters':")
    print(content[start - 100 : start + 200])
else:
    print("No 'Parameters' found")

print("\n" + "=" * 50 + "\n")

print("Looking for 'Example' in content:")
if "Example" in content:
    start = content.find("Example")
    print(f"Found 'Example' at position {start}")
    print("Context around 'Example':")
    print(content[start - 100 : start + 200])
else:
    print("No 'Example' found")

# Save the raw content to a file for inspection
with open("raw_content.html", "w", encoding="utf-8") as f:
    f.write(content)
print("\nRaw content saved to raw_content.html")
