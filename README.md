# OpenHands Workflow: Streamlining Development with GitHub Actions

Welcome to the OpenHands Workflow repository! This guide provides an overview of how to use the OpenHands resolver GitHub Actions workflow for efficient development processes. The OpenHands resolver automates tasks and ensures consistency across your projects.

## Repository Overview

This repository contains the necessary files and scripts to implement the OpenHands resolver workflow in your GitHub projects. The key components include:

- **GitHub Actions Workflow**: Automates the resolution of issues using the OpenHands resolver.
- **Scripts**: Tools to facilitate the creation of GitHub issues and other automation tasks.
- **Create Issues Action**: A GitHub Action to create issues from comments.

## Prerequisites

Before you begin, ensure you have the following:

- A GitHub account.
- Basic proficiency in Git and GitHub.
- A project repository where you intend to implement the OpenHands resolver workflow.

## Setting Up the OpenHands Resolver Workflow

### Step 1: Add the OpenHands Resolver Workflow

1. Navigate to your project repository on GitHub.
2. Access the `.github/workflows` directory. If it does not exist, create it.
3. Within the `workflows` directory, create a new file named `openhands-resolver.yml`.
4. Copy the content from the [OpenHands resolver example](https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/resolver/examples/openhands-resolver.yml) and paste it into your `openhands-resolver.yml` file.

### Step 2: Customize the Workflow

The workflow file is a template that may require customization to align with your project's specific needs. Key sections to consider adjusting include:

- **Environment**: Configure the necessary environment variables and secrets to support your jobs.

### Step 3: Commit and Push

After customizing the workflow file, commit your changes and push them to your repository:

```bash
git add .github/workflows/openhands-resolver.yml
git commit -m "Add OpenHands resolver workflow"
git push origin main
```

### Set Up GitHub Secrets

To ensure the workflow functions correctly, set up the following GitHub secrets in your repository settings:

- **Required**:
  - `LLM_API_KEY`: Your LLM API key.

- **Optional**:
  - `PAT_USERNAME`: GitHub username for the personal access token.
  - `PAT_TOKEN`: The personal access token.
  - `LLM_BASE_URL`: Base URL for LLM API (only if using a proxy).

## Automating Issue Creation

### GitHub Action for Creating Issues

The repository includes a GitHub Action that automates the creation of issues from comments. This action is triggered when a comment containing `/create_issues` is added to an issue.  It uses the `github-script` action and the built-in `GITHUB_TOKEN`, so no additional secrets need to be configured. Here's how it works:

- **Trigger**: The action is triggered by an `issue_comment` event with the type `created`.
- **Criteria**: The comment must contain the text `/create_issues` followed by a list of issues in the format `[["title", "body"], ["title", "body"]]`.  Note the use of double quotes.
- **Job**: The job `create-issues` runs on `ubuntu-latest` and performs the following steps:
   - Extracts issues from the comment body using `github-script`.
   - Creates the issues using the GitHub API.
   - Updates the original comment with links to the created issues, or an error message if issue creation fails.
- **Features**:
    - **Error Handling:** The workflow handles potential errors during issue creation (e.g., invalid input format) and updates the original comment with error messages.
    - **No Additional Secrets:**  This workflow uses the built-in `GITHUB_TOKEN` provided by GitHub Actions.  Ensure your repository settings grant "Read and write permissions" to Actions.

#### Example Trigger

To trigger the `create-issues` workflow, add a comment to an issue in the following format:

```
/create_issues [["Title 1", "Body 1"], ["Title 2", "Body 2"]]
```

This comment will trigger the workflow to create two issues with the specified titles and bodies.

## Benefits of the OpenHands Resolver

- **Automation**: Automate repetitive tasks to enhance efficiency and minimize human error.
- **Consistency**: Ensure adherence to best practices and maintain a consistent codebase.
- **Integration**: Seamlessly integrate with other GitHub Actions and third-party services.

For more detailed information on using the OpenHands GitHub Action, refer to the [official documentation](https://docs.all-hands.dev/modules/usage/how-to/github-action).

## Contributing

We encourage contributions from the community. If you have suggestions, bug reports, or wish to contribute code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
