
import os

folder = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
os.makedirs(folder, exist_ok=True)

problems = [('7.1', 'MOS amplifier VTC active-region segment'), ('7.2', 'Required RD for specified VTC endpoint'), ('7.3', 'Biasing MOS amplifier at given VOV and VDS'), ('7.4', 'Bias point for specified MOS amplifier gain'), ('7.5', 'Saturation-region VTC endpoints and bias point'), ('7.6', 'Extracting Vt and W/L from amplifier measurements'), ('7.7', 'Gain and negative swing tradeoff in MOS amplifier'), ('7.8', 'Maximum-gain MOS amplifier with output swing constraint'), ('7.9', 'Linear amplifier with NMOS active load'), ('7.10', 'BJT amplifier gain and signal swing'), ('7.11', 'CE amplifier gain and swing versus collector current'), ('7.12', 'Optimal bias for maximum output sine-wave amplitude'), ('7.13', 'Low-voltage BJT amplifier gain limits'), ('7.14', 'Minimum VCC for required gain and output amplitude'), ('7.15', 'Gain of transistor circuit using Thevenin equivalent'), ('7.16', 'Voltage-transfer characteristics of pnp amplifiers'), ('7.17', 'Including Early effect in small-signal gain'), ('7.18', 'Collector signal change from small VBE variation'), ('7.19', 'Low-voltage CE amplifier complete operating analysis'), ('7.20', 'Deriving transistor transconductance gm'), ('7.21', 'Graphical analysis of BJT circuit and load line'), ('7.22', 'BJT characteristics with Early effect and load line'), ('7.23', 'Second-harmonic distortion in MOS amplifier'), ('7.24', 'Estimating gm from MOSFET current changes'), ('7.25', 'Common-source amplifier with finite ro'), ('7.26', 'NMOS amplifier design for required loaded output'), ('7.27', 'Optimum CS amplifier design'), ('7.28', 'Completing MOS small-signal parameter table'), ('7.29', 'Finding width for required gm at given current'), ('7.30', 'NMOS amplifier using T equivalent circuit'), ('7.31', 'Gain of NMOS amplifier with current source load'), ('7.32', 'Small-signal parameters in 0.18-μm CMOS'), ('7.33', 'Discrete common-source amplifier analysis'), ('7.34', 'Range of validity of BJT small-signal approximation'), ('7.35', 'Comparing exact and small-signal CE analysis'), ('7.36', 'Finding gm, rπ, and re for different bias currents'), ('7.37', 'Small-signal parameters of pnp BJT follower'), ('7.38', 'Design for specified gm and base input resistance'), ('7.39', 'Base resistance range with β and IC variation'), ('7.40', 'Signal quantities in transistor amplifier'), ('7.41', 'Design for maximum collector signal swing'), ('7.42', 'Completing BJT small-signal attributes table'), ('7.43', 'Four BJT small-signal models at given bias'), ('7.44', 'Showing T-model input resistance equals rπ'), ('7.45', 'Equivalence of T-model and hybrid collector currents'), ('7.46', 'Hybrid-π as incremental version of large-signal model'), ('7.47', 'T model as incremental version of large-signal model'), ('7.48', 'Transistor amplifier with current-source bias'), ('7.49', 'Finding vbe and ib from collector signal'), ('7.50', 'Overall voltage gain of general BJT amplifier'), ('7.51', 'Small-signal resistance of diode-connected transistor'), ('7.52', 'Emitter follower input resistance and gain'), ('7.53', 'Small-signal equivalent of RC-coupled BJT amplifier'), ('7.54', 'BJT amplifier input resistance and overall gain'), ('7.55', 'Maximum possible gain with finite Early effect'), ('7.56', 'Redesigning grounded-base amplifier for 75-Ω input'), ('7.57', 'Grounded-base amplifier design for 50-Ω source'), ('7.58', 'Signal gains in emitter and collector outputs'), ('7.59', 'Overall voltage and current gain of practical amplifier'), ('7.60', 'Specifying Rin, Avo, and Ro from system constraints'), ('7.61', 'Alternative amplifier equivalent circuit with Gm'), ('7.62', 'Overall-gain equivalent circuit with Gvo and Rout'), ('7.63', 'Amplifier with feedback resistance and non-unilateral behavior'), ('7.64', 'Overall voltage gain of common-source amplifier'), ('7.65', 'CS amplifier parameters and required signal amplitude'), ('7.66', 'Common-source amplifier design with load'), ('7.67', 'Two-stage cascaded common-source amplifier'), ('7.68', 'CE amplifier parameters and allowed signal swing'), ('7.69', 'Effect of β variability on CE amplifier gain'), ('7.70', 'Two-stage cascaded CE amplifier'), ('7.71', 'Finding source resistance from reduced transconductance'), ('7.72', 'Reducing CS amplifier gain with source resistance'), ('7.73', 'Gain change in CS amplifier with source degeneration'), ('7.74', 'CE amplifier with emitter resistance'), ('7.75', 'Design of CE amplifier with specified Rin and vπ'), ('7.76', 'Choosing Re to reduce gain sensitivity to β'), ('7.77', 'Common-gate amplifier input resistance and gain'), ('7.78', 'Extracting gm and VOV from CG gain measurements'), ('7.79', 'Bias current for matched-input CB amplifier'), ('7.80', 'Output signal of CB circuit driven by current source'), ('7.81', 'CB amplifier gain and allowed signal amplitude'), ('7.82', 'Source follower output resistance requirement'), ('7.83', 'Source follower design for 0.5-V peak output'), ('7.84', 'Emitter follower design for 0.5-V peak output'), ('7.85', 'Emitter follower Rin, gains, and output resistance'), ('7.86', 'Effect of β variation on emitter follower'), ('7.87', 'Emitter follower gain from measured output resistance'), ('7.88', 'General amplifier with source and emitter resistances'), ('7.89', 'CE gain including Early effect'), ('7.90', 'Source follower gain including ro'), ('7.91', 'Effect of IC on CE overall voltage gain'), ('7.92', 'Classical MOS biasing with 9-V supply'), ('7.93', 'Two-supply MOS biasing design'), ('7.94', 'Effect of missing source resistor in MOS bias circuit'), ('7.95', 'MOS bias current sensitivity to kn variation'), ('7.96', 'MOS bias sensitivity to threshold-voltage variation'), ('7.97', 'Two-supply MOS design for maximum gain'), ('7.98', 'PMOS bias design with divider network'), ('7.99', 'Sensitivity of MOS bias current to K'), ('7.100', 'Sensitivity of MOS bias current to threshold voltage'), ('7.101', 'Node voltages in feedback-biased MOS circuit'), ('7.102', 'Feedback-biased MOS design for target current'), ('7.103', 'Feedback-bias MOS design with resistor divider'), ('7.104', 'BJT voltage-divider bias with resistor tolerances'), ('7.105', 'Simple BJT bias design and β sensitivity'), ('7.106', 'Single-supply BJT bias network design'), ('7.107', 'Bias design with larger divider current'), ('7.108', 'Choosing RB/RE for stable emitter current'), ('7.109', 'Two-supply BJT bias arrangement design'), ('7.110', 'Two-supply BJT design with emitter signal coupling'), ('7.111', 'Single-supply feedback bias design using Fig. 7.54'), ('7.112', 'Feedback-bias BJT design and improved version'), ('7.113', 'Large-gain BJT circuit with current-source bias'), ('7.114', 'Output current of current-source circuit in Fig. P7.114'), ('7.115', 'Current generator using matched BJTs'), ('7.116', 'Finding R for current source in Fig. P7.116'), ('7.117', 'Overall gain of practical common-source amplifier'), ('7.118', 'CS amplifier bias, gain, saturation swing, and degeneration'), ('7.119', 'PMOS common-source amplifier design and swing'), ('7.120', 'High-frequency pulse amplifier with CS-CG pair'), ('7.121', 'Multifunction MOS amplifier design and gains'), ('7.122', 'Source follower plus common-gate cascade'), ('7.123', 'Feedback MOS amplifier resembling inverting op-amp'), ('7.124', 'Feedback MOS amplifier resembling noninverting op-amp'), ('7.125', 'Common-emitter amplifier with divider bias'), ('7.126', 'Design of CE amplifier between 2-kΩ source and load'), ('7.127', 'Effect of scaling resistor values in CE amplifier'), ('7.128', 'CE amplifier with current-source bias'), ('7.129', 'Two-supply BJT amplifier design'), ('7.130', 'Two-stage common-emitter amplifier'), ('7.131', 'BJT current-source-biased amplifier'), ('7.132', 'Amplifier analysis using BJT T model'), ('7.133', 'Input resistance and gain of BJT amplifier'), ('7.134', 'Emitter follower with wide β range'), ('7.135', 'Direct-coupled emitter follower'), ('7.136', 'Bootstrapped follower analysis'), ('7.137', 'Two-transistor follower analysis'), ('7.138', 'Bandwidth tradeoff with emitter degeneration')]

