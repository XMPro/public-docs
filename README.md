# Public Docs Pages

## Git Image Handling

This repository includes a `.gitattributes` file that properly handles binary image files to prevent them from incorrectly showing as modified in git status.

### Issue Fixed

Six image files were consistently showing as modified in git status even when no changes were made:
- docs/.gitbook/assets/Email.PNG
- docs/.gitbook/assets/Import_2.png
- docs/.gitbook/assets/Main.PNG
- docs/.gitbook/assets/PM Output.PNG
- docs/.gitbook/assets/Timeline.png
- docs/.gitbook/assets/Tooltip.png

### Solution Implemented

1. Created a `.gitattributes` file with:
   - Specific rules for the problematic files
   - General rules for all image file extensions

2. Used `git update-index --assume-unchanged` for the specific files

### If Issues Persist

If you still see these or other image files incorrectly showing as modified, run:

```bash
git update-index --assume-unchanged "path/to/image.png"
```

To undo this setting (if you need to actually modify the file):

```bash
git update-index --no-assume-unchanged "path/to/image.png"
```

For new developers cloning the repository, if they encounter the same issue with these or other image files, they should run:

```bash
git update-index --assume-unchanged "docs/.gitbook/assets/Email.PNG" "docs/.gitbook/assets/Import_2.png" "docs/.gitbook/assets/Main.PNG" "docs/.gitbook/assets/PM Output.PNG" "docs/.gitbook/assets/Timeline.png" "docs/.gitbook/assets/Tooltip.png"
