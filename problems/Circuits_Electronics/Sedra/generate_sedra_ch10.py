
from pathlib import Path
import os, re, html

DEFAULT_TARGET = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
TARGET_DIR = Path(os.environ.get("SEDRA_TARGET_DIR", DEFAULT_TARGET))

RAW_TEXT = r"""
**PROBLEMS
Computer Simulation Problems
Problems identified by the Multisim/PSpice icon are
intended to demonstrate the value of using SPICE simulation
to verify hand analysis and design, and to investigate important issues such as gain–bandwidth trade-off. Instructions to
assist in setting up PSpice and Multisim simulations for all
the indicated problems can be found in the corresponding
files on the website. Note that if a particular parameter value
is not specified in the problem statement, you are to make a
reasonable assumption.
Section 10.1: Low-Frequency Response
of Discrete-Circuit Common-Source and
Common-Emitter Amplifiers
D 10.1 For the amplifier in Fig. 10.3(a), if RG1 = 2 M,
R
G2 = 1M, and Rsig = 200k, find the value of the coupling
capacitor CC1 (specified to one significant digit) that places
the associated pole at 10 Hz or lower.
D 10.2 For the amplifier in Fig. 10.3(a), if RD = 10 k,
R
L = 10 k, and ro is very large, find the value of CC2
(specified to one significant digit) that places the associated
pole at 10 Hz or lower.
D 10.3 The amplifier in Fig. 10.3(a) is biased to operate at
gm = 5 mA/V, and RS = 1.8k. Find the value of CS (specified
to one significant digit) that places its associated pole at 100
Hz or lower. What are the actual frequencies of the pole and
zero realized?
10.4 The amplifier in Fig. 10.3(a) is biased to operate at
gm = 5 mA/V, and has the following component values:
R
sig = 100 k, RG1 = 47 M, RG2 = 10 M, CC1 = 0.01 μF,
R
S = 2 k, CS = 10 μF, RD = 4.7 k, RL = 10 k, and
C
C2 = 1 μF. Find AM, fP1, fP2, fZ, fP3, and fL.
D 10.5 The amplifier in Fig. P10.5 is biased to operate at
gm = 2 mA/V. Neglect ro.
RD
Vo
CS
RS
4.5 k
VSS
Vi
VDD
2
2
1
Figure P10.5
(a) Determine the value of RD that results in a midband gain
of −20 V/V.
(b) Determine the value of CS that results in a pole frequency
of 100 Hz.
(c) What is the frequency of the transmission zero introduced
by CS?
(d) Give an approximate value for the 3-dB frequency fL.
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
790 Chapter 10 Frequency Response
(e) Sketch a Bode plot for the gain of this amplifier. What
does the plot tell you about the gain at dc? Does this make
sense? Why or why not?
D 10.6 Figure P10.6 shows a CS amplifier biased by a
constant-current source I. Let R
sig = 0.5 M, RG = 2 M,
gm = 3 mA/V, RD = 20 k, and RL = 10 k. Find AM. Also,
design the coupling and bypass capacitors to locate the three
low-frequency poles at 100 Hz, 10 Hz, and 1 Hz. Use a
minimum total capacitance, with the capacitors specified only
to a single significant digit. What value of fL results?
D 10.7 Figure P10.7 shows a current-biased CE amplifier
operating at 100 μA from ±3-V power supplies. It employs
R
G
I
CC2
CS
CC1
R
L
R
D
VDD
–VSS
Vo
12
V
sig
R
sig
Figure P10.6
R
B
I
CC2
CE
CC1
R
L
R
C
VCC
–VEE
Vo
12
V
sig
R
sig
Figure P10.7
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 791
R
C = 20 k, RB = 200 k, and operates between a 20-k
source and a 10-k load. The transistor β = 100. Select CE
first, for a minimum value specified to one significant digit
and providing up to 80% of fL where fL is to be 100 Hz. Then
choose C
C1 and CC2, each specified to one significant digit,
and each contributing about 10% of fL. What fL results? What
total capacitance is needed?
10.8 Consider the common-emitter amplifier of Fig. 10.9(a)
under the following conditions: Rsig = 5 k, RB1 = 33 k,
R
B2 = 22 k, RE = 3.9 k, RC = 4.7 k, RL = 5.6 k,
V
CC = 5 V. The dc emitter current can be shown to be
IE
≃0.3 mA, at which β = 120. Find the input resistance
R
in and the midband gain AM. If CC1 = CC2 = 1 μF and
CE
= 20 μF, find the three short-circuit time constants and an
estimate for fL.
D 10.9 For the amplifier described in Problem 10.8, design
the coupling and bypass capacitors for a lower 3-dB frequency
of 50 Hz. Design so that the contribution of each of CC1 and
C
C2 to determining fL is only 10%.
10.10 Consider the circuit of Fig. 10.9(a). For Rsig = 5 k,
R
B ≡ RB1kRB2 = 10 k, rπ = 1 k, β0 = 100, and
R
E = 1.5 k, what is the ratio CE/CC1 that makes their
contributions to the determination of fL equal?
D *10.11 For the common-emitter amplifier of Fig. P10.11,
neglect ro and assume the current source to be ideal.
R
L
R
sig
R
C
V
sig
Vo
CE
CC
VCC
I
12
Figure P10.11
(a) Derive an expression for the midband gain.
(b) Convince yourself that the two poles caused by CE and
C
C do not interact. Find expressions for their frequencies,
ω
PE and ωPC.
(c) Give an expression for the amplifier voltage gain
Vo
(s)/Vsig(s) in terms of AM, ωPE, and ωPC.
(d) For Rsig = RC = RL = 10 k, β = 100, and I = 1 mA, find
the value of the midband gain.
(e) Select values for CE and CC to place the two pole
frequencies a decade apart and to obtain a lower
3-dB frequency of 100 Hz while minimizing the total
capacitance.
(f) Sketch a Bode plot for the gain magnitude, and estimate
the frequency at which the gain becomes unity.
*10.12 The BJT common-emitter amplifier of Fig. P10.12
includes an emitter-degeneration resistance Re.
R
e
R
C
VCC
V
sig
CE
I
Vo
12
Figure P10.12
(a) Assuming α≃1, neglecting ro, and assuming the current source to be ideal, derive an expression for the
small-signal voltage gain A(s) ≡ Vo/Vsig that applies in
the midband and the low-frequency band. Hence find the
midband gain AM and the lower 3-dB frequency fL.
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
792 Chapter 10 Frequency Response
(b) Show that including Re reduces the magnitude of AM by
a certain factor. What is this factor?
(c) Show that including Re reduces fL by the same factor as in
(b) and thus one can use Re to trade off gain for bandwidth.
(d) For I = 0.25 mA, RC = 10 k, and CE = 10 μF, find
A
M and fL with Re = 0. Now find the value of Re that
lowers fL by a factor of 10. What will the gain become?
Sketch on the same diagram a Bode plot for the gain
magnitude for both cases.
Section 10.2: Internal Capacitive Effects and the
High-Frequency Model of the MOSFET and the
BJT
10.13 Refer to the MOSFET high-frequency model in
Fig. 10.12(a). Evaluate the model parameters for an
NMOS transistor operating at ID = 200 μA, VSB = 1 V, and
V
DS = 1.5 V. The MOSFET has W = 20 μm, L = 1 μm,
t
ox = 8 nm, μn = 450 cm2/V·s, γ = 0.5 V1/2, 2φ f = 0.65 V,
λ = 0.05 V−1, V0 = 0.7 V, Csb0 = Cdb0 = 20 fF, and
L
ov = 0.05 μm. [Recall that gmb = χgm, where χ =
γ / 2p2φf +VSB, and that eox = 3.45×10−11 F/m.]
10.14 Find fT for a MOSFET operating at ID = 200 μA and
V
OV = 0.3 V. The MOSFET has Cgs = 25 fF and Cgd = 5 fF.
10.15 Starting from the expression of fT for a MOSFET,
fT =
gm
2π(Cgs +Cgd)
and making the approximation that Cgs ≫ Cgd and that the
overlap component of Cgs is negligibly small, show that
fT ≃
1.5
πL s μnID
2C
oxWL
Thus note that to obtain a high fT from a given device, it must
be operated at a high current. Also note that faster operation
is obtained from smaller devices.
10.16 Starting from the expression for the MOSFET
unity-gain frequency,
fT =
gm
2π(Cgs +Cgd)
and making the approximation that Cgs ≫ Cgd and that the
overlap component of Cgs is negligibly small, show that for
an n-channel device
fT ≃
3μnVOV
4πL2
Observe that for a given channel length, fT can be increased
by operating the MOSFET at a higher overdrive voltage.
Evaluate fT for devices with L = 0.5 μm operated at overdrive
voltages of 0.2 V and 0.4 V. Use μn = 450 cm2/V·s.
10.17 It is required to calculate the intrinsic gain A0 and the
unity-gain frequency fT of an n-channel transistor fabricated
in a 0.13-μm CMOS process for which Lov = 0.1 L, μn =
400 cm2/V·s, and VA′ = 5 V/μm. The device is operated at
V
OV = 0.2 V. Find A0 and fT for devices with L = Lmin,
2L
min, 3Lmin, 4Lmin, and 5Lmin. Present your results in
a table. (Hint: For fT, use the approximate expression
fT ≃
3μnVOV
4πL2
.)
10.18 A particular BJT operating at IC = 0.5 mA has Cμ =
1 pF, Cπ = 8 pF, and β = 100. What are fT and fβ for this
situation?
10.19 For the transistor described in Problem 10.18, Cπ
includes a relatively constant depletion-layer capacitance
Transistor IE(mA) re() gm(mA/V) rπ (k) β0 fT (MHz) Cμ(pF) Cπ(pF) fβ(MHz)
(a) 2 100 500 2
(b) 25 2 10.7 4
(c) 2.5 100 500 10.7
(d) 10 100 500 2
(e) 0.1 100 150 2
(f) 1 10 500 2
(g) 800 1 9 80
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 793
of 2 pF. If the device is operated at IC = 0.25 mA, what does
its fT become?
10.20 An npn transistor is operated at IC = 1 mA and
V
CB = 2 V. It has β0 = 100, VA = 50 V, τF = 30 ps,
C
je0 = 20 fF, Cμ0 = 30 f F, V0c = 0.75 V, mCBJ = 0.5, and
rx
= 100 . Sketch the complete hybrid-π model, and specify
the values of all its components. Also, find fT.
10.21 Measurement of h
fe of an npn transistor at 50 MHz
shows that h
fe = 10 at IC = 0.2 mA and 12 at IC = 1.0 mA.
Furthermore, C
μ was measured and found to be 0.1 pF. Find
fT at each of the two collector currents used. What must τF
and C
je be?
10.22 A particular small-geometry BJT has fT of 10 GHz
and C
μ = 0.1 pF when operated at IC = 1.0 mA. What is Cπ
in this situation? Also, find gm. For β = 120, find rπ and fβ.
10.23 For a BJT whose unity-gain bandwidth is 2 GHz and
β0 = 200, at what frequency does themagnitude ofhfe become
40? What is fβ?
*10.24 For a sufficiently high frequency, measurement of
the complex input impedance of a BJT having (ac) grounded
emitter and collector yields a real part approximating rx. For
what frequency, defined in terms of ωβ, is such an estimate
of r
x good to within 10% under the condition that rx ≤ rπ/10?
*10.25 Complete the table entries on the previous page for
transistors (a) through (g), under the conditions indicated.
Neglect rx.
Section 10.3: High-Frequency Response of the
CS and CE Amplifiers
10.26 In a particular common-source amplifier for which the
midband voltage gain between gate and drain (i.e., −gmRL′ )
is −39 V/V, the NMOS transistor has C
gs = 1.0 pF and
C
gd = 0.1 pF. What input capacitance would you expect? For
what range of signal-source resistances can you expect the
3-dB frequency to exceed 1 MHz? Neglect the effect of RG.
D 10.27 In the circuit of Fig. P10.27, the voltage amplifier is
ideal (i.e., it has an infinite input resistance and a zero output
resistance).
(a) Use the Miller approach to find an expression for the input
capacitance Cin in terms of A and C.
(b) Use the expression for Cin to obtain the transfer function
Vo
(s)/Vsig(s).
V
sig
C
R
sig
Cin
1 Vo 2
Vi
1 2
12
2 1
A
Figure P10.27
(c) If Rsig = 1 k, and the gain Vo/Vsig is to have a dc value of
40 dB and a 3-dB frequency of 100 kHz, find the values
required for A and C.
(d) Sketch a Bode plot for the gain and use it to determine the frequency at which its magnitude reduces to
unity.
10.28 An ideal voltage amplifier having a voltage gain of
–1000 V/V has a 0.2-pF capacitance connected between its
output and input terminals. What is the input capacitance
of the amplifier? If the amplifier is fed from a voltage
source V
sig having a resistance Rsig = 1 k, find the transfer
function V
o/Vsig as a function of the complex-frequency
variable s and hence the 3-dB frequency fH and the unity-gain
frequency ft.
D 10.29 A design is required for a CS amplifier for which
the MOSFET is operated at gm = 5 mA/V and has Cgs = 5 pF
and C
gd = 1 pF. The amplifier is fed with a signal source
having Rsig = 1 k, and RG is very large. What is the largest
value of R′
L for which the upper 3-dB frequency is at least
6 MHz? What is the corresponding value of midband gain
and gain–bandwidth product? If the specification on the upper
3-dB frequency can be relaxed by a factor of 3, that is, to
2 MHz, what can AM and GB become?
10.30 Reconsider Example 10.3 for the situation in which
the transistor is replaced by one whose width W is half
that of the original transistor while the bias current remains
unchanged. Find modified values for all the device parameters
along with AM, fH, and the gain–bandwidth product, GB.
Contrast this with the original design by calculating the ratios
of new value to old for W, VOV, gm, Cgs, Cgd, Cin, AM, fH,
and GB.
D *10.31 In a CS amplifier, such as that in Fig. 10.3(a),
the resistance of the source R
sig = 100 k, amplifier
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
794 Chapter 10 Frequency Response
input resistance (which is due to the biasing network)
R
in = 100 k, Cgs = 1 pF, Cgd = 0.2 pF, gm = 3 mA/V,
ro
= 50 k, RD = 8 k, and RL = 10 k. Determine the
expected 3-dB cutoff frequency fH and the midband gain.
In evaluating ways to double fH, a designer considers the
alternatives of changing either RL or Rin. To raise fH as
described, what separate change in each would be required?
What midband voltage gain results in each case?
10.32 A discrete MOSFET common-source amplifier has
R
G = 2 M, gm = 5 mA/V, ro = 100 k, RD = 20 k,
C
gs = 3 pF, and Cgd = 0.5 pF. The amplifier is fed from a
voltage source with an internal resistance of 500 k and is
connected to a 20-k load. Find:
(a) the overall midband gain AM
(b) the upper 3-dB frequency fH
(c) the frequency of the transmission zero, fZ.
10.33 For the discrete-circuit CS amplifier in Fig. 10.3(a)
let R
sig = 100 k, RG1 = 47 M, RG2 = 10 M, RS = 2 k,
R
D = 4.7 k, RL = 10 k, gm = 3 mA/V, ro = 100 k,
C
gs = 1 pF, and Cgd = 0.2 pF. Find AM and fH.
10.34 Consider the integrated-circuit CS amplifier in
Fig. P10.34 for the case IBIAS = 100 μA, Q2 and Q3 are
matched, and Rsig = 200 k. For Q1: μnCox = 90 μA/V2,
VA
= 12.8 V, W/L = 100 μm/1.6 μm, Cgs = 0.2 pF, and
C
gd = 0.015 pF. For Q2: |VA| = 19.2 V. Neglecting the
effect of the capacitance inevitably present at the output node,
find the low-frequency gain, the 3-dB frequency fH, and the
frequency of the zero fZ.
Q1
Q3 Q2
IBIAS
V
o
V
sig
R
sig
Figure P10.34
10.35 A common-emitter amplifier is measured at midband
and found to have a gain of −50 V/V between base and
collector. If C
π = 10 pF, Cμ = 1 pF, and the effective source
resistance R′
sig = 5 k [refer to Fig. 10.19(b)], find Cin and the
3-dB frequency fH.
10.36 For a CE amplifier represented by the equivalent
circuit in Fig. 10.19(a), let Rsig = 10 k, RB = 100 k, rx =
100 , Cπ = 10 pF, Cμ = 1 pF, gm = 40 mA/V, ro = 100 k,
R
C = 10 k, RL = 10k, and β = 100. Find the midband gain
and the 3-dB frequency fH.
10.37 A designer wishes to investigate the effect of changing
the bias current I
E on the midband gain and high-frequency
response of the CE amplifier considered in Example 10.4.
Let I
E be doubled to 2 mA, and assume that β0 and fT remain
unchanged at 100 and 800 MHz, respectively. To keep the
node voltages nearly unchanged, the designer reduces RB and
R
C by a factor of 2, to 50 k and 4 k, respectively. Assume
rx
= 50 , and recall that VA = 100 V and that Cμ remains
constant at 1 pF. As before, the amplifier is fed with a source
having Rsig = 5 k and feeds a load RL = 5 k. Find the new
values of A
M, fH, and the gain–bandwidth product, AM fH.
Comment on the results. Note that the price paid for whatever
improvement in performance is achieved is an increase in
power. By what factor does the power dissipation increase?
*10.38 The purpose of this problem is to investigate the
high-frequency response of the CE amplifier when it is
fed with a relatively large source resistance Rsig. Refer
to the amplifier in Fig. 10.9(a) and to its high-frequency,
equivalent-circuit model and the analysis shown in Fig. 10.19.
Let R
B ≫ Rsig, rx ≪ Rsig, Rsig ≫ rπ, gmRL′ ≫ 1, and gmRL′ Cμ ≫
Cπ
. Under these conditions, show that:
(a) the midband gain AM ≃ −βRL′ /Rsig
(b) the upper 3-dB frequency fH ≃ 1/2πCμβRL′
(c) the gain–bandwidth product |AM| fH ≃ 1/2πCμRsig
Evaluate this approximate value of the gain–bandwidth
product for the case Rsig = 25 k and Cμ = 1 pF. Now, if
the transistor is biased at I
C = 1 mA and has β = 100, find
the midband gain and fH for the two cases RL′ = 25 k and
R′
L = 2.5 k. On the same coordinates, sketch Bode plots
for the gain magnitude versus frequency for the two cases.
What fH is obtained when the gain is unity? What value of RL′
corresponds?
10.39 For a version of the CE amplifier circuit in
Fig. 10.9(a), Rsig = 10 k, RB1 = 68 k, RB2 = 27 k,
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 795
R
E = 2.2 k, RC = 4.7 k, and RL = 10 k. The collector
current is 0.8 mA, β = 200, fT = 1 GHz, and Cμ = 0.8 pF.
Neglecting the effect of rx and ro, find the midband voltage
gain and the upper 3-dB frequency fH.
10.40 Consider an ideal voltage amplifier with a gain of
0.9 V/V, and a resistance R = 100 k connected in the feedback path—that is, between the output and input terminals.
Use Miller’s theorem to find the input resistance of this
circuit.
10.41 The amplifiers listed below are characterized by the
descriptor (A, C), where A is the voltage gain from input to
output and C is an internal capacitor connected between input
and output. For each, find the equivalent capacitances at the
input and at the output as provided by the use of Miller’s
theorem:
(a) –1000 V/V, 1 pF
(b) –10 V/V, 10 pF
(c) –1 V/V, 10 pF
(d) +1 V/V, 10 pF
(e) +10 V/V, 10 pF
Note that the input capacitance found in case (e) can be
used to cancel the effect of other capacitance connected
from input to ground. In (e), what capacitance can be
canceled?
*10.42 Figure P10.42 shows an ideal voltage amplifier with
a gain of +2 V/V (usually implemented with an op amp
connected in the noninverting configuration) and a resistance
R connected between output and input.
(a) Using Miller’s theorem, show that the input resistance
R
in = −R.
(b) Use Norton’s theorem to replace Vsig, Rsig, and Rin with a
signal current source and an equivalent parallelresistance.
Show that by selecting Rsig = R, the equivalent parallel
12
V
sig
Vo
R
sig
R
12
Rin
IL ZL
Figure P10.42
resistance becomes infinite and the current I
L into the load
impedance ZL becomes Vsig/R. The circuit then functions
as an ideal voltage-controlled current source with an
output current IL.
(c) If ZL is a capacitor C, find the transfer function Vo/Vsig and
show it is that of an ideal noninverting integrator.
10.43 Use Miller’s theorem to investigate the performance
of the inverting op-amp circuit shown in Fig. P10.43. Assume
the op amp to be ideal except for having a finite differential
gain, A. Without using any knowledge of op-amp circuit
analysis, find Rin, Vi, Vo, and Vo/Vsig, for each of the following
values of A: 10 V/V, 100 V/V, 1000 V/V, and 10,000 V/V.
Assume V
sig = 1 V. Present your results in the table below.
V
sig
10 k
1 k
Rin
1 Vo 2
Vi
2 1
12
2 1
Figure P10.43
A Rin Vi Vo Vo/Vsig
10 V/V
100 V/V
1000 V/V
10,000 V/V
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
796 Chapter 10 Frequency Response
*10.44 The amplifier shown in Fig. P10.44 has
R
sig = RL = 1 k, RC = 1 k, RB = 47 k, β = 100,
Cμ
= 0.8 pF, and fT = 600 MHz. Assume the coupling
capacitors to be very large.
(a) Find the dc collector current of the transistor.
(b) Find gm and rπ.
(c) Neglecting ro, find the midband voltage gain from base
to collector (neglect the effect of RB).
(d) Use the gain obtained in (c) to find the component of Rin
that arises as a result of R
B. Hence find Rin.
(e) Find the overall gain at midband.
(f) Find Cin.
(g) Find fH.
R
sig
Rin
CC1
V
sig
R
C
12
11.5 V
CC2
Vo
R
B
R
L
Figure P10.44
*10.45 Figure P10.45 shows a diode-connected transistor with the bias circuit omitted. Utilizing the BJT
high-frequency, hybrid-π model with rx = 0 and ro = ∞,
derive an expression for Zi(s) as a function of re and Cπ. Find
the frequency at which the impedance has a phase angle of
45° for the case in which the BJT has fT = 400 MHz and the
bias current is relatively high. What is the frequency when the
bias current is reduced so that C
π ≃ Cμ? Assume α = 1.
Figure P10.45
10.46 A CS amplifier modeled with the equivalent circuit
of Fig. 10.22(a) is specified to have Cgs = 2 pF, Cgd = 0.1 pF,
gm = 4 mA/V, CL = 2 pF, and RL′ = 20 k. Find AM, f3dB, fZ,
and ft.
D 10.47 A common-source amplifier fed with a
low-resistance signal source and operating with gm = 2 mA/V
has a unity-gain frequency of 2 GHz. What additional
capacitance must be connected to the drain node to reduce ft
to 1 GHz?
*10.48 It is required to analyze the high-frequency response
of the CMOS amplifier shown in Fig. P10.34 for the
case R
sig = 0. The dc bias current is 100 μA. For Q1,
μnCox = 90 μA/V2, VA = 12.8 V, W/L = 100 μm/1.6 μm,
C
gs = 0.2 pF, Cgd = 0.015 pF, and Cdb = 20 fF. For Q2,
C
gd = 0.015 pF, Cdb = 36 fF, and VA = 19.2 V. For simplicity, assume that the signal voltage at the gate of Q2 is zero.
Find the low-frequency gain, the frequency of the pole, and
the frequency of the zero. (Hint: The total capacitance at the
output mode = Cdb1 +Cdb2 +Cgd2).
10.49 Consider an active-loaded common-emitter amplifier.
Let the amplifier be fed with an ideal voltage source Vi, and
neglect the effect of rx. Assume that the load current source has
a very highresistance and that there is a capacitance CL present
between the output node and ground. This capacitance represents the sum of the input capacitance of the subsequent stage
and the inevitable parasitic capacitance between collector and
ground. Show that the voltage gain is given by
Vo Vi
= −gmro
1−s C
μ/gm
1+s CL +Cμro
If the transistor is biased at I
C = 200 μA and VA = 100 V,
Cμ
= 0.2 pF, and CL = 1 pF, find the dc gain, the 3-dB
frequency, the frequency of the zero, and the frequency at
which the gain reduces to unity. Sketch a Bode plot for the
gain magnitude.
10.50 A particular BJT operating at 2 mA is specified to
have fT = 2 GHz, Cμ = 1 pF, rx = 100 , and β = 120.
The device is used in a CE amplifier operating from a
very-low-resistance voltage source.
(a) If the midband gain obtained is −10 V/V, what is the
value of fH?
(b) If the midband gain is reduced to −1 V/V (by changing
R′
L), what fH is obtained?
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 797
Section 10.4: Useful Tools for the Analysis of
the High-Frequency Response of Amplifiers
10.51 A direct-coupled amplifier has a low-frequency gain
of 40 dB, poles at 2 MHz and 20 MHz, a zero on the negative
real axis at 200 MHz, and another zero at infinite frequency.
Express the amplifier gain function in the form of Eqs. (10.70)
and (10.71), and sketch a Bode plot for the gain magnitude.
What do you estimate the 3-dB frequency fH to be?
10.52 An amplifier with a dc gain of 60 dB has a single-pole,
high-frequency response with a 3-dB frequency of 100 kHz.
(a) Give an expression for the gain function A(s).
(b) Sketch Bode diagrams for the gain magnitude and phase.
(c) What is the gain–bandwidth product?
(d) What is the unity-gain frequency?
(e) If a change in the amplifier circuit causes its transfer
function to acquire another pole at 1 MHz, sketch the
resulting gain magnitude and specify the unity-gain
frequency. Note that this is an example of an amplifier
with a unity-gain bandwidth that is different from its
gain–bandwidth product.
10.53 Consider an amplifier whose FH(s) is given by
FH
(s) =
1
1+ ωsP1 1+ ωsP2 
with ω
P1 < ωP2. Find the ratio ωP2/ωP1 for which the
value of the 3-dB frequency ωH calculated using the
dominant-pole approximation differs from that calculated
using the root-sum-of-squares formula (Eq. 10.77) by:
(a) 10%
(b) 1%
10.54 The high-frequency response of a direct-coupled
amplifier having a dc gain of –1000 V/V incorporates zeros at
∞ and 104 rad/s (one at each frequency) and poles at 103 rad/s
and 105 rad/s (one at each frequency). Write an expression for
the amplifier transfer function. Find ωH using
(a) the dominant-pole approximation
(b) the root-sum-of-squares approximation (Eq. 10.77).
If a way is found to lower the frequency of the finite zero to
103 rad/s, what does the transfer function become? What is
the 3-dB frequency of the resulting amplifier?
10.55 A direct-coupled amplifier has a dominant pole at
1000 rad/s and three coincident poles at a much higher frequency. These nondominant poles cause the phase lag of the
amplifier at high frequencies to exceed the 90° angle due to the
dominant pole. It is required to limit the excess phase at ω =
107 rad/s to 30° (i.e., to limit the total phase angle to –120°).
Find the corresponding frequency of the nondominant poles.
10.56 An IC CS amplifier has gm = 2 mA/V, Cgs = 30 fF,
C
gd = 5 fF, CL = 30 fF, Rsig ′ = 10 k, and RL′ = 20 k.
Use the method of open-circuit time constants to obtain an
estimate for fH. Also, find the frequency of the transmission
zero, fZ.
10.57 For a particular amplifier modeled by the circuit of
Fig. 10.18(a), gm = 5 mA/V, Rsig = 150 k, RG = 0.65 M,
R′
L = 10 k, Cgs = 2 pF, and Cgd = 0.5 pF. There is also a
load capacitance of 30 pF. Find the corresponding midband
voltage gain, the open-circuit time constants, and an estimate
of the 3-dB frequency.
10.58 Consider the high-frequency response of an amplifier
consisting of two identical stages in cascade, each with an
input resistance of 10 k and an output resistance of 2 k.
The two-stage amplifier is driven from a 10-k source and
drives a 1-k load. Associated with each stage is a parasitic
input capacitance (to ground) of 10 pF and a parasitic output
capacitance (to ground) of 2 pF. Parasitic capacitances of
10 pF and 7 pF also are associated with the signal-source and
load connections, respectively. For this arrangement, find the
three poles and estimate the 3-dB frequency fH.
10.59 A CS amplifier that can be represented by the
equivalent circuit of Fig. 10.24 has Cgs = 2 pF, Cgd = 0.1 pF,
CL
= 2 pF, gm = 4 mA/V, Rsig ′ = RL′ = 20 k. Find the
midband gain AM, the input capacitance Cin using the Miller
approximation, and hence an estimate of the 3-dB frequency
fH. Also, obtain another estimate of fH using the method of
open-circuit time constants. Which of the two estimates is more appropriate
and why?
D 10.60 For a CS amplifier with gm = 5 mA/V, Cgs = 5 pF,
C
gd = 1 pF, CL = 5 pF, Rsig ′ = 10 k, and RL′ = 10 k, find
τH
and fH. What is the percentage of τH that is caused by the
interaction of R′
sig with the input capacitance? To what value
must R′
sig be lowered in order to double fH?
D 10.61 For the CS amplifier in Example 10.8, find the value
of the additional capacitance to be connected at the output
node in order to lower fH to 100 MHz.
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
798 Chapter 10 Frequency Response
10.62 Consider the CE amplifier whose equivalent circuit is
shown in Fig. 10.19(a) but with a capacitance CL connected
across the output terminals. Let Rsig ′ = 5 k, RB = ∞, rx = 0,
gm = 20 mA/V, β = 100, Cπ = 10 pF, Cμ = 1 pF, RL′ = 5 k,
and C
L = 10 pF. Find AM and fH.
10.63 A common-emitter amplifier has Cπ = 10 pF, Cμ =
0.3 pF, CL = 3 pF, gm = 40 mA/V, β = 100, rx = 100 ,
R′
L = 5 k, and Rsig = 1 k. Find the midband gain AM
and an estimate of the 3-dB frequency fH using the Miller
approximation. Also, obtain another estimate of fH using
the method of open-circuit time constants. Which of the
two estimates would you consider to be more realistic,
and why?
10.64 Consider a CS amplifier loaded in a current source
with an output resistance equal to ro of the amplifying
transistor. The amplifier is fed from a signal source with Rsig =
ro
/2. The transistor is biased to operate at gm = 2 mA/V and
ro
= 20 k; C
gs = Cgd = 0.1 pF. Use the Miller approximation
to determine an estimate of fH. Repeat for the following two
cases: (i) the bias current I in the entire system is reduced by
a factor of 4, and (ii) the bias current I in the entire system
is increased by a factor of 4. Remember that both Rsig and RL
will change as ro changes.
10.65 Use the method of open-circuit time constants to
find fH for a CS amplifier for which gm = 1.5 mA/V, Cgs =
C
gd = 0.2 pF, ro = 20 k, RL = 12 k, and Rsig = 100 k
for the following cases: (a) CL = 0, (b) CL = 10 pF, and (c)
CL
= 50 pF. Compare with the value of fH obtained using the
Miller approximation.
Section 10.5: High-Frequency Response of the
Common-Gate and Cascode Amplifiers
10.66 A CG amplifier is specified to have Cgs = 4 pF, Cgd =
0.2 pF, CL = 2 pF, gm = 5 mA/V, Rsig = 1 k, and RL =
10 k. Neglecting the effects of ro, find the low-frequency
gain Vo/Vsig, the frequencies of the poles fP1 and fP2, and hence
an estimate of the 3-dB frequency fH.
*10.67 Sketch the high-frequency equivalent circuit of a CB
amplifier fed from a signal generator characterized by Vsig
and R
sig and feeding a load resistance RL in parallel with a
capacitance CL.
(a) Show that for rx = 0 and ro = ∞, the circuit can be
separated into two parts: an input part that produces a
pole at
fP1 =
1
2πC
π Rsigkre
and an output part that forms a pole at
fP2 =
1
2π(Cμ + CL)RL
Note that these are the bipolar counterparts of the MOS
expressions in Eqs. (10.94) and (10.95).
(b) Evaluate fP1 and fP2 and hence obtain an estimate for
fH for the amplifier with I = 1 mA, Cπ = 10 pF, Cμ = 1 pF,
CL = 1 pF, β = 100, RL = 10 k, and rx = 0 in the following two cases:
(i) Rsig = 1 k
(ii) Rsig = 10 k
10.68 Consider a CG amplifier loaded in a resistance RL = ro
and fed with a signal source having a resistance Rsig = ro/2.
Also let C
L = Cgs. Use the method of open-circuit time
constants to show that for gmro ≫ 1, the upper 3-dB frequency
is related to the MOSFET fT by the approximate expression
fH = fT/ gmro
10.69 For the CG amplifier in Example 10.9, how much
additional capacitance should be connected between the
output node and ground to reduce fH to 200 MHz?
10.70 An IC CG amplifier is fed from a signal source with
R
sig = ro/2, where ro is the MOSFET output resistance. It has a
current-source load with an output resistance equal to ro. The
MOSFET is operated at ID = 100 μA and has gm = 1.5 mA/V,
VA
= 10 V, C
gs = 0.2 pF, Cgd = 0.015 pF, and Cdb = 20 fF.
As well, the current-source load provides an additional 30 fF
capacitance at the output node. Find fH.
10.71 Find the dc gain and the 3-dB frequency of a MOS
cascode amplifier operated at gm = 2 mA/V and ro = 20 k.
The MOSFETs have C
gs = 20 fF, Cgd = 5 fF, and Cdb = 5 fF.
The amplifier is fed with a signal source with Rsig = 100 k
and is connected to a load resistance of 1 M. There is also
a load capacitance CL of 20 fF.
*10.72 (a) Consider a CS amplifier having Cgd = 0.2 pF,
R
sig = RL = 20 k, gm = 4mA/V, Cgs = 2 pF, CL (including
C
db) = 1 pF, Cdb = 0.2 pF, and ro = 20 k. Find the
low-frequency gain AM, and estimate fH using open-circuit
time constants. Hence determine the gain–bandwidth product.
(b) If a CG stage utilizing an identical MOSFET is cascaded
with the CS transistor in (a) to create a cascode amplifier,
determine the new values of A
M, fH, and gain–bandwidth
product. Assume RL remains unchanged.
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 799
D 10.73 It is required to design a cascode amplifier to
provide a dc gain of 74 dB when driven with a low-resistance
generator and utilizing NMOS transistors for which VA =
10 V, μnCox = 200 μA/V2, W/L = 50, Cgd = 0.1 pF, and
CL
= 1 pF. Assuming that RL = Ro, determine the overdrive
voltage and the drain current at which the MOSFETs should
be operated. Find the unity-gain frequency and the 3-dB
frequency. If the cascode transistor is removed and RL remains
unchanged, what will the dc gain become?
10.74 (a) Show that introducing a cascode transistor to an IC
CS amplifier whose bandwidth is limited by the interaction
of R
sig and the input capacitance, and whose load resistance
is equal to ro, increases the dc gain by approximately a factor
of 2 and fH by the factor N,
N =
C
gs +
1 2
(gmro)Cgd
C
gs +3Cgd
Assume that the bandwidth of the cascode amplifier is
primarily determined by the input circuit.
(b) If Cgd = 0.1Cgs and the dc gain of the CS amplifier is 50,
what is the value of N?
(c) If VA = 10 V, μnCox = 400 μA/V2, and W/L = 10,
find V
OV and ID at which the transistors must be
operating.
10.75 (a) For an integrated-circuit MOS cascode amplifier
fed with a source having a very smallresistance and loaded in a
resistance equal to its Ro, use the expression for the unity-gain
bandwidth in Fig. 10.29 to show that
ft =
p2μnCox(W/L)
2π(CL +Cgd)
pID
(b) For μnCox = 400 μA/V2, W/L = 20, CL = 20 fF, Cgd =
5 fF, and VA = 10 V, provide in table form ft (GHz), VOV (V),
gm (mA/V), ro (k), Ro (M), AM (V/V), and fH (MHz) for
ID
= 100 μA, 200 μA, and 500 μA.
10.76 Consider a bipolar cascode amplifier biased at a
current of 1 mA. The transistors used have β = 100, ro =
100 k, Cπ = 10 pF, Cμ = 2 pF, Ccs = 0, and rx = 50 . The
amplifier is fed with a signal source having Rsig = 5 k. The
load resistance R
L = 2 k. Find the low-frequency gain AM,
and estimate the value of the 3-dB frequency fH.
*10.77 In this problem we consider the frequency response
of the bipolar cascode amplifier in the case that ro can be
neglected.
(a) Refer to the circuit in Fig. 10.30, and note that the total
resistance between the collector of Q1 and ground will be
equal to re2, which is usually very small. It follows that the
pole introduced at this node will typically be at a very high
frequencyandthuswillhavenegligibleeffectonfH.Italso
follows that at the frequencies of interest the gain from
the base to the collector of Q1 will be −gm1re2 ≃ −1. Use
this to find the capacitance at the input of Q1 and hence
show that the pole introduced at the input node will have
a frequency
fP1 ≃
1
2πR′
sig Cπ1 +2Cμ1
Then show that the pole introduced at the output node
will have a frequency
fP2 ≃
1
2πR
L CL +Ccs2 +Cμ2
(b) Evaluate fP1 and fP2, and use the sum-of-the-squares
formula to estimate fH for the amplifier with I = 1 mA,
Cπ
= 10 pF, Cμ = 2 pF, Ccs = CL = 0, β = 100, RL = 2
k, and rx = 0 in the following two cases:
(i) Rsig = 1 k
(ii) Rsig = 10 k
10.78 A BJT cascode amplifier uses transistors for which
β = 100, VA = 100 V, fT = 1 GHz, and Cμ = 0.1 pF. It operates
at a bias current of 0.1 mA between a source with R
sig = rπ and
a load R
L = βro. Let CL = Ccs = 0, and rx = 0. Find the overall
voltage gain at dc. By evaluating the various components of τH
show that the pole introduced at the output mode is dominant.
Find its frequency and hence an estimate of fH and ft.
Section 10.6: High-Frequency Response of the
Source and Emitter Followers
10.79 A source follower has gm = 5 mA/V, gmb = 0, ro =
20 k, Rsig = 20 k, RL = 2 k, Cgs = 2 pF, Cgd = 0.1 pF,
and C
L = 1 pF. Find AM, Ro, fZ, the frequencies of the two
poles, and an estimate of fH.
10.80 Using the expression for the source follower fH in
Eq. (10.124) show that for situations in which CL = 0, Rsig
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
800 Chapter 10 Frequency Response
is large and RL is small,
fH ≃
1
2πR
sigCgd + Cgs
1+gmRL′ 
Find fH for the case Rsig = 100 k, RL = 2 k, ro = 20 k,
gm = 5 mA/V, Cgd = 10 pF, and Cgs = 2 pF.
10.81 Refer to Fig. 10.31(c). In situations in which Rsig is
large, the high-frequency response of the source follower is
determined by the low-pass circuit formed by Rsig and the input
capacitance. An estimate of Cin can be obtained by using the
Miller approximation to replace Cgs with an input capacitance
C
eq = Cgs(1−K) where K is the gain from gate to source.
Using the low-frequency value of K = gmRL′ /(1 + gmRL′ ) find
C
eq and hence Cin and an estimate of fH.
10.82 A source follower has a maximally flat gain response
with a dc gain of 0.8 and a 3-dB frequency of 1 MHz. Give
its transfer function.
10.83 A discrete-circuit source follower driven with R
sig =
100 k has C
gs = 10 pF, Cgd = 1 pF, CL = 10 pF, gmb = 0,
and r
o very large. The transfer function of the source follower
is measured as R
L is varied. At what value of RL will the
transfer function be maximally flat? At this value of RL the dc
gain is found to be 0.9 V/V. What is the 3-dB frequency?
What is the value of gm at which the source follower is
operating?
10.84 For an emitter follower biased at I
C = 1 mA, having
R
sig = RL = 1 k, and using a transistor specified to have
fT = 2 GHz, Cμ = 0.1 pF, CL = 0, rx = 100 , β = 100, and
VA
= 20 V, evaluate the low-frequency gain AM, the frequency
of the transmission zero, the pole frequencies, and an estimate
of the 3-dB frequency fH.
Section 10.7: High-Frequency Response
of Differential Amplifiers
10.85 A MOSFET differential amplifier such as that shown
in Fig. 10.34(a) is biased with a current source I = 400 μA.
The transistors have W/L = 16, kn′ = 400 μA/V2,VA = 20 V,
C
gs = 40 fF, Cgd = 5 fF, and Cdb = 5 fF. The drain resistors
are 10 k each. Also, there is a 100-fF capacitive load
between each drain and ground.
(a) Find VOV and gm for each transistor.
(b) Find the differential gain Ad.
(c) If the input signal source has a small resistance Rsig and
thus the frequency response is determined primarily by
the output pole, estimate the 3-dB frequency fH.
(d) If, in a different situation, the amplifier is fed symmetrically with a signal source of 40 k resistance (i.e., 20 k
in series with each gate terminal), use the open-circuit
time-constants method to estimate fH.
10.86 A MOS differential amplifier is biased with a current
source having an output resistance RSS =100 k and an output
capacitance CSS = 1 pF. If the differential gain is found to have
a dominant pole at 20 MHz, what is the 3-dB frequency of the
CMRR?
10.87 The differential gain of a MOS amplifier is 100 V/V
with a dominant pole at 10 MHz. The common-mode gain
is 0.1 V/V at low frequencies and has a transmission zero at
1 MHz. Sketch a Bode plot for the CMRR.
10.88 In a particular MOS differential amplifier design, the
bias current I = 100 μA is provided by a single transistor
operating at VOV = 0.4 V with VA = 40 V and output
capacitance CSS of 100 fF. What is the frequency of the
common-mode gain zero fZ at which Acm begins to rise
above its low-frequency value? To meet a requirement for
reduced power supply, consideration is given to reducing
V
OV to 0.2 V while keeping I unchanged. Assuming the
current-source capacitance to be directly proportional to the
device width, what is the impact on fZ of this proposed
change?
10.89 Repeat Exercise 10.26 for the situation in which the
bias current is reduced to 80 μA and RD is raised to 20 k.
For (d), let Rsig be raised from 20 k to 100 k. (Note: This
is a low-voltage, low-power design.)
10.90 A BJT differential amplifier operating with a 0.5-mA
current source uses transistors for which β = 100, fT = 500
MHz, C
μ = 0.5 pF, and rx = 100 . Each of the collector
resistances is 10 k, and ro is very large. The amplifier is fed
in a symmetrical fashion with a source resistance of 10 k in
series with each of the two input terminals.
(a) Sketch the differential half-circuit and its high-frequency
equivalent circuit.
(b) Determine the low-frequency value of the overall differential gain.
(c) Use the Miller approximation to determine the input
capacitance and hence estimate the 3-dB frequency fH
and the gain–bandwidth product.
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 801
10.91 A differential amplifier is biased by a current source
having an outputresistance of 1Mand an output capacitance
of 1 pF. The differential gain exhibits a dominant pole at
2 MHz. What are the poles of the CMRR?
10.92 A current-mirror-loaded MOS differential amplifier
is biased with a current source I = 0.2 mA. The two NMOS
transistors of the differential pair are operating atVOV = 0.2 V,
and the PMOS devices of the mirror are operating at |VOV| =
0.2 V. The Early voltage VAn = VAp = 10 V. The total
capacitance at the input node of the mirror is 0.1 pF and that
at the output node of the amplifier is 0.2 pF. Find the dc value
and the frequencies of the poles and zero of the differential
voltage gain.
10.93 Consider the current-mirror-loaded CMOS differential amplifier of Fig. 10.37(a) for the case of all transistors
operated at the same VOV and having the same VA . Also let
the total capacitance at the output node CL be four times
the total capacitance at the input node of the current mirror
Cm
. Give expressions for Ad, fP1, fP2, and fZ. Hence show that
fP2/fP1 = 4Ad and ft = gm/2πCL. For VA = 20 V, VOV = 0.2 V,
I = 0.2 mA, CL = 100 fF, and Cm = 25 fF, find the dc value
of A
d, and the value of fP1, ft, fP2, and fZ and sketch a Bode
plot for Ad .
*10.94 For the current mirror in Fig. P10.94, derive an
expression for the current transfer function Io(s)/Ii(s) taking
into account the BJT internal capacitances and neglecting
rx
and r
o. Assume the BJTs to be identical. Observe that a
signal ground appears at the collector of Q2. If the mirror
is biased at 1 mA and the BJTs at this operating point are
characterized by fT = 500 MHz, Cμ = 2 pF, and β0 = 100,
find the frequencies of the pole and zero of the transfer
function.
Figure P10.94
Section 10.8: Other Wideband Amplifier
Configurations
10.95 Consider the case of a discrete-circuit CS amplifier in
which a source-degeneration resistance is utilized to control
the bandwidth. Assume that r
o is very large and CL is
negligibly small. Adapt the formulas given in the text for
this case and thus give the expressions for AM and fH. Let
R
sig = 100 k, gm = 5 mA/V, RL = 5 k, Cgs = 10 pF, and
C
gd = 2 pF. Find |AM|, fH, and the gain–bandwidth product
for these three cases: R
s = 0, 100 , and 200 .
10.96 A CS amplifier is specified to have gm = 5 mA/V,
ro
= 40 k, C
gs = 2 pF, ggd = 0.1 pF, CL = 1 pF,
R
sig = 20 k, and RL = 40 k.
(a) Find the low-frequency gain AM, and use open-circuit
time constants to estimate the 3-dB frequency fH. Hence
determine the gain–bandwidth product.
(b) If a 400- resistance is connected in the source lead,
find the new values of A
M , fH, and the gain–bandwidth
product.
D 10.97 (a) Use the approximate expression in Eq. (10.156)
to determine the gain–bandwidth product of a CS amplifier
with a source-degeneration resistance. Assume Cgd = 0.2 pF
and R
sig = 100 k.
(b) If a low-frequency gain of 20 V/V is required, what fH
corresponds?
(c) For gm = 5 mA/V, A0 = 100 V/V, and RL = 20 k, find
the required value of Rs.
10.98 For the CS amplifier with a source-degeneration
resistance R
s, show for Rsig ≫ Rs, ro ≫ Rs, and RL = ro that
A
M =
−A
0
2 +k
and
τH
≃
C
gsRsig
1+(k/2)
+C
gdRsig1+ A0
2 +k 
+ CL +Cgdro1+k
2 +k 
where k ≡ gmRs
D *10.99 It is required to generate a table of AM ,
fH, and ft versus k ≡ gmRs for a CS amplifier with a
source-degeneration resistance Rs. The table should have
entries for k = 0,1,2,..., 15. The amplifier is specified to
have gm = 5 mA/V, ro = 40 k, RL = 40 k, Rsig = 20 k,
C
gs = 2 pF, Cgd = 0.1 pF, and CL = 1 pF. Use the formulas
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
802 Chapter 10 Frequency Response
for A
M and τH given in the statement for Problem 10.98. If
fH = 2 MHz is required, find the value needed for Rs and the
corresponding value of AM .
*10.100 In this problem we investigate the bandwidth
extension obtained by placing a source follower between the
signal source and the input of the CS amplifier.
(a) First consider the CS amplifier of Fig. P10.100(a). Show
that
A
M = −gmro
τH
= C
gsRsig +CgdRsig 1+gmro +ro +CLro
where C
L is the total capacitance between the output
node and ground. Calculate the value of AM, fH, and the
gain–bandwidth product for the case gm = 1 mA/V,
ro
= 20 k, Rsig = 20 k, Cgs = 20 fF, Cgd = 5 fF, and
CL
= 10 fF.
(b) For the CD−CS amplifier in Fig. P10.100(b), show that
A
M = −
ro
1
1/gm1 +ro1
gm2ro2
τH
= C
gd1Rsig +Cgs1
R
sig +ro1
1+gm1ro1
+C
gs2g1m1 kro1
+C
gd2g1m1 kro1 1+gm2ro2 +ro2
+CLro2
Calculate the values of A
M, fH, and the gain–bandwidth
product for the same parameter values used in (a). Compare
with the results of (a).
*10.101 The transistors in the circuit of Fig. P10.101 have
β0 = 100, VA = 100 V, and Cμ = 0.2 pF. At a bias current
of 100 μA, fT = 200 MHz. (Note that the bias details are not
shown.)
V
sig
(a)
R
sig
I

Vo
V
sig
(b)
R
sig
Q1
 I
Q2
I
Vo
Figure P10.100
R
sig
V
sig
100 A
100 A
Figure P10.101
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
Problems 803
(a) Find Rin and the midband gain.
(b) Find an estimate of the upper 3-dB frequency fH. Which
capacitor dominates? Which one is the second most
significant?
(Hint: Use the formulas in Example 10.13.)
10.102 Consider the circuit of Fig. P10.102 for the case:
I = 200 μA and VOV = 0.2 V, Rsig = 100 k, RD = 50 k,
C
gs = 4 pF, and Cgd = 0.5 pF. Find the dc gain, the
high-frequency poles, and an estimate of fH.
Q1 Q2
R
D
R
sig
V
sig
VDD
Vo
I
12
Figure P10.102
10.103 For the amplifier in Fig. 10.41(a), let I = 1 mA,
β = 120, fT = 500 MHz, and Cμ = 0.5 pF, and neglect rx and
ro
. Assume that a load resistance of 10 k is connected to
the output terminal. If the amplifier is fed with a signal Vsig
having a source resistance Rsig = 12 k, find AM and fH.
10.104 Consider the CD–CG amplifier of Fig. 10.41(c) for
the case gm = 5 mA/V, Cgs = 2 pF, Cgd = 0.1 pF, CL (at the
output node) = 1 pF, and Rsig = RL = 20 k. Neglecting ro,
find A
M and fH. (Hint: Evaluate fH directly from the transfer
function.)
D **10.105 This problem investigates the use of MOSFETs
in the design of wideband amplifiers (Steininger, 1990). Such
amplifiers can be realized by cascading low-gain stages.
(a) Show that for the case Cgd ≪ Cgs and the gain of
the common-source amplifier is low so that the Miller
effect is negligible, the MOSFET can be modeled by the
approximate equivalent circuit shown in Fig. P10.105(a),
where ω
T is the unity-gain frequency of the MOSFET.
(b) Figure P10.105(b) shows an amplifier stage suitable
for the realization of low gain and wide bandwidth.
Transistors Q1 and Q2 have the same channel length L but
different widths W
1 and W2. They are biased at the same
V
GS and have the same fT. Use the MOSFET equivalent
circuit of Fig. P10.105(a) to model this amplifier stage,
assuming that its output is connected to the input of
an identical stage. Show that the voltage gain Vo/Vi is
given by
Vo Vi
= −
G
0
1+
s
ω
T/ G0 +1
where
G
0 =
gm1
gm2
=
W1 W2
(a)
(b)
Figure P10.105
(c) For L = 0.5 μm, W2 = 25 μm, fT = 12 GHz, and
μnCox = 200 μA/V2, design the circuit to obtain a gain
of 3 V/V per stage. Bias the MOSFETs at VOV = 0.3 V.
Specify the required values of W1 and I. What is the 3-dB
frequency achieved?
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
804 Chapter 10 Frequency Response
*10.106 Figure P10.106 shows an amplifier formed by
cascading two CS stages. Note that the input bias voltage
is not shown. Each of Q1 and Q2 is operated at an overdrive
voltage of 0.2 V, and VA = 10 V. The transistor capacitances
are as follows: C
gs = 20 fF, Cgd = 5 fF, and Cdb = 5 fF. The
signal-source resistance Rsig = 10 k.
(a) Find the dc voltage gain.
(b) Use the method of open-circuit time constants to
determine an estimate for the 3-dB frequency fH.
Q2
Q1 0.1 mA
0.1 mA
Vo
V
sig
R
sig
VDD
Figure P10.106
**10.107 Consider the BiCMOS amplifier shown in
Fig. P10.107. The BJT has VBE = 0.7 V, β = 200,
Cμ
= 0.8 pF, and fT = 600 MHz. The NMOS transistor has
Vt
= 1 V, kn′W/L = 2 mA/V2, and Cgs = Cgd = 1 pF.
(a) Consider the dc bias circuit. Neglect the base current of Q2
in determining the current in Q1. Find the dc bias currents
in Q1 and Q2, and show that they are approximately
100 μA and 1 mA, respectively.
(b) Evaluate the small-signal parameters of Q1 and Q2 at their
bias points.
(c) Consider the circuit at midband frequencies. First,
determine the small-signal voltage gain Vo /Vi. (Note that
R
G can be neglected in this process.) Then use Miller’s
theorem on R
G to determine the amplifier input resistance
R
in. Finally, determine the overall voltage gain Vo /Vsig.
Assume r
o of both transistors to be very large.
(d) Consider the circuit at low frequencies. Determine the
frequency of the poles due to C1 and C2, and hence
estimate the lower 3-dB frequency, fL.
(e) Consider the circuit at higher frequencies. Use Miller’s
theorem to replace RG with a resistance at the input.
(The one at the output will be too large to matter.) Use
open-circuit time constants to estimate fH.
***10.108 In each of the six circuits in Fig. P10.108, let
β = 100, Cμ = 2 pF, and fT = 400 MHz, and neglect rx and
ro
. Calculate the midband gain AM and the 3-dB frequency fH.
Rin
C1
V
sig
Vi
5 V
1 F
0.1 F
Vo
1 k
100 k
6.8 k
R
G 10 M C2
Q2
Q1
3 k
Figure P10.107
= Multisim/PSpice; * = difficult problem; ** = more difficult; *** = very challenging; D = design problemCHAPTER 10 PROBLEMS
805
(a)
V
sig
Vo
V
sig
Vo
(b)
V
sig
Vo
(c)
V
sig
Vo
(d)
V
sig
Vo
(e)
V
sig
Vo
(f)
Figure P10.108
"""

