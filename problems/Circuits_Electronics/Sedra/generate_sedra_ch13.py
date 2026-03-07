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
Section 13.1: The Two-Stage CMOS Op Amp
13.1 A particular design of the two-stage CMOS operational
amplifier of Fig. 13.1 utilizes ±1-V power supplies. All
transistors are operated at overdrive voltages of 0.2-V
magnitude. The process technology provides devices with
Vtn = Vtp = 0.4 V. Find the input common-mode range and
the range allowed for vO.
13.2 The CMOS op amp of Fig. 13.1 is fabricated in a process
for which V′An = 25 V/μm and VAp′ = 20 V/μm. Find A1, A2,
and Av if all devices are 0.3 μm long, Q1 and Q2 are operated
at overdrive voltages of 0.15-V magnitude, and Q6 is operated
at VOV = 0.2 V. Also, determine the op-amp output resistance
obtained when the second stage is biased at 0.3 mA. What
do you expect the output resistance of a unity-gain voltage
amplifier to be, using this op amp?
D 13.3 The CMOS op amp of Fig. 13.1 is fabricated in
a process for which VA′ for all devices is 20 V/μm.
If all transistors have L = 0.3 μm and are operated at
equal overdrive voltages, find the magnitude of the overdrive voltage required to obtain a dc open-loop gain
of 1600 V/V.
13.4 Consider the circuit in Fig. 13.1 with the device geometries shown at the top of this page. Let IREF = 40 μA,
Vt for all devices = 0.45 V, μnCox = 270 μA/V2, μpCox =
70 μA/V2, VA for all devices = 15 V, VDD = VSS = 1 V.
Determine the width of Q6, W, that will ensure that the
op amp will not have a systematic offset voltage. Then,
for all devices, evaluate ID, VOV, VGS, gm, and ro.
Provide your results in a table. Also find A1, A2, the dc
open-loop voltage gain, the input common-mode range, and
the output voltage range. Neglect the effect of VA on the bias
currents.
D 13.5 Design the two-stage CMOS op amp in Fig. 13.1 to
provide a CMRR of about 72 dB. If all the transistors are
operated at equal overdrive voltages of 0.15 V and have equal
channel lengths, find the minimum required channel length.
For this technology, VA′ = 15 V/μm. What is the dc gain
realized?
13.6 A two-stage CMOS op amp has Gm1 = 0.8 mA/V,
Gm2 = 2.4 mA/V, C1 = 0.1 pF, and C2 = 1.2 pF. Find the value
of CC that will provide a unity-gain frequency of 120 MHz.
Also, determine the values of fP2 and fZ.
13.7 For the CMOS amplifier in Fig. 13.1, whose equivalent
circuit is shown in Fig. 13.2, let Gm1 = 1 mA/V, R1 =
100 kΩ, C1 = 0.1 pF, Gm2 = 2 mA/V, R2 = 50 kΩ, and
C2 = 2 pF.
(a) Find the dc gain.
(b) Without CC connected, find the frequencies of the two
poles in radians per second and sketch a Bode plot for the
gain magnitude.
(c) With CC connected, find ωP2. Then find the value of CC
that will result in a unity-gain frequency ωt at least two
octaves below ωP2. For this value of CC, find ωP1 and ωZ
and sketch a Bode plot for the gain magnitude.
13.8 A CMOS op amp with the topology in Fig. 13.1 has
gm1 = gm2 = 1 mA/V, gm6 = 3 mA/V, the total capacitance
between node D2 and ground is 0.2 pF, and the total
capacitance between the output node and ground is 3 pF. Find
the value of CC that results in ft = 50 MHz, and verify that ft
is lower than fZ and fP2.
13.9 A particular design of the two-stage CMOS op amp
of Fig. 13.1 has Gm1 = 1 mA/V and Gm2 = 2 mA/V. The
total capacitance at the output node is 1 pF. While utilizing a
Miller compensation capacitor CC without a series resistance
R, the amplifier is made to have a uniform −20-dB/decade
frequency response with a unity-gain frequency of 100 MHz.
(a) What must the value of CC be?
(b) What do you estimate the frequencies of the poles, fP1 and
fP2, and of the right-half-plane zero, fZ, to be?
(c) What is the phase margin obtained?
(d) To increase the phase margin, a resistance R is connected
in series with CC. What is the value of R that results in
fZ = ∞, and what is the resulting phase margin?
(e) If R is increased further, until it moves the zero into the
left half-plane and thus turns the phase it introduces into
phase lead, what value of R is needed to obtain a phase
margin of 85°?
D 13.10 A particular implementation of the CMOS amplifier of Figs. 13.1 and 13.2 provides Gm1 = 0.3 mA/V,
Gm2 = 0.6 mA/V, ro2 = ro4 = 222 kΩ, ro6 = ro7 = 111 kΩ,
and C2 = 1 pF.
(a) Find the dc gain.
(b) Find the frequency of the second pole, fP2.
(c) Find the value of the resistance R that, when placed in
series with CC, causes the transmission zero to be located
at s = ∞.
(d) With R in place, as in (c), find the value of CC that results
in the highest possible value of ft while providing a phase
margin of 80°. What value of ft is realized? What is the
corresponding frequency of the dominant pole?
(e) To what value should CC be changed to double the
value of ft? At the new value of ft, what is the
phase shift introduced by the second pole? To reduce
this excess phase shift to 10° and thus obtain an
80° phase margin, as before, what value should R be
changed to?
13.11 A two-stage CMOS op amp has each of its first-stage
transistors Q1 and Q2 operating at an overdrive voltage of
0.2 V. The op amp has a uniform −20-dB/decade frequency
response with a unity-gain frequency of 100 MHz. What do
you expect the slew rate of this amplifier to be? If each
of Q1 and Q2 is biased at 50 μA, what must the value
of CC be?
D 13.12 A two-stage CMOS op amp similar to that in
Fig. 13.1 is found to have a capacitance between the output
node and ground of 0.7 pF. If it is desired to have a unity-gain
bandwidth ft of 100 MHz with a phase margin of 72° what
must gm6 be set to? Assume that a resistance R is connected
in series with the frequency-compensation capacitor CC and
adjusted to place the transmission zero at infinity. What
value should R have? If the first stage is operated at
VOV = 0.15 V, what is the value of slew rate obtained? If
the first-stage bias current I = 100 μA, what is the required
value of CC?
D 13.13 A CMOS op amp with the topology shown
in Fig. 13.1 is designed to provide Gm1 = 1 mA/V and
Gm2 = 5 mA.
(a) Find the value of CC that results in ft = 80 MHz.
(b) What is the maximum value that C2 can have while
achieving a 70° phase margin?
D 13.14 A CMOS op amp with the topology shown
in Fig. 13.1 but with a resistance R included in series
with CC is designed to provide Gm1 = 0.8 mA/V and
Gm2 = 2 mA/V.
(a) Find the value of CC that results in ft = 100 MHz.
(b) For R = 500 Ω, what is the maximum allowed value
of C2 for which a phase margin of at least 60° is
obtained?
13.15 A two-stage CMOS op amp resembling that in
Fig. 13.1 is found to have a slew rate of 60 V/μs and a
unity-gain bandwidth ft of 60 MHz.
(a) Estimate the value of the overdrive voltage at which the
input-stage transistors are operating.
(b) If the first-stage bias current I = 120 μA, what value of
CC must be used?
(c) For a process for which μpCox = 60 μA/V2, what W/L
ratio applies for Q1 and Q2?
D 13.16 Sketch the circuit of a two-stage CMOS amplifier having the structure of Fig. 13.1 but utilizing NMOS
transistors in the input stage (i.e., Q1 and Q2).
D 13.17 (a) Show that the PSRR− of a CMOS two-stage op
amp for which all transistors have the same channel length
and are operated at equal VOV is given by
PSRR− = 2(VA/VOV)^2
(b) For VOV = 0.15 V, what is the minimum channel length
required to obtain a PSRR− of 72 dB? For the technology
available, VA′ = 15 V/μm.
D 13.18 It is required to design the circuit of Fig. 13.8 to
provide a bias current IREF of 225 μA with Q8 and Q9 as
matched devices having W/L = 60/0.5. Transistors Q10, Q11,
and Q13 are to be identical and must have the same gm as Q8
and Q9. Transistor Q12 is to be four times as wide as Q13. Let
kn′ = 3kp′ = 180 μA/V2, and Vtn =|Vtp|= 0.5 V; let all channel
lengths be equal; and let VDD = VSS = 1.5 V. Find the required
value of RB. What is the voltage drop across RB? Also specify
the W/L ratios of Q10, Q11, Q12, and Q13 and give the expected
dc voltages at the gates of Q12, Q10, and Q8.
Section 13.2: The Folded-Cascode CMOS
Op Amp
D 13.19 The op-amp circuit of Fig. 13.10 is operated from
±1-V power supplies. If the power dissipated in the circuit is
to be limited to 1 mW, find the maximum value of IB allowed.
If this value is used, and each of Q1 and Q2 is to be biased at
a current four times that used for each of Q3 and Q4, find the
value of I, ID1,2, and ID3,4.
D 13.20 For the folded-cascode op amp in Fig. 13.10
utilizing power supplies of ±1 V, find the values of
VBIAS1, VBIAS2, and VBIAS3 to maximize the allowable range of
VICM and vO. Assume that all transistors are operated at equal
overdrive voltages of 0.15 V. Assume Vt for all devices is
0.4 V. Specify the maximum range of VICM and of vO.
D 13.21 For the folded-cascode op-amp circuit of Figs. 13.9
and 13.10 with bias currents I = 400 μA and IB = 250 μA,
and with all transistors operated at overdrive voltages of
0.2 V, find the W/L ratios for all devices. Assume that the
technology available is characterized by kn′ = 400 μA/V2 and
kp′ = 100 μA/V2.
13.22 Consider a design of the cascode op amp of Fig. 13.10
for which I = 400 μA and IB = 250 μA. Assume that all
transistors are operated at VOV = 0.2 V and that for all
devices, VA = 10 V. Find Gm, Ro, and Av. Also, if the
op amp is connected in the feedback configuration shown
in Fig. P13.22, find the voltage gain and output resistance of
the closed-loop amplifier.
C/9 C
Vi
Vo
Rof
Figure P13.22
D 13.23 Consider the folded-cascode op amp of Fig. 13.9
when loaded with a 10-pF capacitance. What should the bias
current IB be to obtain a slew rate of at least 10 V/μs? If the
input-stage transistors are biased at a current three times that
at which each of Q3 and Q4 is biased, find the value of I. If the
input-stage transistors are operated at overdrive voltages of
0.15 V, what is the unity-gain bandwidth realized? If the two
nondominant poles have the same frequency of 50 MHz, what
is the phase margin obtained? If it is required to have a phase
margin of 75°, what must ft be reduced to? By what amount
should CL be increased? What is the new value of SR?
13.24 For a particular design of the folded-cascode op amp
in Fig. 13.9, I < IB. What slew rate is obtained?
D *13.25 Design the folded-cascode circuit of Fig. 13.10 to
provide voltage gain of 80 dB and a unity-gain frequency of
20 MHz when CL = 10 pF. Design for IB = I, and operate
all devices at the same VOV. Utilize transistors with 1-μm
channel length for which VA is specified to be 12 V. Find the
required overdrive voltages and bias currents. What slew rate
is achieved? Also, for kn′ = 2.5kp′ = 400 μA/V2, specify the
required width of each of the 11 transistors used.
D 13.26 Sketch the circuit that is complementary to that in
Fig. 13.10, that is, one that uses an input p-channel differential
pair.
**13.27 This problem presents a very interesting addition to
the folded-cascode op-amp circuit of Fig. 13.10, designed to
deal with the situation during amplifier slewing. In particular,
the additional circuitry does two things: It prevents Q1 and
Q11 from going into the triode region, and it increases the
current available to charge CL and thus increases the slew rate.
The circuit is shown in Fig. P13.27 (with the current-mirror
circuit omitted, for simplicity). Observe that three transistors
are added: Q14, which is biased by a constant-current source
(20 μA), establishes the dc currents in Q9 and Q10. Assume
with respect to Q9 and Q10 that each has a W/L ratio 10 times
that of Q14. The other two additional transistors are Q12 and
Q13, which are diode connected and are normally cut off.
(a) For Vid = 0, find the bias current in each of Q1, Q2, Q3,
Q4, Q14, Q9, and Q10. Also, for the dc voltages shown,
and assuming Vtn =|Vtp|= 0.45 V and that all conducting
devices are operating at |VOV| = 0.15 V, show that Q12
and Q13 will be cut off.
(b) For an input differential signal that causes Q2 to turn off
and Q1 to conduct the entire bias current (320 μA), Q12
turns on (while Q13 remains off). Noting that the drain
current of Q12 adds to the 20 μA flowing through Q14,
find the current that now flows through Q10 and onto CL.
By what factor does the slew rate increase relative to
the value without Q12 present? Also give an approximate
estimate of the voltage at the drain of Q1 during the
slewing transient.
CL
Q4
Q10
Q9
Q13
Q14
Q12
Q3
Q1 Q2
Q11
−0.25 V
20 μA
320 μA
+1.2 V
−1 V
+1 V
−0.4 V
Figure P13.27
13.28 For the circuit in Fig. 13.12, assume that all transistors
are operating at equal overdrive voltages of 0.15-V magnitude
and have Vt = 0.45 V and that VDD = VSS = 1 V. Find (a)
the range over which the NMOS input stage operates, (b) the
range over which the PMOS input stage operates, (c) the range
over which both operate (the overlap range), and (d) the input
common-mode range. Assume that all current sources require
a minimum voltage of |VOV| to operate properly.
13.29 A particular design of the wide-swing current mirror of Fig. 13.13(b) utilizes devices having W/L = 20,
kn′ = 400 μA/V2, and Vt = 0.45 V. For IREF = 90 μA, what
value of VBIAS is needed? Also give the voltages that you
expect to appear at all nodes and specify the minimum voltage
allowable at the output terminal. If VA is specified to be 10 V,
what is the output resistance of the mirror?
D 13.30 For the folded-cascode circuit of Fig. 13.9, let the
total capacitance to ground at each of the source nodes of
Q3 and Q4 be denoted CP. Assuming that the incremental
resistance between the drain of Q3 and ground is small,
show that the pole that arises at the interface between the
first and second stages has a frequency fP ≃ gm3/2πCP.
Now, if this is the only nondominant pole, what is the
largest value that CP can be (expressed as a fraction of CL)
while a phase margin of 80° is achieved? Assume that all
transistors are operated at the same bias current and overdrive
voltage.
Section 13.3: The 741 BJT Op Amp
13.31 In the 741 op-amp circuit of Fig. 13.14, Q1, Q2, Q5, and
Q6 are biased at collector currents of 9.5 μA; Q16 is biased at
a collector current of 16.2 μA; and Q17 is biased at a collector
current of 550 μA. All these devices are of the “standard npn”
type, having IS = 10−14 A, β = 200, and VA = 125 V. For each
of these transistors, find VBE, gm, re, rπ, and ro. Provide your
results in table form. (Note that these parameter values are
utilized in the text in the analysis of the 741 circuit.)
D 13.32 For the circuit in Fig. P13.32, neglect base currents
and use the exponential iC−vBE relationship to show that
I3 = I1 sqrt((IS3 IS4)/(IS1 IS2))
Find I1 for the case in which IS3 = IS4 = 3 × 10−14 A,
IS1 = IS2 = 10−14 A, and a bias current I3 = 150 μA is required.
I3
I1
Q4
Q2
+15 V
−15 V
Q3
Q1
Figure P13.32
13.33 Transistor Q13 in the circuit of Fig. 13.14 consists, in
effect, of two transistors whose emitter–base junctions are
connected in parallel and for which ISA = 0.25 × 10−14A,
ISB = 0.75 × 10−14 A, β = 50, and VA = 50 V. For operation
at a total emitter current of 0.73 mA, find values for the
parameters VEB, gm, re, rπ, and ro for the A and B devices.
13.34 In the circuit of Fig. 13.14, Q1 and Q2 exhibit
emitter–base breakdown at 7 V, while for Q3 and Q4 such
a breakdown occurs at about 50 V. What differential input
voltage would result in the breakdown of the input-stage
transistors?
D 13.35 Figure P13.35 shows the CMOS version of the
circuit in Fig. P13.32. Find the relationship between I3 and I1
in terms of k1, k2, k3, and k4 of the four transistors, assuming
the threshold voltages of all devices to be equal in magnitude.
Note that k denotes μCoxW/L. In the event that k1 = k2 and
k3 = k4 = 16k1, find the required value of I1 to yield a bias
current in Q3 and Q4 of 1.6 mA.
Figure P13.35
D 13.36 For the 741 circuit, estimate the reference current
IREF in the event that ±10-V supplies are used. What value of
R5 would be necessary to reestablish the same bias current for
±10-V supplies as exists for ±15 V in the original design?
D 13.37 Design a Widlar current source to supply a current
of 10 μA given a reference input current of 0.3 mA. Assume
that the transistors have IS = 10−14 A and high β. Find VBE of
each of the two transistors as well as the value of R.
13.38 Consider the dc analysis of the 741 input stage shown
in Fig. 13.15.
(a) Derive an expression for I taking βP into account. What
is the percentage change in I if βP drops from 50 to 20?
(b) Now, consider an alternative design of this circuit in
which the feedback loop is eliminated. That is, Q8 and
Q9 are eliminated and IC10 is fed to the common-base
connection of Q3 and Q4. What is I now in terms of IC10? If
βP changes from 50 to 20, what is the resulting percentage
change in I?
D 13.39 Consider the dc analysis of the 741 input stage
shown in Fig. 13.15 for the situation in which IS9 = 2IS8.
For IC10 = 19 μA and assuming βP to be high, what does
I become? Redesign the Widlar source to reestablish IC1 =
IC2 = 9.5 μA.
D 13.40 Consider the circuit shown in Fig. 13.15. If IC10 =
40 μA and I is required to be 10 μA, what must be the ratio
of the emitter–junction area of Q9 to that area of Q8? Assume
that βP is large.
13.41 For the mirror circuit shown in Fig. 13.16 with
the bias and component values given in the text for the
741 circuit, what does the current in Q6 become if R2 is
shorted?
D 13.42 It is required to redesign the circuit of Fig. 13.16 by
selecting a new value for R3 so that when the base currents
are not neglected, the collector currents of Q5, Q6, and Q7 all
become equal, assuming that the input current IC3 = 9.5 μA.
Find the new value of R3 and the three currents. Recall that
βN = 200.
13.43 Consider the input circuit of the 741 op amp of
Fig. 13.14 when the emitter current of Q8 is about 19 μA.
If β of Q1 is 150 and that of Q2 is 220, find the
input bias current IB and the input offset current IOS of
the op amp.
13.44 For a particular application, consideration is being
given to selecting 741 ICs for input bias and offset currents
limited to 60 nA and 5 nA, respectively. Assuming other
aspects of the selected units to be normal, what minimum
βN and what βN variation are implied?
13.45 For a 741 employing ±5-V supplies, |VBE| = 0.6 V,
and |VCEsat| = 0.2 V, find the input common-mode range.
Neglect the voltage drops across R1 and R2.
D 13.46 Consider the design of the second stage of the 741.
What value of R9 would be needed to reduce IC16 to 9.5 μA?
(Hint: Build on Exercise 13.21)
D 13.47 Reconsider the 741 output stage as shown in
Fig. 13.17, in which R10 is adjusted to make IC19 = IC18. What
is the new value of R10? What values of IC14 and IC20 result?
Recall that IREF = 0.73 mA.
D *13.48 An alternative approach to providing the voltage
drop needed to bias the output transistors is the VBE–multiplier
circuit shown in Fig. P13.48. Design the circuit to provide a
terminal voltage of 1.118 V (the same as in the 741 circuit).
Base your design on half the current flowing through R1, and
assume that IS = 10−14 A and β = 200. What is the incremental
resistance between the two terminals of the VBE multiplier
circuit?
I = 180 μA
180 μA
Figure P13.48
13.49 For the circuit of Fig. 13.14, what is the total current
required from the power supplies when the op amp is operated
in the linear mode, but with no load? Hence, estimate the
quiescent power dissipation in the circuit. (Hint: Use the data
given in Table 13.1.)
13.50 Consider the 741 input stage as modeled in Fig. 13.18,
with two additional npn diode-connected transistors, Q1a and
Q2a, connected between the present npn and pnp devices, one
per side. Convince yourself that each of the additional devices
will be biased at the same current as Q1 to Q4—that is, 9.5 μA.
What does Rid become? What does Gm1 become? What is the
value of Ro4 now? What is the output resistance of the first
stage, Ro1? (Note that Ro6 remains unchanged at 18.2 MΩ.)
What is the new open-circuit voltage gain, Gm1Ro1? Compare
these values with the original ones, namely, Rid = 21 MΩ,
Gm1 = 0.19 mA/V, Ro4 = 10.5 MΩ, Ro1 = 6.7 MΩ, and
|Avo| = 1273 V/V.
13.51 Consider the current mirror in Fig. 13.19. What value
must R2 be increased to in order to increase Ro6 by a factor of
2? Recall that Q6 is operating at IC6 = 9.5 μA and has β = 200
and VA = 125 V.
13.52 Repeat Exercise 13.24 with R1 = R2 replaced by 2-kΩ
resistors.
13.53 A manufacturing problem in a 741 op amp causes
the current-transfer ratio of the mirror circuit that loads the
input stage to become 0.8 A/A. For input devices (Q1–Q4)
appropriately matched and with high β, and normally biased
at 9.5 μA, what input offset voltage results?
*13.54 In Example 13.4 we investigated the effect of a
mismatch between R1 and R2 on the input offset voltage
of the op amp. Conversely, R1 and R2 can be deliberately mismatched (using the circuit shown in Fig. P13.54,
for example) to compensate for the op-amp input offset
voltage.
(a) Show that an input offset voltage VOS can be compensated
for (i.e., reduced to zero) by creating a relative mismatch
ΔR/R between R1 and R2,
ΔR/R = [VOS/(2VT)] [1+re/R] / [1−VOS/(2VT)]
where re is the emitter resistance of each of Q1 to Q6, and
R is the nominal value of R1 and R2. (Hint: Use Eq. 13.94.)
(b) Find ΔR/R to trim a 3-mV offset to zero.
(c) What is the maximum offset voltage that can be trimmed
this way (corresponding to R2 completely shorted)?
(Recall that each of Q5 and Q6 is biased at 9.5 μA.)
Figure P13.54
13.55 Through a processing imperfection, the β of Q4 in
Fig. 13.14 is reduced to 10, while the β of Q3 remains at its
regular value of 50. Assuming that the collector current of Q3
remains unchanged at 9.5 μA, find the net output dc current of
the Q5−Q6 mirror, and hence find also the input offset voltage
that this mismatch introduces.
13.56 If the current transfer ratio of the mirror load of the 741
input stage is 0.995, find the CMRR of the input stage. (Hint:
Use Eq. 13.102 together with the output resistance values
determined in Exercise 13.28. Recall that the input-stage
transistors are biased at 9.5 μA.)
13.57 Consider the circuit of Fig. 13.14 modified to include
resistors R in series with the emitters of each of Q8 and
Q9. What does the resistance looking into the collector
of Q9, Ro9, become? For what value of R does it equal
Ro10 (i.e., 31.1 MΩ)? For this case, what does Ro looking
to the left of node Y become? (Recall that Q9 is biased
at 0.73 mA.)
*13.58 What is the effect on the differential gain of the 741
op amp of short-circuiting one or the other or both of R1 and
R2 in Fig. 13.14? (Refer to Fig. 13.19.) For simplicity, assume
β = ∞.
13.59 An alternative approach to that presented in Example 13.5 for determining the CMRR of the 741 input stage
is investigated in this problem. Rather than performing the
analysis on the closed loop shown in Fig. 13.23, we observe
that the negative feedback increases the resistance at node Y
by the amount of negative feedback. Thus, we can break the
loop at Y and connect a resistance Rf = (1+Aβ)Ro between
the common-base connection of Q3−Q4 and ground. We can
then determine the current i and Gmcm. Using the fact that the
loop gain is approximately equal to βP (Exercise 13.17) show
that this approach yields an identical result to that found in
Example 13.5.
13.60 Consider a variation on the design of the 741 second
stage in which R8 = 50 Ω. What Ri2 and Gm2 correspond?
D 13.61 In the analysis of the 741 second stage, note that Ro2
is affected most strongly by the low value of Ro13B. Consider
the effect of placing appropriate resistors in the emitters of
Q12, Q13A, and Q13B on this value. What resistor in the emitter
of Q13B would be required to make Ro13B equal to Ro17 and thus
Ro2 half as great? What resistors in each of the other emitters
would be required?
13.62 For a 741 employing ±5-V supplies, VBE = 0.6 V
and VCEsat = 0.2 V, find the output voltage limits that
apply.
D 13.63 Consider an alternative to the present 741 output
stage in which Q23 is not used, that is, in which its base and
emitter are joined. Reevaluate the reflection of RL = 2 kΩ to
the collector of Q17. What does A2 become?
13.64 Figure P13.64 shows the circuit for determining the
op-amp output resistance when vO is positive and Q14 is
conducting most of the current. Using the resistance of the
Q18−Q19 network calculated in Exercise 13.35 (163 Ω) and
neglecting the large output resistance of Q13A, find Rout when
Q14 is sourcing an output current of 5 mA.
Rout
Figure P13.64
13.65 Consider the positive current-limiting circuit involving Q13A, Q15, and R6. Find the current in R6 at which the
collector current of Q15 equals the current available from Q13A
(180 μA) minus the base current of Q14. (You need to perform
a couple of iterations.)
D 13.66 Consider the 741 sinking-current limit involving R7,
Q21, Q24, R11, and Q22. For what current through R7 is the
current in Q22 equal to the maximum current available from
the input stage (i.e., the current in Q8)? What simple change
would you make to reduce this current limit to 10 mA?
13.67 Using the data provided in Eq. (13.115) (alone) for
the overall gain of the 741 with a 2-kΩ load, and realizing the
significance of the factor 0.97 in relation to the load, calculate
the open-circuit voltage gain, the output resistance, and the
gain with a load of 500 Ω.
13.68 A 741 op amp has a phase margin of 80°. If the excess
phase shift is due to a second single pole, what is the frequency
of this pole?
13.69 A 741 op amp has a phase margin of 80°. If the op
amp has nearly coincident second and third poles, what is
their frequency?
D *13.70 For a modified 741 whose second pole is at 5
MHz, what dominant-pole frequency is required for 85°
phase margin with a closed-loop gain of 100? Assuming CC
continues to control the dominant pole, what value of CC
would be required?
13.71 An internally compensated op amp having an ft of 5
MHz and dc gain of 106 utilizes Miller compensation around
an inverting amplifier stage with a gain of –1000. If space
exists for at most a 50-pF capacitor, what resistance level
must be reached at the input of the Miller amplifier for
compensation to be possible?
13.72 Consider the integrator op-amp model shown in
Fig. 13.30. For Gm1 = 2 mA/V, CC = 100 pF, and a resistance
of 2 × 10^7 Ω shunting CC, sketch and label a Bode plot for
the magnitude of the open-loop gain. If Gm1 is related to the
first-stage bias current as Gm1 = I/2VT, find the slew rate of
this op amp.
13.73 For an amplifier with a slew rate of 10 V/μs, what
is the full-power bandwidth for outputs of ±10 V? What
unity-gain bandwidth, ωt, would you expect if the topology
was similar to that of the 741?
D 13.74 If a resistance RE is included in each of the emitter
leads of Q3 and Q4 of the 741 circuit, show that the slew rate
is 4(VT + IRE/2)ωt. Hence find the value of RE that would
double the 741 slew rate while keeping ωt and I unchanged.
What are the new values of CC, the dc gain, and the 3-dB
frequency?
Figure P13.75
D 13.75 Figure P13.75 shows a circuit suitable for op-amp
applications. For all transistors β = 100, VBE = 0.7 V, and
ro = ∞.
(a) For inputs grounded and output held at 0 V (by negative
feedback) find the collector currents of all transistors.
Neglect base currents.
(b) Calculate the input resistance.
(c) Calculate the gain of the amplifier with a load of 5 kΩ.
(d) With load as in (c) calculate the value of the capacitor C
required for a 3-dB frequency of 100 Hz.
Section 13.4: Modern Techniques for the
Design of BJT Op Amps
Unless otherwise specified, for the problems in this section
assume βN = 40, βP = 10, VAn = 30 V, VAp = 20 V, VBE =
0.7 V, VCEsat = 0.1 V.
D 13.76 Design the circuit in Fig. 13.33 to generate a current
I = 5 μA. Utilize transistors Q1 and Q2 having areas in a ratio
of 1:4. Assume that Q3 and Q4 are matched and design for a
0.15-V drop across each of R3 and R4. Specify the values of
R2, R3, and R4. Ignore base currents.
D 13.77 Consider the circuit of Fig. 13.33 for the case
designed in Exercise 13.37, namely, I = 10 μA, IS2/IS1 =
2, R2 = 1.73 kΩ, R3 = R4 = 20 kΩ. Augment the circuit
with npn transistors Q5 and Q6 with emitters connected to
ground and bases connected to VBIAS1, to generate constant
currents of 10 μA and 40 μA, respectively. What should
the emitter areas of Q5 and Q6 be relative to that of Q1?
What value of a resistance R6 will, when connected in the
emitter of Q6, reduce the current generated by Q6 to 10 μA?
Assuming that the VBIAS1 line has a low incremental resistance
to ground, find the output resistance of current source Q5
and of current source Q6 with R6 connected. Ignore base
currents.
D 13.78 It is required to use the circuit in Fig. 13.33 to bias
an npn differential pair. The bias current-source transistor of
the pair, Q5, is identical to Q2 and its base is connected to
the BIAS1 line. In its emitter lead is connected a resistance
R5 equal to R2. The differential pair has two equal collector
resistances RC connected to VCC, and the output voltage vo is
taken between the two collectors.
(a) Find an expression for the differential gain Ad in terms
of (RC/R5) and (IS5/IS1). Comment on the expected
temperature dependence of Ad. Neglect the effect of
finite βN.
(b) Design the circuit for I = 20 μA and Ad = 10 V/V. Let
the emitter areas of Q1 and Q5 be in the ratio 1:4. Specify
the required values of R5 and RC.
D 13.79 (a) Find the input common-mode range of the circuit
in Fig. 13.35(a). Let VCC = 3 V and VBIAS = 2.3 V.
(b) Give the complementary version of the circuit in
Fig. 13.35(a), that is, the one in which the differential pair
is npn. For the same conditions as in (a), what is the input
common-mode range?
13.80 For the circuit in Fig. 13.35(b), let VCC = 3 V,
VBIAS = 2.3 V, I = 20 μA, and RC = 25 kΩ. Find the input
common-mode range and the differential voltage gain vo/vid.
Neglect base currents.
D 13.81 For the circuit in Fig. 13.36, let VCC = 3 V,
VBIAS = 0.7 V, and IC6 = 40 μA. Find RC that results in a
differential gain of 10 V/V. What is the input common-mode
range and the input differential resistance? Ignore base currents except
when calculating Rid. If Rid is to be increased by a factor of 4
while the gain and VICM remain unchanged, what must I and
RC be changed to?
13.82 It is required to find the input resistance and the
voltage gain of the input stage shown in Fig. 13.37. Let
VICM ≪ 0.8 V so that the Q3−Q4 pair is off. Assume that
Q5 supplies 8 μA, that each of Q7 to Q10 is biased at 8 μA,
and that all four cascode transistors are operating in the
active mode. The input resistance of the second stage of
the op amp is 1.5 MΩ. The emitter-degeneration resistances
are R7 = R8 = 22 kΩ, and R9 = R10 = 33 kΩ. [Hint: Refer
to Fig. 13.38.]
D *13.83 Consider the equivalent half-circuit shown in
Fig. 13.38. Assume that in the original circuit, Q1 is biased
at a current I, Q7 and Q9 are biased at 2I, the dc voltage drop
across R7 is 0.2 V, and the dc voltage drop across R9 is 0.3 V.
Find the output resistance in terms of I, and hence find the
open-circuit voltage gain (i.e., the voltage gain for RL = ∞).
Now with RL connected, find the voltage gain in terms of
(IRL). For RL = 1MΩ, find I that will result in the voltage
gains of 150 V/V and 300 V/V.
*13.84 (a) For the circuit in Fig. 13.39, show that the loop
gain of the common-mode feedback loop is
Aβ ≃ (Ro9 || Ro7)/(re7 +R7)
Recall that the CMF circuit responds only to the average
voltage VCM of its two input voltages and realizes the
transfer characteristic VB = VCM + 0.4. Ignore the loading
effect of the CMF circuit on the collectors of the cascode
transistors.
(b) For the values in Example 13.8, calculate the loop
gain Aβ.
(c) In Example 13.8, we found that with the CMF absent, a
current mismatch ΔI = 0.3 μA gives rise to ΔVCM = 2.5 V.
Now, with the CMF present, use the value of loop gain found
in (b) to calculate the expected ΔVCM and compare to the value
found by a different approach in Example 13.8. [Hint: Recall
that negative feedback reduces change by a factor equal to
(1+Aβ).]
13.85 The output stage in Fig. 13.41 operates at a quiescent
current IQ of 0.6 mA. The maximum current iL that the stage
can provide in either direction is 12 mA. Also, the output
stage is equipped with a feedback circuit that maintains a
minimum current of IQ/2 in the inactive output transistor.
Also, VCC = 3 V.
(a) What is the allowable range of vO?
(b) For iL = 0, what is the output resistance of the op amp?
(c) If the open-loop gain of the op amp is 100,000 V/V,
find the closed-loop output resistance obtained when the
op amp is connected in the unity-gain voltage follower
configuration, with iL = 0.
(d) If the op amp is sourcing a load current iL = 12 mA, find
iP, iN, and the open-loop output resistance.
(e) Repeat (d) for the case of the open-loop op amp sinking
a load current of 12 mA.
13.86 It is required to derive the expressions in Eqs. (13.130)
and (13.131). Toward that end, first find vB7 in terms of vBEN
and hence iN. Then find vB6 in terms of iP. For the latter
purpose note that Q4 measures vEBP and develops a current
i4 = (vEBP −vEB4)/R4. This current is supplied to the series
connection of Q5 and R5 where R5 = R4. In the expression you
obtain for vB6, use the relationship
ISP/IS4 = ISN/IS5
to express vB6 in terms of iP and ISN. Now with vB6 and vB7
determined, find iC6 and iC7.
13.87 It is required to derive the expression for vE in
Eq. (13.132). Toward that end, note from the circuit in
Fig. 13.43 that vE = vEB7 + vBEN and note that QN conducts a current iN and Q7 conducts a current iC7 given
by Eq. (13.131).
D 13.88 For the output stage in Fig. 13.43, find the current
IREF that results in a quiescent current IQ = 0.6 mA. Assume
that I = 12 μA, QN has eight times the area of Q10, and Q7
has four times the area of Q11. What is the minimum current
in QN and QP?"""

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

CARD_TEMPLATE = """<article class="card" data-tags="circuits-electronics sedra chapter-13 op-amps">
  <h3>Sedra — Chapter 13</h3>
  <p>Problem {num}: {title}</p>
  <div class="btn-row">
    <a href="./Sedra/Sedra_ch13_prob_{num}.html">OPEN THEORY</a>
    <a href="./Sedra/Sedra_ch13_prob_{num}_sim.html">OPEN SIM</a>
  </div>
