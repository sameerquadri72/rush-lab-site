#!/usr/bin/env python3
"""Build the Rush Lab one-page site into ./dist.

Usage:
  python3 build.py                      # no canonical, no sitemap (works on any domain)
  python3 build.py https://rush-lab.vercel.app   # adds canonical, og:url, sitemap.xml
"""
import re
import shutil
import sys
from pathlib import Path

root = Path(__file__).parent
dist = root / "dist"
site = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else None

html = (root / "src" / "index.template.html").read_text(encoding="utf-8")
if site:
    html = html.replace("{{SITE_URL}}", site)
    html = html.replace("<!--CANONICAL-->", "").replace("<!--/CANONICAL-->", "")
else:
    html = re.sub(r"<!--CANONICAL-->.*?<!--/CANONICAL-->", "", html, flags=re.S)

if dist.exists():
    shutil.rmtree(dist)
dist.mkdir()
(dist / "index.html").write_text(html, encoding="utf-8")

for f in root.glob("google*.html"):
    shutil.copy(f, dist / f.name)

for f in root.glob("[0-9a-f]" * 32 + ".txt"):
    shutil.copy(f, dist / f.name)

for name in ("logo.png",):
    if (root / name).exists():
        shutil.copy(root / name, dist / name)

robots = "User-agent: *\nAllow: /\n"
if site:
    robots += f"\nSitemap: {site}/sitemap.xml\n"
(dist / "robots.txt").write_text(robots, encoding="utf-8")

if site:
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>{site}/</loc>
    <lastmod>2026-09-24</lastmod>
    <video:video>
      <video:thumbnail_loc>https://i.ytimg.com/vi/yWdmJB05FNM/maxresdefault.jpg</video:thumbnail_loc>
      <video:title>Rush Lab Creators Challenge, Part 1: 12 Creators Compete for ₹20,000 in 8 Challenges</video:title>
      <video:description>12 creators compete in 8 challenges for a ₹20,000 cash prize in the first Rush Lab Creators Challenge. Part 1 covers the Wall Climb and the Rope Course.</video:description>
      <video:player_loc>https://www.youtube.com/embed/yWdmJB05FNM</video:player_loc>
      <video:duration>1367</video:duration>
      <video:publication_date>2026-09-21</video:publication_date>
    </video:video>
  </url>
</urlset>
"""
    (dist / "sitemap.xml").write_text(sitemap, encoding="utf-8")

(dist / "vercel.json").write_text(
    """{
  "rewrites": [
    { "source": "/favicon.ico", "destination": "/logo.png" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; script-src 'self' 'unsafe-inline' https://forms.app; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' https://forms.app https://*.forms.app; frame-src https://www.youtube.com https://forms.app https://*.forms.app; connect-src 'self' https://forms.app https://*.forms.app; base-uri 'self'; form-action 'self'; object-src 'none'; frame-ancestors 'self'; upgrade-insecure-requests" }
      ]
    }
  ]
}
""",
    encoding="utf-8",
)
print("built", dist, "site=", site)
