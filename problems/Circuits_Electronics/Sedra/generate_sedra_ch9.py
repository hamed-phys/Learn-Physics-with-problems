from pathlib import Path
import html

TARGET_DIR = Path(r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra")

PROBLEMS = [
  {
    "num": "9.1",
    "title": "For an NMOS differential pair with a common-mode voltageVCM applied,asshowninFig.",
    "text": "9.1 For an NMOS differential pair with a common-mode\nvoltageVCM applied,asshowninFig. 9.2,letVDD = VSS = 1.0 V,\nk′\nn = 0.4 mA/V2, (W/L)1,2 = 10, Vtn = 0.4 V, I = 0.16 mA,\nR\nD = 5 k, and neglect channel-length modulation.\n(a) Find VOV and VGS for each transistor.\n(b) For VCM = 0, find VS, ID1, ID2, VD1, and VD2.\n(c) Repeat (b) for VCM = +0.4 V.\n(d) Repeat (b) for VCM = −0.1 V.\n(e) What is the highest value of VCM for which Q1 and Q2\nremain in saturation?\n(f) If current source I requires a minimum voltage of 0.2 V\nto operate properly, what is the lowest value allowed for\nVS\nand hence for V\nCM?"
  },
  {
    "num": "9.2",
    "title": "For the PMOS differential amplifier shown in Fig.",
    "text": "9.2 For the PMOS differential amplifier shown in\nFig. P9.2 let Vtp = −0.8 V and kp′W/L = 4 mA/V2. Neglect\nchannel-length modulation.\n(a) For vG1 = vG2 =0 V, find |VOV | and VSG for each of Q1\nand Q2. Also find VS, VD1, and VD2.\n(b) If the current source requires a minimum voltage of 0.4 V,\nfind the input common-mode range."
  },
  {
    "num": "9.3",
    "title": "For the differential amplifier specified in Problem 9.1 let v G2 grounded and vG1 =vid.",
    "text": "9.3 For the differential amplifier specified in Problem 9.1 let\nv\nG2 grounded and vG1 =vid. Find the value of vid that corresponds\nto each of the following situations:\n(a) iD1 =iD2 =0.08 mA; (b) iD1 =0.12 mA and iD2 =0.04 mA;\n(c) iD1 =0.16 mA and iD2 =0 (Q2 just cuts off); (d)\ni\nD1 =0.04 mA and iD2 =0.12 mA; (e) iD1 =0 mA (Q1 just cuts\noff) and iD2 =0.16 mA. For each case, find vS, vD1, vD2, and\n(vD2 – vD1)."
  },
  {
    "num": "9.4",
    "title": "For the differential amplifier specified in Problem 9.2, let vG2 =0 and vG1 =vid.",
    "text": "9.4 For the differential amplifier specified in Problem 9.2, let vG2 =0 and vG1 =vid. Find the range of vid needed\nto steer the bias current from one side of the pair to the other.\nAt each end of this range, give the value of the voltage at the\ncommon-source terminal and the drain voltages."
  },
  {
    "num": "9.5",
    "title": "Consider the differential amplifier specified in Problem 9.1 with G 2 grounded and vG1 =vid.",
    "text": "9.5 Consider the differential amplifier specified in Problem 9.1 with G\n2 grounded and vG1 =vid. Let vid be adjusted to\nthe value that causes i\nD1 =0.09 mA and iD2 =0.07 mA. Find\nthe corresponding values of vGS2, vS, vGS1, and hence vid.\nWhat is the difference output voltage vD2 −vD1? What is the\nvoltage gain (vD2 − vD1)/vid? What value of vid results in\ni\nD1 =0.07 mA and iD2 =0.09 mA?"
  },
  {
    "num": "9.6",
    "title": "Design the circuit in Fig.",
    "text": "9.6 Design the circuit in Fig. P9.6 to obtain a dc voltage\nof +0.1 V at each of the drains of Q1 and Q2 when\nv\nG1 = vG2 = 0 V. Operate all transistors at VOV = 0.15 V"
  },
  {
    "num": "9.7",
    "title": "The table providing the answers to Exercise 9.3 shows that as the maximum input signal to be applied to the different...",
    "text": "9.7 The table providing the answers to Exercise 9.3 shows\nthat as the maximum input signal to be applied to the\ndifferential pair is increased, linearity is maintained at the\nsame level by operating at a higher VOV. If vid max is to be 220\nmV, use the data in the table to determine the required VOV\nand the corresponding values of W/L and gm."
  },
  {
    "num": "9.8",
    "title": "Use Eq.",
    "text": "9.8 Use Eq. (9.23) to show that if the term involving v 2 id is to\nbe kept to a maximum value of k then the maximum possible\nfractional change in the transistor current is given by\n1I\nmax\nI/2\n= 2pk(1−k)\nand the corresponding maximum value of vid is given by\nv\nidmax = 2√k VOV\nEvaluate both expressions for k = 0.01, 0.1, and 0.2."
  },
  {
    "num": "9.9",
    "title": "AMOS differential amplifier biasedwith a current source I = 200 μA is found to switch currents completely to one side...",
    "text": "9.9 AMOS differential amplifier biasedwith a current source\nI = 200 μA is found to switch currents completely to one side\nof the pair when a difference signal vid = 0.3 V is applied. At\nwhat overdrive voltage will each of Q1 and Q2 be operating\nwhen v\nid = 0? If vid for full current switching is to be 0.5 V,\nwhat must the bias current I be changed to?"
  },
  {
    "num": "9.10",
    "title": "Design the MOS differential amplifier of Fig.",
    "text": "9.10 Design the MOS differential amplifier of Fig. 9.5 to\noperate at VOV =0.25 V and to provide a transconductance\ngm of 1 mA/V. Specify the W/L ratios and the bias\ncurrent. The technology available provides Vt =0.5 V and\nμnCox =400 μA/V2."
  },
  {
    "num": "9.11",
    "title": "For the MOS differential pair in Fig.",
    "text": "9.11 For the MOS differential pair in Fig. 9.5, specify the\nvalue of v\nid ≡ vG1 −vG2, in terms of VOV, that\n(a) causes iD1 to increase by 10% above its equilibrium value\nof I/2.\n(b) makes iD1/iD2 = 1.0; 2.0; 1.1; 1.01; 20."
  },
  {
    "num": "9.12",
    "title": "An NMOS differential amplifier is operated at a bias current I of 0.2 mA and has a W/L ratio of 32, μnCox =200 μA/V2,...",
    "text": "9.12 An NMOS differential amplifier is operated at a\nbias current I of 0.2 mA and has a W/L ratio of 32,\nμnCox =200 μA/V2, VA =10 V, and RD =10 k. Find VOV, gm,\nro\n, and Ad."
  },
  {
    "num": "9.13",
    "title": "It is required to design an NMOS differential amplifier to operate with a differential input voltage that can be as h...",
    "text": "9.13 It is required to design an NMOS differential\namplifier to operate with a differential input voltage that\ncan be as high as 0.1 V while keeping the nonlinear term\nunder the square root in Eq. (9.23) to a maximum of 0.04. A\ntransconductance gm of 2 mA/V is needed and the amplifier\nis required to provide a differential output signal of 1 V when\nthe input is at its maximum value. Find the required values\nof V\nOV, I, RD, and W/L. Assume that the technology available\nhas μnCox =200 μA/V2 and λ = 0."
  },
  {
    "num": "9.14",
    "title": "Design a MOS differential amplifier to operate from ±1-V power supplies and dissipate no more than 1 mW in the equili...",
    "text": "9.14 Design a MOS differential amplifier to operate from\n±1-V power supplies and dissipate no more than 1 mW in\nthe equilibrium state. The differential voltage gain Ad is to\nbe 10 V/V and the output common-mode dc voltage is to be\n0.2 V. (Note: This is the dc voltage at the drains.) Assume\nμnCox = 400 μA/V2 and neglect the Early effect. Specify I,\nR\nD, and W/L."
  },
  {
    "num": "9.15",
    "title": "Design a MOS differential amplifier to operate from ±1-V supplies and dissipate no more than 1 mW in its equilibrium...",
    "text": "9.15 Design a MOS differential amplifier to operate\nfrom ±1-V supplies and dissipate no more than 1 mW\nin its equilibrium state. Select the value of VOV so that\nthe value of v\nid that steers the current from one side of\nthe pair to the other is 0.25 V. The differential voltage\ngain Ad is to be 10 V/V. Assume kn′ = 400 μA/V2 and\nneglect the Early effect. Specify the required values of I, RD,\nand W/L."
  },
  {
    "num": "9.16",
    "title": "An NMOS differential amplifier employing equal drain resistors, RD = 47 k, has a differential gain Ad of 20 V/V.",
    "text": "9.16 An NMOS differential amplifier employing equal\ndrain resistors, RD = 47 k, has a differential gain Ad of\n20 V/V."
  },
  {
    "num": "9.17",
    "title": "A MOS differential amplifier is designed to have a differential gain Ad equal to the voltage gain obtained from a com...",
    "text": "9.17 A MOS differential amplifier is designed to have a\ndifferential gain Ad equal to the voltage gain obtained from\na common-source amplifier. Both amplifiers utilize the same\nvalues of R\nD and supply voltages, and all the transistors have\nthe same W/L ratios. What must the bias current I of the\ndifferential pair be relative to the bias current ID of the CS\namplifier? What is the ratio of the power dissipation of the\ntwo circuits?"
  },
  {
    "num": "9.18",
    "title": "A differential amplifier is designed to have a differential voltage gain equal to the voltage gain of a common-source...",
    "text": "9.18 A differential amplifier is designed to have a differential\nvoltage gain equal to the voltage gain of a common-source\namplifier. Both amplifiers use the same values of RD and\nsupply voltages and are designed to dissipate equal amounts\nof power in their equilibrium or quiescent state. As well, all\nthe transistors use the same channel length. What must the\nwidth W of the differential-pair transistors be relative to the\nwidth of the CS transistor?"
  },
  {
    "num": "9.19",
    "title": "",
    "text": "9.19 Figure P9.19 shows a MOS differential amplifer with\nthe drain resistors R\nD implemented using diode-connected\nPMOS transistors, Q3 and Q4. Let Q1 and Q2 be matched,\nand Q3 and Q4 be matched."
  },
  {
    "num": "9.20",
    "title": "Find the differential half-circuit for the differential amplifier shown in Fig.",
    "text": "9.20 Find the differential half-circuit for the differential\namplifier shown in Fig. P9.20 and use it to derive an\nexpression for the differential gain Ad ≡ vod/vid in terms of\ngm, RD, and Rs. Neglect the Early effect. What is the gain with\nR\ns = 0? What is the value of Rs (in terms of 1/gm) that reduces\nthe gain to half this value?"
  },
  {
    "num": "9.21",
    "title": "The resistance R s in the circuit of Fig.",
    "text": "9.21 The resistance R\ns in the circuit of Fig. P9.20 can be\nimplemented by using a MOSFET operated in the triode\nregion, as shown in Fig. P9.21. Here Q3 implements Rs, with\nthe value of R\ns determined by the voltage VC at the gate of Q3."
  },
  {
    "num": "9.22",
    "title": "The circuit of Fig.",
    "text": "9.22 The circuit of Fig. P9.22 shows an effective way of\nimplementing the resistance Rs needed for the circuit in\nFig. P9.20. Here Rs is realized as the series equivalent of two\nMOSFETs Q3 and Q4 that are operated in the triode region,\nthus, Rs = rDS3 + rDS4. Assume that Q1 and Q2 are matched\nand operate in saturation at an overdrive voltage VOV that\ncorresponds to a drain bias current of I/2. Also, assume that\nQ3 and Q4 are matched."
  },
  {
    "num": "9.23",
    "title": "",
    "text": "9.23 Figure P9.23 shows a circuit for a differential\namplifier with an active load. Here Q1 and Q2 form the\ndifferential pair, while the current source transistors Q4 and\nQ5 form the active loads for Q1 and Q2, respectively."
  },
  {
    "num": "9.24",
    "title": "A design error has resulted in a gross mismatch in the circuit of Fig.",
    "text": "9.24 A design error has resulted in a gross mismatch in the\ncircuit of Fig. P9.24. Specifically, Q2 has twice the W/L ratio\nof Q1. If vid is a small sine-wave signal, find:"
  },
  {
    "num": "9.25",
    "title": "For the cascode differential amplifier of Fig.",
    "text": "9.25 For the cascode differential amplifier of Fig. 9.13(a),\nshow that if all transistors have the same channel length and\nare operated at the same VOV and assuming that VAn ′ = VAp ′ =\nV ′\nA , the differential gain Ad is given by"
  },
  {
    "num": "9.26",
    "title": "For the differential amplifier of Fig.",
    "text": "9.26 For the differential amplifier of Fig. 9.15(a) let I =\n0.4 mA, VCC =VEE =2.5 V, VCM =−1 V, RC =5 k, and\nβ = 100. Assume that the BJTs havevBE =0.7 V at iC =1 mA.\nFind the voltage at the emitters and at the outputs."
  },
  {
    "num": "9.27",
    "title": "An npn differential amplifier with I = 0.4 mA, VCC = V EE = 2.5 V, and RC = 5 k utilizes BJTs with β = 100 and v BE...",
    "text": "9.27 An npn differential amplifier with I = 0.4 mA, VCC =\nV\nEE = 2.5 V, and RC = 5 k utilizes BJTs with β = 100 and\nv\nBE = 0.7 V at iC = 1 mA. If vB2 = 0, find VE, VC1, and VC2\nobtained with v\nB1 = +0.5 V, and with vB1 = −0.5 V. Assume\nthat the current source requires a minimum of 0.3 V for proper\noperation."
  },
  {
    "num": "9.28",
    "title": "An npn differential amplifier with I = 0.4 mA, VCC = V EE = 2.5 V, and RC = 5 k utilizes BJTs with β = 100 and v BE...",
    "text": "9.28 An npn differential amplifier with I = 0.4 mA, VCC =\nV\nEE = 2.5 V, and RC = 5 k utilizes BJTs with β = 100 and\nv\nBE = 0.7 V at iC = 1 mA. Assuming that the bias current is\nobtained by a simple current source and that all transistors\nrequire a minimum vCE of 0.3 V for operation in the active\nmode, find the input common-mode range."
  },
  {
    "num": "9.29",
    "title": "Repeat Exercise 9.7 for an input of –0.3 V.",
    "text": "9.29 Repeat Exercise 9.7 for an input of –0.3 V."
  },
  {
    "num": "9.30",
    "title": "An npn differential pair employs transistors for which v BE = 690 mV at iC = 1 mA, and β = 50.",
    "text": "9.30 An npn differential pair employs transistors for which\nv\nBE = 690 mV at iC = 1 mA, and β = 50. The transistors leave\nthe activemode atv\nCE ≤ 0.3 V. The collectorresistors RC = 82\nk, and the power supplies are ±1.2 V. The bias current\nI = 20 μA and is supplied with a simple current source."
  },
  {
    "num": "9.31",
    "title": "Consider the BJT differential amplifier when fed with a common-mode voltage VCM as shown in Fig.",
    "text": "9.31 Consider the BJT differential amplifier when fed with\na common-mode voltage VCM as shown in Fig. 9.15(a). As is\noften the case, the supply voltage VCC may not be pure dc\nbut might include a ripple component vr of small amplitude\nand a frequency of 120 Hz (see Section 4.5). Thus the supply\nvoltage becomes VCC + vr."
  },
  {
    "num": "9.32",
    "title": "Consider the differential amplifier of Fig.",
    "text": "9.32 Consider the differential amplifier of Fig. 9.14 and\nlet the BJT β be very large:"
  },
  {
    "num": "9.33",
    "title": "To provide insight into the possibility of nonlinear distortion resulting from large differential input signals appli...",
    "text": "9.33 To provide insight into the possibility of nonlinear\ndistortion resulting from large differential input signals\napplied to the differential amplifier of Fig. 9.14, evaluate the\nnormalized change in the current iE1, 1iE1/I = \u0003iE1 −(I/2)\u0001/I,\nfor differential input signals vid of 2, 5, 8, 10, 20, 30,\nand 40 mV."
  },
  {
    "num": "9.34",
    "title": "Design the circuit of Fig.",
    "text": "9.34 Design the circuit of Fig. 9.14 to provide a differential output voltage (i.e., one taken between the two collectors)\nof 1 V when the differential input signal is 10 mV. A current\nsource of 1 mA and a positive supply of +5 V are available.\nWhat is the largest possible input common-mode voltage for\nwhich operation is as required? Assume α ≃1."
  },
  {
    "num": "9.35",
    "title": "For the circuit in Fig.",
    "text": "9.35 For the circuit in Fig. 9.14, assuming α = 1 and\nIR\nC =5 V, use Eqs. (9.48) and (9.49) to find iC1 and iC2, and\nhence determine v\nod = vC2 −vC1 for input differential signals\nv\nid ≡ vB1 − vB2 of 2 mV, 5 mV, 10 mV, 15 mV, 20 mV,\n25 mV, 30 mV, 35 mV, and 40 mV."
  },
  {
    "num": "9.36",
    "title": "In a differential amplifier using a 1.5-mA emitter bias current source, the two BJTs are not matched.",
    "text": "9.36 In a differential amplifier using a 1.5-mA emitter bias\ncurrent source, the two BJTs are not matched. Rather, one has\ntwice the emitter junction area of the other. For a differential\ninput signal of zero volts, what do the collector currents\nbecome? What difference input is needed to equalize the\ncollector currents? Assume α = 1."
  },
  {
    "num": "9.37",
    "title": "This problem explores the linearization of the transfer characteristics of the differential pair achieved by includin...",
    "text": "9.37 This problem explores the linearization of the transfer\ncharacteristics of the differential pair achieved by including\nemitter-degeneration resistances Re in the emitters (see\nFig. 9.17). Consider the case I = 200 μA with the transistors\nexhibiting vBE = 690 mV at iC = 1 mA and assume α ≃ 1."
  },
  {
    "num": "9.38",
    "title": "A BJT differential amplifier uses a 400-μA bias current.",
    "text": "9.38 A BJT differential amplifier uses a 400-μA bias current.\nWhat is the value of gm of each device? If β is 160, what is\nthe differential input resistance?"
  },
  {
    "num": "9.39",
    "title": "Design the basic BJT differential amplifier circuit of Fig.",
    "text": "9.39 Design the basic BJT differential amplifier circuit\nof Fig. 9.18 to provide a differential input resistance of at\nleast 20 k and a differential voltage gain of 100 V/V. The\ntransistor β is specified to be at least 100. Specify I and RC."
  },
  {
    "num": "9.40",
    "title": "For a differential amplifier to which a total difference signal of 10 mV is applied, what is the equivalent signal to...",
    "text": "9.40 For a differential amplifier to which a total difference\nsignal of 10 mV is applied, what is the equivalent signal to its\ncorresponding CE half-circuit? If the emitter current source I\nis 200 μA, what is re of the half-circuit? For a load resistance\nof 10 k in each collector, what is the half-circuit gain? What\nmagnitude of signal output voltage would you expect at each\ncollector? Between the two collectors?"
  },
  {
    "num": "9.41",
    "title": "A BJT differential amplifier is biased from a 0.5-mA constant-current source and includes a 400- resistor in each em...",
    "text": "9.41 A BJT differential amplifier is biased from a 0.5-mA\nconstant-current source and includes a 400- resistor in\neach emitter. The collectors are connected to V\nCC via 10-k\nresistors. A differential input signal of 0.1 V is applied\nbetween the two bases."
  },
  {
    "num": "9.42",
    "title": "Design a BJT differential amplifier to amplify a differential input signal of 0.1 V and provide a differential output...",
    "text": "9.42 Design a BJT differential amplifier to amplify a\ndifferential input signal of 0.1 V and provide a differential\noutput signal of 2 V. To ensure adequate linearity, it is\nrequired to limit the signal amplitude across each base–emitter\njunction to a maximum of 5 mV. Another design requirement\nis that the differential input resistance be at least 100 k. The\nBJTs available are specified to have β ≥ 100. Give the circuit\nconfiguration and specify the values of all its components."
  },
  {
    "num": "9.43",
    "title": "Design a bipolar differential amplifier such as that in Fig.",
    "text": "9.43 Design a bipolar differential amplifier such as that\nin Fig. 9.18 to operate from ±2.5 V power supplies and to\nprovide differential gain of 60 V/V. The power dissipation in\nthe quiescent state should not exceed 1 mW."
  },
  {
    "num": "9.44",
    "title": "In this problem we explore the trade-off between input common-mode range and differential gain in the design of the b...",
    "text": "9.44 In this problem we explore the trade-off between\ninput common-mode range and differential gain in the design\nof the bipolar BJT."
  },
  {
    "num": "9.45",
    "title": "For the differential amplifier of Fig.",
    "text": "9.45 For the differential amplifier of Fig. 9.14, let VCC =\n+5 V and IRC = 4 V. Find the differential gain Ad. Sketch and\nclearly label the waveforms for the total collector voltages vC1\nand v\nC2 and for (vC2 −vC1) for the case:"
  },
  {
    "num": "9.46",
    "title": "Consider a bipolar differential amplifier in which the collector resistors R C are replaced with simple current sourc...",
    "text": "9.46 Consider a bipolar differential amplifier in which the\ncollector resistors R\nC are replaced with simple current sources\nimplemented using pnp transistors. Sketch the circuit and give\nits differential half-circuit. If V\nA = 20 V for all transistors, find\nthe differential voltage gain achieved."
  },
  {
    "num": "9.47",
    "title": "For each of the emitter-degenerated differential amplifiers shown in Fig.",
    "text": "9.47 For each of the emitter-degenerated differential amplifiers shown in Fig. P9.47, find the differential half-circuit and\nderive expressions for the differential gain Ad and differential\ninput resistance Rid."
  },
  {
    "num": "9.48",
    "title": "Consider a bipolar differential amplifier that, in addition to the collector resistances R C, has a load resistance R...",
    "text": "9.48 Consider a bipolar differential amplifier that, in addition\nto the collector resistances R\nC, has a load resistance RL connected between the two collectors. What does the differential\ngain Ad become?"
  },
  {
    "num": "9.49",
    "title": "A bipolar differential amplifier having resistance Re inserted in series with each emitter (as in Fig.",
    "text": "9.49 A bipolar differential amplifier having resistance Re\ninserted in series with each emitter (as in Fig. P9.47(a)) is\nbiased with a constant current I. When both input terminals\nare grounded, the dc voltage measured across each Re is found\nto be 4 V\nT and that measured across each RC is found to be\n60 V\nT. What differential voltage gain Ad do you expect the\namplifier to have?"
  },
  {
    "num": "9.50",
    "title": "A bipolar differential amplifier with emitterdegeneration resistances Re and Re is fed with the arrangement shown in...",
    "text": "9.50 A bipolar differential amplifier with emitterdegeneration resistances Re and Re is fed with the arrangement\nshown in Fig. P9.50. Derive an expression for the overall\ndifferential voltage gain Gv ≡ vod/vsig. If Rsig is of such a\nvalue that v\nid = 0.5vsig, find the gain Gv in terms of RC,\nre\n, Re, and α. Now if β is doubled, by what factor does Gv\nincrease?"
  },
  {
    "num": "9.51",
    "title": "A particular differential amplifier operates from an emitter current source I = 0.4 mA.",
    "text": "9.51 A particular differential amplifier operates from an\nemitter current source I = 0.4 mA. Each of the collector\nresistances R\nC = 20 k and a load resistance RL = 40 k\nis connected between the two collectors. If the amplifier is\nfed in the manner shown in Fig. P9.50 with Rsig = 100 k,\nfind the overall voltage gain. Let β = 100."
  },
  {
    "num": "9.52",
    "title": "Find the voltage gain and the input resistance of the amplifier shown in Fig.",
    "text": "9.52 Find the voltage gain and the input resistance of the\namplifier shown in Fig. P9.52 assuming β = 100."
  },
  {
    "num": "9.53",
    "title": "Find the voltage gain and input resistance of the amplifier in Fig.",
    "text": "9.53 Find the voltage gain and input resistance of the\namplifier in Fig. P9.53 assuming that β = 100."
  },
  {
    "num": "9.54",
    "title": "Derive an expression for the small-signal voltage gain v o/vi of the circuit shown in Fig.",
    "text": "9.54 Derive an expression for the small-signal voltage gain\nv\no/vi of the circuit shown in Fig. P9.54 in two different ways:"
  },
  {
    "num": "9.55",
    "title": "An NMOS differential pair is biased by a current source I = 0.2 mA having an output resistance R SS =100 k.",
    "text": "9.55 An NMOS differential pair is biased by a\ncurrent source I = 0.2 mA having an output resistance\nR\nSS =100 k. The amplifier has drain resistances RD =10 k,\nusing transistors with kn′W/L = 3 mA/V2, and ro that is\nlarge. If the output is taken differentially and there is a 1%\nmismatch between the drain resistances, find Ad , Acm ,\nand CMRR."
  },
  {
    "num": "9.56",
    "title": "For the differential amplifier shown in Fig.",
    "text": "9.56 For the differential amplifier shown in Fig. P9.2 let Q1\nand Q2 have kp′(W/L) = 4 mA/V2, and assume that the bias\ncurrent source has an output resistance of 30 k. Find VOV ,\ngm, Ad , Acm , and the CMRR(in dB) obtainedwith the output\ntaken differentially. The drain resistances are known to have\na mismatch of 2%."
  },
  {
    "num": "9.57",
    "title": "The differential amplifier in Fig.",
    "text": "9.57 The differential amplifier in Fig. P9.57 utilizes\na resistor connected to the negative power supply to establish\nthe bias current I."
  },
  {
    "num": "9.58",
    "title": "It can be shown that if the drain resistors of a MOS differential amplifier have a mismatch 1RD and if simultaneously...",
    "text": "9.58 It can be shown that if the drain resistors of a\nMOS differential amplifier have a mismatch 1RD and if\nsimultaneously the transconductances of Q1 and Q2 have a\nmismatch 1gm, the common-mode gain is given by"
  },
  {
    "num": "9.59",
    "title": "It is required to design a MOS differential amplifier to have a CMRR of 80 dB.",
    "text": "9.59 It is required to design a MOS differential amplifier\nto have a CMRR of 80 dB. The only source of mismatch in the\ncircuit is a 2% difference between the W/L ratios of the two\ntransistors. Let I = 100 μA and assume that all transistors are\noperated at VOV = 0.2 V. For the 0.18-μm CMOS fabrication\nprocess available, VA′ = 5 V/μm. What is the value of L\nrequired for the current-source transistor?"
  },
  {
    "num": "9.60",
    "title": "A MOS differential amplifier utilizing a simple current source to provide the bias current I is found to have a CMRR...",
    "text": "9.60 A MOS differential amplifier utilizing a simple\ncurrent source to provide the bias current I is found to have\na CMRR of 60 dB. If it is required to raise the CMRR to\n100 dB by adding a cascode transistor to the current source,\nwhat must the intrinsic gain A0 of the cascode transistor\nbe? If the cascode transistor is operated at VOV = 0.2 V,\nwhat must its V\nA be? If for the specific technology utilized\nV ′\nA = 5 V/μm, specify the channel length L of the cascode\ntransistor."
  },
  {
    "num": "9.61",
    "title": "The differential amplifier circuit of Fig.",
    "text": "9.61 The differential amplifier circuit of Fig. P9.61 utilizes\na resistor connected to the negative power supply to establish\nthe bias current I."
  },
  {
    "num": "9.62",
    "title": "For the differential amplifier shown in Fig.",
    "text": "9.62 For the differential amplifier shown in Fig. P9.62,\nidentify and sketch the differential half-circuit and the\ncommon-mode half-circuit."
  },
  {
    "num": "9.63",
    "title": "Consider the basic differential circuit in which the transistors have β = 100 and VA =100 V, with I = 0.2 mA, R EE =5...",
    "text": "9.63 Consider the basic differential circuit in which the\ntransistors have β = 100 and VA =100 V, with I = 0.2 mA,\nR\nEE =500 k, and RC =25 k. The collector resistances are\nmatched to within 1%. Find:"
  },
  {
    "num": "9.64",
    "title": "In a bipolar differential-amplifier circuit, the bias current generator consists of a simple common-emitter transisto...",
    "text": "9.64 In a bipolar differential-amplifier circuit, the bias current generator consists of a simple common-emitter transistor\noperating at 200 μA. For this transistor, and those used in the\ndifferential pair, VA =20 V and β = 50. What common-mode\ninput resistance would result? Assume RC ≪ ro."
  },
  {
    "num": "9.65",
    "title": "A bipolar differential amplifier with I = 0.5 mA utilizes transistors for which V A = 50 V and β = 100.",
    "text": "9.65 A bipolar differential amplifier with I = 0.5 mA utilizes\ntransistors for which V\nA = 50 V and β = 100. The collector\nresistances R\nC = 5 k and are matched to within 10%. Find:"
  },
  {
    "num": "9.66",
    "title": "It is required to design a differential amplifier to provide the largest possible signal to a pair of 10-k load resi...",
    "text": "9.66 It is required to design a differential amplifier to\nprovide the largest possible signal to a pair of 10-k load\nresistances. The input differential signal is a sinusoid of\n5-mV peak amplitude, which is applied to one input terminal\nwhile the other input terminal is grounded."
  },
  {
    "num": "9.67",
    "title": "Design a BJT differential amplifier that provides two single-ended outputs (at the collectors).",
    "text": "9.67 Design a BJT differential amplifier that provides\ntwo single-ended outputs (at the collectors). The amplifier\nis to have a differential gain (to each of the two outputs)\nof at least 100 V/V, a differential input resistance ≥ 10 k,\nand a common-mode gain (to each of the two outputs) no\ngreater than 0.1 V/V."
  },
  {
    "num": "9.68",
    "title": "When the output of a BJT differential amplifier is taken differentially, its CMRR is found to be 34 dB higher than wh...",
    "text": "9.68 When the output of a BJT differential amplifier is taken\ndifferentially, its CMRR is found to be 34 dB higher than\nwhen the output is taken single-endedly. If the only source of\ncommon-mode gain when the output is taken differentially\nis the mismatch in collector resistances, what must this\nmismatch be (in percent)?"
  },
  {
    "num": "9.69",
    "title": "In a particular BJT differential amplifier, a production error results in one of the transistors having an emitter–ba...",
    "text": "9.69 In a particular BJT differential amplifier, a production\nerror results in one of the transistors having an emitter–base\njunction area twice that of the other. With the inputs\ngrounded, how will the emitter bias current split between the\ntwo transistors? If the output resistance of the current source\nis 500 k and the resistance in each collector (RC) is 12 k,\nfind the common-mode gain obtained when the output is\ntaken differentially. Assume α ≃ 1."
  },
  {
    "num": "9.70",
    "title": "An NMOS differential pair is to be used in an amplifier whose drain resistors are 10 k ± 1%.",
    "text": "9.70 An NMOS differential pair is to be used in an\namplifier whose drain resistors are 10 k ± 1%. For the\npair, kn′W/L = 4 mA/V2. A decision is to be made concerning\nthe bias current I to be used, whether 160 μA or 360 μA.\nContrast the differential gain and input offset voltage for the\ntwo possibilities."
  },
  {
    "num": "9.71",
    "title": "AnNMOS amplifier,whose designed operating point is at V OV =0.3 V, is suspected to have a variability of Vt of ±5 mV,...",
    "text": "9.71 AnNMOS amplifier,whose designed operating point\nis at V\nOV =0.3 V, is suspected to have a variability of Vt of ±5\nmV, and of W/L and RD (independently) of ±1%. What is\nthe worst-case input offset voltage you would expect to find?\nWhat is the major contribution to this total offset? If you used\na variation of one of the drain resistors to reduce the output\noffset to zero and thereby compensate for the uncertainties\n(including that of the other RD), what percentage change from\nnominal would you require?"
  },
  {
    "num": "9.72",
    "title": "An NMOS differential pair operating at a bias current I of 100 μA uses transistors for which kn′ =200 μA/V2 and W/L =...",
    "text": "9.72 An NMOS differential pair operating at a bias current\nI of 100 μA uses transistors for which kn′ =200 μA/V2 and\nW/L = 10. Find the three components of input offset voltage\nunder the conditions that 1R\nD/RD = 4%, 1(W/L)/(W/L) =\n4%, and 1Vt = 5 mV. In the worst case, what might the\ntotal offset be? For the usual case of the three effects being\nindependent, what is the offset likely to be?"
  },
  {
    "num": "9.73",
    "title": "A bipolar differential amplifier uses two well-matched transistors, but collector load resistors that are mismatched...",
    "text": "9.73 A bipolar differential amplifier uses two well-matched\ntransistors, but collector load resistors that are mismatched\nby 10%. What input offset voltage is required to reduce the\ndifferential output voltage to zero?"
  },
  {
    "num": "9.74",
    "title": "A bipolar differential amplifier uses two transistors whose scale currents I S differ by 10%.",
    "text": "9.74 A bipolar differential amplifier uses two transistors\nwhose scale currents I\nS differ by 10%. If the two collector\nresistors are well matched, find the resulting input offset\nvoltage."
  },
  {
    "num": "9.75",
    "title": "Modify Eq.",
    "text": "9.75 Modify Eq. (9.114) for the case of a differential\namplifier having a resistance RE connected in the emitter of\neach transistor. Let the bias current source be I."
  },
  {
    "num": "9.76",
    "title": "A differential amplifier uses two transistors whose β values are β1 and β2.",
    "text": "9.76 A differential amplifier uses two transistors whose β\nvalues are β1 and β2. If everything else is matched, show that\nthe input offset voltage is approximately VT\u00031/β1\u0001−\u00031/β2\u0001\u0003.\nEvaluate V\nOS for β1 =50 and β2 =100."
  },
  {
    "num": "9.77",
    "title": "Two possible differential amplifier designs are considered, one using BJTs and the other MOSFETs.",
    "text": "9.77 Two possible differential amplifier designs are considered, one using BJTs and the other MOSFETs. In both cases,\nthe collector (drain) resistors are maintained within ±2% of\nnominal value. The MOSFETs are operated at VOV = 200 mV.\nWhat input offset voltage results in each case? What does the\nMOS V\nOS become if the devices are increased in width by a\nfactor of 4 while the bias current is kept constant?"
  },
  {
    "num": "9.78",
    "title": "A differential amplifier uses two transistors having VA values of 100 V and 200 V.",
    "text": "9.78 A differential amplifier uses two transistors having VA\nvalues of 100 V and 200 V. If everything else is matched,\nfind the resulting input offset voltage. Assume that the two\ntransistors are intended to be biased at a V\nCE of about 10 V."
  },
  {
    "num": "9.79",
    "title": "A differential amplifier is fed in a balanced or push–pull manner, and the source resistance in series with each base...",
    "text": "9.79 A differential amplifier is fed in a balanced or\npush–pull manner, and the source resistance in series with\neach base is R\ns. Show that a mismatch 1Rs between the\nvalues of the two source resistances gives rise to an input\noffset voltage of approximately (I/2β)1Rs / [1+(gmRs)/β]."
  },
  {
    "num": "9.80",
    "title": "One approach to “offset correction” involves the adjustment of the values of RC1 and RC2 so as to reduce the differen...",
    "text": "9.80 One approach to “offset correction” involves the\nadjustment of the values of RC1 and RC2 so as to reduce\nthe differential output voltage to zero when both input\nterminals are grounded."
  },
  {
    "num": "9.81",
    "title": "A differential amplifier for which the total emitter bias current is 400 μA uses transistors for which β is specified...",
    "text": "9.81 A differential amplifier for which the total emitter bias\ncurrent is 400 μA uses transistors for which β is specified to\nlie between 80 and 200. What is the largest possible input bias\ncurrent? The smallest possible input bias current? The largest\npossible input offset current?"
  },
  {
    "num": "9.82",
    "title": "In a particular BJT differential amplifier, a production error results in one of the transistors having an emitter–ba...",
    "text": "9.82 In a particular BJT differential amplifier, a production\nerror results in one of the transistors having an emitter–base\njunction area twice that of the other. With both inputs\ngrounded, find the current in each of the two transistors and\nhence the dc offset voltage at the output, assuming that the\ncollector resistances are equal."
  },
  {
    "num": "9.83",
    "title": "A large fraction of mass-produced differentialamplifier modules employing 20-k collector resistors is found to have...",
    "text": "9.83 A large fraction of mass-produced differentialamplifier modules employing 20-k collector resistors is\nfound to have an input offset voltage ranging from +2 mV\nto –2 mV. By what amount must one collector resistor be\nadjusted to reduce the input offset to zero?"
  },
  {
    "num": "9.84",
    "title": "The differential amplifier of Fig.",
    "text": "9.84 The differential amplifier of Fig. 9.32(a) is measured\nand found to have a short-circuit transconductance of 2 mA/V.\nA differential input signal is applied and the output voltage\nis measured with a load resistance R\nL connected."
  },
  {
    "num": "9.85",
    "title": "A current-mirror-loadedNMOS differential amplifier is fabricated in a technology for which |VA′| = 5 V/μm.",
    "text": "9.85 A current-mirror-loadedNMOS differential amplifier is\nfabricated in a technology for which |VA′| = 5 V/μm. All the\ntransistors have L = 0.5 μm. If the differential-pair transistors\nare operated at VOV = 0.25 V, what open-circuit differential\ngain is realized?"
  },
  {
    "num": "9.86",
    "title": "The differential amplifier of Fig.",
    "text": "9.86 The differential amplifier of Fig. 9.32(a) is biased with\nI = 200 μA. All transistors have L = 0.5 μm, and Q1 and\nQ2 have W/L = 50. The circuit is fabricated in a process for\nwhich μnCox = 200 μA/V2 and |VA′| = 5 V/μm. Find gm1,2,\nro\n2, ro4, and Ad."
  },
  {
    "num": "9.87",
    "title": "In a current-mirror-loaded differential amplifier of the form shown in Fig.",
    "text": "9.87 In a current-mirror-loaded differential amplifier of\nthe form shown in Fig. 9.32(a), all transistors are characterized by k′W/L = 4 mA/V2, and VA = 5 V. Find the bias\ncurrent I for which the gain vo/vid = 20 V/V."
  },
  {
    "num": "9.88",
    "title": "Consider a current-mirror-loaded differential amplifier such as that shown in Fig.",
    "text": "9.88 Consider a current-mirror-loaded differential amplifier such as that shown in Fig. 9.32(a) with the bias current\nsource implemented with the modified Wilson mirror."
  },
  {
    "num": "9.89",
    "title": "Sketch the circuit of a current-mirror-loaded MOS differential amplifier in which the input transistors are cascoded...",
    "text": "9.89 Sketch the circuit of a current-mirror-loaded MOS\ndifferential amplifier in which the input transistors are\ncascoded and a cascode current mirror is used for the load."
  },
  {
    "num": "9.90",
    "title": "",
    "text": "9.90 Figure P9.91 shows the current-mirror-loaded MOS\ndifferential amplifier prepared for small-signal analysis."
  },
  {
    "num": "9.91",
    "title": "A current-mirror-loaded NMOS differential amplifier operates with a bias current I of 200 μA.",
    "text": "9.91 A current-mirror-loaded NMOS differential amplifier\noperates with a bias current I of 200 μA. The NMOS transistors are operated at VOV = 0.2 V and the PMOS devices at\nV\nOV = 0.3 V. The Early voltages are 20 V for the NMOS and\n12 V for the PMOS transistors. Find G\nm, Ro, and Ad. For what\nvalue of load resistance is the gain reduced by a factor of 2?"
  },
  {
    "num": "9.92",
    "title": "This problem investigates the effect of transistor mismatches on the input offset voltage of the current-mirror-loade...",
    "text": "9.92 This problem investigates the effect of transistor mismatches on the input offset voltage of the\ncurrent-mirror-loaded MOS differential amplifier of\nFig. 9.32(a)."
  },
  {
    "num": "9.93",
    "title": "The differential amplifier in Fig.",
    "text": "9.93 The differential amplifier in Fig. 9.36(a) is operated\nwith I = 500 μA, with devices for which VA =10 V and\nβ = 100. What differential input resistance, output resistance,\nshort-circuit transconductance, and open-circuit voltage gain\nwould you expect? What will the voltage gain be if the input\nresistance of the subsequent stage is equal to Rid of this stage?"
  },
  {
    "num": "9.94",
    "title": "A bipolar differential amplifier having a simple pnp current-mirror load is found to have an input offset voltage of...",
    "text": "9.94 A bipolar differential amplifier having a simple pnp\ncurrent-mirror load is found to have an input offset voltage of\n2 mV. If the offset is attributable entirely to the finite β of the\npnp transistors, what must βP be?"
  },
  {
    "num": "9.95",
    "title": "For the current-mirror-loaded bipolar differential pair, replacing the simple current-mirror load by the base-current...",
    "text": "9.95 For the current-mirror-loaded bipolar differential\npair, replacing the simple current-mirror load by the\nbase-current-compensated mirror of Fig. 8.11, find the\nexpected systematic input offset voltage. Evaluate VOS for\nβP = 50."
  },
  {
    "num": "9.96",
    "title": "For the current-mirror-loaded bipolar differential pair, replacing the simple current-mirror load by the Wilson mirro...",
    "text": "9.96 For the current-mirror-loaded bipolar differential pair,\nreplacing the simple current-mirror load by the Wilson mirror\nof Fig. 8.40(a), find the expected systematic input offset\nvoltage. Evaluate VOS for βP,= 50."
  },
  {
    "num": "9.97",
    "title": "",
    "text": "9.97 Figure P9.98 shows a differential cascode amplifier\nwith an active load formed by a Wilson current mirror."
  },
  {
    "num": "9.98",
    "title": "Consider the bias design of the Wilson-loaded cascode differential amplifier shown in Fig.",
    "text": "9.98 Consider the bias design of the Wilson-loaded\ncascode differential amplifier shown in Fig. P9.98."
  },
  {
    "num": "9.99",
    "title": "",
    "text": "9.99 Figure P9.100 shows a modified cascode differential amplifier. Here Q3 and Q4 are the cascode transistors.\nHowever, the manner in which Q3 is connected with its\nbase current feeding the current mirror Q7–Q8 results in very\ninteresting input properties."
  },
  {
    "num": "9.100",
    "title": "For the folded-cascode differential amplifier of Fig.",
    "text": "9.100 For the folded-cascode differential amplifier of\nFig. 9.38, find the value of VBIAS that results in the largest\npossible positive output swing, while keeping Q3, Q4, and\nthe pnp transistors that realize the current sources out of\nsaturation."
  },
  {
    "num": "9.101",
    "title": "For the BiCMOS differential amplifier in Fig.",
    "text": "9.101 For the BiCMOS differential amplifier in Fig. P9.102\nlet V\nDD = VSS =3 V, I = 0.2 mA, kp′W/L = 6.4 mA/V2; VA\nfor p-channel MOSFETs is 10 V, VA for npn transistors is\n30 V. Find G\nm, Ro, and Ad."
  },
  {
    "num": "9.102",
    "title": "It is required to design the current-mirrorloaded differential MOS amplifier of Fig.",
    "text": "9.102 It is required to design the current-mirrorloaded differential MOS amplifier of Fig. 9.32 to obtain a\ndifferential gain of 50 V/V."
  },
  {
    "num": "9.103",
    "title": "Consider the current-mirror-loaded MOS differential amplifier of Fig.",
    "text": "9.103 Consider the current-mirror-loaded MOS differential\namplifier of Fig. 9.32(a) in two cases:\n(a) Current source I is implemented with a simple current\nmirror.\n(b) Current sourceIis implemented with themodifiedWilson\ncurrent mirror."
  },
  {
    "num": "9.104",
    "title": "The MOS differential amplifier of Fig.",
    "text": "9.104 The MOS differential amplifier of Fig. 9.32(a) is\nbiased with a simple current mirror delivering I = 200 μA.\nAll transistors are operated at VOV = 0.2 V and have VA = 5 V.\nFind G\nm, Ro, Ad, RSS, Gmcm, Rim, Am, Rom, Ro2, Acm, and\nCMRR."
  },
  {
    "num": "9.105",
    "title": "A current-mirror-loaded MOS differential amplifier is found to have a differential voltage gain Ad of 30 V/V.",
    "text": "9.105 A current-mirror-loaded MOS differential amplifier\nis found to have a differential voltage gain Ad of 30 V/V.\nIts bias current source has an output resistance RSS = 45 k.\nThe current mirror utilized has a current gain Am of 0.98 A/A\nand an output resistance Rom of 45 k. If the common-mode\noutput resistances of the amplifier, Ro1 and Ro2, are very large,\nfind A\ncm and CMRR."
  },
  {
    "num": "9.106",
    "title": "It is required to design the circuit of Fig.",
    "text": "9.106 It is required to design the circuit of Fig. 9.36(a) using a basic\ncurrent mirror to implement the current source I. It is required\nthat the short-circuit transconductance be 5 mA/V. Use ±5-V\npower supplies and BJTs that have β = 100 and VA =100 V."
  },
  {
    "num": "9.107",
    "title": "Repeat the design of the amplifier specified in Problem 9.108 utilizing a Widlar current source (Fig.",
    "text": "9.107 Repeat the design of the amplifier specified in\nProblem 9.108 utilizing a Widlar current source (Fig. 8.42)\nto supply the bias current. Assume that the largest resistance\navailable is 2 k."
  },
  {
    "num": "9.108",
    "title": "A bipolar differential amplifier such as that shown in Fig.",
    "text": "9.108 A bipolar differential amplifier such as that shown in\nFig. 9.36(a) has I = 0.4 mA, VA =40 V, and β = 150. Find\nG\nm, Ro, Ad, and Rid. If the bias current source is implemented\nwith a simple npn current mirror, find REE, Acm, and CMRR.\nIf the amplifier is fed differentially with a source having\na total of 30 k resistance (i.e., 15 k in series with the\nbase lead of each of Q1 and Q2), find the overall differential\nvoltage gain."
  },
  {
    "num": "9.109",
    "title": "For the current mirror in Fig.",
    "text": "9.109 For the current mirror in Fig. P9.111, find:\n(a) differential input resistance, Rid\n(b) Ad\n(c) CMRR"
  },
  {
    "num": "9.110",
    "title": "For the current-mirror-loaded differential amplifier in Fig.",
    "text": "9.110 For the current-mirror-loaded differential amplifier in\nFig. P9.112, find:\n(a) differential input resistance, Rid\n(b) Ad\n(c) CMRR"
  },
  {
    "num": "9.111",
    "title": "Consider the circuit in Fig.",
    "text": "9.111 Consider the circuit in Fig. 9.40 with the\ndevice geometries (in μm) shown in Table P9.113."
  },
  {
    "num": "9.112",
    "title": "The two-stage CMOS op amp in Fig.",
    "text": "9.112 The two-stage CMOS op amp in Fig. P9.114 is\nfabricated in a 0.18-μm technology having kn′ = 4kp′ =\n400 μA/V2 and V\ntn = −Vtp = 0.4 V."
  },
  {
    "num": "9.113",
    "title": "In a particular design of the CMOS op amp of Fig.",
    "text": "9.113 In a particular design of the CMOS op amp of\nFig. 9.40 the designer wishes to investigate the effects of\nincreasing the W/L ratio of both Q1 and Q2 by a factor\nof 4."
  },
  {
    "num": "9.114",
    "title": "Consider the amplifier of Fig.",
    "text": "9.114 Consider the amplifier of Fig. 9.40, whose parameters\nare specified in Example 9.6. If a manufacturing error results\nin the W/L ratio of Q7 being 48/0.8, find the current that Q7\nwill now conduct."
  },
  {
    "num": "9.115",
    "title": "Consider the input stage of the CMOS op amp in Fig.",
    "text": "9.115 Consider the input stage of the CMOS op amp in\nFig. 9.40 with both inputs grounded. Assume that the two\nsides of the input stage are perfectly matched except that\nthe threshold voltages of Q3 and Q4 have a mismatch\n1V\nt."
  },
  {
    "num": "9.116",
    "title": "The two-stage op amp in",
    "text": "9.116 The two-stage op amp in Figure P9.114 is fabricated\nin a 65-nm technology having kn′ = 5.4 × kp′ = 540 μA/V2\nand V\ntn = −Vtp = 0.35 V."
  },
  {
    "num": "9.117",
    "title": "",
    "text": "9.117 Figure P9.119 shows a bipolar op-amp circuit\nthat resembles the CMOS op amp of Fig. 9.40."
  },
  {
    "num": "9.118",
    "title": "A BJT differential amplifier, biased to have re =50  and utilizing two 50-emitterresistors and 5-kloads, drives a...",
    "text": "9.118 A BJT differential amplifier, biased to have re =50 \nand utilizing two 50-emitterresistors and 5-kloads, drives\na second differential stage biased to have re =25 ."
  },
  {
    "num": "9.119",
    "title": "In the multistage amplifier of Fig.",
    "text": "9.119 In the multistage amplifier of Fig. 9.41, emitter\nresistors are to be introduced—100  in the emitter lead of\neach of the first-stage transistors and 25  for each of the\nsecond-stage transistors."
  },
  {
    "num": "9.120",
    "title": "Consider the circuit of Fig.",
    "text": "9.120 Consider the circuit of Fig. 9.41 and its output\nresistance. Which resistor has the most effect on the output\nresistance?"
  },
  {
    "num": "9.121",
    "title": "(a) If, in the multistage amplifier of Fig.",
    "text": "9.121 (a) If, in the multistage amplifier of Fig. 9.41, the\nresistor R\n5 is replaced by a constant-current source ≃ 1 mA,\nsuch that the bias situation is essentially unaffected, what does\nthe overall voltage gain of the amplifier become?"
  },
  {
    "num": "9.122",
    "title": "",
    "text": "9.122 Figure P9.124 shows a three-stage amplifier in which\nthe stages are directly coupled. The amplifier, however,\nutilizes bypass capacitors, and, as such, its frequency response\nfalls off at low frequencies."
  },
  {
    "num": "9.123",
    "title": "For the current mirror in Fig.",
    "text": "9.123 For the current mirror in Fig. P9.125, replace the\ntransistors with their hybrid-π models and show that:"
  },
  {
    "num": "9.124",
    "title": "The MOS differential amplifier shown in Fig.",
    "text": "9.124 The MOS differential amplifier shown in\nFig. P9.126 utilizes three current mirrors for signal\ntransmission."
  },
  {
    "num": "9.125",
    "title": "For the circuit shown in Fig.",
    "text": "9.125 For the circuit shown in Fig. P9.127, which uses\na folded cascode involving transistor Q3, all transistors have\nV\nBE = 0.7 V for the currents involved, VA =200 V, and\nβ = 100."
  },
  {
    "num": "9.126",
    "title": "In the CMOS op amp shown in Fig.",
    "text": "9.126 In the CMOS op amp shown in Fig. P9.128, all\nMOS devices have V\nt = 1V, μn Cox =2 μpCox =40 μA/V2,\nVA\n= 50 V, and L = 5 μm."
  }
]

THEORY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      color: #111;
      background: #fff;
    }
    .wrap {
      border: 1px solid #ddd;
      border-radius: 14px;
      padding: 28px;
    }
    h1 {
      margin-top: 0;
      font-size: 28px;
    }
    .meta {
      color: #555;
      margin-bottom: 24px;
      font-size: 14px;
    }
    .problem-box {
      background: #f8f8f8;
      border-left: 4px solid #333;
      padding: 16px;
      white-space: pre-wrap;
    }
    .note {
      margin-top: 24px;
      padding: 14px;
      background: #fff8e1;
      border: 1px solid #f0d98c;
      border-radius: 10px;
    }
    a {
      color: #0b57d0;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>{title}</h1>
    <div class="meta">Sedra — Chapter 9 • Differential and Multistage Amplifiers</div>
    <div class="problem-box">{problem_text}</div>
    <div class="note">
      Solution content can be added here later.
    </div>
  </div>
</body>
</html>
"""

SIM_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Simulation</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      color: #111;
      background: #fff;
    }
    .wrap {
      border: 1px solid #ddd;
      border-radius: 14px;
      padding: 28px;
    }
    h1 {
      margin-top: 0;
      font-size: 28px;
    }
    .meta {
      color: #555;
      margin-bottom: 24px;
      font-size: 14px;
    }
    .placeholder {
      background: #f5f7fb;
      border: 1px dashed #9aa8c7;
      border-radius: 10px;
      padding: 18px;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>{title} — Simulation</h1>
    <div class="meta">Sedra — Chapter 9 • Placeholder simulation page</div>
    <div class="placeholder">Add your simulation, visualization, or interactive model here.</div>
  </div>
</body>
</html>
"""

CARD_TEMPLATE = """<article class=\"card\" data-tags=\"circuits-electronics sedra chapter-9 differential-amplifiers multistage-amplifiers\">
  <h3>Sedra — Chapter 9</h3>
  <p>Problem {num}: {title}</p>
  <div class=\"btn-row\">
    <a href=\"./Sedra/Sedra_ch9_prob_{num}.html\">OPEN THEORY</a>
    <a href=\"./Sedra/Sedra_ch9_prob_{num}_sim.html\">OPEN SIM</a>
  </div>
</article>"""

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def build():
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    cards = []
    for item in PROBLEMS:
        num = item["num"]
        title = f"Sedra Chapter 9 — Problem {num}"
        problem_text = html.escape(item["text"])
        theory_html = THEORY_TEMPLATE.replace("{title}", title).replace("{problem_text}", problem_text)
        sim_html = SIM_TEMPLATE.replace("{title}", title)
        theory_name = f"Sedra_ch9_prob_{num}.html"
        sim_name = f"Sedra_ch9_prob_{num}_sim.html"
        write_text(TARGET_DIR / theory_name, theory_html)
        write_text(TARGET_DIR / sim_name, sim_html)
        cards.append(CARD_TEMPLATE.replace("{num}", num).replace("{title}", html.escape(item["title"])))
    cards_html = "\n".join(cards)
    write_text(TARGET_DIR / "Sedra_ch9_cards.html", cards_html)
    print(f"Created {len(PROBLEMS)} theory files, {len(PROBLEMS)} sim files, and Sedra_ch9_cards.html in {TARGET_DIR}")

if __name__ == "__main__":
    build()
