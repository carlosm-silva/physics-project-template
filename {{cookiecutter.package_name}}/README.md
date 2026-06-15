# {{cookiecutter.project_name}}

## Setup

```bash
cookiecutter gh:yourusername/physics-project-template
cd {{cookiecutter.package_name}}
just bootstrap
conda activate {{cookiecutter.package_name}}
```

## Common tasks

```bash
just check    # full quality gate (mirrors CI)
just test     # tests only
just docs     # serve docs locally
just fix      # auto-fix lint and format issues
just lock     # update environment.lock.yml
```
