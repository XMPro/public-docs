# Migration Helper Script for GitBook to DocFX Migration
# This script helps automate the migration of content from GitBook to DocFX

param (
    [Parameter(Mandatory=$true)]
    [string]$GitBookPath,
    
    [Parameter(Mandatory=$true)]
    [string]$DocFXPath,
    
    [Parameter(Mandatory=$false)]
    [string]$Section = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$CreateStructure,
    
    [Parameter(Mandatory=$false)]
    [switch]$MigrateContent,
    
    [Parameter(Mandatory=$false)]
    [switch]$MigrateImages,
    
    [Parameter(Mandatory=$false)]
    [switch]$GenerateToc
)

# Function to create the directory structure
function Create-DirectoryStructure {
    param (
        [string]$GitBookPath,
        [string]$DocFXPath
    )
    
    Write-Host "Creating directory structure..." -ForegroundColor Green
    
    # Get all directories in the GitBook docs folder
    $gitbookDirs = Get-ChildItem -Path "$GitBookPath\docs" -Directory
    
    # Create corresponding directories in the DocFX docs folder
    foreach ($dir in $gitbookDirs) {
        $docfxDir = "$DocFXPath\docs\$($dir.Name)"
        if (-not (Test-Path $docfxDir)) {
            New-Item -Path $docfxDir -ItemType Directory -Force | Out-Null
            Write-Host "Created directory: $docfxDir" -ForegroundColor Yellow
        }
        
        # Create images directory in each section
        $imagesDir = "$docfxDir\images"
        if (-not (Test-Path $imagesDir)) {
            New-Item -Path $imagesDir -ItemType Directory -Force | Out-Null
            Write-Host "Created directory: $imagesDir" -ForegroundColor Yellow
        }
    }
    
    Write-Host "Directory structure created successfully." -ForegroundColor Green
}

# Function to migrate content
function Migrate-Content {
    param (
        [string]$GitBookPath,
        [string]$DocFXPath,
        [string]$Section
    )
    
    Write-Host "Migrating content..." -ForegroundColor Green
    
    # Determine which directories to process
    $dirsToProcess = @()
    if ($Section -eq "") {
        $dirsToProcess = Get-ChildItem -Path "$GitBookPath\docs" -Directory
    } else {
        $dirsToProcess = Get-ChildItem -Path "$GitBookPath\docs\$Section" -Directory
    }
    
    # Process each directory
    foreach ($dir in $dirsToProcess) {
        $sourcePath = $dir.FullName
        $targetPath = ""
        
        if ($Section -eq "") {
            $targetPath = "$DocFXPath\docs\$($dir.Name)"
        } else {
            $targetPath = "$DocFXPath\docs\$Section\$($dir.Name)"
        }
        
        # Create the target directory if it doesn't exist
        if (-not (Test-Path $targetPath)) {
            New-Item -Path $targetPath -ItemType Directory -Force | Out-Null
        }
        
        # Get all markdown files in the source directory
        $markdownFiles = Get-ChildItem -Path $sourcePath -Filter "*.md"
        
        # Process each markdown file
        foreach ($file in $markdownFiles) {
            $sourceFile = $file.FullName
            $targetFile = "$targetPath\$($file.Name)"
            
            # Convert GitBook markdown to DocFX markdown
            $content = Get-Content -Path $sourceFile -Raw
            $content = Convert-GitBookToDocFX -Content $content
            
            # Write the converted content to the target file
            Set-Content -Path $targetFile -Value $content
            Write-Host "Migrated: $sourceFile -> $targetFile" -ForegroundColor Yellow
        }
    }
    
    # Handle special case for README.md (convert to introduction.md)
    if ($Section -eq "" -and (Test-Path "$GitBookPath\docs\README.md")) {
        $content = Get-Content -Path "$GitBookPath\docs\README.md" -Raw
        $content = Convert-GitBookToDocFX -Content $content
        Set-Content -Path "$DocFXPath\docs\introduction.md" -Value $content
        Write-Host "Migrated: $GitBookPath\docs\README.md -> $DocFXPath\docs\introduction.md" -ForegroundColor Yellow
    }
    
    Write-Host "Content migration completed successfully." -ForegroundColor Green
}

