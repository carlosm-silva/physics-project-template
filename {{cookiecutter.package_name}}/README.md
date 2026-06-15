# {{cookiecutter.project_name}}

## Setup

```bash
cookiecutter gh:carlosm-silva/physics-project-template
cd {{cookiecutter.package_name}}
just bootstrap
conda activate {{cookiecutter.package_name}}

# one-time setup — enable GitHub Pages on the new repo. Wait for the docs workflow to complete
gh api repos/carlosm-silva/{{cookiecutter.package_name}}/pages \
  --method POST \
  --field source='{"branch":"gh-pages","path":"/"}'
```

## Common tasks

```bash
just check    # full quality gate (mirrors CI)
just test     # tests only
just docs     # serve docs locally
just fix      # auto-fix lint and format issues
just lock     # update environment.lock.yml
```
