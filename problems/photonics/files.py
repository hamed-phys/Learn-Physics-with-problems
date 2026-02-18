# photonics_file_generator_ch20_to_ch25.py
# Run this from your project root (the folder that contains ./problems/)

from pathlib import Path

BASE = Path("problems") / "photonics"

FILES = [
  # --- Chapter 20 ---
  ("ch20", "prob_20_1_1.html", "20.1-1 — Diffraction of Light from Various Periodic Structures"),
  ("ch20", "prob_20_1_2.html", "20.1-2 — Bragg Diffraction as a Scattering Process"),
  ("ch20", "prob_20_1_3.html", "20.1-3 — Condition for Raman–Nath Diffraction"),
  ("ch20", "prob_20_1_4.html", "20.1-4 — Combined Acousto-Optic and Electro-Optic Modulation"),
  ("ch20", "prob_20_2_4.html", "20.2-4 — Choice of Materials for Acousto-Optic Modulators"),
  ("ch20", "prob_20_2_5.html", "20.2-5 — Frequency Shifting with a Bragg Reflector"),
  ("ch20", "prob_20_2_6.html", "20.2-6 — Frequency-Shift-Free Bragg Reflector"),
  ("ch20", "prob_20_3_2.html", "20.3-2 — Front Bragg Diffraction"),

  # --- Chapter 21 ---
  ("ch21", "prob_21_1_2.html", "21.1-2 — Response Time of a Phase Modulator"),
  ("ch21", "prob_21_1_3.html", "21.1-3 — Sensitivity of an Interferometric Electro-Optic Intensity Modulator"),
  ("ch21", "prob_21_1_4.html", "21.1-4 — An Elasto-Optic Strain Sensor"),
  ("ch21", "prob_21_1_5.html", "21.1-5 — Magneto-Optic Modulator"),
  ("ch21", "prob_21_2_2.html", "21.2-2 — Silica Integrated-Photonic Phase Modulator"),
  ("ch21", "prob_21_2_3.html", "21.2-3 — Cascaded Phase Modulators"),
  ("ch21", "prob_21_2_4.html", "21.2-4 — The “Push–Pull” Intensity Modulator"),
  ("ch21", "prob_21_2_5.html", "21.2-5 — A LiNbO3 Integrated-Photonic Intensity Modulator"),
  ("ch21", "prob_21_2_6.html", "21.2-6 — Double Refraction in an Electro-Optic Crystal"),

  # --- Chapter 22 ---
  ("ch22", "prob_22_2_2.html", "22.2-2 — Power Exchange in Frequency Up-Conversion"),
  ("ch22", "prob_22_2_3.html", "22.2-3 — Matching Conditions for Collinear Type-II SHG"),
  ("ch22", "prob_22_2_4.html", "22.2-4 — Phase Matching in a Degenerate Parametric Downconverter"),
  ("ch22", "prob_22_2_5.html", "22.2-5 — Matching Conditions for Three-Wave Mixing in a Dispersive Medium"),
  ("ch22", "prob_22_2_6.html", "22.2-6 — Tolerance to Phase Mismatching"),
  ("ch22", "prob_22_2_7.html", "22.2-7 — Backward SHG with QPM"),
  ("ch22", "prob_22_3_4.html", "22.3-4 — Invariants in Four-Wave Mixing"),
  ("ch22", "prob_22_3_5.html", "22.3-5 — Power of a Spatial Soliton"),
  ("ch22", "prob_22_3_6.html", "22.3-6 — An Opto-Optic Phase Modulator"),
  ("ch22", "prob_22_3_7.html", "22.3-7 — SHG in a Third-Order Nonlinear Medium via a Static Electric Field"),
  ("ch22", "prob_22_4_7.html", "22.4-7 — Gain of a Parametric Amplifier"),
  ("ch22", "prob_22_4_8.html", "22.4-8 — Degenerate Parametric Downconverter"),
  ("ch22", "prob_22_4_9.html", "22.4-9 — Threshold Pump Intensity for Parametric Oscillation"),
  ("ch22", "prob_22_5_2.html", "22.5-2 — Combined SHG and SFG"),
  ("ch22", "prob_22_5_3.html", "22.5-3 — Coupled-Wave Equations for Degenerate Four-Wave Mixing"),
  ("ch22", "prob_22_6_1.html", "22.6-1 — Collinear Type-II Three-Wave Mixing in a BBO Crystal"),
  ("ch22", "prob_22_6_2.html", "22.6-2 — Relation Between Nonlinear-Optical and Electro-Optic Coefficients"),

  # --- Chapter 23 ---
  ("ch23", "prob_23_1_1.html", "23.1-1 — Superposition of Two Gaussian Pulses"),
  ("ch23", "prob_23_1_2.html", "23.1-2 — The Hyperbolic-Secant Pulse"),
  ("ch23", "prob_23_2_1.html", "23.2-1 — Thick-Prism Chirp Filter"),
  ("ch23", "prob_23_2_2.html", "23.2-2 — Bragg-Grating Chirp Filter"),
  ("ch23", "prob_23_3_3.html", "23.3-3 — Propagation of a Rectangular Pulse Through an Optical Fiber"),
  ("ch23", "prob_23_3_4.html", "23.3-4 — Temporal Imaging with a Time Lens"),
  ("ch23", "prob_23_5_1.html", "23.5-1 — Mixing of Pulsed Chirped Waves and Chirp Amplification"),
  ("ch23", "prob_23_5_2.html", "23.5-2 — Pulsed Three-Wave Mixing in a Medium with GVD"),
  ("ch23", "prob_23_5_3.html", "23.5-3 — Dependence of Soliton Characteristics on Group Velocity Dispersion"),
  ("ch23", "prob_23_5_4.html", "23.5-4 — Solitons in an Optical Fiber"),
  ("ch23", "prob_23_6_1.html", "23.6-1 — Measurement of a Gaussian Pulse"),
  ("ch23", "prob_23_6_2.html", "23.6-2 — Interferometer with a Two-Photon Absorbing Detector"),

  # --- Chapter 24 ---
  ("ch24", "prob_24_1_3.html", "24.1-3 — Interconnection Hologram for a Conformal Map"),
  ("ch24", "prob_24_2_1.html", "24.2-1 — Cascaded MZI MUX/DMUX"),
  ("ch24", "prob_24_2_2.html", "24.2-2 — AWG DMUX"),
  ("ch24", "prob_24_2_3.html", "24.2-3 — AWG as a 2×2 Wavelength Router"),
  ("ch24", "prob_24_3_1.html", "24.3-1 — Power Loss and Crosstalk"),
  ("ch24", "prob_24_3_2.html", "24.3-2 — MZI Crossbar Switch"),
  ("ch24", "prob_24_3_3.html", "24.3-3 — TSI Switch"),
  ("ch24", "prob_24_4_2.html", "24.4-2 — Photonic Logic Gate"),
  ("ch24", "prob_24_4_3.html", "24.4-3 — Bistable Interferometer"),

  # --- Chapter 25 ---
  ("ch25", "prob_25_1_1.html", "25.1-1 — Optical Fiber Communication Systems"),
  ("ch25", "prob_25_1_2.html", "25.1-2 — Components for Optical Fiber Communication Systems"),
  ("ch25", "prob_25_2_1.html", "25.2-1 — Performance of a Plastic Fiber Link"),
  ("ch25", "prob_25_2_2.html", "25.2-2 — Maximum Length of an Attenuation-Limited System"),
  ("ch25", "prob_25_2_3.html", "25.2-3 — Maximum Data Rate for an Attenuation-Limited System"),
  ("ch25", "prob_25_2_4.html", "25.2-4 — Maximum Length of an Analog Link"),
  ("ch25", "prob_25_2_5.html", "25.2-5 — Time Budget for a Dispersion-Limited System"),
  ("ch25", "prob_25_3_1.html", "25.3-1 — Number of WDM Channels"),
  ("ch25", "prob_25_5_1.html", "25.5-1 — Number of Nodes in a Broadcast-and-Select WDM Network"),
  ("ch25", "prob_25_5_2.html", "25.5-2 — Wavelength-Routed WDM Ring Network"),
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="dark" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #050608;
      --card: rgba(255,255,255,0.06);
      --text: rgba(255,255,255,0.92);
      --muted: rgba(255,255,255,0.72);
      --border: rgba(255,255,255,0.12);
    }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial, sans-serif;
      background: radial-gradient(1200px 600px at 20% 0%, rgba(120,120,255,0.12), transparent 60%),
                  radial-gradient(900px 500px at 100% 20%, rgba(120,255,200,0.10), transparent 55%),
                  var(--bg);
      color: var(--text);
      line-height: 1.55;
    }}
    header, main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 24px 18px;
    }}
    .box {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px;
    }}
    h1 {{ margin: 0 0 10px; font-size: 1.25rem; }}
    p {{ margin: 0 0 10px; color: var(--muted); }}
    .hint {{
      margin-top: 10px;
      font-size: 0.95rem;
      color: var(--muted);
    }}
    code {{
      background: rgba(255,255,255,0.08);
      padding: 2px 6px;
      border-radius: 8px;
    }}
  </style>
</head>
<body>
  <header>
    <div class="box">
      <h1>{title}</h1>
      <p>Write your full solution here as a self-contained HTML article (vanilla HTML/CSS/JS only).</p>
      <p class="hint">Path: <code>./problems/photonics/{chapter}/{filename}</code></p>
    </div>
  </header>

  <main>
    <div class="box">
      <p><strong>TODO:</strong> Add problem statement, derivation, final results, and (if desired) a canvas visualization.</p>
    </div>
  </main>
</body>
</html>
"""

def main():
    created = 0
    skipped = 0

    for ch, fname, title in FILES:
        out_dir = BASE / ch
        out_dir.mkdir(parents=True, exist_ok=True)

        out_path = out_dir / fname
        if out_path.exists():
            skipped += 1
            continue

        html = HTML_TEMPLATE.format(title=title, chapter=ch, filename=fname)
        out_path.write_text(html, encoding="utf-8")
        created += 1

    print(f"Done. Created {created} files, skipped {skipped} existing files.")
    print(f"Root used: {BASE.resolve()}")

if __name__ == "__main__":
    main()
