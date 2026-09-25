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

## Creator application form

The "Join" section (`#join`) is a real form (name, email, WhatsApp, Instagram
handle, city, content link, pitch, plus 18+/availability confirmation
checkboxes) submitted client-side to [Web3Forms](https://web3forms.com/) — a
free form-backend API, so the form itself is 100% Rush Lab's own HTML/CSS
with no third-party branding or watermark.

**To activate it:**
1. Go to https://web3forms.com/, enter an email you check, and get a free
   access key (no account/password needed, free tier is 250 submissions/month).
2. Replace `YOUR_WEB3FORMS_ACCESS_KEY` in **both** `index.html` and
   `src/index.template.html` (the hidden `access_key` input near the top of
   the `#apply-form` form) with the real key.
3. Redeploy. Submissions will then email straight to the inbox tied to that
   key; view/export them anytime at web3forms.com.

Until the key is swapped in, the form will show the "Something went wrong"
error on submit — the Instagram DM link beneath the form still works as a
fallback either way.

If you outgrow the 250/month free tier or want more control (custom
notification routing, spreadsheet export, webhooks), swap the `fetch()`
endpoint in the inline `<script>` for a different backend (e.g. Formspree)
without touching the form's markup or styling.
