import os
from pathlib import Path
from datetime import datetime

# =========================
# CONFIG
# =========================
ROOT = Path("problems") / "photonics"

# Minimal, safe tags builder
def tags_for(ch: int, extra: str = "") -> str:
    base = f"photonics ch{ch}"
    extra = extra.strip()
    return (base + (" " + extra if extra else "")).strip()

# Turn "14.3-3" -> ("14","3","3") and filename "prob_14_3_3.html"
def parse_pid(pid: str):
    # pid like "14.3-3"
    left, right = pid.split("-")
    ch, sec = left.split(".")
    prob = right
    return int(ch), int(sec), int(prob)

def filename_from_pid(pid: str) -> str:
    ch, sec, pr = parse_pid(pid)
    return f"prob_{ch}_{sec}_{pr}.html"

def chapter_folder(ch: int) -> Path:
    return ROOT / f"ch{ch}"

def href_for(pid: str) -> str:
    ch, _, _ = parse_pid(pid)
    return f"./problems/photonics/ch{ch}/{filename_from_pid(pid)}"

# =========================
# PROBLEMS LIST (from your message)
# Only include ones you want cards/files for.
# =========================
PROBLEMS = [
    # ---- CH14 ----
    ("14.3-3", "Comparison of Stimulated and Spontaneous Emission"),
    ("14.3-4", "Spontaneous Emission into Prescribed Modes"),
    ("14.4-2", "Rate Equations for Broadband Radiation"),
    ("14.4-3", "Inhibited Spontaneous Emission"),
    ("14.4-4", "Comparison of Stimulated and Spontaneous Emission in Blackbody Radiation"),
    ("14.4-5", "Wien’s Law"),
    ("14.4-6", "Spectral Energy Density of One-Dimensional Blackbody Radiation"),
    ("14.4-7", "Stefan–Boltzmann Law"),
    ("14.5-1", "Statistics of Cathodoluminescence Light"),

    # ---- CH15 ----
    ("15.1-2", "Amplifier Gain and Rod Length"),
    ("15.1-3", "Laser Amplifier Gain and Population Difference"),
    ("15.1-4", "Amplification of a Broadband Signal"),
    ("15.2-4", "Two-Level Pumping System"),
    ("15.2-5", "Two Laser Lines"),
    ("15.4-3", "Significance of the Saturation Photon-Flux Density"),
    ("15.4-4", "Saturation Optical Intensity"),
    ("15.4-5", "Growth of the Photon-Flux Density in a Saturated Laser Amplifier"),
    ("15.4-6", "Resonant Absorption of a Medium in Thermal Equilibrium"),
    ("15.4-7", "Gain in a Saturated Amplifying Medium"),
    ("15.5-2", "Ratio of Signal Power to ASE Power"),
    ("15.5-3", "Photon-Number Distribution for Amplified Coherent Light"),

    # ---- CH16 ----
    ("16.2-2", "Number of Longitudinal Modes"),
    ("16.2-3", "Frequency Drift of the Laser Modes"),
    ("16.2-4", "Mode Control Using an Etalon"),
    ("16.2-5", "Modal Powers in a Multimode Laser"),
    ("16.2-6", "Output of a Single-Mode Gas Laser"),
    ("16.2-7", "Transmittance of a Laser Resonator"),
    ("16.2-8", "Rate Equations for a Four-Level Laser"),
    ("16.3-1", "Operation of an Ytterbium-Doped YAG Laser"),
    ("16.3-2", "Threshold Population Difference for an Ar+-Ion Laser"),
    ("16.3-3", "Spontaneous Lifetime of an EUV Transition"),
    ("16.4-4", "Transients in a Gain-Switched Laser"),
    ("16.4-5", "Q-Switched Ruby Laser Power"),
    ("16.4-6", "Operation of a Cavity-Dumped Laser"),
    ("16.4-7", "Mode Locking with Lorentzian Amplitudes"),
    ("16.4-8", "Second-Harmonic Generation"),

    # ---- CH17 ----
    ("17.1-6", "Donor-Electron Ionization Energies and Radii"),
    ("17.1-7", "Fermi Level of an Intrinsic Semiconductor"),
    ("17.1-8", "Electron–Hole Recombination Under Strong Injection"),
    ("17.1-9", "Bowing Parameters for Ternary Semiconductors"),
    ("17.1-10", "Energy Levels in a GaAs/AlGaAs Quantum Well"),
    ("17.2-3", "Validity of the Approximation for Absorption/Emission Rates"),
    ("17.2-4", "Peak Spontaneous Emission Rate in Thermal Equilibrium"),
    ("17.2-5", "Radiative Recombination Rate in Thermal Equilibrium"),

    # ---- CH18 ----
    ("18.1-5", "LED Spectral Widths"),
    ("18.1-6", "Extraction Efficiency for an LED"),
    ("18.1-7", "Coupling Light from an LED into an Optical Fiber"),
    ("18.2-1", "Bandwidth of a Semiconductor Optical Amplifier"),
    ("18.2-2", "Peak Gain Coefficient of a Semiconductor Optical Amplifier at T = 0° K"),
    ("18.2-3", "Gain Coefficient of a GaAs Semiconductor Optical Amplifier"),
    ("18.2-4", "Bandgap Reduction Arising from Band-Tail States"),
    ("18.2-5", "Amplifier Gain and Bandwidth"),
    ("18.2-6", "Transition Cross Section"),
    ("18.2-7", "Gain Profile"),
    ("18.3-1", "Dependence of Laser-Diode Output Power on Refractive Index"),
    ("18.3-2", "Number of Longitudinal Modes"),
    ("18.3-3", "Minimum Gain Required for Lasing"),
    ("18.3-4", "Modal Spacings with a Wavelength-Dependent Refractive Index"),

    # ---- CH19 ----
    ("19.1-1", "Effect of Reflectance on Quantum Efficiency"),
    ("19.1-2", "Maximum Responsivity"),
    ("19.1-3", "Transit Time Current and Duration for a Single Carrier Pair"),
    ("19.1-4", "Transit-Time Spread for a Uniformly Illuminated Semiconductor Photodetector"),
    ("19.1-5", "Two-Photon Photodetectors"),
    ("19.2-1", "Photoconductive Detector Circuit"),
    ("19.2-2", "Photoconductivity in Intrinsic Si"),
    ("19.3-1", "Quantum Efficiency and Responsivity of a Photodiode Detector"),
    ("19.4-1", "Quantum Efficiency of an APD"),
    ("19.4-2", "Gain of a Ge APD"),
    ("19.6-1", "Comparison of Excess Noise Factors for SCISCM and SCIDCM Conventional APDs"),
    ("19.6-2", "Mean Gain of a Staircase APD"),
    ("19.6-3", "Excess Noise Factor for a Photomultiplier Tube"),
    ("19.6-4", "Excess Noise Factor for a Photoconductive Detector"),
    ("19.6-5", "Bandwidth of an RC Circuit"),
    ("19.6-6", "Signal-to-Noise Ratio for an Analog APD Receiver"),
    ("19.6-7", "Noise in an Analog APD Receiver"),
    ("19.6-8", "Optimal Gain for an APD in an Analog Receiver"),
    ("19.6-9", "Analog Receiver Sensitivity"),
    ("19.6-10", "Noise Comparison for Three Photodetectors"),
    ("19.6-11", "Sensitivity of an AM Receiver"),
    ("19.6-12", "Dependence of Digital Receiver Sensitivity on Wavelength"),
    ("19.6-13", "Bit Error Rate for a Digital Receiver"),
    ("19.6-14", "Sensitivity of a Photon-Counting Receiver"),
    ("19.6-15", "Single-Dynode PMT Illuminated by Photon-Number-Squeezed Light"),
]

