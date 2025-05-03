import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
from pathlib import Path
import json

import os
from pathlib import Path

config_file = Path(r"scripts/scrape-xmpro-blogs-config.json")

config = None

with open(config_file, "rb") as file:
    config = json.load(file)

if config is None:
    raise Exception(f"No config defined in file at {config_file}")

os.makedirs(config["folderPath"], exist_ok=True)




class BlogScraper:

    def __init__(self, base_url:str) -> None:
        self.base_url = base_url   # "https://xmpro.com/category/blog/"
        self.last_page_number = None
        self.all_blog_urls = set()  # Use a set to avoid duplicate URLs
        self.get_last_page_number()
        self.get_all_links()


    def get_soup(self, url:str) -> BeautifulSoup:

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for bad status codes
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

        # Direct attempt to find the last page number without intermediate checks
        try:
            last_page_number_text = soup.find('ul', class_='page-numbers nav-pagination links text-center').find_all('li')[-2].text
            self.last_page_number = int(last_page_number_text)
        except (AttributeError, IndexError):
            return  # If any step fails, simply return without setting last_page_number

            

    def get_all_links(self) -> None:
        if self.last_page_number is None:
            print("Last page number is not set")
            return

        for page_num in range(1, self.last_page_number + 1):
            sleep(1)  # Respectful crawling by waiting a bit between requests
            soup_url = urljoin(self.base_url, f"page/{page_num}/")
            soup = self.get_soup(soup_url)

            # Directly find all 'a' tags within 'h5' with class 'post-title is-large'
            for link in soup.select('h5.post-title.is-large a[href]'):
                absolute_url = urljoin(self.base_url, link['href'])
                print(f"Found\t{absolute_url}")
                self.all_blog_urls.add(absolute_url)




    def scrape(self, save:bool=False, folder_path:str="Blog Content") -> None:
        errors = []

        for blog_url in self.all_blog_urls:
            sleep(1)  # Respectful crawling

            try:
                soup = self.get_soup(blog_url)
                if not soup:
                    continue

                title_tag = soup.find('title')
                title = title_tag.get_text().strip() if title_tag else "Untitled"
                paragraphs = soup.find('div', class_='entry-content').find_all('p')
                content = '\n'.join(p.get_text() for p in paragraphs)

                # print(f"Title: {title}\nContent: {content}\n\n")

                if save:
                    # Normalize folder and file paths
                    path = Path(folder_path)
                    path.mkdir(parents=True, exist_ok=True)
                    
                    # Safe file naming
                    safe_title = re.sub(r'[^\w\s]', '', title)[:50].strip() or "Untitled"
                    safe_title = safe_title.replace(" ", "-").lower()
                    filename = path / f"{safe_title}.md"
                    
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f"# {title}\n\n{blog_url}\n\n{content}")

            except Exception as e:
                errors.append(f"{blog_url}\t{e}")
                print(f"Error occurred while scraping {blog_url}: {e}")

        # Handle errors
        if errors and save:
            error_file = path / "_errors.txt"
            with open(error_file, "w") as file:
                file.writelines(errors)

                

scraper = BlogScraper("https://xmpro.com/category/blog/")

scraper.scrape(save=True, folder_path=config["folderPath"])