# Function to migrate images
function Migrate-Images {
    param (
        [string]$GitBookPath,
        [string]$DocFXPath,
        [string]$Section
    )
    
    Write-Host "Migrating images..." -ForegroundColor Green
    
    # Check if the assets directory exists in the GitBook docs folder
    $assetsPath = "$GitBookPath\docs\assets"
    if (-not (Test-Path $assetsPath)) {
        Write-Host "Assets directory not found: $assetsPath" -ForegroundColor Red
        return
    }
    
    # Get all image files in the assets directory
    $imageFiles = Get-ChildItem -Path $assetsPath -Include "*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg" -Recurse
    
    # Determine which directories to process
    $dirsToProcess = @()
    if ($Section -eq "") {
        $dirsToProcess = Get-ChildItem -Path "$DocFXPath\docs" -Directory
    } else {
        $dirsToProcess = @("$DocFXPath\docs\$Section")
    }
    
    # Create a mapping of image references to track which images have been copied
    $imageMapping = @{}
    
    # Process each directory
    foreach ($dir in $dirsToProcess) {
        $targetImagesDir = ""
        
        if ($Section -eq "") {
            $targetImagesDir = "$dir\images"
        } else {
            $targetImagesDir = "$dir\images"
        }
        
        # Create the target images directory if it doesn't exist
        if (-not (Test-Path $targetImagesDir)) {
            New-Item -Path $targetImagesDir -ItemType Directory -Force | Out-Null
        }
        
        # Get all markdown files in the directory
        $markdownFiles = Get-ChildItem -Path $dir -Filter "*.md" -Recurse
        
        # Process each markdown file to find image references
        foreach ($file in $markdownFiles) {
            $content = Get-Content -Path $file.FullName -Raw
            
            # Find all image references in the markdown file
            $imageRefs = [regex]::Matches($content, '!\[.*?\]\((.*?)\)')
            
            # Process each image reference
            foreach ($imageRef in $imageRefs) {
                $imagePath = $imageRef.Groups[1].Value
                
                # Extract the image filename
                $imageFilename = [System.IO.Path]::GetFileName($imagePath)
                
                # Find the corresponding image file in the assets directory
                $imageFile = $imageFiles | Where-Object { $_.Name -eq $imageFilename }
                
                if ($imageFile) {
                    # Copy the image file to the target images directory if it hasn't been copied already
                    if (-not $imageMapping.ContainsKey($imageFile.FullName)) {
                        Copy-Item -Path $imageFile.FullName -Destination "$targetImagesDir\$imageFilename" -Force
                        $imageMapping[$imageFile.FullName] = $true
                        Write-Host "Copied image: $($imageFile.FullName) -> $targetImagesDir\$imageFilename" -ForegroundColor Yellow
                    }
                    
                    # Update the image reference in the markdown file
                    $newImageRef = "![" + $imageRef.Groups[1].Value + "](images/$imageFilename)"
                    $content = $content -replace [regex]::Escape($imageRef.Value), $newImageRef
                }
            }
            
            # Write the updated content back to the markdown file
            Set-Content -Path $file.FullName -Value $content
        }
    }
    
    Write-Host "Image migration completed successfully." -ForegroundColor Green
}

