from pathlib import Path
import os, re, html

DEFAULT_TARGET = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
TARGET_DIR = Path(os.environ.get("SEDRA_TARGET_DIR", DEFAULT_TARGET))

RAW_TEXT = r"""***PROBLEMS
Computer Simulation Problems
Problems identified by the Multisim/PSpice icon are
intended to demonstrate the value of using SPICE simulation
to verify hand analysis and design, and to investigate
important issues such as allowable signal swing and amplifier
nonlinear distortion. Instructions to assist in setting up PSpice
and Multisim simulations for all the indicated problems can
be found in the corresponding files on the website. Note that
if a particular parameter value is not specified in the problem
statement, you are to make a reasonable assumption.
Section 12.2: Class A Output Stage
12.1 A class A emitter follower, biased using the circuit
shown in Fig. 12.2, uses VCC =10 V, R = RL =1 kΩ, with
all transistors (including Q3) identical. Assume VBE =0.7 V,
VCE sat =0.3 V, and β to be very large. For linear operation,
what are the upper and lower limits of output voltage, and
the corresponding inputs? How do these values change if the
emitter–base junction area of Q3 is made twice as big as that
of Q2? Half as big?
12.2 A source-follower circuit using NMOS transistors is
constructed following the pattern shown in Fig. 12.2. All three
transistors used are identical, with Vt =0.5 V and μnCoxW/L =
20 mA/V2; VCC =2.5 V, R = RL =1 kΩ. For linear operation,
what are the upper and lower limits of the output voltage, and
the corresponding inputs?
D 12.3 Using the follower configuration shown in Fig. 12.2
with ± 5-V supplies, provide a design capable of ±3-V
outputs with a 1-kΩ load, using the smallest possible total
supply current. You are provided with four identical, high-β
BJTs and a resistor of your choice. Select a standard resistor
value of 5% tolerance, and specify the maximum power drawn
from the negative supply.
D 12.4 An emitter follower using the circuit of Fig. 12.2,
for which the output voltage range is ±5 V, is required using
VCC =10 V. The circuit is to be designed such that the current
variation in the emitter-follower transistor is no greater than
a factor of 15, for load resistances as low as 100 Ω. What is
the value of R required? Find the incremental voltage gain of
the resulting follower at vO =+5, 0, and –5 V, with a 100-Ω
load. What is the percentage change in gain over this range
of vO?
*12.5 Consider the operation of the follower circuit of
Fig. 12.2 for which RL =VCC/I, when driven by a square wave
such that the output ranges from +VCC to −VCC (ignoring
VCE sat). For this situation, sketch the equivalent of Fig. 12.4
for vO, iC1, and pD1. Repeat for a square-wave output that has
peak levels of ±VCC/2. What is the average power dissipation
in Q1 in each case? Compare these results to those for sine
waves of peak amplitude VCC and VCC/2, respectively.
12.6 Consider the situation described in Problem 12.5. For
square-wave outputs having ±VCC levels and ± 1/2 VCC levels,
and for sine waves of the same peak-to-peak values, find the
average power loss in the current-source transistor Q2.
12.7 Reconsider the situation described in Exercise 12.3
for variation in VCC—specifically for VCC =16 V, 12 V,
10 V, and 8 V. Assume VCE sat is nearly zero. What is the
power-conversion efficiency in each case?
D 12.8 The emitter-follower output stage of Fig. 12.2 is
designed to provide a maximum output swing of ±V̂ volts,
across the load RL. Neglecting the saturation voltage, what
are the minimum required values of VCC and I? Now, if the
output voltage is a sine wave of peak amplitude (V̂ /2), what
is the power-conversion efficiency realized?
Section 12.3: Class B Output Stage
12.9 Consider the circuit of a complementary-BJT class B
output stage. For what amplitude of input signal does the
crossover distortion represent a 10% loss in peak amplitude?
12.10 Consider the feedback configuration with a class B
output stage shown in Fig. 12.9. Let the amplifier gain A0 =
100 V/V. Derive an expression for vO versus vI, assuming that
VBE = 0.7 V. Sketch the transfer characteristic vO versus vI,
and compare it with that without feedback.
12.11 Consider the class B output stage, using
MOSFETs, shown in Fig. P12.11. Let the devices have Vt =
0.5 V and μCoxW/L = 2 mA/V2. With a 10-kHz sine-wave
input of 5-V peak and a high value of load resistance, what
peak output would you expect? What fraction of the sine-wave
period does the crossover interval represent? For what value
of load resistor is the peak output voltage reduced to half the
input?
25 V
15 V
Figure P12.11
12.12 Consider the complementary-BJT class B output
stage and neglect the effects of finite VBE and VCE sat. For
±10-V power supplies and an 8-Ω load resistance, what
is the maximum sine-wave output power available? What
supply power corresponds? What is the power-conversion
efficiency? For output signals of half this amplitude, find the
output power, the supply power, and the power-conversion
efficiency.
D 12.13 A class B output stage operates from ±10-V
supplies. Assuming relatively ideal transistors, what is the
output voltage for maximum power-conversion efficiency?
What is the output voltage for maximum device dissipation?
If each of the output devices is individually rated for 2-W
dissipation, and a factor-of-2 safety margin is to be used, what
is the smallest value of load resistance that can be tolerated,
if operation is always at full output voltage? If operation is
allowed at half the full output voltage, what is the smallest
load permitted? What is the greatest possible output power
available in each case?
D 12.14 A class B output stage is required to deliver an
average power of 50 W into an 8-Ω load. The power supply
should be 4 V greater than the corresponding peak sine-wave
output voltage. Determine the power-supply voltage required
(to the nearest volt in the appropriate direction), the peak
current from each supply, the total supply power, and the
power-conversion efficiency. Also, determine the maximum
possible power dissipation in each transistor for a sine-wave
input.
12.15 Consider the class B BJT output stage with a
square-wave output voltage of amplitude V̂o across a load
RL and employing power supplies ±VSS. Neglecting the
effects of finite VBE and VCE sat, determine the load power, the
supply power, the power-conversion efficiency, the maximum
attainable power-conversion efficiency and the corresponding
value of V̂o, and the maximum available load power. Also
find the value of V̂o at which the power dissipation in the
transistors reaches its peak, and the corresponding value of
power-conversion efficiency.
12.16 Sketch a graph for the small-signal voltage gain of the
class B circuit of Fig. 12.5 as a function of vI, for vI both
positive and negative.
Section 12.4: Class AB Output Stage
12.17 A class AB output stage, such as that in Fig. 12.11,
utilizing transistors with IS = 10−14A, is biased at a quiescent
current IQ = 1 mA. Find VBB, the output resistance Rout at
vI = 0, and the corresponding small-signal voltage gain. The
load resistance RL = 100 Ω. What does the incremental gain
become when vO = 10 V?
D 12.18 Design the quiescent current of a class AB BJT
output stage so that the incremental voltage gain for vI in
the vicinity of the origin is in excess of 0.97 V/V for loads
larger than 100 Ω. Assume that the BJTs have VBE of 0.7 V at
a current of 100 mA and determine the value of VBB required.
D 12.19 A class AB output stage, such as that in Fig. 12.11,
drives a load resistance RL of 100 Ω. What bias current IQ will
serve to limit the variation in the small-signal voltage gain to
5% as iL changes from 0 to 50 mA?
12.20 For the class AB output stage considered in Example 12.3, add two columns to the table of results as follows: the
total input current drawn from vI (iI, mA); and the large-signal
input resistance Rin ≡ vI/iI. Assume βN =βP =β =49. Compare the values of Rin to the approximate value obtained using
the resistance-reflection rule, Rin ≃ βRL.
12.21 In this problem we investigate an important trade-off
in the design of the class AB output stage of Fig. 12.11:
Increasing the quiescent current IQ reduces the nonlinearity
of the transfer characteristic at the expense of increased
quiescent power dissipation. As a measure of nonlinearity,
we use the maximum deviation of the stage incremental gain,
which occurs at vO = 0, namely,
e = 1−(vo/vi)|vO=0
(a) Show that e is given by
e = (VT/2IQ)/(RL +VT/2IQ)
which for 2IQRL ≫ VT can be approximated by
e ≃ VT/(2IQRL)
(b) If the stage is operated from power supplies of ±VCC, find
the quiescent power dissipation, PD.
(c) Show that for given VCC and RL, the product of the
quiescent power dissipation and the gain error is a
constant given by
ePD ≃ VT(VCC/RL)
(d) For VCC = 10 V and RL = 100 Ω, find the required values
of PD and IQ if e is to be 5%, 2%, and 1%.
*12.22 A class AB output stage, resembling that in
Fig. 12.11 but utilizing a single supply of +10 V and biased
at VI = 6 V, is capacitively coupled to a 100-Ω load. For
transistors for which VBE = 0.7 V at 1 mA and for a bias
voltage VBB =1.4 V, what quiescent current results? For a
step change in output from 0 to –1 V, what input step is
required? Assuming transistor-saturation voltages of zero,
find the largest possible positive-going and negative-going
steps at the output.
Section 12.5: Biasing the Class AB Circuit
D 12.23 Consider the diode-biased class AB circuit of
Fig. 12.14. For IBIAS =200 μA, find the relative size (n) that
should be used for the output devices (in comparison to the
biasing devices) to ensure that an output resistance of 8 Ω or
less is obtained in the quiescent state. Neglect the resistance
of the biasing diodes.
D*12.24 A class AB output stage using a two-diode bias
network as shown in Fig. 12.14 utilizes diodes having the
same junction area as the output transistors. For VCC =10 V,
IBIAS = 1 mA, RL =100 Ω, βN =50, and VCEsat = 0 V, what is
the quiescent current? What are the largest possible positive
and negative output signal levels? To achieve a positive peak
output level equal to the negative peak level, what value of βN
is needed if IBIAS is not changed? What value of IBIAS is needed
if βN is held at 50? For this value, what does IQ become?
D 12.25 It is required to evaluate the small-signal input
resistance and small-signal voltage gain of the class AB
output stage in Fig. 12.14. To simplify matters, assume the
small-signal resistances of D1 and D2 to be negligibly small.
Replace each of QN and QP with its hybrid-π model and
neglect ro. Hence show that the class AB stage is equivalent,
from a small-signal point of view, to an emitter-follower
transistor whose rπ = rπN || rπP and gm = gmN +gmP, and hence
re = reN || reP and β = (gmN +gmP)(rπN || rπP). Now show that
vo/vi = RL / [RL +(reN || reP)]
and
Rin ≃ β[RL +(reN || reP)]
12.26 Figure P12.26 shows a class AB output stage with a
common-emitter transistor added to increase the voltage gain
and reduce the current that vI has to supply. Neglecting the
small-signal resistances of D1 and D2, find the small-signal
voltage gain vo/vi. (Hint: Use the expressions for voltage gain
and input resistance of the class AB stage without Q3, given
in the statement for Problem 12.25.)
QN
QP
Q3
D2
D1
vI
vO
IBIAS
+VCC
−VCC
RL
Figure P12.26
12.27 It is required to find an expression for the output
resistance Rout of the class AB output stage in Fig. P12.26.
Toward that end, neglect the small-signal resistance of each of
D1 and D2 and assume the current source supplying IBIAS has an
output resistance RBIAS. Transistors QN and QP are equivalent
to a single transistor with rπ = rπN || rπP, re = reN || reP, and
gm = gmN +gmP.
**12.28 A class AB output stage using a two-diode bias
network as shown in Fig. 12.14 utilizes diodes having the
same junction area as the output transistors. At a room
temperature of about 20°C the quiescent current is 1 mA and
VBE = 0.6 V. Through a manufacturing error, the thermal
coupling between the output transistors and the biasing
diode-connected transistors is omitted. After some output
activity, the output devices heat up to 70°C while the
biasing devices remain at 20°C. Thus, while the VBE of
each device remains unchanged, the quiescent current in the
output devices increases. To calculate the new current value,
recall that there are two effects: IS increases by about 14%/°C
and VT =kT/q changes, where T = 273° + temperature in
°C, and VT =25 mV only at 20°C. However, you may assume
that βN remains almost constant. This assumption is based on
the fact that β increases with temperature but decreases with
current. What is the new value of IQ? If the power supply
is ±20 V, what additional power is dissipated? If thermal
runaway occurs, and the temperature of the output transistors
increases by 10°C for every watt of additional power
dissipation, what additional temperature rise and current
increase result?
D 12.29 Repeat Example 12.5 for the situation in which the
peak positive output current is 250 mA. Use the same general
approach to safety margins. What are the values of R1 and R2
you have chosen?
**12.30 A VBE multiplier is designed with equal resistances
for nominal operation at a terminal current of 1 mA, with half
the current flowing in the bias network. The initial design is
based on β = ∞ and VBE =0.7 V at 1 mA.
(a) Find the required resistor values and the terminal voltage.
(b) Find the terminal voltage that results when the terminal
current increases to 2 mA. Assume β = ∞.
(c) Repeat (b) for the case the terminal current becomes
10 mA.
(d) Repeat (c) using the more realistic value of β = 100.
*12.31 By replacing the transistor in the VBE multiplier by its
hybrid-π, small-signal model (with ro neglected), show that
the incremental resistance between the two terminals of the
multiplier is given by
r = [R2 +(R1||rπ)] / [1+gm(R1||rπ)]
Evaluate r for the case R1 = R2 = 1.2 kΩ, with the transistor
operating at IC = 1 mA and having β = 100.
Section 12.6: Variations on the Class AB
Configuration
12.32 Use the results given in the answer to Exercise 12.9
to determine the input current of the circuit in Fig. 12.17 for
vI =0 and ±10 V with infinite and 100-Ω loads.
12.33 For the circuit in Fig 12.17, operated near vI = 0 and
fed with a signal source having zero resistance, show that the
output resistance is given by
Rout = 1/2 [R3 +re3 +(R1||re1)/(β3 +1)]
Assume that the top and bottom halves of the circuit are
perfectly matched.
D ***12.34 Consider the circuit of Fig. 12.17 in which Q1
and Q2 are matched, and Q3 and Q4 are matched but have
three times the junction area of the others. Resistors R3 and
R4 also are matched. For VCC =10 V, find values for resistors
R1 through R4 that allow for a base current of at least 10 mA
in Q3 (and Q4) at vI =+5 V (vI = −5 V), when a load
demands it, with at most a 2-to-1 variation in currents in
Q1 (and Q2). The quiescent current in Q3 is to be 40 mA.
Let β1,2 ≥ 150 and β3,4 ≥ 50. For input voltages around
0 V, estimate the output resistance of the overall follower
driven by a source having zero resistance. For an input
voltage of +1 V and a load resistance of 2 Ω, what output
voltage results? Q1 and Q2 have VBE of 0.7 V at a current
of 10 mA.
12.35 Figure P12.35 shows a variant on the class AB circuit
of Fig. 12.17. Assume that all four transistors are matched and
have β = 100.
(a) For vI = 0, find the quiescent current in Q3 and Q4, the
input current iI, and the output voltage vO.
(b) Since the circuit has perfect symmetry, the small-signal
performance around vI =0 can be determined by considering either the top or bottom half of the circuit only.
In this case, the load on the half-circuit must be 2RL, the
input resistance found is 2Rin, and the output resistance
found is 2Rout. Using this approach, find Rin, vo/vi, and
Rout (assuming that the circuit is fed with a zero-resistance
source).
Q3
vI vO
iI −VCC
1 mA
Q4
Q1
+VCC
+VCC
−VCC
1 mA
Q2 RL = 200 Ω
Figure P12.35
12.36 For the Darlington configuration shown in Fig. 12.18,
show that for β1 ≫ 1 and β2 ≫ 1:
(a) The equivalent composite transistor has β ≃ β1β2.
(b) If the composite transistor is operated at a current IC, then
Q2 will be operating at a collector current approximately
equal to IC, and Q1 will be operating at a collector current
approximately equal to IC/β2.
(c) The composite transistor has a base–emitter voltage
VBE ≃ 2VT ln(IC/IS) − VT lnβ2, where IS is the saturation
current of each of Q1 and Q2.
(d) The composite transistor has an equivalent rπ ≃
2β1β2(VT/IC).
(e) The composite transistor has an equivalent gm ≃
1/2 (IC/VT).
*12.37 For the circuit in Fig. P12.37 in which the transistors
have VBE = 0.7 V and β = 100:
(a) Find the dc collector current for each of Q1 and Q2.
(b) Find the small-signal current ic that results from an input
signal vi, and hence find the voltage gain vo/vi.
(c) Find the input resistance Rin.
Q2
vo
2 MΩ
2 kΩ
Q1
Rin
+15 V
vi ic
Figure P12.37
**12.38 The BJTs in the circuit of Fig. P12.38 have
βP =10, βN =100, VBE = 0.7 V, and VA = 100 V.
(a) Find the dc collector current of each transistor and the
value of VC.
(b) Replacing each BJT with its hybrid-π model, show that
vo/vi ≃ gm1[ro1 || βN(ro2 || Rf)]
(c) Find the values of vo/vi and Rin.
Figure P12.38
D **12.39 Consider the compound-transistor class AB output stage shown in Fig. 12.20 in which Q2 and Q4 are matched
transistors with VBE = 0.7 V at 10 mA and β = 100, Q1 and Q5
have VBE =0.7 V at 1-mA currents and β = 100, and Q3 has
VEB = 0.7 V at a 1-mA current and β = 10. Design the circuit
for a quiescent current of 2 mA in Q2 and Q4, IBIAS that is 100
times the standby base current in Q1, and a current in Q5 that
is nine times that in the associated resistors. Find the values
of the input voltage required to produce outputs of ±10 V for
a 1-kΩ load. Use VCC of 15 V.
*12.40 Figure P12.40 shows a variant on the class AB
amplifier known as class G. Here, in addition to the
Q2
Q1
Q5
Q4
Q3
D1
D2
Z1
R1
R2
Z2
vO
vI
IBIAS
IBIAS
VCC2
VCC1
−VCC1
−VCC2
RL
Figure P12.40
normal power supply ±VCC1, the circuit is equipped with a
higher voltage supply ±VCC2. The latter supply is utilized only
infrequently. The circuit operates as follows. Normally, D1
and D2 are turned on and thus connect the ±VCC1 supply to the
class AB stage transistors Q1 and Q2. Simultaneously, Q3 and
Q4 are off. For vI positive and exceeding a certain threshold,
Q3 turns on, D1 turns off, and Q1 is then effectively operating
from the higher voltage supply VCC2. This continues as long as
vI is larger than the specified threshold. As vI decreases below
the threshold value, Q3 is turned off and D1 turns on, thus
connecting Q1 to its normal supply VCC1. A similar process
happens in the negative direction, with D2 and Q4 taking the
place of D1 and Q3. Let VCC1 =35 V,VCC2 =70 V,VZ1 =3.3 V,
and the voltage of the VBE multiplier VBB = 1.2 V.
(a) Find the positive threshold value of vI at which Q3 is
turned on.
(b) If for 95% of the time vI is in the vicinity of 30 V and
only 5% of the time it is in the vicinity of 65 V, use Eq.
(12.19) to estimate the average power dissipated in the
transistors, PD. Compare to the value of PD dissipated in
a class AB stage operated from a ±70 V supply.
12.41 Repeat Exercise 12.11 for a design variation in which
transistor Q5 is increased in size by a factor of 20, all other
conditions remaining the same.
12.42 Repeat Exercise 12.11 for a design in which the
limiting output current and normal peak current are 100 mA
and 75 mA, respectively.
D 12.43 The circuit shown in Fig. P12.43 operates in a
manner analogous to that in Fig. 12.21 to limit the output
IBIAS
Figure P12.43
current from Q3 in the event of a short circuit or other mishap.
It has the advantage that the current-sensing resistor R does
not appear directly at the output. Find the value of R that
causes Q5 to turn on and absorb all of IBIAS =2 mA, when the
current being sourced reaches 100 mA. For Q5, IS = 10−14 A.
If the normal peak output current is 75 mA, find the voltage
drop across R and the collector current in Q5.
D 12.44 Consider the thermal shutdown circuit shown in
Fig. 12.22. At 25°C, Z1 is a 6.8-V zener diode with a TC of
−2 mV/°C, and Q1 and Q2 are BJTs that display VBE of 0.7 V at
a current of 100 μA and have a TC of –2 mV/°C. Design the
circuit so that at 125°C, a current of 200 μA flows in each of
Q1 and Q2. What is the current in Q2 at 25°C?
Section 12.7: CMOS Class AB Output Stages
D 12.45 (a) Show that for the class AB circuit in Fig. 12.23,
the small-signal output resistance in the quiescent state is
given by
Rout ≃ 1/(gmn +gmp)
which for matched devices becomes
Rout = 1/(2gm)
(b) For a circuit that utilizes MOSFETs with Vt = 0.5 V and
k′(W/L) = 200 mA/V2, find the voltage VGG that results in
Rout = 20 Ω. Also, find IQ.
D 12.46 (a) For the circuit in Fig. 12.23 in which Q1 and Q2
are matched, QN and QP are matched, and all devices have
the same |Vt|, show that the small-signal voltage gain at the
quiescent condition is given by
vo/vi = RL / [RL +2/gm]
where gm is the transconductance of each of QN and QP and
where channel-length modulation is neglected.
(b) For the case IBIAS = 0.2 mA, RL = 1 kΩ, kn = kp = nk1 =
nk2, where k = μCox(W/L), and k1 = 20 mA/V2, find the ratio
n that results in an incremental gain of 0.98. Also find the
quiescent current IQ.
D 12.47 Design the circuit of Fig. 12.23 to operate at IQ
= 1 mA with IBIAS = 0.1 mA. Let μnCox = 250 μA/V2,
μpCox = 100 μA/V2, Vtn = −Vtp =0.45 V, and VDD = VSS =
2.5 V. Design so that Q1 and Q2 are matched and QN and QP
are matched, and that in the quiescent state each operates at
an overdrive voltage of 0.15 V.
(a) Specify the W/L ratio for each of the four transistors.
(b) In the quiescent state with vO = 0, what must vI be?
(c) If QN is required to supply a maximum load current
of 10 mA, find the maximum allowable output voltage.
Assume that the transistor supplying IBIAS needs a
minimum of 0.2 V to operate properly.
D 12.48 Consider the design of the class AB output stage of
Fig. 12.23 for the following conditions. The stage is operated
from ±2.5-V power supplies and is required to provide a
minimum output voltage swing of ±1.5 V while supplying
a maximum current equal to 10 times the quiescent current
IQ. Assume that QN and QP are matched and Q1 and Q2
are matched, that all devices have |Vt| = 0.5 V, and that in
the quiescent state all transistors are operated at the same
overdrive voltage. What is the value of VOV required, and
what VGG is needed?
12.49 The class AB output stage in Fig. 12.24 utilizes two
matched transistors with kn =kp =200 mA/V2 and is operated
from ±2.5-V power supplies. If the stage is required to supply
a maximum current of ±20 mA, what is the output voltage
swing realized?
12.50 For the CMOS output stage of Fig. 12.25 with IQ =
2 mA, VOV = 0.2 V for each of QP and QN at the quiescent
point, and μ = 5, find the output resistance at the quiescent
point.
12.51 (a) Show that for the CMOS output stage of Fig. 12.25,
|Gain error| = Rout/RL
(b) For a stage that drives a load resistance of 100 Ω with a
gain error of less than 3%, find the overdrive voltage at which
QP and QN should be operated. Let IQ = 2.5 mA and μ = 5.
12.52 Show that in the CMOS class AB common-source
output stage (Fig. 12.25), QN turns off when vO = 4I QRL and
QP turns off when vO = −4I QRL. This is equivalent to saying
that one of the transistors turns off when iL reaches 4IQ.
D *12.53 It is required to design the circuit of Fig. 12.25
to drive a load resistance of 50 Ω while exhibiting an
output resistance, around the quiescent point, of 2.5 Ω.
Operate QN and QP at IQ =1.5mA and VOV =0.15 V. The
technology utilized is specified to have kn′ =250 μA/V2,
kp′ =100 μA/V2, Vtn =−Vtp =0.5 V, and VDD =VSS =2.5 V.
(a) Specify (W/L) for each of QN and QP.
(b) Specify the required value of μ.
(c) What is the expected error in the stage gain?
(d) In the quiescent state, what dc voltage must appear at the
output of each of the error amplifiers?
(e) At what value of positive vO will QP be supplying all the
load current? Repeat for negative vO and QN supplying
all the load current.
(f) What is the linear range of vO?
*12.54 Figure P12.54 shows a class AB output stage utilizing a pair of complementary MOSFETs (QN, QP) and
employing BJTs for biasing and in the driver stage. The
latter consists of complementary Darlington emitter followers
formed by Q1 through Q4 and has the low output resistance
necessary for driving the output MOSFETs at high speeds.
Of special interest is the bias circuit utilizing two VBE
multipliers formed by Q5 and Q6 and their associated resistors.
Transistor Q6 is placed in direct thermal contact with the
output transistors and thus has the same temperature as that
of QN and QP.
(a) Show that VGG is given by
VGG = (1+R3/R4)VBE6 +(1+R1/R2)VBE5 −4VBE
(b) Noting that VBE6 is thermally coupled to the output devices
while the other BJTs remain at constant temperature,
show that
∂VGG/∂T = (1+R3/R4) ∂VBE6/∂T
(c) To keep the overdrive voltages of QN and QP, and
hence their quiescent current, constant with temperature
variation, ∂VGG/∂T is made equal to ∂(VtN + VtP)/∂T.
Find R3/R4 that provides this temperature stabilization when |Vt| changes by −3 mV/°C and ∂VBE/∂T =
−2 mV/°C.
(d) Using the value of R3/R4 found in (c) and assuming that
the nominal value of VBE is 0.7 V and that the MOSFETs
have |Vt| = 3 V and μCox(W/L) = 2 A/V2, find |VGS|,
VGG, R, and R1/R2 to establish a quiescent current of
100 mA in the output transistors and 20 mA in the driver
stage.
Section 12.8: IC Power Amplifiers
D 12.55 In the power-amplifier circuit of Fig. 12.29, two
resistors are important in controlling the overall voltage gain.
Which are they? Which controls the gain alone? Which affects
both the dc output level and the gain? A new design is being
considered in which the output dc level is approximately 2/3 VS
(rather than approximately 1/2 VS) with a gain of 50 (as before).
What changes are needed?
12.56 Consider the front end of the circuit in Fig. 12.29.
For VS =−22 V, calculate approximate values for the bias
currents in Q1 through Q6. Assume βnpn =100, βpnp =20, and
VBE = 0.7 V. Also find the dc voltage at the output.
D 12.57 It is required to use the LM380 power amplifier
to drive an 8-Ω loudspeaker while limiting the maximum
possible device dissipation to 2 W. Use the graph of Fig. 12.31
to determine the maximum possible power-supply voltage
that can be used. (Use only the given graphs; do not
interpolate.) If the maximum allowed THD is to be 3%, what
is the maximum possible load power? To deliver this power
to the load what peak-to-peak output sinusoidal voltage is
required?
12.58 For the circuit in Fig. P12.58, assuming all transistors
to have large β, show that iO = vI/R. [This voltage-to-current
converter is an application of a versatile circuit building
block known as the current conveyor; see Sedra and Roberts
(1990).] For β = 100, by what approximate percentage is iO
actually lower than this ideal value?
Figure P12.58
D 12.59 For the bridge amplifier of Fig. 12.32, let R1 =
R3 = 10 kΩ. Find R2 and R4 to obtain an overall gain of 8 V/V.
D 12.60 An alternative bridge amplifier configuration, with
high input resistance, is shown in Fig. P12.60. [Note the
similarity of this circuit to the front end of the instrumentation
amplifier circuit shown in Fig. 2.20(b).] What is the gain
vo/vi? For op amps (using ±15-V supplies) that limit at
±13 V, what is the largest sine wave you can provide across
RL? Using 1 kΩ as the smallest resistor, find resistor values
that make vo/vi = 8 V/V. Make sure that the signals at the
outputs of the two amplifiers are complementary.
Figure P12.60
Section 12.9 Class D Power Amplifiers
12.61 Sketch diagrams resembling those in Figs. 12.33(a),
(b). Let vT have ±10 V peaks and assume vA is a sine
wave with 5-V peak amplitude. Let the frequency of vT
be 5 times that of vA. The comparator output levels are
±10 V.
12.62 A pulse waveform swinging between ±10 V has
a duty ratio of 0.65. What is its average value? If the
duty ratio is changed to 0.35, what does the average value
become?
12.63 For the circuit in Fig. 12.34(b):
(a) If vA is a sine wave, what is the maximum power supplied
to a load of resistance R, in terms of VDD?
(b) The power loss is mostly due to the repeated charging
and discharging of a capacitance C across the load. It can
be shown that this switching power is given by 4fsCVDD^2.
Find an expression for the power-conversion efficiency
η and evaluate the value of η for the case fs = 250 kHz
and C = 1000 pF.
Section 12.10 Power Transistors
12.64 A power MOSFET is specified to have IDmax = 5 A,
VDSmax = 50 V, and PDmax = 50 W.
(a) Sketch the SOA boundaries.
(b) If the MOSFET is used in the common-source configuration as shown in Fig. P12.64, show that the maximum
current occurs when VDS = 0, the maximum VDS occurs
when ID = 0, and the maximum power dissipation occurs
when VDS = VDD/2.
(c) For VDD = 40 V, find the smallest resistance R for which
the operating point is always within the SOA. What are
the corresponding values of IDmax and PDmax?
(d) Repeat (c) for VDD = 30 V.
(e) Repeat (c) for VDD = 15 V.
R
VDD
VGS
ID
Figure P12.64
D 12.65 A particular transistor having a thermal resistance
θJA = 2.5°C/W is operating at an ambient temperature of
30°C with a collector–emitter voltage of 20 V. If long life
requires a maximum junction temperature of 130°C, what is
the corresponding device power rating? What is the greatest
average collector current that should be considered?
12.66 A particular transistor has a power rating at 25°C
of 10 W, and a maximum junction temperature of 150°C.
What is its thermal resistance? What is its power rating
when operated at an ambient temperature of 50°C? What is
its junction temperature when dissipating 5 W at an ambient
temperature of 50°C?
12.67 A power transistor operating at an ambient temperature of 50°C, and an average emitter current of 3 A, dissipates
20 W. If the thermal resistance of the transistor is known to
be less than 3°C/W, what is the highest junction temperature
you would expect? If the transistor VBE measured using a
pulsed emitter current of 3 A at a junction temperature of
25°C is 0.80 V, what average VBE would you expect under
normal operating conditions? (Use a temperature coefficient
of –2 mV/°C.)
12.68 For a particular application of the transistor specified
in Example 12.7, extreme reliability is essential. To improve
reliability, the maximum junction temperature is to be limited
to 100°C. What are the consequences of this decision for the
conditions specified?
12.69 A power transistor is specified to have a maximum
junction temperature of 150°C. When the device is operated
at this junction temperature with a heat sink, the case
temperature is found to be 97°C. The case is attached
to the heat sink with a bond having a thermal resistance
θCS =0.5°C/W and the thermal resistance of the heat sink
θSA =0.1°C/W. If the ambient temperature is 25°C, what is
the power being dissipated in the device? What is the thermal
resistance of the device, θJC, from junction to case?
12.70 A power transistor for which TJmax =180°C can
dissipate 50 W at a case temperature of 30°C. If it is connected
to a heat sink using an insulating washer for which the
thermal resistance is 0.6°C/W, what heat-sink temperature
is necessary to ensure safe operation at 30 W? For an ambient
temperature of 27°C, what heat-sink thermal resistance is
required? If, for a particular extruded-aluminum-finned heat
sink, the thermal resistance in still air is 6°C/W per centimeter
of length, how long a heat sink is needed?"""

