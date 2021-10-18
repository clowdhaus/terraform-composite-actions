# Terraform Composite GitHub :octocat: Actions

Contains [composite GitHub actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) used within [Terraform AWS Module](https://github.com/terraform-aws-modules) projects.

## Actions

### [Directories](./directories)

The `clowdhaus/terraform-composite-actions/directories` action will return a list of directories that contain a `versions.tf`, where the presence of a `versions.tf` file is loosely representative of a Terraform project root directory. This is useful for running a set of commands in each Terraform root directory under a given project.

```yml
jobs:
  search:
    name: Get Terraform directories
    runs-on: ubuntu-latest
    steps:
      - name: Sign AWS Lambda artifact
        uses: clowdhaus/terraform-composite-actions/directories@main
        id: search
      - name: Outputs
        run: echo "${{ steps.search.outputs.directories }}"
```

### [Format-Docs](./format-docs)

The `clowdhaus/terraform-composite-actions/format-docs` action will format your Terraform codebase and update the documentation using `terraform-docs` before commiting any changes back to your `git-branch`. This action is intended to ensure that pull-requests are well formatted and the automatically generated documentation is updated.

#### GitHub Token Permissions

A GitHub personal access token is required in order for the action to be able to successfully commit and push any changes back to the specified branch.

<p align="center">
  <img src=".github/images/pat.png " alt="Directories" height="196px">
</p>

```yml
jobs:
  pre-commit:
    name: Format docs
    runs-on: ubuntu-latest
    steps:
      - name: Format and update docs
        uses: clowdhaus/terraform-composite-actions/format-docs@main
        with:
          terraform-version: 1.0.2
          terraform-docs-version: v15.0.0
          git-branch: ${{ env.GITHUB_HEAD_REF }}
          github-token: ${{ secrets.YOUR_GITHUB_PAT }}
```

### [Pre-Commit](./pre-commit)

The `clowdhaus/terraform-composite-actions/pre-commit` action will install the following tools which are intended to support the pre-commit hooks used within Terraform modules:

- [terraform](https://github.com/hashicorp/terraform) using provided `terraform-version` input
- [pre-commit](https://github.com/pre-commit/pre-commit)
- [tflint](https://github.com/terraform-linters/tflint)
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) using provided `terraform-docs-version` input

```yml
jobs:
  pre-commit:
    name: Pre-commit hooks execute
    runs-on: ubuntu-latest
    steps:
      - name: Sign AWS Lambda artifact
        uses: clowdhaus/terraform-composite-actions/pre-commit@main
        with:
          terraform-version: 1.0.2
          terraform-docs-version: v15.0.0
          args: "--all-files --color always --show-diff-on-failure"
```

## License

Apache-2.0 Licensed. See [LICENSE](LICENSE).
