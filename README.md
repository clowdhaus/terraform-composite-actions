# Terraform Composite GitHub :octocat: Actions

Contains [composite GitHub actions](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) used within [Terraform AWS Module](https://github.com/terraform-aws-modules) projects.

## Actions

- [directories](./directories) - collects list of Terraform directories
- [format-docs](./format-docs) - executes pre-commit to format Terraform code, update docs, and add commit if any changes
- [pre-commit](./pre-commit) - execute pre-commit for Terraform codebase

## Misc

- Workflow for releases (looks like its a [token issue](https://github.com/gr2m/create-or-update-pull-request-action/issues/281) and then it should be ready)

## License

Apache-2.0 Licensed. See [LICENSE](LICENSE).
