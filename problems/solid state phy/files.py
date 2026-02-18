# kittel_scaffold_generator.py
# Creates:
#   ./problems/kittel/ch_1 ... ch_22
# And inside each chapter folder:
#   kittel_ch_<N>_prob_1.html ... kittel_ch_<N>_prob_5.html
#
# Run from your project root (the folder that should contain ./problems/)

from pathlib import Path

BASE = Path("problems") / "kittel"
CH_START = 1
CH_END = 22
PROBS_PER_CH = 5

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="dark" />
  <meta name="theme-color" content="#050608" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #050608;
      --panel: rgba(255,255,255,0.06);
      --text: rgba(255,255,255,0.92);
      --muted: rgba(255,255,255,0.72);
      --border: rgba(255,255,255,0.14);
      --shadow: 0 18px 50px rgba(0,0,0,0.35);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      background:
        radial-gradient(900px 500px at 15% 0%, rgba(120,120,255,0.14), transparent 60%),
        radial-gradient(800px 500px at 100% 10%, rgba(120,255,200,0.10), transparent 55%),
        var(--bg);
      color: var(--text);
      line-height: 1.6;
    }}

    header, main, footer {{
      max-width: 980px;
      margin: 0 auto;
      padding: 22px 16px;
    }}

    .card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: var(--shadow);
      padding: 18px;
    }}

    h1 {{
      margin: 0 0 10px;
      font-size: 1.25rem;
      letter-spacing: 0.2px;
    }}

    p {{
      margin: 0 0 10px;
      color: var(--muted);
    }}

    code {{
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.10);
      padding: 2px 6px;
      border-radius: 8px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }}

    @media (min-width: 820px) {{
      .grid {{ grid-template-columns: 1.2fr 0.8fr; }}
    }}

    .badge {{
      display: inline-block;
      font-size: 0.85rem;
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.12);
      color: rgba(255,255,255,0.82);
    }}
  </style>
</head>
<body>
  <header>
    <div class="card">
      <span class="badge">Kittel • Chapter {ch} • Problem {p}</span>
      <h1>{title}</h1>
      <p>Replace this scaffold with your full solution as a self-contained HTML learning article (no external libraries).</p>
      <p><strong>File path:</strong> <code>./problems/kittel/ch_{ch}/kittel_ch_{ch}_prob_{p}.html</code></p>
    </div>
  </header>

  <main>
    <div class="grid">
      <section class="card">
        <h2 style="margin:0 0 8px; font-size:1.05rem;">Problem</h2>
        <p><em>Paste the problem statement here.</em></p>
      </section>

      <aside class="card">
        <h2 style="margin:0 0 8px; font-size:1.05rem;">Plan</h2>
        <p><em>List givens, unknowns, and the method you’ll use.</em></p>
      </aside>

      <section class="card" style="grid-column: 1 / -1;">
        <h2 style="margin:0 0 8px; font-size:1.05rem;">Solution</h2>
        <p><em>Derivation + final numerical/analytic result.</em></p>
      </section>
    </div>
  </main>

  <footer>
    <div class="card">
      <p style="margin:0;">© Your site • Kittel problem scaffold</p>
    </div>
  </footer>
</body>
</html>
"""

def safe_write(path: Path, content: str) -> bool:
    """Write only if file doesn't exist. Returns True if created."""
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True

def main():
    BASE.mkdir(parents=True, exist_ok=True)

    created_files = 0
    skipped_files = 0
    created_dirs = 0

    for ch in range(CH_START, CH_END + 1):
        ch_dir = BASE / f"ch_{ch}"
        if not ch_dir.exists():
            ch_dir.mkdir(parents=True, exist_ok=True)
            created_dirs += 1

        for p in range(1, PROBS_PER_CH + 1):
            fname = f"kittel_ch_{ch}_prob_{p}.html"
            fpath = ch_dir / fname
            title = f"Kittel Chapter {ch} — Problem {p}"
            html = HTML_TEMPLATE.format(ch=ch, p=p, title=title)

            if safe_write(fpath, html):
                created_files += 1
            else:
                skipped_files += 1

    print("Kittel scaffold generation complete.")
    print(f"Base folder: {BASE.resolve()}")
    print(f"Directories created: {created_dirs}")
    print(f"HTML files created: {created_files}")
    print(f"HTML files skipped (already existed): {skipped_files}")

if __name__ == "__main__":
    main()
