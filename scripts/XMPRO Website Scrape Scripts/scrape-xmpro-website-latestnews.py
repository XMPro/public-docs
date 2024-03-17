import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
import json

def scrape_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Get title
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text().strip()
        else:
            title = "Untitled"

        # Get paragraph content
        paragraphs = soup.find('div', class_='entry-content').find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs])

        return title, content
    except requests.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error occurred while fetching content from {url}: {e}")
        return None, None

def save_to_md(title, content, url, folder_path):
    try:
        # Ensure the title is not empty
        if title.strip():
            # Truncate title if it's too long
            truncated_title = title[:20]
            # Remove special characters from the title and replace spaces with underscores
            filename = os.path.join(folder_path, f"{re.sub(r'[^\w\s]', '', truncated_title.strip().replace(' ', '_')).lower().replace('_', '-')}.md")
        else:
            filename = os.path.join(folder_path, "Untitled.md")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(f"URL: {url}\n\n")
            file.write(content)
        print(f"Content saved to {filename}")
        return filename
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")
        return None

def get_all_blog_urls(base_url, num_pages):
    all_blog_urls = set()  # Use a set to avoid duplicate URLs
    for page_num in range(1, num_pages+1):
        page_url = f"{base_url}page/{page_num}/"
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            with requests.Session() as session:
                response = session.get(page_url, headers=headers)
                response.raise_for_status()  # Raise an exception for bad status codes
                soup = BeautifulSoup(response.text, 'html.parser')
                # Find the div with class 'large-9 col'
                target_div = soup.find('div', class_='large-9 col')
                if target_div:
                    # Find all anchor tags within the target div
                    for link in target_div.find_all('a', href=True):
                        # Resolve relative URLs to absolute URLs
                        absolute_url = urljoin(base_url, link['href'])
                        all_blog_urls.add(absolute_url)
                else:
                    print(f"Could not find the target div on page {page_num}")
        except requests.RequestException as e:
            print(f"Failed to retrieve content for page {page_num}: {e}")
        except Exception as e:
            print(f"Error occurred: {e}")
        # Introduce a delay of 1 seconds between navigating to a new page
        sleep(1)
    return all_blog_urls

def get_max_page_numbers(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    page_numbers = soup.find_all(class_='page-number')
    max_page = 1  # Default value if no page numbers are found
    for page_number in page_numbers:
        try:
            page = int(page_number.text)
            page_url = urljoin(base_url, page_number.get('href'))
            if page > max_page:
                max_page = page
        except ValueError:
            pass  # Ignore non-integer page numbers
    return max_page

def generate_readme(files, folder_path):
    try:
        readme_content = []
        for file_info in files:
            # Remove "docs/" from file path and replace "\" with "/"
            file_path = file_info['path'].replace("docs/", "").replace("\\", "/")
            readme_content.append(f"* [{file_info['title']}]({file_path})\n")
        
        # Create the README.md file in the same folder as the exported files
        readme_file_path = os.path.join(folder_path, 'copy-me-latest-news.md')
        with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
            readme_file.write("".join(readme_content))
        print(f"README.md file created successfully at: {readme_file_path}")
    except Exception as e:
        print(f"Error occurred while generating README.md: {e}")

def main():
    # Load configuration from JSON file
    with open('scripts\XMPRO Website Scrape Scripts\scrape-xmpro-website-latestnews-config.json') as json_file:
        config = json.load(json_file)

    # Extract folder path from config
    folder_path = config.get('folderPath')

    if folder_path:
        # Ensure the folder path exists, create if it doesn't
        os.makedirs(folder_path, exist_ok=True)

        # Example HTML snippet
        html_snippet = '''
        <ul class="page-numbers nav-pagination links text-center">
            <li><span aria-current="page" class="page-number current">1</span></li>
            <li><a class="page-number" href="/category/news/page/2/">2</a></li>
            <li><a class="page-number" href="/category/news/page/3/">3</a></li>
            <li><a class="page-number" href="/category/news/page/4/">4</a></li>
            <li><span class="page-number dots">…</span></li>
            <li><a class="page-number" href="/category/news/page/14/">14</a></li>
            <li><a class="next page-number" href="/category/news/page/2/"><i class="icon-angle-right"></i></a></li>
        </ul>
        '''

        base_url = "https://xmpro.com/category/news/"
        num_pages = get_max_page_numbers(html_snippet, base_url)

        all_blog_urls = get_all_blog_urls(base_url, num_pages)
        exported_files = []

        for url in all_blog_urls:
            # Introduce a delay of 1 second before scraping each page
            sleep(1)
            title, content = scrape_page(url)
            if title and content:
                filename = save_to_md(title, content, url, folder_path)
                if filename:
                    exported_files.append({'title': title, 'path': filename})
            else:
                print(f"Failed to scrape the page: {url}")

        # Generate README.md file with links to exported files
        generate_readme(exported_files, folder_path)
    else:
        print("Folder path not found in config.")

if __name__ == "__main__":
    main()
