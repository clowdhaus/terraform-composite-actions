<p align="center">
  <img src="../.github/images/directory.png " alt="Directories" height="296px">
</p>
<h1 style="font-size: 56px; margin: 0; padding: 0;" align="center">
  directories
</h1>

## Usage

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