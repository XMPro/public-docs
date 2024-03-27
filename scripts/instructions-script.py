def create_instructions():
    try:
        readme_file_path = "docs/INSTRUCTIONS.md"  # Manual file path
        readme_content = """# XMPro Learning Repository Instructions

# XMPro Learning Repository Instructions

## Introduction

Welcome to the XMPro Public Docs Repository! This repository serves as a central hub for storing and accessing external content related to XMPro Learning for GitBook Intergration. The content is organised into categories, each with its own "copy-me" file containing markdown filepaths of the content. This document provides step-by-step instructions on how to effectively utilise the extracted content for GitBook.



### Step 1: Navigate to External Content

Navigate to the "docs" then "external-content" directory to access the various external resources and materials related to XMPro.

### Step 2: Navigate to Category

Within the "external-content" directory, navigate to the specific category directory (e.g., "blogs") containing the content you wish to update.

### Step 3: Access Copy Me File

Open the "copy-me" file corresponding to the category (e.g., "copy-me-blogs.md"). This file contains markdown-formatted content extracted from external sources.

### Step 4: Copy Content

Select and copy the content from the "copy-me" file.

### Step 5: Navigate to Summary File

Navigate to the "SUMMARY.md" file within the "external-content" directory.

### Step 6: Scroll and Find Corresponding Heading

Scroll through the SUMMARY.md file until you find the corresponding heading that matches the category you selected in Step 2 (e.g., "Blogs").

### Step 7: Paste Content Under Corresponding Heading

Paste the copied content under the corresponding heading in the SUMMARY.md file. Ensure that the indentation is correct. If there is existing content under the heading, replace it with the new content. You can compare with other external content categories on the page for indentation reference.

### Step 8: Repeat for Other Categories

Repeat Steps 2 to 7 for other categories as needed.

"""

        with open(readme_file_path, 'w') as readme_file:
            readme_file.write(readme_content)
            print(f"INSTRUCTIONS.md file created successfully at {readme_file_path}")
    except Exception as e:
        print(f"An error occurred while creating INSTRUCTIONS.md: {e}")

# Call the function to create the INSTRUCTIONS.md file
create_instructions()