</article>"""

def parse_problems(raw: str):
    pattern = re.compile(r'(?m)^(?:[D*= ]+)?(13\.\d+)\s')
    matches = list(pattern.finditer(raw))
    problems = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        block = raw[start:end].strip()
        first_line = block.splitlines()[0]
        first_line = re.sub(r'^(?:[D*= ]+)?13\.\d+\s*', '', first_line).strip()
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
        title = f"Sedra Chapter 13 — Problem {num}"
        problem_text = html.escape(item["text"])
        theory_html = THEORY_TEMPLATE.replace("{title}", title).replace("{problem_text}", problem_text)
        sim_html = SIM_TEMPLATE.replace("{title}", title)
        theory_name = f"Sedra_ch13_prob_{num}.html"
        sim_name = f"Sedra_ch13_prob_{num}_sim.html"
        write_text(TARGET_DIR / theory_name, theory_html)
        write_text(TARGET_DIR / sim_name, sim_html)
        cards.append(CARD_TEMPLATE.replace("{num}", num).replace("{title}", html.escape(item["title"])))
    cards_html = "\n".join(cards)
    write_text(TARGET_DIR / "Sedra_ch13_cards.html", cards_html)
    print(f"Created {len(problems)} theory files, {len(problems)} sim files, and Sedra_ch13_cards.html in {TARGET_DIR}")

if __name__ == "__main__":
    build()
