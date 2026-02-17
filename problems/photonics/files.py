from pathlib import Path
from datetime import datetime
import html

BASE = Path("./problems/photonics")

PROBLEMS = [
    # -------- CH 6 --------
    ("ch6", "6.1-5",  "Orthogonal Elliptical Polarizations",
     "Show that if two elliptically polarized states are orthogonal, the major axes of their ellipses are perpendicular and the senses of rotation are opposite."),
    ("ch6", "6.1-6",  "Rotating a Polarization Rotator",
     "Show that the Jones matrix of a polarization rotator is invariant to rotation of the coordinate system."),
    ("ch6", "6.1-7",  "Jones Matrix of a Linear Polarizer",
     "Show that the Jones matrix of a linear polarizer whose transmission axis makes an angle θ with the x axis is ... Derive using the referenced equations."),
    ("ch6", "6.1-8",  "Half-Wave Retarder Rotation Effect",
     "For linearly polarized light through a half-wave retarder: if the polarization plane makes angle θ with the fast axis, show transmitted light is at angle −θ (rotation 2θ). Explain why not equivalent to a rotator."),
    ("ch6", "6.1-9",  "Wave Retarders in Tandem",
     "Write the Jones matrices for the given retarders, show cascading yields 90° rotation, and analyze reversed order."),
    ("ch6", "6.1-10", "Mirror Reflection Flips Circular Handedness",
     "Show circularly polarized light changes handedness upon reflection from a mirror."),
    ("ch6", "6.1-11", "Anti-Glare Screen with Polarizer + QWP",
     "Show an antiglare screen can be made from a linear polarizer plus a quarter-wave retarder at 45° to its axis. Can it be regarded as an optical isolator?"),
    ("ch6", "6.2-2",  "Derivation of Fresnel TE Reflection Equation",
     "Derive the TE reflection equation used to obtain the Fresnel TE coefficient. How would you approach the reflection coefficient for an incident beam rather than a plane wave?"),
    ("ch6", "6.2-3",  "TE/TM Reflectance of Glass at 45°",
     "A plane wave from air (n=1) hits glass (n=1.5) at 45°. Determine TE and TM power reflectances and average reflectance for unpolarized light."),
    ("ch6", "6.2-4",  "Brewster Angle and Orthogonal Rays",
     "Use given conditions and Snell’s law to derive Brewster-angle expression. Show θ1+θ2=90° and interpret why TM reflection vanishes."),
    ("ch6", "6.2-5",  "Phase Retardation in Total Internal Reflection",
     "Determine TE–TM phase retardation introduced by TIR at glass–air boundary for θ = 1.2 θc."),
    ("ch6", "6.2-6",  "Goos–Hänchen Shift from Phase Slope",
     "For two TE waves at θ and θ+dθ under TIR, with dφ = ξ dθ, find ξ and relate it to lateral shift (Goos–Hänchen effect)."),
    ("ch6", "6.2-7",  "Reflection from an Absorptive Medium",
     "Use Maxwell’s equations and boundary conditions to derive complex amplitude reflectance r for a medium with refractive index n and absorption coefficient α at normal incidence."),
    ("ch6", "6.3-1",  "Maximum Retardation in Quartz",
     "Quartz: ne=1.553, no=1.544. (a) Retardation per mm at λ0=633 nm when maximized. (b) Thickness(es) for quarter-wave operation."),
    ("ch6", "6.3-2",  "Maximum Extraordinary Walk-Off in Quartz",
     "Find propagation direction in quartz maximizing the angle between wavevector k and Poynting vector S."),
    ("ch6", "6.3-3",  "Double Refraction in Quartz at 30° Incidence",
     "Unpolarized plane wave incident at 30° onto quartz. Optic axis lies in plane of incidence and is perpendicular to incident direction inside crystal. Determine directions of wavevectors and rays for two refracted components."),
    ("ch6", "6.3-4",  "Geometry for Maximum Lateral Shift in Double Refraction",
     "Find the optimum geometry maximizing lateral shift between ordinary and extraordinary beams in a positive uniaxial crystal."),
    ("ch6", "6.3-5",  "Transmission Through a LiNbO3 Plate",
     "He–Ne beam (633 nm) normally incident on LiNbO3 plate (ne=2.29, no=2.20), thickness 1 cm, optic axis at 45° to normal. Find lateral shift and retardation."),
    ("ch6", "6.3-6",  "Conical Refraction in a Biaxial Crystal",
     "Show that for k along an optic axis, refraction forms a cone (conical refraction). What happens at the exit face into air?"),
    ("ch6", "6.6-1",  "Jones Matrix for Circular Dichroism Converter",
     "Determine the Jones matrix for a device that converts any input polarization into right circularly polarized light."),
    ("ch6", "6.6-2",  "Polarization Rotation via Many Polarizers",
     "Linearly x-polarized light passes through N polarizers with axes mθ, θ=π/2N. Show output is y-polarized and amplitude reduces by cos^N θ. Analyze N→∞."),

    # -------- CH 7 --------
    ("ch7", "7.1-2",  "Beamsplitter Slab at 45°",
     "A lossless dielectric slab (n, width d) at 45° is used as a beamsplitter. Derive TM transmittance/reflectance and sketch spectral dependence; compare with TE."),
    ("ch7", "7.1-3",  "Transmission Through a Thin Air Gap in Glass",
     "Find transmittance through air gap of width d=λ/2 in glass of index n for (a) normal incidence, (b) TE incidence above critical angle. Discuss tunneling."),
    ("ch7", "7.1-4",  "Multilayer Device in an Unmatched Medium",
     "Given multilayer reflectance rm in matched medium n1, show reflectance becomes r=(rb+rm)/(1+rbrm) when placed in medium n; evaluate limiting cases."),
    ("ch7", "7.1-5",  "Quarter-Wave Film Reflectance vs Angle",
     "Derive reflectance vs incidence angle for a quarter-wave antireflection coating."),
    ("ch7", "7.1-6",  "Fabry–Perot Etalon Length and Finesse",
     "Measured transmittance peaks have period 150 MHz and FWHM 5 MHz. For n=1, determine resonator length and finesse; infer mirror reflectances."),
    ("ch7", "7.1-7",  "Quarter-Wave and Half-Wave Dielectric Stacks",
     "Derive reflectance for a stack of N double layers with equal optical thickness (λ0/4 and λ0/2)."),
    ("ch7", "7.1-8",  "GaAs/AlAs Bragg Reflector vs N",
     "Alternating GaAs (n1=3.57) and AlAs (n2=2.94) quarter-wave layers in GaAs medium. Calculate and plot T and R vs N (1..10) at Bragg frequency."),
    ("ch7", "7.1-9",  "Bragg Grating Reflectance: Spectral & Angular",
     "Using matrix algebra, derive wave-transfer matrix and reflectance of an N-layer Bragg grating; verify spectral and angular plots."),
    ("ch7", "7.2-1",  "Bragg Frequency and Gap–Midgap Ratio (1D Stack)",
     "Using Fourier optics, determine Bragg frequency and gap–midgap ratio for lowest bandgap of a 1D periodic stack; compare two index-contrast cases."),
    ("ch7", "7.2-2",  "Off-Axis Wave in a 1D Periodic Medium",
     "Derive equations analogous to the on-axis case for an off-axis wave with transverse wavevector kx."),
    ("ch7", "7.2-3",  "No Bandgaps for Lateral Propagation (K=0)",
     "Use off-axis results to show no bandgaps exist for waves traveling laterally in a 1D periodic medium."),
    ("ch7", "7.2-4",  "Omnidirectional Reflector: Projected Dispersion",
     "For a periodic stack with n2=2n1, plot projected dispersion with air light line and determine ω-range (in ωB units) for omnidirectional reflection."),

    # -------- CH 8 --------
    ("ch8", "8.1-1",  "SPP at DPS–Lossy SNG Boundary",
     "Consider a DPS–SNG boundary with μ1=μ2=μ0, ε1 real positive, ε2 complex with negative real part. Show approximate formulas for plasmon wavelength and propagation length."),
    ("ch8", "8.1-2",  "NIM Slab Near-Field Imaging",
     "Demonstrate near-field imaging of a slab with n=-2 in air: derive imaging equation, reflection/transmission at interfaces, and evanescent transmission profile."),
    ("ch8", "8.1-3",  "Lossy NIM Slab: Resolution Limit",
     "For n=-2 slab with attenuation coefficient γ=0.1k0, find kx/k0 where amplification is smaller than attenuation and corresponding resolution in wavelengths."),
    ("ch8", "8.1-4",  "Type-II Hyperbolic Medium k-Surface",
     "Find k-surface for Type-II hyperbolic medium (ε1=ε2<0, ε3>0). Show it supports very short wavelengths but can be highly reflective."),
    ("ch8", "8.2-1",  "Group Velocity in a Drude Metal",
     "Using simplified Drude model permittivity, show the product of phase velocity and group velocity has the stated form."),
    ("ch8", "8.2-2",  "Prism Coupler for Ag–Air SPP",
     "SPP at air/60-nm Ag with SiN prism (n=2.0). At λ0=700 nm, εr(Ag)=-20+j1.3. Find prism angle to couple to SPP."),
    ("ch8", "8.2-3",  "Silver Nanosphere in Glass: Qs, Qa, Ei/E0",
     "For silver nanosphere a=10 nm in glass (n=1.45), compute and plot Qs, Qa, and Ei/E0 vs λ0 in 350–1000 nm; identify resonance."),
    ("ch8", "8.3-1",  "Maxwell–Garnett Effective Permittivity: Ag in Water",
     "Use Maxwell-Garnett to compute εe of water with silver nanospheres (f=3%) from 250–1000 nm; find ranges where Re{εe}<0 and study effects."),
    ("ch8", "8.3-2",  "Layered Metal–Dielectric Hyperbolic Metamaterial",
     "Use effective-medium approximation for layered metal/dielectric to show hyperbolic behavior under Drude εm; identify whether ε1 or ε3 becomes negative."),

    # -------- CH 9 --------
    ("ch9", "9.1-3",  "Mirror Waveguide Field Distribution Constraints",
     "Show a single TEM plane wave cannot satisfy mirror boundary conditions, and analyze why a two-wave sum fails under the stated symmetry conditions."),
    ("ch9", "9.1-4",  "Modal Dispersion in a Mirror Waveguide",
     "For λ0=0.633 μm, d=10 μm, n=1: count TE/TM modes, compute fastest/slowest group velocities, and estimate pulse spreading over 1 m."),
    ("ch9", "9.2-3",  "Dielectric Slab Waveguide Parameters",
     "For λ0=0.87 μm, d=2 μm, n1=1.6, n2=1.4: find θc, NA, acceptance angle, number of TE modes, bounce angle and group velocity of m=0 TE."),
    ("ch9", "9.2-4",  "Effect of Cladding: Air-Suspended Film",
     "Redo the slab waveguide parameter calculations for n2=1 and compare results."),
    ("ch9", "9.2-5",  "TE Mode Profile and Confinement Factor",
     "Derive constant ratio, plot m=0 TE mode for given parameters, and compute confinement factor."),
    ("ch9", "9.2-6",  "Slab Waveguide Fields from Maxwell’s Equations",
     "Starting with Ex=u(y)e^{-jβz}, derive Hy and Hz using Maxwell’s equations and verify boundary conditions and self-consistency relation."),
    ("ch9", "9.2-7",  "Single-Mode Slab Waveguide Thickness",
     "Find largest thickness d giving only one TE mode at 1.3 μm; then number of modes at 0.85 μm."),
    ("ch9", "9.2-8",  "Approximate TE Cutoff Condition (Weak Guidance)",
     "Show approximate cutoff condition for TE mode m>0 when n1≈n2, in terms of Δn."),
    ("ch9", "9.2-9",  "TM Mode Bounce Angles and Mode Count",
     "Derive TM bounce-angle expression and generate TM plot similar to reference figure; determine number of TM modes."),
    ("ch9", "9.3-1",  "Rectangular Waveguide: TE Modes vs Frequency",
     "Square cross section area 10^-2 mm^2 and NA=0.1: plot number of TE modes vs frequency and compare with reference."),
    ("ch9", "9.4-1",  "Coupling Coefficient Between Two Slabs (3-dB Coupler)",
     "Compute coupling coefficient for two identical slabs and determine the length for 3-dB coupling."),
    ("ch9", "9.6-1",  "Silver-Slab Waveguide Dispersion (Drude)",
     "Plot dispersion for symmetric and antisymmetric modes of a 20-nm silver slab; compute mode properties and compare with single-interface SPP."),
]


