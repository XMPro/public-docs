import os
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import time

# Function to save content to Markdown file
def save_to_md(title, content, url, folder_path):
    try:
        sanitized_title = title.strip().replace("&", "").replace("/", "-")
        truncated_title = sanitized_title[:20]
        filename = os.path.join(folder_path, f"{truncated_title.lower().replace(' ', '-')}.md")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(f"[url]({url})\n\n")
            file.write(content)
        print(f"Content saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

# Function to scrape content from each page
def scrape_page(url, folder_path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            title_elem = soup.find("title")
            if title_elem:
                title = title_elem.text.strip()

                portfolio_top_div = soup.find("div", class_="portfolio-top")

                if portfolio_top_div:
                    process_images(portfolio_top_div)
                    content = str(portfolio_top_div)
                    content = content.replace('<div', '\n<div')
                    return {'title': title, 'filename': save_to_md(title, content, url, folder_path)}
                else:
                    print("Portfolio top div not found.")
            else:
                print("Title element not found.")
        else:
            print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping page {url}: {e}")
    return None

# Function to process images in the content
def process_images(content):
    for element in content.find_all():
        if element.name == "img":
            prop = "src"
            if "data-src" in element.attrs:
                prop = "data-src"
            w = element.get("width")
            h = element.get("height")
            if w and h:
                element.replace_with(BeautifulSoup(f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n', 'html.parser'))
            else:
                print(f"Image dimensions missing for {element[prop]}. Skipping...")
        elif element.name == "iframe" and "youtube.com" in element.get("src", ""):
            pass

# Function to update or create README.md with hyperlinks to exported markdown files
def update_readme(folder_path, md_files):
    try:
        readme_file = Path(folder_path) / "copy-me.md"

        # Sort the md_files list by title in alphabetical order
        md_files.sort(key=lambda x: x['title'])

        with open(readme_file, 'w', encoding='utf-8') as file:
            file.write("# Scraped Content\n\n")
            for md_file_info in md_files:
                title = md_file_info['title'].replace(" - XMPRO", "")
                formatted_filename = Path(md_file_info['filename']).as_posix().replace("docs/", "")
                file.write(f"* [{title}]({formatted_filename})\n")
        print("copy-me.md updated with hyperlinks to exported markdown files in alphabetical order.")
    except Exception as e:
        print(f"Error occurred while updating copy-me.md: {e}")

# Main function
def main():
    url = "https://xmpro.com/solutions-library/use-cases/"
    
    config_file_path = (r'scripts\xmpro-website-scripts\scrape-xmpro-website-usecases-config.json')

    with open(config_file_path) as json_file:
        config_data = json.load(json_file)
        folder_path = config_data.get("folderPath")

    os.makedirs(folder_path, exist_ok=True)

    md_files = []

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        content_div = soup.find("div", id="content", class_="page-wrapper")
        if content_div:
            hyperlinks = content_div.find_all("a", href=True)

            for hyperlink in hyperlinks:
                page_url = hyperlink["href"]
                md_file_info = scrape_page(page_url, folder_path)
                if md_file_info:
                    md_files.append(md_file_info)
                    print("Scraped content from", page_url)
                    time.sleep(2)
        else:
            print("Content div not found.")
    else:
        print(f"Failed to retrieve page {url}. Status code: {response.status_code}")

    if md_files:
        update_readme(folder_path, md_files)
    else:
        print("No markdown files found to update README.md.")

if __name__ == "__main__":
    main()