# Function to generate TOC files
function Generate-Toc {
    param (
        [string]$GitBookPath,
        [string]$DocFXPath,
        [string]$Section
    )
    
    Write-Host "Generating TOC files..." -ForegroundColor Green
    
    # Check if the SUMMARY.md file exists in the GitBook docs folder
    $summaryPath = "$GitBookPath\docs\SUMMARY.md"
    if (-not (Test-Path $summaryPath)) {
        Write-Host "SUMMARY.md file not found: $summaryPath" -ForegroundColor Red
        return
    }
    
    # Read the SUMMARY.md file
    $summaryContent = Get-Content -Path $summaryPath -Raw
    
    # Parse the SUMMARY.md file to extract the TOC structure
    $tocStructure = Parse-Summary -Content $summaryContent
    
    # Generate the main TOC file
    $mainTocPath = "$DocFXPath\docs\toc.yml"
    $mainTocContent = ""
    
    foreach ($item in $tocStructure) {
        if ($item.Level -eq 1) {
            $mainTocContent += "- name: $($item.Title)`r`n"
            
            if ($item.HasChildren) {
                $mainTocContent += "  items:`r`n"
                
                foreach ($child in $tocStructure | Where-Object { $_.ParentId -eq $item.Id }) {
                    $mainTocContent += "  - name: $($child.Title)`r`n"
                    $mainTocContent += "    href: $($child.Href)`r`n"
                }
            } else {
                $mainTocContent += "  href: $($item.Href)`r`n"
            }
        }
    }
    
    # Write the main TOC file
    Set-Content -Path $mainTocPath -Value $mainTocContent
    Write-Host "Generated main TOC file: $mainTocPath" -ForegroundColor Yellow
    
    # Generate section TOC files
    $sections = $tocStructure | Where-Object { $_.Level -eq 1 -and $_.HasChildren }
    
    foreach ($section in $sections) {
        $sectionName = $section.Title.ToLower().Replace(" ", "-")
        $sectionTocPath = "$DocFXPath\docs\$sectionName\toc.yml"
        $sectionTocContent = ""
        
        foreach ($item in $tocStructure | Where-Object { $_.ParentId -eq $section.Id }) {
            $sectionTocContent += "- name: $($item.Title)`r`n"
            $sectionTocContent += "  href: $($item.Href)`r`n"
            
            if ($item.HasChildren) {
                $sectionTocContent += "  items:`r`n"
                
                foreach ($child in $tocStructure | Where-Object { $_.ParentId -eq $item.Id }) {
                    $sectionTocContent += "  - name: $($child.Title)`r`n"
                    $sectionTocContent += "    href: $($child.Href)`r`n"
                }
            }
        }
        
        # Create the section directory if it doesn't exist
        $sectionDir = [System.IO.Path]::GetDirectoryName($sectionTocPath)
        if (-not (Test-Path $sectionDir)) {
            New-Item -Path $sectionDir -ItemType Directory -Force | Out-Null
        }
        
        # Write the section TOC file
        Set-Content -Path $sectionTocPath -Value $sectionTocContent
        Write-Host "Generated section TOC file: $sectionTocPath" -ForegroundColor Yellow
    }
    
    Write-Host "TOC generation completed successfully." -ForegroundColor Green
}

# Function to parse the SUMMARY.md file
function Parse-Summary {
    param (
        [string]$Content
    )
    
    $lines = $Content -split "`r`n"
    $tocStructure = @()
    $currentId = 0
    $currentParentId = 0
    $currentLevel = 0
    
    foreach ($line in $lines) {
        # Skip empty lines
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        
        # Determine the level based on the number of leading spaces
        $level = 0
        $match = [regex]::Match($line, '^\s*')
        if ($match.Success) {
            $level = $match.Length / 2
        }
        
        # Extract the title and href from the line
        $match = [regex]::Match($line, '\[(.*?)\]\((.*?)\)')
        if ($match.Success) {
            $title = $match.Groups[1].Value
            $href = $match.Groups[2].Value
            
            # Convert the href to the DocFX format
            $href = Convert-HrefToDocFX -Href $href
            
            # Determine the parent ID based on the level
            if ($level -eq 0) {
                $parentId = 0
            } elseif ($level -eq $currentLevel) {
                $parentId = $currentParentId
            } elseif ($level -gt $currentLevel) {
                $parentId = $currentId
            } else {
                # Find the parent at the appropriate level
                $parentLevel = $level - 1
                $parent = $tocStructure | Where-Object { $_.Level -eq $parentLevel } | Select-Object -Last 1
                $parentId = $parent.Id
            }
            
            # Add the item to the TOC structure
            $currentId++
            $tocStructure += [PSCustomObject]@{
                Id = $currentId
                ParentId = $parentId
                Level = $level
                Title = $title
                Href = $href
                HasChildren = $false
            }
            
            # Update the current level and parent ID
            $currentLevel = $level
            $currentParentId = $parentId
        }
    }
    
    # Update the HasChildren property
    foreach ($item in $tocStructure) {
        $children = $tocStructure | Where-Object { $_.ParentId -eq $item.Id }
        $item.HasChildren = ($children.Count -gt 0)
    }
    
    return $tocStructure
}