# =========================
# HTML TEMPLATE for each theory file
# (Simple + clean; you can later replace with your advanced interactive template)
# =========================
def theory_html(pid: str, title: str) -> str:
    ch, sec, pr = parse_pid(pid)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    safe_id = pid.replace(".", "_").replace("-", "_")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="dark" />
  <meta name="theme-color" content="#050608" />
  <title>{pid} — {title}</title>
  <style>
    :root {{
      --bg: #050608;
      --panel: rgba(255,255,255,0.06);
      --text: rgba(255,255,255,0.92);
      --muted: rgba(255,255,255,0.72);
      --stroke: rgba(255,255,255,0.10);
      --accent: #7ee7ff;
      --accent2: #a7ffb6;
      --shadow: 0 18px 60px rgba(0,0,0,0.45);
      --radius: 18px;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      background: radial-gradient(1200px 700px at 20% -10%, rgba(126,231,255,0.10), transparent 60%),
                  radial-gradient(1000px 700px at 90% 10%, rgba(167,255,182,0.08), transparent 60%),
                  var(--bg);
      color: var(--text);
    }}
    header {{
      padding: 28px 18px 10px;
      max-width: 1050px;
      margin: 0 auto;
    }}
    .crumbs {{
      font-size: 13px;
      color: var(--muted);
      opacity: 0.9;
    }}
    .crumbs a {{ color: var(--muted); text-decoration: none; border-bottom: 1px dotted transparent; }}
    .crumbs a:hover {{ border-bottom-color: var(--muted); }}
    h1 {{
      margin: 10px 0 6px;
      font-size: clamp(22px, 2.5vw, 34px);
      letter-spacing: 0.2px;
    }}
    .subtitle {{
      color: var(--muted);
      margin: 0 0 12px;
      line-height: 1.5;
    }}
    main {{
      max-width: 1050px;
      margin: 0 auto;
      padding: 0 18px 34px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--stroke);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 16px;
    }}
    .row {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 12px;
    }}
    @media (max-width: 880px) {{
      .row {{ grid-template-columns: 1fr; }}
    }}
    h2 {{
      margin: 0 0 10px;
      font-size: 18px;
    }}
    .mono {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      color: rgba(255,255,255,0.86);
      font-size: 13px;
      white-space: pre-wrap;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      border-radius: 999px;
      padding: 10px 14px;
      text-decoration: none;
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(255,255,255,0.06);
      color: rgba(255,255,255,0.9);
      transition: transform 0.15s ease, background 0.15s ease, border-color 0.15s ease;
      cursor: pointer;
    }}
    .btn:hover {{
      transform: translateY(-1px);
      background: rgba(255,255,255,0.09);
      border-color: rgba(255,255,255,0.22);
    }}
    footer {{
      max-width: 1050px;
      margin: 0 auto;
      padding: 0 18px 30px;
      color: var(--muted);
      font-size: 12px;
    }}
    .pill {{
      display: inline-flex;
      gap: 8px;
      align-items: center;
      padding: 6px 10px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(255,255,255,0.05);
      color: rgba(255,255,255,0.85);
      font-size: 12px;
    }}
  </style>
