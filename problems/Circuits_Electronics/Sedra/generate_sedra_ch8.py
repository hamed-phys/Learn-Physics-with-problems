
import os

folder = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
os.makedirs(folder, exist_ok=True)

problems = [('8.1', 'Design of MOS current-source circuit in Fig. 8.1'), ('8.2', 'Matched-MOS current source design with output-current tolerance'), ('8.3', 'PMOS counterpart of current-source circuit'), ('8.4', 'MOS current mirror with unequal widths'), ('8.5', 'Current steering with four MOSFETs'), ('8.6', 'CMOS current-steering circuit design'), ('8.7', 'PMOS current mirror with selectable transistor widths'), ('8.8', 'Basic bipolar current mirror over wide current range'), ('8.9', 'BJT current mirror with area ratio m'), ('8.10', 'pnp version of the basic current mirror'), ('8.11', 'Effect of collector-voltage change on basic current mirror'), ('8.12', 'pnp current-source circuit design and output variation'), ('8.13', 'Node voltages and branch currents in transistor network'), ('8.14', 'Finding node voltages and current for two values of R'), ('8.15', 'Multiple-mirror BJT circuit using ±5-V supplies'), ('8.16', 'Current conveyor analysis'), ('8.17', 'MOS current mirror Rin, Ais, and Ro'), ('8.18', 'MOS current mirror design for target gain and resistances'), ('8.19', 'Amplifier using current mirror active load'), ('8.20', 'Small-signal analysis of BJT current mirror'), ('8.21', 'Incremental resistance of diode-connected transistors'), ('8.22', 'Base-current-compensated mirror behavior'), ('8.23', 'Extending base-current-compensated mirror to n outputs'), ('8.24', 'Incremental input resistance of compensated BJT mirror'), ('8.25', 'Basic CE gain cell parameters versus current'), ('8.26', 'CE amplifier characteristics and changing bias current'), ('8.27', 'Intrinsic gain of NMOS transistor'), ('8.28', 'Intrinsic gain versus drain current'), ('8.29', 'NMOS design for target intrinsic gain and gm'), ('8.30', 'PMOS current-source-loaded CS amplifier'), ('8.31', 'Matching MOS gm to BJT gm'), ('8.32', 'NMOS gm, ro, and A0 in 0.5-μm process'), ('8.33', 'NMOS gm, ro, and A0 in 0.18-μm process'), ('8.34', 'Completing BJT and MOS basic gain-cell table'), ('8.35', 'Bias current for target intrinsic gain'), ('8.36', 'gm and A0 versus current for CS amplifier'), ('8.37', 'Operating-condition tradeoffs in 0.18-μm NMOS'), ('8.38', 'NMOS design for given A0 and current'), ('8.39', 'Current-source-loaded CS amplifier design'), ('8.40', 'CMOS amplifier design with current-source load'), ('8.41', 'CMOS amplifier design in 0.18-μm technology'), ('8.42', 'Two-stage cascoded common-source amplifier'), ('8.43', 'NMOS amplifier with resistive feedback'), ('8.44', 'CMOS amplifier design for target gain and output resistance'), ('8.45', 'Bias point for maximum signal swing in CMOS amplifier'), ('8.46', 'Effect of increasing supply voltage in CMOS amplifier'), ('8.47', 'Detailed CMOS amplifier design and gain evaluation'), ('8.48', 'Complementary MOS amplifier with feedback resistor'), ('8.49', 'CE amplifier with current-mirror active load'), ('8.50', 'CMOS amplifier design with specified swing and gain'), ('8.51', 'Common-gate amplifier Rin, Rout, and gain'), ('8.52', 'Common-gate amplifier as current buffer'), ('8.53', 'Design of MOS current source with source resistor'), ('8.54', 'Increasing current-source output resistance using source resistors'), ('8.55', 'Common-gate amplifier with active PMOS load'), ('8.56', 'CB amplifier input resistance versus load'), ('8.57', 'Load resistance for doubling CB input resistance'), ('8.58', 'CB amplifier output resistance versus emitter resistance'), ('8.59', 'CB amplifier used as current buffer'), ('8.60', 'Constant-current source circuit with BJT'), ('8.61', 'Increasing CE output resistance with emitter resistor'), ('8.62', 'Cascode transistor requirement for 50× resistance boost'), ('8.63', 'Cascode current source figure of merit'), ('8.64', 'Double-cascode current source tradeoffs with channel length'), ('8.65', 'Design of MOS cascode amplifier'), ('8.66', 'CMOS cascode amplifier gain and output resistances'), ('8.67', 'CMOS cascode amplifier design for target gain'), ('8.68', 'PMOS cascode current source design'), ('8.69', 'Shielding property of cascode transistor'), ('8.70', 'Comparing cascode to longer-channel CS amplifier'), ('8.71', 'Output range of CMOS cascode amplifier'), ('8.72', 'Loaded gain of CMOS cascode amplifier'), ('8.73', 'Signal distribution throughout cascode amplifier'), ('8.74', 'Double-cascode current source design'), ('8.75', 'Folded-cascode CMOS amplifier'), ('8.76', 'Output resistance of BJT cascode current source'), ('8.77', 'Figure of merit for BJT cascode current source'), ('8.78', 'Voltage gain of BJT cascode amplifier'), ('8.79', 'Bipolar cascode amplifier with current-source load'), ('8.80', 'Comparing four folded-cascode realizations'), ('8.81', 'Comparing BJT and MOS cascode devices'), ('8.82', 'Cascoded current mirror with specified dimensions'), ('8.83', 'Output resistance of double-cascode current mirror'), ('8.84', 'Wilson current mirror output-current variation'), ('8.85', 'Modified Wilson current mirror with split output'), ('8.86', 'pnp Wilson current mirror design'), ('8.87', 'Incremental input resistance of Wilson current mirror'), ('8.88', 'Wilson MOS mirror with systematic-error analysis'), ('8.89', 'Incremental input resistance of Wilson MOS mirror'), ('8.90', 'Widlar current source design'), ('8.91', 'Three Widlar current sources and output resistance'), ('8.92', 'Current-source circuit with three BJTs'), ('8.93', 'Exponential-current-setting transistor circuit'), ('8.94', 'Output resistance of source follower from equivalent circuit'), ('8.95', 'Source follower level shift and small-signal parameters'), ('8.96', 'BiCMOS amplifier input resistance and gain'), ('8.97', 'Detailed BiCMOS amplifier design and bootstrapping'), ('8.98', 'Darlington follower input and output resistances'), ('8.99', 'BJT amplifier in Fig. 8.48(a)'), ('8.100', 'CD–CG amplifier overall gain'), ('8.101', 'Overall gain of six transistor-pair circuits')]

