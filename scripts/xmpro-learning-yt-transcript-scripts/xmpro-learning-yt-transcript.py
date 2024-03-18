import json
import os
from pathlib import Path
import re
from time import sleep
from youtube_transcript_api import YouTubeTranscriptApi

import scrapetube

# Load config
config_file = Path(r"scripts\xmpro-learning-yt-transcript-scripts\scrape-xmpro-learning-yt-transcrcipt-config.json")

config = None

with open(config_file, "r", encoding="utf-8") as file:
    config = json.load(file)

if config is None:
    raise Exception(f"No config defined in file at {config_file}")

os.makedirs(config["folderPath"], exist_ok=True)

# Regular expression pattern to remove emojis
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def make_windows_compatible_filename(filename):
    # Replace reserved characters
    replacements = {
        '<': '[',
        '>': ']',
        ':': '-',
        '"': "'",
        '/': '-',
        '\\': '-',
        '|': '_',
        '?': '!',
        '*': 'x',
    }
    for old_char, new_char in replacements.items():
        filename = filename.replace(old_char, new_char)
    
    # Remove control characters (integer values < 31)
    filename = ''.join(char for char in filename if ord(char) > 31)
    
    # Trim spaces and periods from the end
    filename = filename.rstrip('. ')
    filename = filename.replace(" ", "-").lower()
    
    return filename

# Scrape YouTube videos
videos = scrapetube.get_channel(channel_username="XMProLearning")

# List to store information about saved markdown files
md_files = []

for video in videos:
    title = video['title']['runs'][0]['text']
    title = title.replace('|', '-').replace('?', '-')
    title = emoji_pattern.sub(r'', title)
    description = video['descriptionSnippet']['runs'][0]['text'] if 'descriptionSnippet' in video else ''
    video_id = video['videoId']

    title = make_windows_compatible_filename(title)
    filename = f'{config["folderPath"]}/{title}.md'

    # Skip if file exists and clean mode is on
    if os.path.exists(filename) and config["clean"]:
        continue

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(e)
        continue

    text = '\n\n'.join([t['text'] for t in transcript])

    with open(filename, 'w', encoding="utf-8") as f:
        try:
            print(f'[NEW]\t{title}')
            f.write("# " + title + "\n")  
            f.write('{% embed url="' + f'https://www.youtube.com/watch?v={video_id}' + '" %}\n\n')
            f.write('\n\n')
            f.write(description)
            f.write('\n')
            f.write('<details>\n')
            f.write('<summary>Transcript</summary>')
            f.write(description)
            f.write('\n')
            f.write(text)
            f.write('\n')
            f.write('</details>')
        except Exception as e:
            print(e)
            print(title)
            print(description)
            print(text)
            continue    

    md_files.append({'title': title, 'filename': filename})

    sleep(0.5)

# Create or update README.md with links to the exported markdown files
def update_readme(md_files, readme_filename):
    try:
        with open(readme_filename, 'w', encoding='utf-8') as file:
            file.write("# XMPro Learning YouTube Videos\n\n")
            for md_file in md_files:
                relative_path = os.path.relpath(md_file['filename'])
                file_path = relative_path.replace("docs\\", "")
                file_path = file_path.replace("\\", "/")
                file.write(f"* [{md_file['title']}]({file_path})\n")
        print(f"{readme_filename} updated with hyperlinks to exported markdown files.")
    except Exception as e:
        print(f"Error occurred while updating {readme_filename}: {e}")

if md_files:
    update_readme(md_files, os.path.join(config["folderPath"], "copy-me-xmpro-learning.md"))
else:
    print("No markdown files found to update copy-me-xmpro-learning.md.")
