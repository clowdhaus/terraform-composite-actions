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
