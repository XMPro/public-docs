import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
from pathlib import Path
import json


class BlogScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.last_page_number = None
        self.all_blog_urls = set()
        self.get_last_page_number()
        self.get_all_links()

    def get_soup(self, url: str) -> BeautifulSoup:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup
        except requests.RequestException as e:
            print(f"Failed to retrieve content from {url}: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while fetching content from {url}: {e}")
            return None

    def get_last_page_number(self) -> None:
        page_number = 1

        soup_url = urljoin(self.base_url, f"page/{page_number}/")
        soup = self.get_soup(soup_url)
        if not soup:
            return

        try:
            # Find all the page-number <a> tags, excluding the 'Next' button
            page_numbers = soup.find_all('a', class_='page-number')
            
            # If page numbers exist, get the last valid one
            if page_numbers:
                last_page_number_url = page_numbers[-2]['href']  # Last page number is second-to-last
                last_page_number_match = re.search(r'page/(\d+)', last_page_number_url)
                if last_page_number_match:
                    self.last_page_number = int(last_page_number_match.group(1))
                    print(f"Last page number is: {self.last_page_number}")
            else:
                print("No page numbers found.")
        except (AttributeError, IndexError, TypeError):
            return




    def get_all_links(self) -> None:
        if self.last_page_number is None:
            print("Last page number is not set")
            return

        for page_num in range(1, self.last_page_number + 1):
            sleep(1)
            soup_url = urljoin(self.base_url, f"page/{page_num}/")
            soup = self.get_soup(soup_url)

            for link in soup.select('h5.post-title.is-large a[href]'):
                absolute_url = urljoin(self.base_url, link['href'])
                print(f"Found\t{absolute_url}")
                self.all_blog_urls.add((absolute_url, link.text.strip()))  # Store URL and title together

    def scrape(self, save: bool = False, folder_path: str = "Blog Content") -> None:
        errors = []
        exported_files = {}

        for blog_url, title in self.all_blog_urls:
            sleep(1)  # Sleep to avoid hitting rate limits or getting blocked

            try:
                soup = self.get_soup(blog_url)
                if not soup:
                    continue

                div_content = soup.find('div', class_='large-9 col')
                if not div_content:
                    continue  # Skip if no content found

                self.adjust_images(div_content)

                # Extract the year from the 'time' element
                time_element = soup.find('time', class_='entry-date published updated') or soup.find('time', class_='entry-date published')
                year = "Unknown"
                if time_element and 'datetime' in time_element.attrs:
                    datetime_str = time_element['datetime']
                    year_match = re.search(r'\d{4}', datetime_str)
                    year = year_match.group() if year_match else "Unknown"

                # Create the folder path based on the extracted year
                path = Path(folder_path, year)
                path.mkdir(parents=True, exist_ok=True)

                # Generate a safe filename for saving
                safe_title = re.sub(r'[^\w\s]', '', title)[:100].strip() or "Untitled"
                safe_title = safe_title.replace(" ", "-").lower()
                filename = path / f"{safe_title}.md"

                # Remove 'updated' tags if 'entry-date published' exists
                if div_content.find('time', class_='entry-date published'):
                    updated_time_elements = div_content.find_all('time', class_='updated')
                    for element in updated_time_elements:
                        element.decompose()

                # Additional clean-up: removing specific div elements
                for div_class in ['nav-next', 'nav-previous']:
                    div_to_remove = div_content.find(f'div', class_=div_class)
                    if div_to_remove:
                        div_to_remove.decompose()

                # Encode and save content
                content = div_content.encode_contents()

                if save:
                    with open(filename, 'wb') as file:
                        file.write(content)

                # Store exported files for tracking
                exported_files.setdefault(year, []).append((filename, blog_url))

            except Exception as e:
                errors.append(f"{blog_url}\t{e}")
                print(f"Error while scraping {blog_url}: {e}")

        # Save error logs if errors occurred
        if errors and save:
            error_file = Path(folder_path, "_errors.txt")
            with open(error_file, "w") as file:
                file.writelines([f"{err}\n" for err in errors])

        # Create a "copy-me.md" file with links to exported files
        if exported_files and save:
            for year, files in exported_files.items():
                copy_me_path = Path(folder_path, year, "copy-me.md")
                with open(copy_me_path, "w", encoding="utf-8") as copy_me:
                    copy_me.write(f"Blogs: {year}\n\n")
                    for exported_file, url in files:
                        relative_path = Path(exported_file).relative_to('docs/').as_posix()
                        # Use the correct title from the tuple of (url, title)
                        title = next((title for u, title in self.all_blog_urls if u == url), "Untitled")  # Find title corresponding to URL
                        copy_me.write(f"* [{title}]({relative_path})\n")


    def adjust_images(self, soup: BeautifulSoup) -> None:
        for element in soup.find_all():
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
            elif element.name == "iframe" and "youtube.com" in element["src"]:
                # Handle YouTube embeds if needed
                pass


if __name__ == "__main__":
    config_file = Path(r"scripts\xmpro-website-scripts\scrape-xmpro-website-blogs-config.json")

    with open(config_file, "r") as file:
        config = json.load(file)

    if config is None:
        raise Exception(f"No config defined in file at {config_file}")

    scraper = BlogScraper("https://xmpro.com/category/blog/")
    scraper.scrape(save=True, folder_path=config["folderPath"])