THEORY_TEMPLATE = r"""<!DOCTYPE html>
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
    <div class=\"meta\">Sedra — Chapter 11 • Frequency Response</div>
    <div class=\"problem-box\">{problem_text}</div>
    <div class=\"note\">Solution content can be added here later.</div>
  </div>
</body>
</html>
"""

SIM_TEMPLATE = r"""<!DOCTYPE html>
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
    <div class=\"meta\">Sedra — Chapter 11 • Placeholder simulation page</div>
    <div class=\"placeholder\">Add your simulation, visualization, or interactive model here.</div>
  </div>
</body>
</html>
"""

CARD_TEMPLATE = """<article class="card" data-tags="circuits-electronics sedra chapter-12 output-stages-power-amplifiers">
  <h3>Sedra — Chapter 12</h3>
  <p>Problem {num}: {title}</p>
  <div class="btn-row">
    <a href="./Sedra/Sedra_ch12_prob_{num}.html">OPEN THEORY</a>
    <a href="./Sedra/Sedra_ch12_prob_{num}_sim.html">OPEN SIM</a>
  </div>
</article>"""

def parse_problems(raw: str):
    pattern = re.compile(r'(?m)^(?:[D*= ]+)?(12\.\d+)\s')
    matches = list(pattern.finditer(raw))
    problems = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        block = raw[start:end].strip()
        first_line = block.splitlines()[0]
        first_line = re.sub(r'^(?:[D*= ]+)?12\.\d+\s*', '', first_line).strip()
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
        title = f"Sedra Chapter 12 — Problem {num}"
        problem_text = html.escape(item["text"])
        theory_html = THEORY_TEMPLATE.replace("{title}", title).replace("{problem_text}", problem_text)
        sim_html = SIM_TEMPLATE.replace("{title}", title)
        theory_name = f"Sedra_ch12_prob_{num}.html"
        sim_name = f"Sedra_ch12_prob_{num}_sim.html"
        write_text(TARGET_DIR / theory_name, theory_html)
        write_text(TARGET_DIR / sim_name, sim_html)
        cards.append(CARD_TEMPLATE.replace("{num}", num).replace("{title}", html.escape(item["title"])))
    cards_html = "\n".join(cards)
    write_text(TARGET_DIR / "Sedra_ch12_cards.html", cards_html)
    print(f"Created {len(problems)} theory files, {len(problems)} sim files, and Sedra_ch12_cards.html in {TARGET_DIR}")

if __name__ == "__main__":
    build()
