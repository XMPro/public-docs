import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
import json
from pathlib import Path


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


def add_unique_title(title, titles_trunc, MAX_CHARS):
    # Truncate title to leave space for suffix if needed
    if len(title) > MAX_CHARS:
        truncated_title = title[:MAX_CHARS-3] + "..."
        if truncated_title in titles_trunc:
            # Append a number to make it unique
            i = 2
            while f"{truncated_title} ({i})" in titles_trunc:
                i += 1
            truncated_title = f"{truncated_title} ({i})"
        titles_trunc.append(truncated_title)
        return truncated_title
    else:
        if title in titles_trunc:
            # Append a number to make it unique
            i = 2
            while f"{title} ({i})" in titles_trunc:
                i += 1
            title = f"{title} ({i})"
        titles_trunc.append(title)
        return title


def save_to_md(content, page_title, page_url, folder_path):
    try:
        titles_trunc = []
        # Remove special characters from the title
        title = re.sub(r'[^\w\s-]', '', page_title)

        # Ensure the title is not empty after removing special characters
        if title.strip():
            # Truncate the title if it's too long
            truncated_title = add_unique_title(
                title.strip(), titles_trunc, MAX_CHARS=20)
            # Convert title to lowercase and replace spaces with "-"
            truncated_title = truncated_title.lower().replace(' ', '-')
            filename = os.path.join(folder_path, f"{truncated_title}.md")
        else:
            filename = os.path.join(folder_path, "Untitled.md")

        # Replace invalid characters in the filename
        filename = filename.replace("\n", "").replace("\xa0", " ")

        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as file:
            # Write the title
            file.write(f"# {page_title}\n\n")
            # Write the URL in the specified format
            file.write(f"[URL]({page_url})\n\n")
            # Write the content
            file.write(content)
        print(f"Content saved to {filename}")
        return truncated_title, filename
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")
        return None, None




def create_readme(file_info_list, folder_path):
    try:
        # Get the folder name
        folder_name = Path(folder_path).name.capitalize().replace("-", " ")
        readme_content = [f"# {folder_name}\n\n"]
        readme_filename = Path(folder_path) / "copy-me.md"
        
        for file_info in file_info_list:
            # Get relative path of the file
            relative_path = Path(file_info['filename']).relative_to(folder_path)
            # Replace backslashes with forward slashes
            relative_path = relative_path.as_posix()
            # Remove "docs/" from the relative path
            relative_path = relative_path.replace("docs/", "")
            # Construct the file path relative to the folder path
            file_path = Path(folder_path) / relative_path
            # Remove "../../docs/" prefix from the file path
            file_path = file_path.relative_to("docs/").as_posix()
            
            name = file_info['title'].title().replace("-", " ")

            readme_content.append(f"* [{name} - XMPRO]({file_path})\n")
        
        with open(readme_filename, 'w', encoding='utf-8') as readme_file:
            readme_file.write("".join(readme_content))
        
        print(f"copy-me.md file created successfully at: {readme_filename}")
   
    except Exception as e:
        print(f"Error occurred while generating copy-me.md: {e}")

def scrape_xmpro_platform_pages(folder_path):
    base_url = "https://xmpro.com/platform/"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(base_url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Find the sub-menu with page URLs
        sub_menu = soup.find('div', class_='sub-menu nav-dropdown')
        if sub_menu:
            # Find all links in the sub-menu
            links = sub_menu.find_all('a', href=True)
            exported_files = []
            for link in links:
                page_url = urljoin(base_url, link['href'])
                content_div = scrape_page_content(page_url)
                if content_div:
                    page_title = link.text.strip()
                    if not page_title:
                        h1_heading = content_div.find('h1')
                        if h1_heading:
                            page_title = h1_heading.get_text(strip=True)
                        else:
                            page_title = "Untitled"
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
                                content_md += f"{'#' * heading_level} {element.get_text(strip=True)}\n\n"
                            else:
                                content_md += f"{element.get_text(strip=True)}\n\n"
                    truncated_title, filename = save_to_md(
                        content_md, page_title, page_url, folder_path)
                    if truncated_title and filename:
                        exported_files.append({'title': truncated_title, 'filename': filename})
                else:
                    print(f"Failed to scrape the page: {page_url}")
                    print(f"Page URL with missing title: {page_url}")  # Print the URL with missing title
                # Introduce a delay of 1 second before scraping the next page
                sleep(1)
            
            # Create README.md file
            create_readme(exported_files, folder_path)
        else:
            print("Could not find the sub-menu")
    except requests.RequestException as e:
        print(f"Failed to retrieve sub-menu: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Define the path to the config file
config_file_path = r'scripts\xmpro-website-scripts\scrape-xmpro-website-platform-config.json'

# Load JSON config file
with open(config_file_path) as json_file:
    config_data = json.load(json_file)
    folder_path = config_data.get("folderPath")

# Scrape and save pages from the "XMPro Platform" submenu
scrape_xmpro_platform_pages(folder_path)
