# Rush Lab site

One-page site for Rush Lab (https://rush-lab-site.vercel.app), deployed on
Vercel from this repo.

## Layout

- `index.html`, `logo.png`, `vercel.json`, `robots.txt`, `sitemap.xml`,
  `googleb2dcc8f8a00336b5.html` — the deployed static site, served from the
  repo root.
- `src/index.template.html` + `build.py` — source template and build script.
  Run `python3 build.py <site-url>` to regenerate `index.html` for a new
  domain (rewrites the canonical URL, og:url, and JSON-LD).

## Deploying

Vercel is connected via its GitHub integration: pushes to `main` deploy to
production automatically. No build command is needed (static files are
served as-is); if Vercel prompts for one when linking, leave build/install
commands empty and set the output directory to `.` (repo root).

Keep `googleb2dcc8f8a00336b5.html` and the `google-site-verification` meta
tag in `index.html` in place — both are required for the site's Google
Search Console verification.
