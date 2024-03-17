import os
import requests
from bs4 import BeautifulSoup
import json

# Function to save content to Markdown file with renamed file
def save_to_md(title, content, url, folder_path):
    try:
        # Format the title to use as filename
        filename_title = title.strip().lower().replace(" ", "-")
        
        # Rename the file as the page title but in lowercase, and replace all spaces with "-"
        filename = os.path.join(folder_path, f"{filename_title}.md")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(f"URL: {url}\n\n")
            file.write(content)
        
        print(f"Content saved to {filename}")
        return {'title': title, 'filename': filename}
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

# Function to update or create README.md with hyperlinks to exported markdown files
def update_readme(folder_path, md_files, title):
    try:
        readme_file = os.path.join(folder_path, "copy-me-about.md")
        with open(readme_file, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            for md_file in md_files:
                # Capitalize the first letter of each word in the title
                formatted_title = md_file['title'].title().replace(" ", "-")
                
                # Remove "docs/" in the file path location and replace "\" with "/"
                formatted_filename = md_file['filename'].replace("docs/", "").replace("\\", "/")
                
                file.write(f"* [{formatted_title}]({formatted_filename})\n")
        print(f"copy-me-about.md updated with hyperlinks to exported markdown files.")
    except Exception as e:
        print(f"Error occurred while updating copy-me-about.md: {e}")

# Main function
def main():
    # Load configuration from JSON file
    with open('scripts\XMPRO Website Scrape Scripts\scrape-xmpro-website-about-config.json') as json_file:
        config = json.load(json_file)

    # Extract folder path from config
    folder_path = config.get('folderPath')

    if folder_path:
        # Ensure the folder path exists, create if it doesn't
        os.makedirs(folder_path, exist_ok=True)

        # Define the URLs to scrape
        urls = [
            "https://xmpro.com/about/",
            "https://xmpro.com/partners/",
            "https://xmpro.com/press-room/"
        ]

        # Scrape and export content for each URL
        md_files = []
        for url in urls:
            # Scrape page content
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string.strip()
            content = soup.find('div', class_='content-area').get_text()

            # Save content to Markdown file
            md_file_info = save_to_md(title, content, url, folder_path)
            if md_file_info:
                md_files.append(md_file_info)

        # Update or create README.md with hyperlinks to exported markdown files
        if md_files:
            update_readme(folder_path, md_files, "About")
        else:
            print("No markdown files found to update README.md.")
    else:
        print("Folder path not found in config.")

if __name__ == "__main__":
    main()
