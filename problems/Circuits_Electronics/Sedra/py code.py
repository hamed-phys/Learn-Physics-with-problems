import os

folder = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
os.makedirs(folder, exist_ok=True)

problems = [
    ("6.1", "Identifying BJT Mode of Operation from Terminal Voltages"),
    ("6.2", "Finding IS and Relative Junction Areas"),
    ("6.3", "Scaling Saturation Current and Base–Emitter Voltage"),
    ("6.4", "Base–Emitter Voltage Difference for Different EBJ Areas"),
    ("6.5", "Collector Current and Required vBE for Two Transistors"),
    ("6.6", "Comparing Old and New BJT Technologies"),
    ("6.7", "Current and vBE Change for a Particular npn Transistor"),
    ("6.8", "Finding β and α from Base and Collector Currents"),
    ("6.9", "β Values Corresponding to Given α Values"),
    ("6.10", "α Values Corresponding to Given β Values"),
    ("6.11", "Relation Between Small Changes in α and β"),
    ("6.12", "Range of Collector and Emitter Currents for Given Base Current"),
    ("6.13", "Range of iC, iB, and iE for Given IS and β Range"),
    ("6.14", "Finding iC, β, and α from Measured Base Currents"),
    ("6.15", "Completing the BJT Measurement Table"),
    ("6.16", "Creating Specific Transistor Models from Data"),
    ("6.17", "Analysis Using the npn Model of Fig. 6.5(b)"),
    ("6.18", "Designing RB and RC for Specified IC and VCE"),
    ("6.19", "Comparing EBJ and CBJ Forward Characteristics"),
    ("6.20", "npn Transistor Operation in Saturation"),
    ("6.21", "Expression for VCEsat as a Function of Forced β"),
    ("6.22", "pnp Large-Signal Model Analysis"),
    ("6.23", "vEB Change for Higher Collector Currents"),
    ("6.24", "pnp Transistor with Emitter Current Injection"),
    ("6.25", "Power pnp Transistor Area Comparison"),
    ("6.26", "Missing pnp Large-Signal Equivalent Circuits"),
    ("6.27", "pnp Saturation Equivalent Circuit"),
    ("6.28", "Finding the Labeled Voltages and Currents in Fig. P6.28"),
    ("6.29", "Finding β from the Circuits of Fig. P6.29"),
    ("6.30", "Simple Circuit for Measuring β"),
    ("6.31", "Repeat of Exercise 6.13 with ±2.5 V Supplies"),
    ("6.32", "Design of Fig. P6.32 for Given Emitter Current and Collector Voltage"),
    ("6.33", "Practical Resistor Values for Example 6.2"),
    ("6.34", "Design of Fig. P6.34 for Given IC and VC"),
    ("6.35", "Voltages and Currents in the Circuits of Fig. P6.35"),
    ("6.36", "Temperature Dependence of ICBO"),
    ("6.37", "Augmented npn Model Including ICBO"),
    ("6.38", "Base–Emitter Voltage Versus Temperature"),
    ("6.39", "Temperature Effect on vEB and Emitter Current"),
    ("6.40", "Apparent Threshold Behavior of the BJT"),
    ("6.41", "Plotting iC Versus vCE with Early Effect"),
    ("6.42", "Temperature Compensation in the Circuit of Fig. P6.42"),
    ("6.43", "Output Resistance and Early Voltage from the iC–vCE Slope"),
    ("6.44", "Output Resistance for a Given Early Voltage"),
    ("6.45", "Early Voltage and Output Resistance from Measured Data"),
    ("6.46", "pnp Equivalent Circuits Corresponding to Fig. 6.19"),
    ("6.47", "Incremental β and Collector Current Change"),
    ("6.48", "Choosing VBB for Different Operating Modes"),
    ("6.49", "Saturated BJT Design with Forced β Constraint"),
    ("6.50", "pnp Saturation Analysis and RB Adjustment"),
    ("6.51", "VE and VC for Different VB Values"),
    ("6.52", "Highest VB for Active Mode and VB for Saturation"),
    ("6.53", "Complete Operating Analysis of Fig. P6.53"),
    ("6.54", "Cutoff and Saturation Conditions in Fig. P6.54"),
    ("6.55", "Voltage Divider Design for Fig. P6.51"),
    ("6.56", "Extracting BJT Quantities from One Measurement"),
    ("6.57", "pnp Circuit Design Using Two Resistors and ±3 V"),
    ("6.58", "Effect of Changing RB in Fig. P6.58"),
    ("6.59", "Maximum RC for Active-Mode Operation"),
    ("6.60", "VB, VE, and VC for Different RB Values"),
    ("6.61", "Node Voltages and Branch Currents in Fig. P6.61"),
    ("6.62", "Repeat of Problem 6.61 with β = 100"),
    ("6.63", "Robust Design of Fig. P6.63 Over β Variation"),
    ("6.64", "Choosing RC in the pnp Circuit of Fig. P6.64"),
    ("6.65", "Detailed Analysis of the Circuit of Fig. P6.65"),
    ("6.66", "Node Voltages in the Circuit of Fig. P6.66"),
    ("6.67", "Design of the Multi-Transistor Circuit of Fig. P6.67"),
    ("6.68", "Finding VB and VE for the Circuit of Fig. P6.68"),
    ("6.69", "Collector Voltages and Forced β in Fig. P6.69"),
]

theory_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Circuits and Electronics — Sedra Ch 6 — Problem {num}</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 6</h1>
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
  <title>Circuits and Electronics — Sedra Ch 6 — Problem {num} Simulation</title>
</head>
<body>
  <h1>Circuits and Electronics — Sedra Ch 6</h1>
  <h2>Problem {num} — {title}</h2>

  <section>
    <h3>Simulation</h3>
    <p><!-- Add simulation here --></p>
  </section>
</body>
</html>
"""

for num, title in problems:
    theory_name = f"Sedra_ch6_prob_{num}.html"
    sim_name = f"Sedra_ch6_prob_{num}_sim.html"

    with open(os.path.join(folder, theory_name), "w", encoding="utf-8") as f:
        f.write(theory_template.format(num=num, title=title))

    with open(os.path.join(folder, sim_name), "w", encoding="utf-8") as f:
        f.write(sim_template.format(num=num, title=title))

print("Chapter 6 files created successfully.")