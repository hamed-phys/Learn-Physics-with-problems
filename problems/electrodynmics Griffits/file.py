import os

# ✅ New target folder (your updated path)
folder_path = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\electrodynmics Griffits"

# Ensure folder exists
os.makedirs(folder_path, exist_ok=True)

# Create files 1.1 to 1.17
for i in range(1, 18):
    filename = f"Griffits_1.{i}.html"
    file_path = os.path.join(folder_path, filename)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Electrodynamics — Griffiths 4th — Problem 1.{i}</title>
</head>
<body>

  <h1>Electrodynamics — Griffiths 4th</h1>
  <h2>Problem 1.{i}</h2>

  <section>
    <h3>Problem Statement</h3>
    <p>
      <!-- Paste the original problem text here -->
    </p>
  </section>

  <section>
    <h3>Solution</h3>
    <p>
      <!-- Write the full solution here -->
    </p>
  </section>

</body>
</html>
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print("✅ All Griffiths Problem 1.1 to 1.17 HTML files created successfully.")