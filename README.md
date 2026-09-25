# Rush Lab site

One-page site for Rush Lab (https://rush-lab-site.vercel.app), deployed on
Vercel from this repo.

## Layout

- `index.html`, `logo.png`, `vercel.json`, `robots.txt`, `sitemap.xml`,
  `googleb2dcc8f8a00336b5.html`, `49a5cfd4fa7cfcba6d191347d641bdbc.txt` — the
  deployed static site, served from the repo root.
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

## SEO / technical notes

- `49a5cfd4fa7cfcba6d191347d641bdbc.txt` is an IndexNow key file (the
  filename must stay identical to its contents). Once the site is live at
  its final domain, submit URLs via a GET to
  `https://api.indexnow.org/indexnow?url=<page>&key=49a5cfd4fa7cfcba6d191347d641bdbc`
  to get faster (non-Google) indexing on Bing/Yandex/Seznam.cz. Google does
  not consume IndexNow.
- `vercel.json` sets security headers (CSP, HSTS, X-Frame-Options,
  Permissions-Policy) on every response. If you add external resources
  (scripts, fonts, embeds) to `index.html`, update the
  `Content-Security-Policy` value in both `vercel.json` and `build.py` to
  allow the new host, or the browser will block it.
- `index.html` and `src/index.template.html` must be kept in sync by hand
  for anything outside the `{{SITE_URL}}`-templated bits (title, meta
  description, OG/Twitter tags, JSON-LD). `build.py <site-url>` only
  rewrites the canonical/og:url/JSON-LD `logo` URL from the template; it
  does not diff the two files.
