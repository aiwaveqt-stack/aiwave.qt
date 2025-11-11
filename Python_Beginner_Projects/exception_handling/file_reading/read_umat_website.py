"""
Read UMaT Website
Fetches and prints the HTML content of a website.
"""

import urllib.request


def main():
    """Fetch and print the HTML content of the UMaT website."""
    try:
        url = "https://www.umat.edu.gh/"
        with urllib.request.urlopen(url) as response:
            for line in response:
                print(line.decode('utf-8').rstrip())
    except Exception as e:
        print(f"Error fetching website: {e}")


if __name__ == "__main__":
    main()
