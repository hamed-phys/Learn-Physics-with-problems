from pathlib import Path

BASE = Path("./problems/photonics")
OVERWRITE = False  # set True if you want to overwrite existing files

PROBLEM_CODES = [
    # ---- CH10 ----
    ("ch10", "10.1-1"), ("ch10", "10.1-2"),
    ("ch10", "10.2-1"), ("ch10", "10.2-2"), ("ch10", "10.2-3"),
    ("ch10", "10.2-4"), ("ch10", "10.2-5"),
    ("ch10", "10.3-3"), ("ch10", "10.3-4"), ("ch10", "10.3-5"), ("ch10", "10.3-6"),

    # ---- CH11 ----
    ("ch11", "11.1-3"), ("ch11", "11.1-4"), ("ch11", "11.1-5"), ("ch11", "11.1-6"),
    ("ch11", "11.2-5"), ("ch11", "11.2-6"), ("ch11", "11.2-7"), ("ch11", "11.2-8"),
    ("ch11", "11.2-9"), ("ch11", "11.2-10"), ("ch11", "11.2-11"), ("ch11", "11.2-12"),
    ("ch11", "11.3-2"),

    # ---- CH12 ----
    ("ch12", "12.1-4"), ("ch12", "12.1-5"), ("ch12", "12.1-6"), ("ch12", "12.1-7"),
    ("ch12", "12.1-8"), ("ch12", "12.1-9"), ("ch12", "12.1-10"),
    ("ch12", "12.2-1"), ("ch12", "12.2-2"), ("ch12", "12.2-3"),
    ("ch12", "12.3-1"), ("ch12", "12.3-2"), ("ch12", "12.3-3"), ("ch12", "12.3-4"),
    ("ch12", "12.4-2"),

    # ---- CH13 ----
    ("ch13", "13.1-5"), ("ch13", "13.1-6"), ("ch13", "13.1-7"), ("ch13", "13.1-8"),
    ("ch13", "13.1-9"), ("ch13", "13.1-10"), ("ch13", "13.1-11"), ("ch13", "13.1-12"),
    ("ch13", "13.2-2"), ("ch13", "13.2-3"), ("ch13", "13.2-4"), ("ch13", "13.2-5"),
    ("ch13", "13.2-6"), ("ch13", "13.2-7"), ("ch13", "13.2-8"), ("ch13", "13.2-9"),
    ("ch13", "13.2-10"), ("ch13", "13.2-11"), ("ch13", "13.2-12"),
    ("ch13", "13.3-1"), ("ch13", "13.3-2"),
]

def code_to_filename(code: str) -> str:
    # "10.3-6" -> "prob_10.3_6_saleh.html"
    return f"prob_{code.replace('-', '_')}_saleh.html"

def minimal_html(title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
</head>
<body>
  <h1>{title}</h1>
  <p>TODO: write solution.</p>
</body>
</html>
"""

def main():
    created = 0
    skipped = 0

    for ch, code in PROBLEM_CODES:
        out_dir = BASE / ch
        out_dir.mkdir(parents=True, exist_ok=True)

        path = out_dir / code_to_filename(code)

        if path.exists() and not OVERWRITE:
            skipped += 1
            continue

        path.write_text(minimal_html(f"{code} (Saleh)"), encoding="utf-8")
        created += 1

    print(f"✅ Created: {created}")
    print(f"⏭️ Skipped (already existed): {skipped}")
    print(f"📁 Base folder: {BASE.resolve()}")

if __name__ == "__main__":
    main()
