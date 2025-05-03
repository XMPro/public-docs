import os
import requests
from bs4 import BeautifulSoup
import json

def scrape_and_export(url, folder_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the main content area
            main_content = soup.find('main', id='main', class_='')
            if main_content:
                page_title = soup.title.string.strip()[:20]  # Truncate title to a maximum of 20 characters

                # Ensure the title is not empty after truncation
                if page_title.strip():
                    # Format the filename to be all lowercase and replace spaces with hyphens ("-")
                    filename = os.path.join(folder_path, f"{page_title.lower().replace(' ', '-')}.md")
                else:
                    filename = os.path.join(folder_path, "Untitled.md")

                with open(filename, 'w', encoding='utf-8') as file:
                    # Write page title as main heading
                    file.write(f"# {page_title}\n\n")

                    # Write page URL in the specified format
                    file.write(f"[URL]({url})\n\n")

                    # Find all text, image, and video elements within the main content area
                    for element in main_content.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "img", "iframe"]):
                        if element.name == "img":
                            prop = "src"
                            if "data-src" in element.attrs:
                                prop = "data-src"
                            # Get image dimensions
                            w = element.get("width")
                            h = element.get("height")
                            # If width or height is missing, skip the image
                            if w and h:
                                file.write(f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n')
                            else:
                                print(f"Image dimensions missing for {element[prop]}. Skipping...")
                        elif element.name == "iframe" and "youtube.com" in element["src"]:
                            youtube_id = element["src"].split("/")[-1].split("?")[0]
                            file.write(f'[![Watch the video](https://img.youtube.com/vi/{youtube_id}/default.jpg)](https://youtu.be/{youtube_id})\n\n')  # Embed YouTube video thumbnail
                        else:
                            if element.name.startswith("h"):
                                heading_level = int(element.name[1])
                                file.write(f"{'#' * heading_level} {element.get_text().strip()}\n\n")
                            else:
                                file.write(f"{element.get_text().strip()}\n\n")

                print(f"Content saved to {filename}")
                return {'title': page_title, 'filename': filename}
            else:
                print("Main content area not found.")
    except requests.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
    except Exception as e:
        print(f"Error occurred while fetching content from {url}: {e}")

def generate_readme(files, folder_path):
    try:
        folder_name = os.path.basename(folder_path).replace("-", " ").title()
        readme_content = []
        for file_info in files:         
            # Get the relative path of the file
            relative_path = os.path.relpath(file_info['filename'], folder_path)
            # Replace backslashes with forward slashes
            relative_path = relative_path.replace("\\", "/")
            # Modify the folder path to remove "docs/" prefix
            modified_folder_path = folder_path.replace("docs/", "")
            # Append the folder path and filename to the README content
            readme_content.append(f"* [{file_info['title']}]({os.path.join(modified_folder_path, relative_path)})\n")
        
        # Create the README.md file in the same folder as the exported files
        readme_file_path = os.path.join(folder_path, 'copy-me.md')
        with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
            # Replace backslashes with forward slashes in the README content
            readme_file.write("# " + folder_name + "\n\n" + "".join(readme_content).replace("\\", "/"))
        print(f"copy-me.md file created successfully at: {readme_file_path}")
    except Exception as e:
        print(f"Error occurred while generating copy-me.md: {e}")

def main():
    # Load configuration from JSON file
    with open(r'scripts\xmpro-website-scripts\scrape-xmpro-website-keyfeatures-config.json') as json_file:
        config = json.load(json_file)

    # Extract folder path from config
    folder_path = config.get('folderPath')

    if folder_path:
        # Ensure the folder path exists, create if it doesn't
        os.makedirs(folder_path, exist_ok=True)

        # Define the URLs to scrape
        urls = [
            "https://xmpro.com/intelligent-integration/",
            "https://xmpro.com/xmpro-ai/",
            "https://xmpro.com/interactive-3d-models/",
            "https://xmpro.com/pricing/"
        ]

        # Scrape and export content for each URL
        exported_files = []
        for url in urls:
            file_info = scrape_and_export(url, folder_path)
            if file_info:
                exported_files.append(file_info)
        
        # Generate README.md file with links to exported files
        generate_readme(exported_files, folder_path)
    else:
        print("Folder path not found in config.")

if __name__ == "__main__":
    main()
