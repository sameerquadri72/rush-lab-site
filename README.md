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

The "Join" section (`#join`) embeds a [forms.app](https://forms.app/) form
(free plan: unlimited responses, up to 5 forms) via their JS embed widget,
loaded from `https://forms.app/cdn/embed.js`. Unlike a plain HTML form, the
actual fields live on forms.app's platform, not in this repo — the site only
holds the embed snippet.

**To activate it:**
1. Sign up free at https://forms.app/ and build a form with these fields
   (matching what the site used to collect directly): full name, email,
   WhatsApp number, Instagram handle, city, link to best video/reel
   (optional), a short "why should you be on Rush Lab" text field
   (optional), and two checkboxes — 18+ confirmation and "can attend
   in-person filming / agree to be featured."
2. In forms.app, open **Share → Embed → Inline**, copy the generated
   `<script>...onload="new formsapp(...)"...</script>` snippet.
3. In **both** `index.html` and `src/index.template.html`, replace the
   placeholder script tag inside `#apply-form-embed`'s section — swap
   `YOUR_FORMS_APP_FORM_ID` and `https://YOUR_ACCOUNT.forms.app` for the real
   form ID and account subdomain from that snippet.
4. Redeploy. View/export responses anytime from the forms.app dashboard;
   free-plan integrations (Google Sheets, Slack, webhooks, Zapier, etc.) can
   route them further from there.

Until the placeholders are swapped in, the embed will fail to load silently
— the Instagram DM link beneath it still works as a fallback either way.

Note: unlike the site's own HTML, the form itself renders as forms.app's own
widget (colors/logo are themeable in their editor, but it isn't literally
Rush Lab's markup). If `Content-Security-Policy` in `vercel.json`/`build.py`
ever needs loosening further for forms.app (e.g. a different embed layout),
update both files together.
