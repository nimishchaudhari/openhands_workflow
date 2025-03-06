# OpenHands Workflow: Streamlining Development with GitHub Actions

Welcome to the OpenHands Workflow repository! This guide provides an overview of how to use the OpenHands resolver GitHub Actions workflow for efficient development processes. The OpenHands resolver automates tasks and ensures consistency across your projects.

## Repository Overview

This repository contains the necessary files and scripts to implement the OpenHands resolver workflow in your GitHub projects. The key components include:

- **GitHub Actions Workflow**: Automates the resolution of issues using the OpenHands resolver.
- **Scripts**: Tools to facilitate the creation of GitHub issues and other automation tasks.

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

- **Triggers**: Define the conditions under which the workflow should execute, such as on every push to the main branch or upon a pull request.
- **Jobs**: Specify the tasks the workflow should perform, which may include running tests, linting code, or deploying applications.
- **Environment**: Configure the necessary environment variables and secrets to support your jobs.

### Step 3: Commit and Push

After customizing the workflow file, commit your changes and push them to your repository:

```bash
git add .github/workflows/openhands-resolver.yml
git commit -m "Add OpenHands resolver workflow"
git push origin main
```

## Utilizing the OpenHands Resolver

To effectively leverage the OpenHands GitHub Action within your repository, follow these steps:

1. **Create an Issue**: Initiate the process by creating an issue in your repository that outlines the problem or task requiring resolution.
2. **Add the `fix-me` Label**: Apply the `fix-me` label to the issue to trigger the OpenHands resolver.
3. **Alternative Trigger**: Alternatively, leave a comment on the issue starting with `@openhands-agent` to activate the resolver.
4. **Review the Pull Request**: The resolver will generate a pull request with proposed changes. Thoroughly review these changes to ensure they meet your project's standards.
5. **Provide Feedback**: If the changes are not satisfactory, offer feedback through general comments, review comments, or inline thread comments. Reapply the `fix-me` label to the pull request or address specific comments by starting with `@openhands-agent` to request further modifications.

### Custom Configurations

Tailor the behavior of the OpenHands resolver by setting specific repository variables:

- **LLM_MODEL**: Specify the language model to be used with OpenHands.
- **OPENHANDS_MAX_ITER**: Set the maximum limit for agent iterations.
- **OPENHANDS_MACRO**: Customize the default macro for invoking the resolver.
- **OPENHANDS_BASE_CONTAINER_IMAGE**: Define a custom sandbox container image.
- **TARGET_BRANCH**: Merge to a branch other than `main`.

## Automating Issue Creation

To streamline the issue creation process, you can use the `create_issues.py` script available in the [scripts directory](https://github.com/nimishchaudhari/openhands_workflow/blob/main/scripts/create_issues.py). This script automates the creation of GitHub issues by leveraging the GitHub API. Here's how you can use it:

1. **Set Up Environment Variables**: Ensure the following environment variables are set:
   - `REPO_OWNER`: The owner of the repository.
   - `REPO_NAME`: The name of the repository.
   - `AUTH_TOKEN`: Your GitHub personal access token.
   - `ISSUES`: A string representation of a list of tuples, where each tuple contains the title and body of an issue.

2. **Run the Script**: Execute the script to create issues in your repository. The script will read the issues from the `ISSUES` environment variable and create them using the GitHub API.

```bash
python scripts/create_issues.py
```

## How to Make Use of This Workflow

### Using the OpenHands GitHub Action

To use the OpenHands GitHub Action in your own repository, follow these steps:

1. **Create an Issue**: Start by creating an issue in your repository that describes the problem or task you want the resolver to address.
2. **Add the `fix-me` Label**: Add the `fix-me` label to the issue. This will trigger the OpenHands resolver to attempt to resolve the issue.
3. **Alternative Trigger**: Instead of adding a label, you can leave a comment on the issue starting with `@openhands-agent` to trigger the resolver.
4. **Review the Pull Request**: The resolver will create a pull request with the proposed changes. Review these changes to ensure they meet your requirements.
5. **Provide Feedback**: If the changes are not satisfactory, provide feedback through general comments, review comments, or inline thread comments. Add the `fix-me` label to the pull request or address a specific comment by starting with `@openhands-agent` to request further adjustments.

### Custom Configurations

You can customize the behavior of the OpenHands resolver by setting specific repository variables:

- **LLM_MODEL**: Set the language model to use with OpenHands.
- **OPENHANDS_MAX_ITER**: Set the maximum limit for agent iterations.
- **OPENHANDS_MACRO**: Customize the default macro for invoking the resolver.
- **OPENHANDS_BASE_CONTAINER_IMAGE**: Specify a custom sandbox container image.
- **TARGET_BRANCH**: Merge to a branch other than `main`.

## Benefits of the OpenHands Resolver

- **Automation**: Automate repetitive tasks to enhance efficiency and minimize human error.
- **Consistency**: Ensure adherence to best practices and maintain a consistent codebase.
- **Integration**: Seamlessly integrate with other GitHub Actions and third-party services.

## Contributing

We encourage contributions from the community. If you have suggestions, bug reports, or wish to contribute code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
