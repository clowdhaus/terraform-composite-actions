<p align="center">
  <img src="../.github/images/docs.png " alt="Docs" height="196px">
</p>
<h1 style="font-size: 56px; margin: 0; padding: 0;" align="center">
  format-docs
</h1>

## Usage

The `clowdhaus/terraform-composite-actions/format-docs` action will format your Terraform codebase and update the documentation using `terraform-docs` before commiting any changes back to your `git-branch`. This action is intended to ensure that pull-requests are well formatted and the automatically generated documentation is updated.

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