</head>
<body>
  <header>
    <div class="crumbs">
      <a href="../../index.html">Home</a> / <a href="../../photonics.html">Photonics</a> / <span>ch{ch}</span>
    </div>
    <h1>{pid} — {title}</h1>
    <p class="subtitle">Theory page template. Replace placeholders with your full derivation + figures + simulations.</p>
    <div class="pill">ID: <span class="mono">{safe_id}</span> · Generated: {now}</div>
  </header>

  <main>
    <section class="card">
      <h2>Problem Statement</h2>
      <div class="mono">TODO: Paste the full statement for {pid} here.</div>
    </section>

    <section class="row">
      <article class="card">
        <h2>Given / Parameters</h2>
        <div class="mono">TODO: List given quantities, units, constants.</div>
      </article>
      <article class="card">
        <h2>Target / What to Find</h2>
        <div class="mono">TODO: List requested outputs (probability density, time constant, etc.).</div>
      </article>
    </section>

    <section class="card">
      <h2>Solution Outline</h2>
      <div class="mono">TODO:
1) Identify relevant formulas (Einstein A/B, mode density, gain, etc.)
2) Apply lineshape + cavity mode density if needed
3) Compute numeric results
4) Sanity-check units + scaling</div>
    </section>

    <section class="card">
      <h2>Final Answer</h2>
      <div class="mono">TODO: Put final numeric answer(s) with units.</div>
      <button class="btn" onclick="navigator.clipboard.writeText(document.querySelector('#final').innerText)">Copy Final</button>
      <div id="final" class="mono" style="margin-top:10px;">TODO: Final answer block for copy.</div>
    </section>
  </main>

  <footer>
    <div>Tip: keep filenames lowercase + underscores only (GitHub Pages safe).</div>
  </footer>
</body>
</html>
"""

# =========================
# Generate files + cards
# =========================
def main():
    ROOT.mkdir(parents=True, exist_ok=True)

    cards = []
    for pid, title in PROBLEMS:
        ch, sec, pr = parse_pid(pid)

        # Folder
        folder = chapter_folder(ch)
        folder.mkdir(parents=True, exist_ok=True)

        # File
        out_file = folder / filename_from_pid(pid)
        if not out_file.exists():
            out_file.write_text(theory_html(pid, title), encoding="utf-8")

        # Card
        # You can tweak tags per chapter/topic later
        extra_tags = title.lower().replace("–", " ").replace("’", "").replace(",", "")
        extra_tags = " ".join([w for w in extra_tags.split() if len(w) > 2][:8])  # short, safe
        card = f'''<article class="card" data-tags="{tags_for(ch, extra_tags)}">
  <h3>{pid} — {title}</h3>
  <p>Auto-generated theory page template (you will fill solution + plots later).</p>
  <a href="{href_for(pid)}">OPEN THEORY</a>
</article>'''
        cards.append(card)

    # Write all cards in one paste-ready file
    cards_out = Path("photonics_cards_generated.html")
    cards_out.write_text("\n\n".join(cards) + "\n", encoding="utf-8")

    print("Done.")
    print(f"- Generated folders/files under: {ROOT}")
    print(f"- Generated cards file: {cards_out.resolve()}")

if __name__ == "__main__":
    main()
