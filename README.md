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

#### Default Tools

- [pre-commit](https://github.com/pre-commit/pre-commit)
- [terraform](https://github.com/hashicorp/terraform) using provided `terraform-version` input (required when `use-opentofu` is `false`)
- [tflint](https://github.com/terraform-linters/tflint) using provided `tflint-version` input (default = `latest`)
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) using provided `terraform-docs-version` input (default = `v0.20.0`)

#### OpenTofu Support

This action supports [OpenTofu](https://opentofu.org/) as a drop-in replacement for Terraform. When using OpenTofu:

- Set `use-opentofu: true` to enable OpenTofu instead of Terraform
- Specify the OpenTofu version with `opentofu-version` input (default = `1.11.4`)
- OpenTofu is installed via the official [opentofu/setup-opentofu](https://github.com/opentofu/setup-opentofu) action
- The action automatically sets `PCT_TFPATH=tofu` to ensure [pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) hooks use the `tofu` binary
- Terraform installation is skipped when `use-opentofu` is enabled

**Key Parameters:**

- `use-opentofu`: Boolean flag to use OpenTofu instead of Terraform (default: `false`)
- `opentofu-version`: OpenTofu version to install when `use-opentofu` is `true` (default: `1.11.4`)
- `terraform-version`: Required when `use-opentofu` is `false`; the action validates this requirement

#### Optional Tools

- [tfsec](https://aquasecurity.github.io/tfsec), when `install-tfsec=true` (default = `false`), using provided `tfsec-version` input (default = `1.28.14`)
- [trivy](https://aquasecurity.github.io/trivy), when `install-trivy=true` (default = `false`), using provided `trivy-version` input (default = `0.65.0`)
- [hcledit](https://github.com/minamijoyo/hcledit) when `install-hcledit=true` (default = `false`), using provided `hcledit-version` input (default = `0.2.17`)

#### Usage Examples

##### Example: Terraform

```yml
jobs:
  pre-commit:
    name: Pre-commit hooks execute
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run pre-commit with Terraform
        uses: clowdhaus/terraform-composite-actions/pre-commit@main
        with:
          # Terraform configuration
          terraform-version: 1.2.0
          # Tool versions
          terraform-docs-version: v0.16.0
          tflint-version: latest
          # Optional tools
          install-hcledit: true
          hcledit-version: 0.2.3
          # Pre-commit arguments
          args: "--all-files --color always --show-diff-on-failure"
```

##### Example: OpenTofu

```yml
jobs:
  pre-commit:
    name: Pre-commit hooks execute
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run pre-commit with OpenTofu
        uses: clowdhaus/terraform-composite-actions/pre-commit@main
        with:
          # Enable OpenTofu (replaces Terraform)
          use-opentofu: true
          opentofu-version: 1.11.4
          # Tool versions (same as Terraform workflow)
          terraform-docs-version: v0.20.0
          tflint-version: latest
          # Pre-commit arguments
          args: "--all-files --color always --show-diff-on-failure"
```

**Note:** When `use-opentofu: true` is set:
- The `terraform-version` input is ignored and not required
- All pre-commit hooks that would normally use `terraform` will automatically use `tofu` via the `PCT_TFPATH` environment variable
- The workflow is otherwise identical to the Terraform example

##### Example: OpenTofu with Optional Security Scanning

```yml
jobs:
  pre-commit:
    name: Pre-commit hooks execute with security scanning
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run pre-commit with OpenTofu and security tools
        uses: clowdhaus/terraform-composite-actions/pre-commit@main
        with:
          # OpenTofu configuration
          use-opentofu: true
          opentofu-version: 1.11.4
          # Enable security scanning
          install-tfsec: true
          tfsec-version: 1.28.14
          install-trivy: true
          trivy-version: 0.65.0
          # Standard tools
          terraform-docs-version: v0.20.0
          args: "--all-files --color always --show-diff-on-failure"
```

#### Inputs Reference

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `use-opentofu` | Use OpenTofu instead of Terraform. When `true`, installs OpenTofu and sets `PCT_TFPATH=tofu` | No | `false` |
| `opentofu-version` | OpenTofu version to install when `use-opentofu` is `true` | No | `1.11.4` |
| `terraform-version` | Terraform version to install. Required when `use-opentofu` is `false` | Conditional | N/A |
| `terraform-docs-version` | Version of terraform-docs to install | No | `v0.20.0` |
| `tflint-version` | Version of tflint to install | No | `latest` |
| `install-hcledit` | Whether to install hcledit | No | `false` |
| `hcledit-version` | Version of hcledit to install when enabled | No | `0.2.17` |
| `install-tfsec` | Whether to install tfsec for security scanning | No | `false` |
| `tfsec-version` | Version of tfsec to install when enabled | No | `1.28.14` |
| `install-trivy` | Whether to install trivy for security scanning | No | `false` |
| `trivy-version` | Version of trivy to install when enabled | No | `0.65.0` |
| `parallelize-init` | Whether to parallelize `terraform init` across directories | No | `false` |
| `args` | Arguments to pass to pre-commit run command | No | `--all-files --color always --show-diff-on-failure` |

## License

Apache-2.0 Licensed. See [LICENSE](LICENSE).
