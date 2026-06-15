# physics-project-template

A cookiecutter template for physics and data science projects.

## Usage

```bash
cookiecutter gh:carlosm-silva/physics-project-template
cd your_project_name
just bootstrap
conda activate your_project_name
just check
gh repo create your-project-name --public --source=. --push

# one-time setup — enable GitHub Pages on the new repo. Wait for the docs workflow to complete
gh api repos/carlosm-silva/your-project-name/pages \
  --method POST \
  --field source='{"branch":"gh-pages","path":"/"}'
```

After the first push, CI runs automatically and docs deploy to GitHub Pages.

---

## What gets generated

### Code quality
- `src/` layout Python package with `core/io/viz/pipeline` separation
- Ruff (lint + format), mypy (strict), pytest + coverage (≥80%) quality gate
- Pre-commit hooks — ruff and mypy run on every `git commit`
- `just check` mirrors CI exactly; `just fix` auto-corrects lint and format issues

### Environment
- Conda environment (`environment.yml` + `environment.lock.yml`)
- System-level deps managed by conda; Python deps declared in `pyproject.toml`
- `just bootstrap` creates the environment, initialises git, installs pre-commit hooks

### CI/CD (GitHub Actions)
- `ci.yml` — runs ruff, mypy, pytest, coverage on every push and pull request
- `docs.yml` — builds and deploys MkDocs to GitHub Pages on every push to `master`/`main`

### Documentation
- MkDocs Material with dark theme, MathJax, and mkdocstrings
- NumPy docstring convention; raw strings required for LaTeX content
- API reference auto-generated from source docstrings
- Live at `https://carlosm-silva.github.io/your-repo-name/` after first push

### Project layout
- `scripts/` — standalone reproducible scripts; naming mirrors output artifacts
- `configs/` — run configuration; committed configs are reproducible checkpoints
- `outputs/` — gitignored; timestamped run directories with config snapshots
- `notebooks/` — exploratory only; reusable logic extracted to `src/`
- `data/` — small reference fixtures only; large data lives outside the repo

### Optional features

| Prompt | Effect |
|--------|--------|
| `has_paper = y` | Includes `paper/` with LaTeX structure and committed `figures/` |
| `use_mpi = y` | Adds `openmpi` and `mpi4py` to `environment.yml` |

---

## Maintaining the template

### Fixing a bug in the template

```bash
cd physics-project-template
# edit the relevant file under {{cookiecutter.package_name}}/
git add .
git commit -m "fix: description of fix"
git push
```

### Testing a change

```bash
# bake a fresh test project
cookiecutter path/to/physics-project-template

cd test_project
just bootstrap
conda activate test_project
just check
```

### Cookiecutter escaping rules

Two template engines collide in this repo — cookiecutter (Jinja2) and the tools
that also use `{{` / `}}` syntax (GitHub Actions, just). Escape non-cookiecutter
expressions with cookiecutter's raw literal syntax:

| Raw expression | Escaped in template |
|---------------|-------------------|
| `${{ env.VAR }}` | `${{"{{"}} env.VAR {{"}}"}}` |
| `{{ args }}` (just) | `{{"{{"}}args{{"}}"}}` |

To find any unescaped non-cookiecutter expressions before baking:

```bash
grep -rn "{{" "{{cookiecutter.package_name}}"/ | grep -v "cookiecutter"
```

---

## Known issues and fixes applied

| Issue | Fix |
|-------|-----|
| `ANN101`/`ANN102` removed from ruff | Removed from `ignore` list in `pyproject.toml` |
| `[tool.hatch.build.targets.wheel]` dropped by Jinja2 | Moved immediately after `[build-system]` |
| `${{ env.VAR }}` in `ci.yml` parsed by cookiecutter | Escaped with raw literal syntax |
| `{{ args }}` in `justfile` parsed by cookiecutter | Escaped with raw literal syntax |
| `pre-commit install` fails — not in a git repo | `git init` added to `bootstrap` recipe before `pre-commit install` |
| `".[dev]"` quotes cause uv parse error via conda | Quotes removed in `environment.yml`; dev extras installed explicitly in CI |
| `conda-solver: libmamba` causes exit code 1 on GHA | Line removed from `ci.yml` |
| `docs_dir` path error — mkdocs.yml inside `docs/` | `mkdocs.yml` moved to repo root |
| `api/` nav entry fails — only `.gitkeep` present | Real `api/index.md` with mkdocstrings directive added |