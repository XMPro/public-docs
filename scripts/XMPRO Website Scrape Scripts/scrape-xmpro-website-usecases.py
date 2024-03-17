import os
import requests
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
import json

# Function to save content to Markdown file
def save_to_md(title, content, url, folder_path):
    try:
        # Sanitize the title to ensure it's suitable for use as a filename
        sanitized_title = sanitize_filename(title.strip().replace("&", ""))
        
        # Truncate the filename to a maximum of 20 characters
        truncated_title = sanitized_title[:20]
        
        # Convert title to lowercase and replace spaces with "-"
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

                # Find the portfolio-inner div
                portfolio_inner_div = soup.find("div", class_="portfolio-inner")

                if portfolio_inner_div:
                    # Find all content elements within the portfolio-inner div
                    content_elements = portfolio_inner_div.find_all(["p", "h1", "h2", "h3", "h4", "img"])

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
                    print("Portfolio inner div not found.")
            else:
                print("Title element not found.")
        else:
            print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping page {url}: {e}")
    return None

# Function to update or create README.md with hyperlinks to exported markdown files
def update_readme(folder_path, md_files, title):
    try:
        readme_file = os.path.join(folder_path, "copy-me-use-cases.md")
        with open(readme_file, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            for md_file in md_files:
                # Get the filename without the folder path
                filename = os.path.basename(md_file['filename'])
                # Get the folder path location without the "docs/" part and replace "\" with "/"
                formatted_filename = md_file['filename'].replace("docs/", "").replace("\\", "/")
                file.write(f"* [{md_file['title']}]({formatted_filename})\n")
        print(f"README.md updated with hyperlinks to exported markdown files.")
    except Exception as e:
        print(f"Error occurred while updating copy-me-use-cases.md: {e}")

# Main function
def main():
    # Define the URL
    url = "https://xmpro.com/solutions-library/use-cases/"
    
    # Define the path to the config file
    config_file_path = 'scripts/XMPRO Website Scrape Scripts/scrape-xmpro-website-usecases-config.json'

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
        
        # Find all page hyperlinks within the specified div
        content_div = soup.find("div", id="content", class_="page-wrapper")
        if content_div:
            hyperlinks = content_div.find_all("a", href=True)

            # Iterate over each hyperlink
            for hyperlink in hyperlinks:
                page_url = hyperlink["href"]
                md_file_info = scrape_page(page_url, folder_path)
                if md_file_info:
                    md_files.append(md_file_info)
        else:
            print("Content div not found.")
    else:
        print(f"Failed to retrieve page {url}. Status code: {response.status_code}")

    # Update or create README.md with hyperlinks to exported markdown files
    if md_files:
        update_readme(folder_path, md_files, "Use-Cases")
    else:
        print("No markdown files found to update README.md.")

if __name__ == "__main__":
    main()
