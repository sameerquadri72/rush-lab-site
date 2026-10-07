# Rush Lab site

One-page site for Rush Lab (https://rushlab.online), deployed on Vercel from
this repo. The old `rush-lab-site.vercel.app` / `rush-lab-site-sams-projects-79b14c62.vercel.app`
URLs still work but 301-redirect to the custom domain (see `vercel.json`).

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
tag in `index.html` in place — they verify the *old* `rush-lab-site.vercel.app`
Search Console property. The custom domain `rushlab.online` is a separate
property and needs its own verification (DNS TXT at Namecheap is easiest
since it covers the apex + `www` + any future subdomain in one shot) — add
it in Search Console under a new "Domain" property.

## Custom domain (rushlab.online)

Bought via Namecheap, attached to the `rush-lab-site` Vercel project
(`rushlab.online` + `www.rushlab.online` → redirects to the apex). DNS is
still hosted at Namecheap (nameservers unchanged), so these records need to
exist in Namecheap's **Advanced DNS** tab for the domain to resolve to
Vercel:

| Type | Host | Value | TTL |
|---|---|---|---|
| A | `@` | `76.76.21.21` | Automatic |
| CNAME | `www` | `cname.vercel-dns.com.` | Automatic |

Remove any existing Namecheap "Parking Page" A/CNAME records for `@`/`www`
first — Vercel's won't take effect if they're still there. DNS propagation
can take a few minutes up to ~24h; `https://rushlab.online` will start
working once it does. Vercel auto-issues the SSL certificate once DNS
resolves correctly — no action needed for that part.

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

The "Join" section (`#join`) is Rush Lab's own HTML/CSS form (no third-party
branding), submitted client-side via `fetch()` to
[Web3Forms](https://web3forms.com/) (free tier: 250 submissions/month). The
access key is already wired in and live.

Fields: first name, last name, email, WhatsApp number, Instagram username
and city (all required), plus an optional link to a video/reel. A
highlighted callout above the fields tells applicants they don't need
Instagram or any social media to apply — the Instagram field stays required
as a text input, so someone without one just types "N/A".

Submissions email straight to the inbox behind the access key; view/export
them anytime at web3forms.com. The Instagram DM link beneath the form
remains as a fallback. If you outgrow the 250/month free tier or want more
control (custom notification routing, spreadsheet export, webhooks), swap
the `fetch()` endpoint in the inline `<script>` for a different backend
without touching the form's markup or styling.
