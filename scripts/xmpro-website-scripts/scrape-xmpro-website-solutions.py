import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# Function to truncate title
def truncate_title(title, max_chars=20):
    return title[:max_chars]

# Function to save content to Markdown file
def save_to_md(title, content, url, folder_path):
    try:
        # Sanitize the title to ensure it's suitable for use as a filename
        sanitized_title = title.strip().replace("&", "").replace("/", "-")
        
        # Truncate the filename to a maximum of 20 characters
        truncated_title = truncate_title(sanitized_title)
        
        # Make the filename lowercase and replace spaces with hyphens
        filename = os.path.join(folder_path, f"{truncated_title.lower().replace(' ', '-')}.md")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(f"URL: {url}\n\n")
            file.write(content)
        print(f"Content saved to {filename}")
        return {'title': title, 'filename': filename}
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

# Function to scrape content from each page
def scrape_page(url, folder_path):
    try:
        # Skip scraping if the URL is excluded
        if url == "https://xmpro.com/solutions-library/solutions/":
            print("Excluded URL. Skipping scraping:", url)
            return None

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

                    # Save content to a Markdown file and return filename with title
                    return save_to_md(title, markdown_content, url, folder_path)
                else:
                    print("Main element not found for URL:", url)
            else:
                print("Title element not found for URL:", url)
        else:
            print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping page {url}: {e}")
    return None


def update_readme(folder_path, md_files, readme_filename):
    try:
        readme_file = os.path.join(folder_path, readme_filename)

        with open(readme_file, 'w', encoding='utf-8') as file:
            file.write("# Copy Me Solutions\n\n")
            for md_file in md_files:
                relative_path = os.path.relpath(md_file['filename'])
                # Replace backslashes with forward slashes
                relative_path = relative_path.replace("\\", "/")
                relative_path = relative_path.replace("docs/", "")
                file.write(f"* [{md_file['title']}]({relative_path})\n")
        print(f"{readme_filename} updated with hyperlinks to exported markdown files.")
    except Exception as e:
        print(f"Error occurred while updating {readme_filename}: {e}")


# Main function
def main():
    # Define the URL
    base_url = "https://xmpro.com"
    url = "https://xmpro.com/solutions-library/"
    
    # Define the path to the config file
    config_file_path = 'scripts\XMPRO Website Scrape Scripts\scrape-xmpro-website-solutions-config.json'

    # Load JSON config file
    with open(config_file_path) as json_file:
        config_data = json.load(json_file)
        folder_path = config_data.get("folderPath")

    os.makedirs(folder_path, exist_ok=True)

    # List to store information about saved markdown files
    md_files = []

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the specified div element
        div_element = soup.find("div", class_="col small-12 large-12", id="col-1436051962")
        
        # Check if the div element exists
        if div_element:
            # Find all hyperlinks (a tags) within the div element
            hyperlinks = div_element.find_all("a")
            
            # Extract and scrape content from each hyperlink
            for hyperlink in hyperlinks:
                href = hyperlink.get("href")
                if href:
                    full_url = urljoin(base_url, href)
                    md_file_info = scrape_page(full_url, folder_path)
                    if md_file_info:
                        md_files.append(md_file_info)
                        print("Scraped content:", md_file_info)
        else:
            print("Specified div element not found for URL:", url)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    # Update or create README.md with hyperlinks to exported markdown files
    if md_files:
        update_readme(folder_path, md_files, "copy-me-solutions.md")
    else:
        print("No markdown files found to update README.md.")

if __name__ == "__main__":
    main()
