<p align="center">
  <img src="../.github/images/git.png " alt="Docs" height="224px">
</p>
<h1 style="font-size: 56px; margin: 0; padding: 0;" align="center">
  commit
</h1>

## Usage

The `clowdhaus/terraform-composite-actions/commit` action will commit any changes back to your `git-branch`. When used in conjunction with `clowdhaus/terraform-composite-actions/pre-commit`, this action will ensure that pull-requests are well formatted and the automatically generated documentation is updated.

### GitHub Token Permissions

A GitHub personal access token is required in order for the action to be able to successfully commit and push any changes back to the specified branch.

<p align="center">
  <img src="../.github/images/pat.png " alt="Directories" height="224px">
</p>

```yml
jobs:
  commit:
    name: Commit changes
    runs-on: ubuntu-latest
    steps:
      - name: Commit changes
        uses: clowdhaus/terraform-composite-actions/commit@main
        with:
          git-branch: ${{ env.GITHUB_HEAD_REF }}
          github-token: ${{ secrets.YOUR_GITHUB_PAT }}
```