# Function to convert GitBook markdown to DocFX markdown
function Convert-GitBookToDocFX {
    param (
        [string]$Content
    )
    
    # Convert GitBook hints to DocFX alerts
    $Content = $Content -replace '{% hint style="info" %}(.*?){% endhint %}', '> [!NOTE]$1' -replace '{% hint style="warning" %}(.*?){% endhint %}', '> [!WARNING]$1' -replace '{% hint style="danger" %}(.*?){% endhint %}', '> [!CAUTION]$1'
    
    # Convert GitBook tabs to DocFX tabs
    $Content = [regex]::Replace($Content, '{% tabs %}(.*?){% endtabs %}', {
        param($match)
        $tabsContent = $match.Groups[1].Value
        $tabMatches = [regex]::Matches($tabsContent, '{% tab title="(.*?)" %}(.*?){% endtab %}')
        $result = ""
        
        foreach ($tabMatch in $tabMatches) {
            $tabTitle = $tabMatch.Groups[1].Value
            $tabContent = $tabMatch.Groups[2].Value
            $tabId = $tabTitle.ToLower().Replace(" ", "-")
            $result += "# [$tabTitle](#tab/$tabId)`r`n$tabContent`r`n`r`n"
        }
        
        $result += "***"
        return $result
    }, [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    # Update image paths
    $Content = [regex]::Replace($Content, '!\[(.*?)\]\((.*?)\)', {
        param($match)
        $altText = $match.Groups[1].Value
        $imagePath = $match.Groups[2].Value
        
        # Extract the image filename
        $imageFilename = [System.IO.Path]::GetFileName($imagePath)
        
        # Update the image path to use the images directory
        $newImagePath = "images/$imageFilename"
        
        return "![$altText]($newImagePath)"
    })
    
    # Update link paths
    $Content = [regex]::Replace($Content, '\[(.*?)\]\((.*?\.md)\)', {
        param($match)
        $linkText = $match.Groups[1].Value
        $linkPath = $match.Groups[2].Value
        
        # Convert the link path to the DocFX format
        $newLinkPath = Convert-HrefToDocFX -Href $linkPath
        
        return "[$linkText]($newLinkPath)"
    })
    
    return $Content
}

# Function to convert href to DocFX format
function Convert-HrefToDocFX {
    param (
        [string]$Href
    )
    
    # Remove the .md extension if it exists
    if ($Href.EndsWith(".md")) {
        $Href = $Href.Substring(0, $Href.Length - 3)
    }
    
    # Handle special cases
    if ($Href -eq "README") {
        $Href = "introduction"
    }
    
    # Add the .md extension back
    $Href = "$Href.md"
    
    return $Href
}

# Main script execution
if ($CreateStructure) {
    Create-DirectoryStructure -GitBookPath $GitBookPath -DocFXPath $DocFXPath
}

if ($MigrateContent) {
    Migrate-Content -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
}

if ($MigrateImages) {
    Migrate-Images -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
}

if ($GenerateToc) {
    Generate-Toc -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
}

# If no specific action is specified, run all actions
if (-not ($CreateStructure -or $MigrateContent -or $MigrateImages -or $GenerateToc)) {
    Create-DirectoryStructure -GitBookPath $GitBookPath -DocFXPath $DocFXPath
    Migrate-Content -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
    Migrate-Images -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
    Generate-Toc -GitBookPath $GitBookPath -DocFXPath $DocFXPath -Section $Section
}

Write-Host "Migration completed successfully." -ForegroundColor Green
