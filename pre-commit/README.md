<p align="center">
  <img src="../.github/images/pre-commit.svg " alt="Pre-Commit" height="296px">
</p>
<h1 style="font-size: 56px; margin: 0; padding: 0;" align="center">
  pre-commit
</h1>

## Usage

The `clowdhaus/terraform-composite-actions/pre-commit` action will install the following tools which are intended to support the pre-commit hooks used within Terraform modules:

### Default Tools

- [terraform](https://github.com/hashicorp/terraform) using provided `terraform-version` input (required when `use-opentofu` is `false`)
- [OpenTofu](https://opentofu.org/) using provided `opentofu-version` input when `use-opentofu` is `true`
- [pre-commit](https://github.com/pre-commit/pre-commit)
- [tflint](https://github.com/terraform-linters/tflint) using provided `tflint-version` input
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) using provided `terraform-docs-version` input

### Optional Tools

- [hcledit](https://github.com/minamijoyo/hcledit) when `install-hcledit` is `true` (using `hcledit-version`)
- [tfsec](https://github.com/aquasecurity/tfsec) when `install-tfsec` is `true` (using `tfsec-version`)
- [trivy](https://github.com/aquasecurity/trivy) when `install-trivy` is `true` (using `trivy-version`)

## Examples

### Terraform

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
          terraform-version: 1.2.0
          terraform-docs-version: v0.16.0
          install-hcledit: true
          hcledit-version: 0.2.3
          args: "--all-files --color always --show-diff-on-failure"
```

### OpenTofu

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
          use-opentofu: true
          opentofu-version: 1.11.4
          terraform-docs-version: v0.20.0
          args: "--all-files --color always --show-diff-on-failure"
```

When `use-opentofu: true`:
- OpenTofu is installed via the official [opentofu/setup-opentofu](https://github.com/opentofu/setup-opentofu) action
- `PCT_TFPATH=tofu` is set to ensure [pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) hooks use the `tofu` binary
- `terraform-version` is not required

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `use-opentofu` | Use OpenTofu instead of Terraform | No | `false` |
| `opentofu-version` | OpenTofu version to install when `use-opentofu` is `true` | No | `1.11.4` |
| `terraform-version` | Terraform version to install. Required when `use-opentofu` is `false` | Conditional | N/A |
| `terraform-docs-version` | Version of terraform-docs to install | No | `v0.20.0` |
| `tflint-version` | Version of tflint to install | No | `latest` |
| `install-hcledit` | Whether to install hcledit | No | `false` |
| `hcledit-version` | Version of hcledit to install when enabled | No | `0.2.17` |
| `install-tfsec` | Whether to install tfsec | No | `false` |
| `tfsec-version` | Version of tfsec to install when enabled | No | `1.28.14` |
| `install-trivy` | Whether to install trivy | No | `false` |
| `trivy-version` | Version of trivy to install when enabled | No | `0.65.0` |
| `parallelize-init` | Whether to parallelize `terraform init` across directories | No | `false` |
| `args` | Arguments to pass to pre-commit run command | No | `--all-files --color always --show-diff-on-failure` |
