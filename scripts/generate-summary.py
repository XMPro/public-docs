import json
import glob
from pathlib import Path

with open("scripts/generate-summary.json", "rb") as file:
    config = json.load(file)

    
base_path = Path(config["path"])

# first level
pages = [folder for folder in base_path.glob("*") if folder.is_dir()]


# external content page
with open(base_path / "README.md", 'w') as file:

    items = "\n".join([f"* [{str(page.stem).title()}]({str(page)}\README.md)" for page in pages])

    content = f"# External Content\n{items}"
            
    file.writelines(content)

# create pages
for page in pages:

    print(str(page.stem) + '\n\n')

    # Find all '.md' files and get their relative paths
    md_files = [base_path/file.relative_to(base_path) for file in page.rglob('*.md')]
    relative_md_files = [(path.stem.title().replace("-", " "), "/".join(path.parts[1:])) for path in md_files]

    print(relative_md_files)


    # external content page
    with open(page / "README.md", 'w') as file:

        items = "\n".join([f"* [{name}]({str(file)})" for name, file in relative_md_files])

        content = f"# {str(page.stem).title()}\n{items}"
                
        file.writelines(content)