theory_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Circuits and Electronics — Sedra Ch 8 — Problem {num}</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 8</h1>
  <h2>Problem {num} — {title}</h2>

  <section>
    <h3>Problem Statement</h3>
    <p><!-- Paste the original problem here --></p>
  </section>

  <section>
    <h3>Solution</h3>
    <p><!-- Write the solution here --></p>
  </section>
</body>
</html>
"""

sim_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Circuits and Electronics — Sedra Ch 8 — Problem {num} Simulation</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 8</h1>
  <h2>Problem {num} — {title}</h2>

  <section>
    <h3>Simulation</h3>
    <p><!-- Add simulation here --></p>
  </section>
</body>
</html>
"""

card_template = """<article class=\"card\" data-tags=\"circuits-electronics circuits electronics sedra chapter-8\">
  <h3>Circuits and Electronics — Sedra Ch 8</h3>
  <p>Problem {num} — {title}</p>
  <div class=\"btn-row\">
    <a href=\"./problems/Circuits_Electronics/Sedra/Sedra_ch8_prob_{num}.html\">OPEN THEORY</a>
    <a href=\"./problems/Circuits_Electronics/Sedra/Sedra_ch8_prob_{num}_sim.html\">OPEN SIM</a>
  </div>
</article>
"""

cards = []
for num, title in problems:
    theory_name = f"Sedra_ch8_prob_{num}.html"
    sim_name = f"Sedra_ch8_prob_{num}_sim.html"

    with open(os.path.join(folder, theory_name), "w", encoding="utf-8") as f:
        f.write(theory_template.format(num=num, title=title))

    with open(os.path.join(folder, sim_name), "w", encoding="utf-8") as f:
        f.write(sim_template.format(num=num, title=title))

    cards.append(card_template.format(num=num, title=title))

cards_path = os.path.join(folder, "Sedra_ch8_cards.html")
with open(cards_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(cards))

print("Chapter 8 files created successfully.")
print(cards_path)
