# Terraform Composite GitHub :octocat: Actions

Contains [composite GitHub actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) used within [Terraform AWS Module](https://github.com/terraform-aws-modules) projects.

## Actions

### [Commit](./commit)

The `clowdhaus/terraform-composite-actions/commit` action will commit any changes back to your `git-branch`. When used in conjunction with `clowdhaus/terraform-composite-actions/pre-commit`, this action will ensure that pull-requests are well formatted and the automatically generated documentation is updated.

#### GitHub Token Permissions

A GitHub personal access token is required in order for the action to be able to successfully commit and push any changes back to the specified branch.

<p align="center">
  <img src=".github/images/pat.png " alt="Directories" height="224px">
</p>

#### :warning: Access Tokens & Pull-Requests from Forked Reposiories :warning:

When using this action from a forked copy, it will only succeed if either of two conditions are met:

1. The user who has forked the project must create a GitHub personal access token with the defined permissions and store it in their forked repository under the same name as the upstream secret (defined in the workflow file)
2. The entity that presides over the source repository extends access to the secret (you should be mindful of what this means - extending secret access to forked repositories means those forks could potentially retrieve those secret values) via https://github.blog/2020-08-03-github-actions-improvements-for-fork-and-pull-request-workflows/

```yml
jobs:
  commit:
    name: Commit changes
    runs-on: ubuntu-latest
    steps:
      - name: Commit changes
        uses: clowdhaus/terraform-composite-actions/commit@main
        with:
          git-branch: ${{ github.event.pull_request.head.ref }}
          github-repository: ${{github.event.pull_request.head.repo.full_name}}
          github-token: ${{ secrets.YOUR_GITHUB_PAT }}
```

### [Directories](./directories)

The `clowdhaus/terraform-composite-actions/directories` action will return a list of directories that contain a `versions.tf`, where the presence of a `versions.tf` file is loosely representative of a Terraform project root directory. This is useful for running a set of commands in each Terraform root directory under a given project.

```yml
jobs:
  directories:
    name: Get Terraform directories
    runs-on: ubuntu-latest
    steps:
      - name: Sign AWS Lambda artifact
        uses: clowdhaus/terraform-composite-actions/directories@main
        id: search
      - name: Outputs
        run: echo "${{ steps.search.outputs.directories }}"
```

### [Pre-Commit](./pre-commit)

The `clowdhaus/terraform-composite-actions/pre-commit` action will install the following tools which are intended to support the pre-commit hooks used within Terraform modules:

#### Default

- [pre-commit](https://github.com/pre-commit/pre-commit)
- [terraform](https://github.com/hashicorp/terraform) using provided `terraform-version` input (required)
- [tflint](https://github.com/terraform-linters/tflint) using provided `tflint-version` input (default = `latest`)
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) using provided `terraform-docs-version` input (default = `v0.16.0`)

#### Optional

- [tfsec](https://aquasecurity.github.io/tfsec), when `install-tfsec=true` (default = `false`), using provided `tfsec-version` input (default = `1.28.0`)
- [hcledit](https://github.com/minamijoyo/hcledit) when `install-hcledit=true` (default = `false`), using provided `hcledit-version` input (default = `0.2.3`)

#### Example

```yml
jobs:
  pre-commit:
    name: Pre-commit hooks execute
    runs-on: ubuntu-latest
    steps:
      - name: Sign AWS Lambda artifact
        uses: clowdhaus/terraform-composite-actions/pre-commit@main
        with:
          # Configure default software
          terraform-version: 1.2.0
          terraform-docs-version: v0.16.0
          terraform-architecture: amd64
          # Configure optional software
          install-hcledit: true
          hcledit-version: 0.2.3
          args: "--all-files --color always --show-diff-on-failure"
```

## License

Apache-2.0 Licensed. See [LICENSE](LICENSE).