def slug_from_code(code: str) -> str:
    # '6.1-10' -> '6.1_10'
    return code.replace("-", "_")


def build_filename(code: str) -> str:
    return f"prob_{slug_from_code(code)}_saleh.html"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <style>
    :root {{
      --bg: #0b0f14;
      --card: #121a23;
      --text: #e6edf3;
      --muted: #9fb0c0;
      --border: rgba(255,255,255,.10);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }}
    header {{
      border-bottom: 1px solid var(--border);
      background: rgba(10,14,20,.75);
    }}
    .wrap {{
      width: min(980px, 92vw);
      margin: 0 auto;
      padding: 18px 0;
    }}
    h1 {{
      margin: 0;
      font-size: 1.6rem;
    }}
    .meta {{
      margin-top: 6px;
      color: var(--muted);
      font-size: .95rem;
    }}
    main .wrap {{ padding: 22px 0 40px; }}
    .card {{
      background: rgba(255,255,255,.04);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px;
    }}
    .label {{
      display: inline-block;
      padding: 6px 10px;
      border: 1px solid var(--border);
      border-radius: 999px;
      color: var(--muted);
      font-size: .85rem;
      margin-bottom: 10px;
    }}
    pre {{
      white-space: pre-wrap;
      word-wrap: break-word;
      background: rgba(0,0,0,.25);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      color: var(--text);
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
      font-size: .95rem;
    }}
    .row {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 12px;
    }}
    .btn {{
      border: 1px solid var(--border);
      background: rgba(255,255,255,.04);
      color: var(--text);
      border-radius: 12px;
      padding: 10px 12px;
      cursor: pointer;
      font-weight: 600;
    }}
    .btn:hover {{ border-color: rgba(255,255,255,.25); }}
    footer {{
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: .9rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>{h1}</h1>
      <div class="meta">Module: Photonics • Folder: {folder} • Generated: {generated}</div>
    </div>
  </header>

  <main>
    <div class="wrap">
      <article class="card">
        <div class="label">Problem Statement</div>
        <pre>{statement}</pre>

        <div class="label" style="margin-top:14px;">Solution (start here)</div>
        <pre>Write your solution here…</pre>

        <div class="row">
          <button class="btn" id="copyProb">Copy Problem Text</button>
          <button class="btn" id="copyTitle">Copy Title</button>
        </div>
      </article>
    </div>
  </main>

  <footer>
    <div class="wrap">Simple Photonics problem template (Saleh) — you can style later.</div>
  </footer>

  <script>
    // Safe JS inside a normal Python .format() template (braces escaped above).
    const probText = {prob_text_js};
    const probTitle = {prob_title_js};

    function copyText(txt) {{
      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(txt).catch(() => fallbackCopy(txt));
      }} else {{
        fallbackCopy(txt);
      }}
    }}

    function fallbackCopy(txt) {{
      const ta = document.createElement('textarea');
      ta.value = txt;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      ta.remove();
    }}

    document.getElementById('copyProb').addEventListener('click', () => copyText(probText));
    document.getElementById('copyTitle').addEventListener('click', () => copyText(probTitle));
  </script>
</body>
</html>
"""


def make_page(code: str, title: str, statement: str, folder_str: str) -> str:
    # Escape for HTML display inside <pre>
    statement_html = html.escape(statement)

    # Use Python repr for safe JS string literal
    prob_text_js = repr(statement)
    prob_title_js = repr(f"{code} (Saleh) — {title}")

    return HTML_TEMPLATE.format(
        page_title=f"{code} (Saleh) — {title}",
        h1=f"{code} (Saleh) — {title}",
        folder=folder_str,
        generated=datetime.now().strftime("%Y-%m-%d %H:%M"),
        statement=statement_html,
        prob_text_js=prob_text_js,
        prob_title_js=prob_title_js,
    )


def main():
    created = 0
    for chapter_folder, code, title, statement in PROBLEMS:
        out_dir = BASE / chapter_folder
        out_dir.mkdir(parents=True, exist_ok=True)

        filename = build_filename(code)
        out_path = out_dir / filename

        folder_str = str(out_dir).replace("\\", "/")
        html_text = make_page(code, title, statement, folder_str)

        out_path.write_text(html_text, encoding="utf-8")
        created += 1

    print(f"✅ Done. Created/updated {created} HTML files under: {BASE.resolve()}")


if __name__ == "__main__":
    main()
