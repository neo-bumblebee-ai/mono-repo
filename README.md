# AI Transition Monorepo

A single, reusable repository to track learning, weekly deliverables, and portfolio projects
over multiple months. Start here, then *promote* any mature project into its own standalone
repo (instructions below).

## Structure
```
ai-transition/
├─ weeks/
│  ├─ week01_python-basics/
│  │  ├─ README.md
│  │  ├─ notebooks/
│  │  └─ src/
│  ├─ week02_pandas-visualization/
│  └─ ...
├─ projects/            # promote mature work here (then split out to its own repo)
│  └─ README.md
├─ eval/                # evaluation assets (golden sets, metrics)
│  └─ README.md
├─ docs/                # diagrams, images for READMEs and LinkedIn/blog
├─ scripts/             # setup, utilities
├─ tests/               # unit/integration tests
├─ .github/workflows/   # CI
├─ requirements.txt
├─ .gitignore
├─ CHANGELOG.md
└─ LICENSE
```

## Workflow
1) Create a new folder under `weeks/` for each week using the template (see below).
2) Commit daily. Tag at the end of each week, e.g., `week01`, `week02`.
3) When a weekly artifact becomes portfolio-grade, copy/move it under `projects/`,
   polish it, and optionally split it into its own repo with history.

### Promote a project to its own repo (with history)
```bash
# From the monorepo root
git subtree split --prefix projects/<project-folder> -b export/<project-name>
git init --bare ../<project-name>.git
git push ../<project-name>.git export/<project-name>:main
```

## Visibility
- Keep `docs/` screenshots and GIFs you embed in LinkedIn/blog posts.
- Use `README_TEMPLATE.md` to ensure every week and project has a clear story.

## Local AI Environment (ai30)

This repo integrates with a local PostgreSQL (pgvector) database for AI experiments.

### Setup
1. Activate your conda environment:
conda activate ai30

2. Start PostgreSQL (if not already running):
pg_ctl -D pgdata -l logfile start

3. Connect via psql:
psql -h localhost -p 5432 -U jigne -d ai30_db

4. Example Python connection:
python projects/db_connect_test.py

Notes:
pgvector is enabled for vector storage and similarity search.
The default table used for embeddings:

CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding VECTOR(1536)
);

Supports integration with psycopg2, NumPy, and OpenAI embeddings for AI use cases.
## License
MIT (adjust if needed).