THEORY_TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
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
  </style>
</head>
<body>
  <div class=\"wrap\">
    <h1>{title}</h1>
    <div class=\"meta\">Sedra — Chapter 10 • Frequency Response</div>
    <div class=\"problem-box\">{problem_text}</div>
    <div class=\"note\">Solution content can be added here later.</div>
  </div>
</body>
</html>
"""

SIM_TEMPLATE = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
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
  <div class=\"wrap\">
    <h1>{title} — Simulation</h1>
    <div class=\"meta\">Sedra — Chapter 10 • Placeholder simulation page</div>
    <div class=\"placeholder\">Add your simulation, visualization, or interactive model here.</div>
  </div>
</body>
</html>
"""

CARD_TEMPLATE = """<article class=\"card\" data-tags=\"circuits-electronics sedra chapter-10 frequency-response\">
  <h3>Sedra — Chapter 10</h3>
  <p>Problem {num}: {title}</p>
  <div class=\"btn-row\">
    <a href=\"./Sedra/Sedra_ch10_prob_{num}.html\">OPEN THEORY</a>
    <a href=\"./Sedra/Sedra_ch10_prob_{num}_sim.html\">OPEN SIM</a>
  </div>
</article>"""

def parse_problems(raw: str):
    pattern = re.compile(r'(?m)^(?:[D*= ]+)?(10\.\d+)\s')
    matches = list(pattern.finditer(raw))
    problems = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        block = raw[start:end].strip()
        first_line = block.splitlines()[0]
        first_line = re.sub(r'^(?:[D*= ]+)?10\.\d+\s*', '', first_line).strip()
        title = first_line if first_line else f"Problem {num}"
        title = re.sub(r'\s+', ' ', title)
        if len(title) > 95:
            title = title[:92].rstrip() + "..."
        problems.append({"num": num, "title": title, "text": block})
    return problems

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def build():
    problems = parse_problems(RAW_TEXT)
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    cards = []
    for item in problems:
        num = item["num"]
        title = f"Sedra Chapter 10 — Problem {num}"
        problem_text = html.escape(item["text"])
        theory_html = THEORY_TEMPLATE.replace("{title}", title).replace("{problem_text}", problem_text)
        sim_html = SIM_TEMPLATE.replace("{title}", title)
        theory_name = f"Sedra_ch10_prob_{num}.html"
        sim_name = f"Sedra_ch10_prob_{num}_sim.html"
        write_text(TARGET_DIR / theory_name, theory_html)
        write_text(TARGET_DIR / sim_name, sim_html)
        cards.append(CARD_TEMPLATE.replace("{num}", num).replace("{title}", html.escape(item["title"])))
    cards_html = "\n".join(cards)
    write_text(TARGET_DIR / "Sedra_ch10_cards.html", cards_html)
    print(f"Created {len(problems)} theory files, {len(problems)} sim files, and Sedra_ch10_cards.html in {TARGET_DIR}")

if __name__ == "__main__":
    build()
