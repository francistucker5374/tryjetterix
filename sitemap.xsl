<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>tryjetterix.com &#8211; XML Sitemap</title><link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<style>
  :root{--ink:#06222a;--mut:#4f6e78;--line:#d6e7ea;--bg:#eef9f9;--blue:#0a96ac;--blue2:#06748a;--mint:#14ccae}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:1000px;margin:0 auto;padding:0 18px 50px}
  body{font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  header{background:linear-gradient(120deg,#06748a,#0a96ac);color:#fff;padding:30px 18px} header .in{max-width:1000px;margin:0 auto}
  .logo .dot{border-radius:50% 50% 50% 0!important;transform:rotate(45deg)}
  .logo{font-weight:800;font-size:22px;letter-spacing:-.02em;display:flex;align-items:center;gap:9px}
  .logo .dot{width:11px;height:11px;border-radius:50%;background:#19c2e6;box-shadow:0 0 0 4px rgba(255,255,255,.25)}
  h1{font-size:20px;margin:14px 0 4px} header p{margin:0;opacity:.9;font-size:14px}
  .card{background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 10px 30px rgba(16,40,70,.07);margin-top:-18px;overflow:hidden}
  table{width:100%;border-collapse:collapse;font-size:13.5px} th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line)}
  th{background:#fbfdff;color:var(--mut);font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:700}
  tr:last-child td{border-bottom:0} tbody tr:hover{background:#f3f9fd} td.idx{color:var(--mut);width:40px}
  a{color:var(--blue2);text-decoration:none;font-weight:600} a:hover{text-decoration:underline}
  .pill{display:inline-block;background:#eaf6fc;color:var(--blue2);border:1px solid #d4ebf7;font-size:11.5px;font-weight:700;padding:2px 9px;border-radius:999px}
  .pri{display:inline-block;min-width:38px;text-align:center;background:#e9fbf3;color:#0a7a55;border:1px solid #c7f0e0;font-weight:700;font-size:12px;padding:2px 8px;border-radius:7px}
  .foot{color:var(--mut);font-size:12.5px;margin-top:16px} @media(max-width:640px){.hideS{display:none}}
</style></head><body>
<header><div class="in"><div class="logo"><span class="dot"></span>Jetterix</div><h1>XML Sitemap</h1>
<p><xsl:value-of select="count(s:urlset/s:url)"/> indexed pages &#183; Jetterix review network</p></div></header>
<div class="wrap"><div class="card"><table>
  <thead><tr><th class="idx">#</th><th>URL</th><th>Languages</th><th class="hideS">Last modified</th><th class="hideS">Frequency</th><th>Priority</th></tr></thead>
  <tbody><xsl:for-each select="s:urlset/s:url"><tr>
    <td class="idx"><xsl:value-of select="position()"/></td>
    <td><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></td>
    <td><span class="pill"><xsl:value-of select="count(xhtml:link)"/> hreflang</span></td>
    <td class="hideS"><xsl:value-of select="s:lastmod"/></td>
    <td class="hideS"><xsl:value-of select="s:changefreq"/></td>
    <td><span class="pri"><xsl:value-of select="s:priority"/></span></td>
  </tr></xsl:for-each></tbody>
</table></div><p class="foot">Machine-readable sitemap for search crawlers &#183; tryjetterix.com</p></div>
</body></html></xsl:template></xsl:stylesheet>
