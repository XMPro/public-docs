# XMPro Documentation Migration: GitBook to DocFX

This document provides an overview of the migration process from GitBook to DocFX for the XMPro documentation.

## Migration Overview

The XMPro documentation is being migrated from GitBook to DocFX. This migration involves:

1. Setting up the DocFX project structure
2. Migrating the navigation structure
3. Migrating content pages
4. Migrating images and other assets
5. Implementing styling and customization
6. Verifying links and functionality
7. Deploying the migrated documentation

## Migration Plan

The detailed migration plan is available in the [migration-plan.md](migration-plan.md) file. This plan outlines the step-by-step process for migrating the documentation, including:

- Branching strategy
- Migration steps
- Content migration guidelines
- Image migration
- Link updates
- Progress tracking

## Migration Helper Script

A PowerShell script (`migration-helper.ps1`) has been created to assist with the migration process. This script helps automate the following tasks:

- Creating the directory structure
- Converting GitBook Markdown to DocFX Markdown
- Migrating images
- Generating TOC files

### Using the Migration Helper Script

To use the migration helper script, follow these steps:

1. Open a PowerShell terminal
2. Navigate to the `docs-docfx` directory
3. Run the script with the appropriate parameters

```powershell
.\migration-helper.ps1 -GitBookPath "C:\path\to\gitbook" -DocFXPath "C:\path\to\docfx"
```

#### Parameters

- `-GitBookPath`: The path to the GitBook repository
- `-DocFXPath`: The path to the DocFX repository
- `-Section`: (Optional) The section to migrate (e.g., "getting-started", "concepts")
- `-CreateStructure`: (Optional) Create the directory structure
- `-MigrateContent`: (Optional) Migrate content
- `-MigrateImages`: (Optional) Migrate images
- `-GenerateToc`: (Optional) Generate TOC files

#### Examples

Migrate everything:
```powershell
.\migration-helper.ps1 -GitBookPath "C:\Work\Git\public-docs-pages\docs-gitbook" -DocFXPath "C:\Work\Git\public-docs-pages\docs-docfx"
```

Migrate a specific section:
```powershell
.\migration-helper.ps1 -GitBookPath "C:\Work\Git\public-docs-pages\docs-gitbook" -DocFXPath "C:\Work\Git\public-docs-pages\docs-docfx" -Section "getting-started"
```

Create the directory structure only:
```powershell
.\migration-helper.ps1 -GitBookPath "C:\Work\Git\public-docs-pages\docs-gitbook" -DocFXPath "C:\Work\Git\public-docs-pages\docs-docfx" -CreateStructure
```

## Migration Progress Tracking

The migration progress is tracked in the following way:

1. Each step in the migration plan is done on a separate feature branch
2. Each branch is reviewed and merged through a pull request
3. The progress is tracked in the migration plan document

## Branching Strategy

The branching strategy for the migration is as follows:

1. Create a feature branch for each step in the migration plan
2. Implement the step on the feature branch
3. Test the changes locally
4. Create a pull request for review
5. Merge the pull request to the main branch

The branch naming convention is:

```
migrate/[section-name]/[specific-task]
```

For example:
- `migrate/navigation/main-toc`
- `migrate/content/getting-started`
- `migrate/assets/images`

### Creating Feature Branches

For each step in the migration process, create a new feature branch from the main branch:

```bash
# Create and switch to the feature branch
git checkout main
git pull
git checkout -b migrate/[section-name]/[specific-task]
```

### Completing a Migration Step

After completing a migration step:

```bash
# Commit changes
git add .
git commit -m "Description of changes"
git push -u origin migrate/[section-name]/[specific-task]

# Create pull request (via GitHub UI)
# After PR is approved and merged, proceed to the next step
```

The migration plan includes specific git commands for each step to ensure consistency throughout the migration process.

## Testing the Migration

To test the migration, follow these steps:

1. Build the DocFX project:
```powershell
cd docs-docfx
docfx build
```

2. Serve the DocFX project locally:
```powershell
cd docs-docfx
docfx serve _site
```

3. Open a browser and navigate to `http://localhost:8080`

4. Verify that the documentation displays correctly

### Handling DocFX Build Warnings

During the migration process, you will encounter various warnings when building the DocFX project. These warnings are normal and expected, especially during the early stages of migration when not all content has been migrated yet.

For detailed information on how to handle these warnings, refer to the [handling-docfx-warnings.md](handling-docfx-warnings.md) document. This document explains:

- Types of warnings you will encounter
- Why these warnings occur
- How to handle these warnings during the migration process
- Strategies for addressing specific warning types
- Using the migration helper script to resolve warnings
- Final cleanup process to address remaining warnings

It's important to note that you can safely ignore most warnings during the migration process, as they will be resolved as you progress through the migration steps. However, it's good practice to keep track of warnings and address them incrementally as you migrate each section.

## Deployment

A GitHub Actions workflow has been set up to automatically deploy the documentation to GitHub Pages whenever changes are merged into the main branch. This ensures that each migration step is immediately visible on the public documentation site once it's completed and merged.

### GitHub Actions Workflow

The deployment workflow is defined in `.github/workflows/deploy-docs.yml` and performs the following steps:

1. Checks out the repository
2. Sets up .NET
3. Installs DocFX
4. Builds the DocFX documentation
5. Deploys the built site to the gh-pages branch

### Deployment Process

The deployment process is as follows:

1. Complete a migration step on a feature branch
2. Test the changes locally
3. Create a pull request for the feature branch
4. Review and merge the pull request into the main branch
5. GitHub Actions automatically builds and deploys the documentation to GitHub Pages
6. Verify the changes on the live site

### Manual Deployment

If needed, you can also trigger a manual deployment by:

1. Going to the GitHub repository
2. Clicking on the "Actions" tab
3. Selecting the "Deploy DocFX to GitHub Pages" workflow
4. Clicking on "Run workflow"

## Conclusion

This migration process is designed to be iterative and incremental. Each step is completed and verified before moving on to the next step. This approach minimizes the risk of issues and ensures that the migration is done correctly.

If you have any questions or issues with the migration process, please contact the documentation team.