theory_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Circuits and Electronics — Sedra Ch 7 — Problem {num}</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 7</h1>
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
  <title>Circuits and Electronics — Sedra Ch 7 — Problem {num} Simulation</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 7</h1>
  <h2>Problem {num} — {title}</h2>

  <section>
    <h3>Simulation</h3>
    <p><!-- Add simulation here --></p>
  </section>
</body>
</html>
"""

card_template = """<article class=\"card\" data-tags=\"circuits-electronics circuits electronics sedra chapter-7\">
  <h3>Circuits and Electronics — Sedra Ch 7</h3>
  <p>Problem {num} — {title}</p>
  <div class=\"btn-row\">
    <a href=\"./problems/Circuits_Electronics/Sedra/Sedra_ch7_prob_{num}.html\">OPEN THEORY</a>
    <a href=\"./problems/Circuits_Electronics/Sedra/Sedra_ch7_prob_{num}_sim.html\">OPEN SIM</a>
  </div>
</article>
"""

cards = []
for num, title in problems:
    theory_name = f"Sedra_ch7_prob_{num}.html"
    sim_name = f"Sedra_ch7_prob_{num}_sim.html"

    with open(os.path.join(folder, theory_name), "w", encoding="utf-8") as f:
        f.write(theory_template.format(num=num, title=title))

    with open(os.path.join(folder, sim_name), "w", encoding="utf-8") as f:
        f.write(sim_template.format(num=num, title=title))

    cards.append(card_template.format(num=num, title=title))

cards_path = os.path.join(folder, "Sedra_ch7_cards.html")
with open(cards_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(cards))

print("Chapter 7 files created successfully.")
print(cards_path)
