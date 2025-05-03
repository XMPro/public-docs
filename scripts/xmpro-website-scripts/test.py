# This is the original blogs scrape script, Ignore
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
            last_page_number_text = soup.find('ul', class_='page-numbers nav-pagination links text-center').find_all('li')[-2].text
            self.last_page_number = int(last_page_number_text)
        except (AttributeError, IndexError):
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

        for blog_url, title in self.all_blog_urls:  # Iterate over (url, title) tuples
            sleep(1)

            try:
                soup = self.get_soup(blog_url)
                if not soup:
                    continue

                div_content = soup.find('div', class_='large-9 col')
                self.adjust_images(div_content)
                content = div_content.encode_contents()

                # Get the publication year from the datetime attribute
                year_match = re.search(r'\d{4}', soup.find('time', class_='updated')['datetime'])
                year = year_match.group() if year_match else "Unknown"

                # Update folder path with the year
                path = Path(folder_path, year)
                path.mkdir(parents=True, exist_ok=True)

                safe_title = re.sub(r'[^\w\s]', '', title)[:50].strip() or "Untitled"
                safe_title = safe_title.replace(" ", "-").lower()
                filename = path / f"{safe_title}.md"

                with open(filename, 'wb') as file:
                    file.write(content)

                exported_files.setdefault(year, []).append((filename, blog_url))  # Store filename and URL together

            except Exception as e:
                errors.append(f"{blog_url}\t{e}")
                print(f"Error occurred while scraping {blog_url}: {e}")

        if errors and save:
            error_file = Path(folder_path, "_errors.txt")
            with open(error_file, "w") as file:
                file.writelines(errors)

        if exported_files and save:
            for year, files in exported_files.items():
                copy_me_content = ""
                year_folder_path = Path(folder_path, year)
                copy_me_file = year_folder_path / "copy-me.md"
                with open(copy_me_file, "w", encoding="utf-8") as copy_me:
                    copy_me.write(f"Blogs: {year}\n\n")
                    for exported_file, url in files:  # Iterate over (filename, url) tuples
                        file_path = Path(exported_file)
                        result = file_path.relative_to("docs/").as_posix()
                        name = exported_file.stem.replace("-", " ").title()  # Capitalize first letter of each word
                        copy_me.write(f"* [{name}]({result})\n")


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