import os
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

# Function to truncate title
def truncate_title(title, max_chars=20):
    return title[:max_chars]

def save_to_md(title, content, url, folder_path):
    try:
        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Sanitize the title to ensure it's suitable for use as a filename
        sanitized_title = title.strip().replace("&", "").replace("/", "-")
        
        # Truncate the filename to a maximum of 20 characters
        truncated_title = truncate_title(sanitized_title)
        
        # Make the filename lowercase and replace spaces with hyphens
        filename = os.path.join(folder_path, f"{truncated_title.lower().replace(' ', '-')}.md")

        with open(filename, 'w', encoding='utf-8') as file:
            # Write the title
            file.write(f"# {title}\n\n")
            # Write the URL
            file.write(f"[URL]({url})\n\n")
            # Write the content
            file.write(content)
        print(f"Content saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")
        return None


# Function to create README.md file
def create_readme(folder_path, md_filenames):
    try:
        # Create the directory if it doesn't exist
        Path(folder_path).mkdir(parents=True, exist_ok=True)

        readme_filename = Path(folder_path) / "copy-me.md"
        with open(readme_filename, 'w', encoding='utf-8') as file:
            file.write("# Scraped Content\n\n")
            for filename in md_filenames:
                # Extract relative path
                relative_path = Path(filename).as_posix().replace("docs/", "")
                # Write file path in README format
                file.write(f"* [{Path(filename).stem} - XMPRO]({relative_path})\n")
        print(f"copy-me.md file created successfully at: {readme_filename}")
    except Exception as e:
        print(f"Error occurred while generating copy-me.md: {e}")

# Function to scrape content from a URL
def scrape_page(url, folder_path):
    try:
        # Send a GET request to the page URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find the title of the page
            title_elem = soup.find("title")
            if title_elem:
                title = title_elem.text.strip()

                # Find the main element
                main_element = soup.find("main", id="main")
                
                if main_element:
                    # Find all content elements within the main element
                    content_elements = main_element.find_all(["p", "h1", "h2", "h3", "h4", "img"])

                    # Initialize markdown content
                    markdown_content = ""

                    # Append content to the markdown content preserving order
                    for element in content_elements:
                        if element.name == "img":
                            prop = "src"
                            if "data-src" in element.attrs:
                                prop = "data-src"
                            w = element.get("width")
                            h = element.get("height")
                            markdown_content += f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n'
                        else:
                            if element.name.startswith("h"):
                                heading_level = int(element.name[1])
                                markdown_content += f"{'#' * heading_level} {element.get_text(strip=True)}\n\n"
                            else:
                                markdown_content += f"{element.get_text(strip=True)}\n\n"

                    # Save content to a Markdown file and return filename
                    return save_to_md(title, markdown_content, url, folder_path)  # Pass folder_path argument here
                else:
                    print("Main element not found for URL:", url)
            else:
                print("Title element not found for URL:", url)
        else:
            print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping page {url}: {e}")
    return None


def main():
    # Load folder path from JSON config file
    with open(r'scripts\xmpro-website-scripts\scrape-xmpro-website-solutions-config.json') as json_file:
        config_data = json.load(json_file)
        folder_path = config_data.get("folderPath")

    # Define the URLs to scrape
    urls_to_scrape = [
        "https://xmpro.com/solutions-library/solutions/condition-monitoring/",
        "https://xmpro.com/solutions-library/solutions/predictive-maintenance/"
    ]

    # List to store filenames of saved markdown files
    md_filenames = []

    # Scrape content from each URL
    for url in urls_to_scrape:
        md_filename = scrape_page(url, folder_path)
        if md_filename:
            md_filenames.append(md_filename)
            print("Scraped content from", url)

    # Print the filenames of saved markdown files
    print("Saved Markdown files:")
    for filename in md_filenames:
        print(filename)

    # Create README.md file with file paths of exported markdown files
    create_readme(folder_path, md_filenames)

if __name__ == "__main__":
    main()
