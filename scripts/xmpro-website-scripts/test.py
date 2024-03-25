import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
from pathlib import Path
import json


class BlogScraper:
    def __init__(self, base_url:str) -> None:
        self.base_url = base_url
        self.last_page_number = None
        self.all_blog_urls = set()
        self.get_last_page_number()
        self.get_all_links()

    def get_soup(self, url:str) -> BeautifulSoup:
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
                self.all_blog_urls.add(absolute_url)

    def scrape(self, save:bool=False, folder_path:str="Blog Content") -> None:
        errors = []
        exported_files = []

        for blog_url in self.all_blog_urls:
            sleep(1)

            try:
                soup = self.get_soup(blog_url)
                if not soup:
                    continue

                title_tag = soup.find('title')
                title = title_tag.get_text().strip() if title_tag else "Untitled"
                div_content = soup.find('div', class_='large-9 col')
                self.adjust_images(div_content)
                content = div_content.encode_contents()

                path = Path(folder_path)
                path.mkdir(parents=True, exist_ok=True)
                safe_title = re.sub(r'[^\w\s]', '', title)[:50].strip() or "Untitled"
                safe_title = safe_title.replace(" ", "-").lower()
                filename = path / f"{safe_title}.md"

                with open(filename, 'wb') as file:
                    file.write(content)

                exported_files.append(filename)

            except Exception as e:
                errors.append(f"{blog_url}\t{e}")
                print(f"Error occurred while scraping {blog_url}: {e}")

        if errors and save:
            error_file = path / "_errors.txt"
            with open(error_file, "w") as file:
                file.writelines(errors)

        if exported_files and save:
            readme_file = path / "copy-me.md"
            with open(readme_file, "w", encoding="utf-8") as file:
                file.write("Blogs:\n\n")
                for exported_file in exported_files:
                    file_path = Path(exported_file)
                    result = file_path.relative_to("docs/").as_posix()
                    name = exported_file.stem.replace("-", " ").title()  # Capitalize first letter of each word
                    file.write(f"* [{name}]({result})\n")

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
    config_file = Path(r"scripts\xmpro-website-scripts\test-config.json")

    with open(config_file, "r") as file:
        config = json.load(file)

    if config is None:
        raise Exception(f"No config defined in file at {config_file}")

    scraper = BlogScraper("https://xmpro.com/category/blog/")
    scraper.scrape(save=True, folder_path=config["folderPath"])
