import requests
import os
from urllib.parse import urlparse

def fetch_image(url, downloaded_files):
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        headers = {"User-Agent": "Ubuntu-Image-Fetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check important headers
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            print(f"✗ Skipping: {url} (not an image, content-type: {content_type})")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        if filename in downloaded_files:
            print(f"⚠ Duplicate skipped: {filename}")
            return
        downloaded_files.add(filename)

        # Save the image safely
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs
    urls = input("Please enter image URLs (separate with spaces): ").split()

    downloaded_files = set() 

    for url in urls:
        fetch_image(url.strip(), downloaded_files)

    print("\nConnection strengthened. Community enriched.")
    print("Ubuntu: 'A person is a person through other persons.'")

if __name__ == "__main__":
    main()
