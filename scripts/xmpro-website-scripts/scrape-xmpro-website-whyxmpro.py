import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
import json

def scrape_page_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all content within the div with id="content" and class="content-area"
        content_div = soup.find('div', id='content', class_='content-area')
        if content_div:
            return content_div
        else:
            print(f"Content not found in {url}")
            return None
    except requests.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while fetching content from {url}: {e}")
        return None

def save_to_md(content, page_title, page_url, folder_path):
    try:
        # Remove special characters from the title
        title = re.sub(r'[^\w\s]', '', page_title)

        # Ensure the title is not empty after removing special characters
        if title.strip():
            # Truncate title to a maximum of 20 characters
            truncated_title = title.strip()[:20]
            # Convert title to lowercase and replace spaces with "-"
            filename = os.path.join(folder_path, f"{truncated_title.lower().replace(' ', '-')}.md")
        else:
            filename = os.path.join(folder_path, "Untitled.md")

        with open(filename, 'w', encoding='utf-8') as file:
            # Write page title as main heading
            file.write(f"# {page_title}\n\n")
            # Write URL under the main heading in the specified format
            file.write(f"URL: [{page_url}]({page_url})\n\n")
            file.write(content)
        print(f"Content saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")
        return None

def create_readme(file_info_list, folder_path):
    try:
        readme_content = "## Exported Files\n\n"
        for file_info in file_info_list:
            file_path = file_info['file_path'].replace('docs/', '')  # Remove "doc/" from file path
            file_path = file_path.replace('\\', '/')  # Replace backslashes with forward slashes
            readme_content += f"* [{file_info['file_name']}]({file_path})\n"
        
        readme_path = os.path.join(folder_path, "copy-me-why-xmpro.md")
        with open(readme_path, 'w', encoding='utf-8') as readme_file:
            readme_file.write(readme_content)
        print(f"README file created at: {readme_path}")
    except Exception as e:
        print(f"Error occurred while creating README file: {e}")

def scrape_why_xmpro_pages():
    base_url = "https://xmpro.com"
    dropdown_url = "https://xmpro.com/why-xmpro/"

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(dropdown_url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Find the dropdown menu items
        dropdown_menu = soup.find('ul', class_='sub-menu')
        if dropdown_menu:
            # Find all links in the dropdown menu
            dropdown_links = dropdown_menu.find_all('a', href=True)
            
            # Load JSON config file
            with open('scripts/XMPRO Website Scrape Scripts/scrape-xmpro-website-whyxmpro-config.json') as json_file:
                config_data = json.load(json_file)
                folder_path = config_data.get("folderPath")
            
            os.makedirs(folder_path, exist_ok=True)

            file_info_list = []

            for link in dropdown_links:
                page_url = urljoin(base_url, link['href'])
                content_div = scrape_page_content(page_url)
                if content_div:
                    page_title = link.text.strip()
                    content_md = ""
                    for element in content_div.find_all(["p", "h1", "h2", "h3", "h4", "img"]):
                        if element.name == "img":
                            prop = "src"
                            if "data-src" in element.attrs:
                                prop = "data-src"
                            w = element.get("width")
                            h = element.get("height")
                            content_md += f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n'
                        else:
                            if element.name.startswith("h"):
                                heading_level = int(element.name[1])
                                content_md += f"{'#' * heading_level} {element.get_text().strip()}\n\n"
                            else:
                                content_md += f"{element.get_text().strip()}\n\n"
                    saved_file_path = save_to_md(content_md, page_title, page_url, folder_path)
                    if saved_file_path:
                        file_info_list.append({"file_name": page_title, "file_path": saved_file_path})
                else:
                    print(f"Failed to scrape the page: {page_url}")
                # Introduce a delay of 1 second before scraping the next page
                sleep(1)
            
            create_readme(file_info_list, folder_path)
        else:
            print("Could not find the dropdown menu")
    except requests.RequestException as e:
        print(f"Failed to retrieve dropdown menu: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Scrape and save pages from the "Why XMPro" dropdown
scrape_why_xmpro_pages()
