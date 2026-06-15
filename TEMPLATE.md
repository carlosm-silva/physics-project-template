# physics-project-template

A cookiecutter template for physics / data science projects.

## Usage

```bash
cookiecutter gh:carlosm-silva/physics-project-template
```

## What gets generated

- src/ layout Python package with core/io/viz/pipeline separation
- conda environment (environment.yml + lock file)
- Full ruff + mypy + pytest + coverage quality gate
- Pre-commit hooks
- GitHub Actions CI (quality + docs jobs)
- MkDocs Material documentation with MathJax
- Optional paper/ folder for LaTeX deliverables

## Conditional features

| Prompt | Effect |
|--------|--------|
| `has_paper = y` | Includes `paper/` with LaTeX structure |
| `use_mpi = y` | Adds openmpi + mpi4py to environment.yml |
