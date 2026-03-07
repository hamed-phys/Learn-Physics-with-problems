
from pathlib import Path
import os, re, html

DEFAULT_TARGET = r"F:\Courcses\website\important to webpage\Learn-Physics-with-problems\problems\Circuits_Electronics\Sedra"
TARGET_DIR = Path(os.environ.get("SEDRA_TARGET_DIR", DEFAULT_TARGET))

RAW_TEXT = r"""**PROBLEMS
Computer Simulation Problems
Problems identified by the Multisim/PSpice icon are
intended to demonstrate the value of using SPICE simulation
to verify hand analysis and design, and to investigate
important issues such as allowable signal swing and amplifier
nonlinear distortion. Instructions to assist in setting up PSpice
and Multisim simulations for all the indicated problems can
be found on the website. Note that if a particular parameter
value is not specified in the problem statement, you are to
make a reasonable assumption.
Section 11.1: The General Feedback Structure
11.1 A negative-feedback amplifier has a closed-loop gain
Af =200 and an open-loop gain A = 10^4.What is the feedback
factor β? If a manufacturing error results in a reduction of A
to 10^3, what closed-loop gain results? What is the percentage
change in Af corresponding to this factor of 10 reduction in A?
11.2 Consider the op-amp circuit shown in Fig. P11.2,
where the op amp has infinite input resistance and zero
output resistance but finite open-loop gain A.
2 1
Vs
A
12
R1
R2
1 Vo 2
Figure P11.2
(a) Convince yourself that β = R1/(R1 + R2).
(b) If R1 = 10 kΩ, find R2 that results in Af = 10 V/V
for the following three cases: (i) A = 1000 V/V;
(ii) A = 200 V/V; (iii) A = 15 V/V.
(c) For each of the three cases in (b), find the percentage
change in Af that results when A decreases by 20%.
Comment on the results.
11.3 The noninverting buffer op-amp configuration shown
in Fig. P11.3 provides a direct implementation of the feedback
loop of Fig. 11.1. Assuming that the op amp has infinite input
resistance and zero output resistance, what is β? If A = 1000,
what is the closed-loop voltage gain? What is the amount of
feedback (in dB)? For Vs = 1 V, find Vo and Vi. If A decreases
by 10%, what is the corresponding percentage decrease in Af?
1A 2
Figure P11.3
11.4 In a particular circuit represented by the block diagram
of Fig. 11.1, a signal of 1 V from the source results in a
difference signal of 10 mV being provided to the amplifying
element A, and 5 V appearing at the output. For this
arrangement, identify the values of A and β that apply.
11.5 (a) Show that in a negative-feedback amplifier with
loop gain Aβ ≫ 1, the closed-loop gain Af is lower than its
ideal value of 1/β by (100/Aβ)%.
(b) What is the minimum loop gain required so that Af is
within (i) 0.1%, (ii) 1%, and (iii) 5% of its ideal value?
11.6 In a particular amplifier design, the β network consists
of a linear potentiometer for which β is 0.00 at one end, 1.00
at the other end, and 0.50 in the middle. As the potentiometer
is adjusted, find the three values of closed-loop gain that result
when the amplifier open-loop gain is (a) 1 V/V, (b) 10 V/V,
(c) 100 V/V, (d) 1000 V/V, and (e) 10,000 V/V. Provide your
results in a table in which there is a row for each value of A
and a column for each value of β.
11.7 A newly constructed feedback amplifier undergoes a
performance test with the following results: With the feedback
connection removed, a source signal of 2 mV is required to
provide a 5-V output; with the feedback connected, a 5-V
output requires a 100-mV source signal. For this amplifier,
identify values of A, β, Aβ, the closed-loop gain, and the
amount of feedback (in dB).
D 11.8 An amplifier has an open-loop gain with a nominal
value of 1000 but can vary from unit to unit by as much as
±50% of nominal. It is required to apply negative feedback
to this amplifier so that the variability of the closed-loop gain
of the resulting feedback amplifier is limited to ±1%. What is
the largest possible nominal value of closed-loop gain that can
be achieved? Now if three of these feedback amplifiers are
placed in cascade, what is the nominal value of the gain of the
resulting cascade amplifier? What is the expected variability
of this gain?
11.9 The op amp in the circuit of Fig. P11.9 has an
open-circuit voltage gain μ, a differential input resistance
Rid, and a negligibly small output resistance. It is connected
in the noninverting configuration with a feedback network
consisting of a voltage divider (R1,R2). While β is still
determined by the divider ratio [i.e., β = R1/(R1 + R2)], the
open-loop gain A is no longer simply equal to μ. This is
because the feedback network now loads the input of the
amplifier (because of the finite Rid). To determine the value
of A, use the method outlined in Section 11.1.3 to determine
the loop gain Aβ. Thus show that
A = μ Rid / (Rid +(R1||R2))
Vs
R1
R2
m
Vo
Figure P11.9
Section 11.2: Some Properties of Negative
Feedback
11.10 For the negative-feedback loop of Fig. 11.1, find the
loop gain Aβ for which the sensitivity of closed-loop gain
to open-loop gain [i.e., (dAf /Af )/(dA/A)] is –40 dB. For what
value of Aβ does the sensitivity become 1/5?
D 11.11 A designer is considering two possible designs of
a feedback amplifier. The ultimate goal is Af = 10 V/V. One
design employs an amplifier for which A = 1000 V/V and
the other uses A = 500 V/V. Find β and the desensitivity
factor in both cases. If the A = 1000 amplifier units have
a gain uncertainty of ±10%, what is the gain uncertainty
for the closed-loop amplifiers utilizing this amplifier type?
If the same result is to be achieved with the A = 500
amplifier, what is the maximum allowable uncertainty in
its gain?
D 11.12 A designer is required to achieve a closed-loop gain
of 10±0.1% V/V using a basic amplifier whose gain variation
is ±10%. What nominal value of A and β (assumed constant)
are required?
D 11.13 A circuit designer requires a gain of 25 ± 1% V/V
using an amplifier whose gain varies by a factor of 10 over
temperature and time. What is the lowest gain required? The
value of β? (Hint: Since the change in the open-loop gain is
very large, do not use differential analysis.)
D 11.14 A power amplifier employs an output stage whose
gain varies from 2 to 12 for various reasons. What is the gain
of an ideal (nonvarying) amplifier connected to drive it so
that an overall gain with feedback of 100 ± 5% V/V can be
achieved? What is the value of β to be used? What are the
requirements if Af must be held within ±0.5%? For each of
these situations, what preamplifier gain and feedback factor
β are required if Af is to be 10 V/V (with the two possible
tolerances)? (Hint: Since the change in the open-loop gain is
very large, do not use differential analysis.)
D 11.15 It is required to design an amplifier with a gain
of 100 that is accurate to within ±1%. You have available
amplifier stages with a gain of 1000 that is accurate to
within ±30%. Provide a design that uses a number of these
gain stages in cascade, with each stage employing negative
feedback of an appropriate amount. Obviously, your design
should use the lowest possible number of stages while meeting
specification.
D *11.16 It is required to design an amplifier to have a
nominal closed-loop gain of 10 V/V using a battery-operated
amplifier whose gain reduces to half its normal full-battery
value over the life of the battery. If only 2% drop in
closed-loop gain is desired, what nominal open-loop amplifier
gain must be used in the design? (Note that since the change
in A is large, it is inaccurate to use differentials.) What value
of β should be chosen? If component-value variation in the
β network may produce as much as a ±1% variation in β, to
what value must A be raised to ensure the required minimum
gain?
D 11.17 Design a feedback amplifier that has a closed-loop
gain of 100 V/V and is relatively insensitive to change
in basic-amplifier gain. In particular, it should provide a
reduction in Af to 99 V/V for a reduction in A to one-tenth its
nominal value. What is the required loop gain? What nominal
value of A is required? What value of β should be used?
What would the closed-loop gain become if A were increased
tenfold? If A were made infinite?
11.18 Consider an amplifier having a midband gain AM
and a low-frequency response characterized by a pole at
s = −ωL and a zero at s = 0. Let the amplifier be connected
in a negative-feedback loop with a feedback factor β. Find
an expression for the midband gain and the lower 3-dB
frequency of the closed-loop amplifier. By what factor have
both changed?
11.19 A capacitively coupled amplifier has a midband gain
of 1000 V/V, a single high-frequency pole at 10 kHz, and a
single low-frequency pole at 100 Hz. Negative feedback is
employed so that the midband gain is reduced to 10. What
are the upper and lower 3-dB frequencies of the closed-loop
gain?
D 11.20 Low-cost audio power amplifiers often avoid direct
coupling of the loudspeaker to the output stage because any
resulting dc bias current in the speaker can use up (and thereby
waste) its limited mechanical dynamic range. Unfortunately,
the coupling capacitor needed can be large! But feedback
helps. For example, for an 8-Ω loudspeaker and fL = 100 Hz,
what size capacitor is needed? Now, if feedback is arranged
around the amplifier and the speaker so that a closed-loop gain
Af = 10 V/V is obtained from an amplifier whose open-loop
gain is 1000 V/V, what value of fLf results? If the ultimate
product-design specification requires a 50-Hz cutoff, what
capacitor can be used?
D *11.21 It is required to design a dc amplifier with a
low-frequency gain of 1000 and a 3-dB frequency of 1 MHz.
You have available gain stages with a gain of 1000 but with
a dominant high-frequency pole at 20 kHz. Provide a design
that employs a number of such stages in cascade, each with
negative feedback of an appropriate amount. Use identical
stages.
Hint: The 3-dB frequency of a cascade of N identical gain stages, each with a 3-dB frequency f3dB|stage is
given by
f3dB|cascade = f3dB|stage sqrt(2^(1/N) − 1)
D 11.22 Design a supply-ripple-reduced power amplifier for
which the output stage can be modeled by the block diagram of
Fig. 11.5, where A1 = 0.9 V/V, and the power-supply ripple
VN = ±1 V. A closed-loop gain of 10 V/V is desired. What
is the gain of the low-ripple preamplifier needed to reduce
the output ripple to ±100 mV? To ±10 mV? To ±1 mV?
For each case, specify the value required for the feedback
factor β.
D 11.23 A feedback amplifier is to be designed using
a feedback loop connected around a two-stage amplifier.
The first stage is a direct-coupled, small-signal amplifier
with a high upper 3-dB frequency. The second stage is a
power-output stage with a midband gain of 10 V/V and upper
and lower 3-dB frequencies of 8 kHz and 80 Hz, respectively.
The feedback amplifier should have a midband gain of
100 V/V and an upper 3-dB frequency of 40 kHz. What is
the required gain of the small-signal amplifier? What value
of β should be used? What does the lower 3-dB frequency of
the overall amplifier become?
*11.24 The complementary BJT follower shown in
Fig. P11.24(a) has the approximate transfer characteristic
shown in Fig. P11.24(b). Observe that for −0.7 V ≤ vI ≤
+0.7 V, the output is zero. This “dead band” leads to crossover
distortion (see Section 12.3). Consider this follower to be
driven by the output of a differential amplifier of gain 100
V
vI vO
V
(a) Figure P11.24
vO
1
1
0.7 0 0.7 v
1
1
(b)
I
Figure P11.24 continued
whose positive-input terminal is connected to the input signal
source vS and whose negative-input terminal is connected to
the emitters of the follower. Sketch the transfer characteristic
vO versus vS of the resulting feedback amplifier. What are
the limits of the dead band, and what are the gains outside the
dead band?
D 11.25 A particular amplifier has a nonlinear transfer
characteristic that can be approximated as follows:
(a) For small input signals, vI ≤ 10 mV, vO/vI = 10^3.
(b) For intermediate input signals, 10 mV ≤ vI ≤ 60 mV,
ΔvO/ΔvI = 10^2.
(c) For large input signals, vI ≥ 60 mV, the output saturates.
If the amplifier is connected in a negative-feedback loop, find
the feedback factor β that reduces the factor-of-10 change in
gain (occurring at vI = 10mV) to only a 10% change. What
is the transfer characteristic vO versus vS of the amplifier with
feedback?
Section 11.3: The Feedback Voltage Amplifier
D 11.26 For the feedback voltage amplifier of Fig. 11.8(a),
let the op amp have an infinite input resistance, a zero
output resistance, and a finite open-loop gain of 1000 V/V.
If R1 = 10 kΩ, what value should R2 have to obtain an ideal
closed-loop gain of 10? Now, calculate the loop gain Aβ and
use it to find the actual value of the closed-loop gain Af. If Af
is to be exactly 10, what must the value of R2 be?
D 11.27 Consider the series–shunt feedback amplifier in
Fig. 11.11(a), which is analyzed in Example 11.3.
(a) If R1 = 10 kΩ, find the value of R2 that results in an ideal
closed-loop gain of 10.
(b) Use the expression for Aβ derived in Example 11.3 to
find the value of the loop gain for the case μ = 1000,
Rid = 100 kΩ, ro = 1 kΩ, Rs = 100 kΩ, and RL = 10 kΩ.
Hence determine the value of the closed-loop gain Af.
(c) By what factor must μ be increased to ensure that Af is
within 1% of the ideal value of 10?
D 11.28 Consider the series–shunt feedback amplifier of
Fig. 11.8(b) that is analyzed in Example 11.2.
(a) If R1 = 1 kΩ, what value should R2 have to obtain a
closed-loop gain whose ideal value is 5 V/V?
(b) If gm1 = gm2 = 4 mA/V, RD1 = RD2 = 10 kΩ, and the
MOSFET’s ro is very large, use the expression for Aβ
derived in Example 11.2 to find the value of Aβ and
hence determine the closed-loop gain Af.
*11.29 In the series–shunt feedback amplifier shown in
Fig. P11.29, the devices operate with VBE = 0.7 V and have
β1 = β2 = 100. The input signal Vs has a zero dc component.
Resistances Rs = 100 Ω, R1 = 1 kΩ, R2 = 10 kΩ, and
RL = 1 kΩ.
(a) If the loop gain is large, what do you expect the
closed-loop gain to be? Give both an expression and
its value.
(b) Find the dc emitter current in each of Q1 and Q2. Also,
find the dc voltage at the emitter of Q2.
(c) Calculate the value of the loop gain Aβ. (Hint: Set Vs = 0
and break the loop at the base of Q1. Simplify the circuit
by eliminating dc sources.)
(d) Calculate the value of Af.
D 11.30 Consider the series–shunt feedback amplifier of
Fig. 11.8(c), which was the subject of Exercise 11.6. Assume
that the voltage divider (R1,R2) is implemented with a
1-MΩ potentiometer. Assume that the MOSFET is biased
so that gm = 4 mA/V and ro is large. Also, RD = 10 kΩ.
Find the value of R1 that results in a closed-loop gain
of 5 V/V.
D 11.31 Figure P11.31 shows a series–shunt feedback
amplifier known as a “feedback triple.” All three MOSFETs
are biased to operate at gm = 4 mA/V. You may neglect
their ro’s.
(a) Select a value for RF that results in a closed-loop gain
that is ideally 10 V/V.
Vs
Rout1
Rout2
Q1
Q2
RD1
10 k Q3
RD2
10 k
RS1
RF
100
RS2
100
Io
Vo
Figure P11.31
(b) Determine the loop gain Aβ and hence the value of Af.
By what percentage does Af differ from the ideal value
you designed for? How can you adjust the circuit to make
Af equal to 10?
11.32 Figure P11.32 shows a series–shunt feedback amplifier without details of the bias circuit.
VCC
RC1
Q1
Q3
RE
RC2
Q2
Vo
Vs
RF
Figure P11.32
(a) If RE is selected to be 50 Ω, find the value for RF
that results in a closed-loop gain with an ideal value
of 25 V/V.
(b) If Q1 is biased at 1 mA, Q2 at 2 mA, and Q3 at 5 mA,
and assuming that the transistors have hfe = 100 and
large ro, and that RC1 = 2 kΩ and RC2 = 1 kΩ, find the
value of the loop gain Aβ and hence of the closed-loop
gain Af.
D 11.33 The current-mirror-loaded differential amplifier in
Fig. P11.33 has a feedback network consisting of the voltage
divider (R1,R2), with R1 + R2 = 1 MΩ. The devices are sized
to operate at |VOV| = 0.2 V. For all devices, |VA| = 10 V. The
input signal source has a zero dc component.
(a) Find the loop gain Aβ and hence the value of A.
(b) Find the values of R1 and R2 that result in a closed-loop
gain of exactly 5 V/V.
Section 11.4: Systematic Analysis of Feedback
Voltage Amplifiers (Series–Shunt)
11.34 A series–shunt feedback amplifier employs a basic
amplifier with input and output resistances each of 2 kΩ and
gain A = 1000 V/V. The feedback factor β = 0.1 V/V. Find
the gain Af, the input resistance Rif, and the output resistance
Rof of the closed-loop amplifier.
11.35 For a particular amplifier connected in a feedback loop
in which the output voltage is sampled, measurement of the
output resistance before and after the loop is connected shows
a change by a factor of 200. Is the resistance with feedback
higher or lower? What is the value of the loop gain Aβ? If
Rof is 100 Ω, what is Ro without feedback?
11.36 The formulas for Rif and Rof in Eqs. (11.20) and
(11.23), respectively, also apply for the case in which A is a
function of frequency. In this case, the resulting impedances
Zif and Zof will be functions of frequency. Consider the case
of a series–shunt amplifier that has an input resistance Ri, an
output resistance Ro, and open-loop gain A = A0/(1+s/ωH),
and a feedback factor β that is independent of frequency. Find
Zif and Zof and give an equivalent circuit for each, together
with the values of all the elements in the equivalent circuits.
11.37 A feedback amplifier utilizing voltage sampling and
employing a basic voltage amplifier with a gain of 1000 V/V
and an input resistance of 1000 Ω has a closed-loop input
resistance of 10 kΩ. What is the closed-loop gain? If the basic
amplifier is used to implement a unity-gain voltage buffer,
what input resistance do you expect?
11.38 Consider the noninverting op-amp circuit of Example
11.4 for the case R1 = ∞ and R2 = 0.
(a) What is the value of β, and what is the ideal value of the
closed-loop gain?
(b) Adapt the expressions found in Example 11.4 to obtain
expressions for A and Aβ for this case.
(c) For μ = 10^4, Rid = 100 kΩ, Rs = 10 kΩ, ro = 1 kΩ, and
RL = 2 kΩ, find A, Aβ, Af, Rin, and Rout.
*11.39 This problem deals with the series–shunt feedback
amplifier of Fig. P11.29 and overlaps somewhat with Problem
11.29. Thus, if you have already solved 11.29, you can use
some of the results in the solution of this problem. The devices
operate with VBE = 0.7 V and have β1 = β2 = 100. The input
signal Vs has a zero dc component. Resistances Rs = 100 Ω,
R1 = 1 kΩ, R2 = 10 kΩ, and RL = 1 kΩ.
(a) If the loop gain is large, what do you expect the
closed-loop gain Vo/Vs to be? Give both an expression
and its approximate value.
(b) Find the dc emitter current in each of Q1 and Q2. Also
find the dc voltage at the emitter of Q2.
(c) Sketch the A circuit without the dc sources. Derive
expressions for A, Ri, and Ro, and find their values.
(d) Give an expression for β and find its value.
(e) Find the closed-loop gain Vo/Vs, the input resistance Rin,
and the output resistance Rout. By what percentage does
the value of Af differ from the approximate value found
in (a)?
D *11.40 Figure P11.40 shows a series–shunt amplifier with a feedback factor β = 1. The amplifier is designed
so that vO = 0 for vS = 0, with small deviations in vO from
0 V dc being minimized by the negative-feedback action. The
technology utilized has kn′ = 2kp′ = 120 μA/V2, Vt = 0.7 V,
and VA′ = 24 V/μm.
(a) Show that the feedback is negative.
(b) With the feedback loop opened at the gate of Q2, and
the gate terminals of Q1 and Q2 grounded, find the dc
current and the overdrive voltage at which each of Q1 to
Q5 is operating. Ignore the Early effect. Also find the dc
voltage at the output.
(c) Find gm and ro of each of the five transistors.
(d) Find expressions and values of A and Ro. Assume that the
bias current sources are ideal.
(e) Find the gain with feedback, Af, and the output resistance
Rout.
(f) How would you modify the circuit to realize a closed-loop
voltage gain of 5 V/V? What is the value of output
resistance obtained?
*11.41 Figure P11.41 shows a series–shunt amplifier in
which the three MOSFETs are sized to operate at VOV =
0.2 V. Let Vt = 0.5 V and VA = 10 V. The current sources
utilize single transistors and thus have output resistances
equal to ro.
(a) Show that the feedback is negative.
(b) Assuming the loop gain to be large, what do you expect
the closed-loop voltage gain Vo/Vs to be approximately?
(c) If Vs has a zero dc component, find the dc voltages at
nodes S1, G2, S3, and G3. Verify that each of the current
sources has the minimum required dc voltage across it for
proper operation.
(d) Find the A circuit. Calculate the gain of each of the three
stages and the overall voltage gain, A.
[Hint: A CS amplifier with a resistance Rs in the source
lead has an effective transconductance gm/(1+gmRs) and
an output resistance ro(1+gmRs).]
(e) Find β.
(f) Find Af = Vo/Vs. By what percentage does this
value differ from the approximate value obtained
in (b)?
(g) Find the output resistance Rout.
D *11.42 This problem deals with the series–shunt feedback
amplifier of Fig. P11.33. Certain aspects of this amplifier
were considered in Problem 11.33. If you have already solved
problem 11.33, you will have the opportunity to compare
results. The current-mirror-loaded differential amplifier has
a feedback network consisting of the voltage divider (R1, R2),
with R1 + R2 = 1 MΩ. The devices are sized to operate at
VOV = 0.2 V. For all devices, VA = 10 V. The input signal
source has a zero dc component.
(a) Show that the feedback is negative.
(b) What do you expect the dc voltage at the gate of Q2 to
be? At the output? (Neglect the Early effect.)
(c) Find the A circuit. Derive an expression for A and find its
value.
(d) Select values for R1 and R2 to obtain a closed-loop voltage
gain Vo/Vs = 5 V/V.
(e) Find the value of Rout.
(f) Utilizing the open-circuit, closed-loop gain (5 V/V) and
the value of Rout found in (e), find the value of gain
obtained when a resistance RL = 10 kΩ is connected to the
output.
(g) As an alternative approach to (f) above, redo the analysis
of the A circuit including RL. Then utilize the values of
R1 and R2 found in (d) to determine β and Af. Compare
the value of Af to that found in (f).
D **11.43 The CMOS op amp in Fig. P11.43(a) is fabricated
in a 1-μm technology for which Vtn = −Vtp = 0.75 V, μnCox =
2μpCox = 100 μA/V2, and VA′ = 10 V/μm. All transistors in
the circuit have L = 1 μm.
(a) It is required to perform a dc bias design of the circuit.
For this purpose, let the two input terminals be at zero
volts dc and neglect channel-length modulation (i.e., let
VA = ∞). Design to obtain ID1 = ID2 = 50 μA, ID5 = 250
μA, and VO = 0, and operate all transistors except for the
source follower Q5 at VOV = 0.25 V. Assume that Q1 and
Q2 are perfectly matched, and similarly for Q3 and Q4.
For each transistor, find ID and W/L.
(b) What is the allowable range of input common-mode
voltage?
(c) Find gm for each of Q1, Q2, and Q5.
(d) For each transistor, calculate ro.
(e) The 100-kΩ potentiometer shown in Fig. 11.43(b)
is connected between the output terminal (Out)
and the inverting input terminal (–In) to provide negative
feedback whose amount is controlled by the setting of
the wiper. A voltage signal Vs is applied between the
noninverting input (+In) and ground. A load resistance
RL = 100 kΩ is connected between the output terminal
and ground. The potentiometer is adjusted to obtain a
closed-loop gain Af ≡ Vo/Vs ≃ 10 V/V.
Specify the required setting of the potentiometer by
giving the values of R1 and R2. Toward this end, find the
A circuit (supply a circuit diagram), the value of A, the β
circuit (supply a circuit diagram), and the value of β.
(f) What is the output resistance of the feedback amplifier,
excluding RL?
D *11.44 Figure P11.32 shows a series–shunt feedback
amplifier without details of the bias circuit.
(a) Eliminating the dc sources, sketch the A circuit and the
circuit for determining β.
(b) Show that if Aβ is large then the closed-loop voltage gain
is given approximately by
Af ≡ Vo/Vs ≃ (RF + RE) / RE
(c) If RE is selected equal to 50 Ω, find RF that will result in
a closed-loop gain of approximately 25 V/V.
(d) If Q1 is biased at 1 mA, Q2 at 2 mA, and Q3 at 5 mA,
and assuming that the transistors have hfe = 100, find
approximate values for RC1 and RC2 to obtain gains from
the stages of the A circuit as follows: a voltage gain of Q1
of about –10 and a voltage gain of Q2 of about –50.
(e) For your design, what is the closed-loop voltage gain
realized?
(f) Calculate the input and output resistances of the
closed-loop amplifier designed.
D *11.45 Figure P11.45 shows a three-stage feedback
amplifier:
A1 has an 82-kΩ differential input resistance, a 20-V/V
open-circuit differential voltage gain, and a 3.2-kΩ output
resistance.
A2 has a 5-kΩ input resistance, a 20-mA/V short-circuit
transconductance, and a 20-kΩ output resistance.
A3 has a 20-kΩ input resistance, unity open-circuit voltage
gain, and a 1-kΩ output resistance.
The feedback amplifier feeds a 1-kΩ load resistance and is
fed by a signal source with a 9-kΩ resistance.
(a) Show that the feedback is negative.
(b) If R1 = 20 kΩ, find the value of R2 that results in a
closed-loop gain Vo/Vs that is ideally 5 V/V.
(c) Supply the small-signal equivalent circuit.
(d) Sketch the A circuit and determine A.
(e) Find β and the amount of feedback.
(f) Find the closed-loop gain Af ≡ Vo/Vs.
(g) Find the feedback amplifier’s input resistance Rin.
(h) Find the feedback amplifier’s output resistance Rout.
(i) If the high-frequency response of the open-loop gain A is
dominated by a pole at 100 Hz, what is the upper 3-dB
frequency of the closed-loop gain?
(j) If for some reason A1 drops to half its nominal value, what
is the percentage change in Af?
Section 11.5: Other Feedback-Amplifier Types
D 11.46 Refer to the circuit in Fig. 11.17(a), which is
analyzed in Example 11.6. Select a value for RF that results in
a closed-loop transconductance Af ≡ Io/Vs ≃ 10 mA/V. Use
the formulas derived in Example 11.6 to find the actual value
of Af realized. Let μ = 1000, Rid = 100 kΩ, gm = 2 mA/V,
and ro2 = 20 kΩ.
D 11.47 Figure P11.47 shows a feedback current amplifier.
The feedback network consists of the highlighted two-port
network comprising RM and RF. It is fed with the output current
Io and delivers a feedback current If at its port 1 to the input
node. The feedback factor β is the current ratio If / Io measured
with port 1 short-circuited (because it is connected in shunt
with the amplifier input).
(a) Find an expression for β and hence for the ideal value
of Af ≡ Io/Is.
(b) Setting Is = 0, break the loop at the gate of Q2 and thus
determine the loop gain Aβ. Show that
A = −gm2 RD / [1+1/(gm1(RM + RF))]
(c) For gm1 = gm2 = 4 mA/V, RD = 10 kΩ, and (RM + RF) =
1 kΩ, find the value of RM that results in a closed-loop
current gain of 5 A/A.
D 11.48 Figure P11.48(a) shows a feedback transresistance
amplifier formed by an op amp and a feedback resistance RF.
Assume that the op amp is modeled by an input resistance Rid,
an open-circuit voltage gain μ, and an output resistance ro.
(a) Show that the feedback factor β, determined as shown
in Fig. P11.48(b), is given by β = −1/RF. Hence find
the ideal value of the closed-loop gain Af ≡ Vo/Is. Find
RF that results in Af of approximately 1 kΩ.
(b) By setting Is = 0 and breaking the loop at the input
terminals of the op amp, show that the loop gain is
given by
Aβ = μ Rid / (Rid + RF + ro)
(c) For μ = 1000, Rid = 100 kΩ, ro = 1 kΩ, and RF having
the value found in (a), what is the actual value of Af
realized?
Feedback Transconductance
Amplifiers (Series–Series)
11.49 A series–series feedback amplifier employs a
transconductance amplifier having a short-circuit transconductance Gm of 0.6 A/V, input resistance of 10 kΩ, and output
resistance of 100 kΩ. The feedback network has β = 200 Ω,
an input resistance (with port 1 open-circuited) of 200 Ω, and
an input resistance (with port 2 open-circuited) of 10 kΩ. The
amplifier operates with a signal source having a resistance
of 10 kΩ and with a load resistance of 10 kΩ. Find Af , Rin,
and Rout.
11.50 Reconsider the circuit in Fig. 11.21(a), analyzed in
Example 11.8, this time with the output voltage taken at the
emitter of Q3. In this case the feedback can be considered
to be of the series–shunt type. Note that RE2 should now be
considered part of the basic amplifier and not of the feedback
network.
(a) Determine β.
(b) Find an approximate value for Af ≡ Ve3/Vs assuming that
the loop gain remains large (a safe assumption, since the
loop in fact does not change).
[Note: If you continue with the feedback analysis, you’ll
find that Aβ in fact changes somewhat; this is a result
of the different approximations made in the feedback
analysis approach.]
(c) If the loop gain remains at the value calculated in Example
11.8 (i.e., 246.3), find the output resistance Rout (measured
between the emitter of Q3 and ground). (Neglect the effect
of ro3.)
D *11.51 Figure P11.31 shows a feedback triple
utilizing MOSFETs. All three MOSFETs are biased and sized
to operate at gm = 4 mA/V. You may neglect their ro’s (except
for the calculation of Rout1 as indicated below).
(a) Considering the feedback amplifier as a transconductance
amplifier with output current Io, find the value of RF
that results in a closed-loop transconductance of approximately 100 mA/V.
(b) Sketch the A circuit and find the value of A ≡ Io/Vi.
(c) Find 1 + Aβ and Af ≡ Io/Vs. Compare to the value of
Af you designed for. What is the percentage difference?
What resistance can you change to make Af exactly
100 mA/V, and in which direction (increase or decrease)?
(d) Assuming that ro3 = 20 kΩ, find Ro of the A circuit. For
this purpose, recall that the resistance looking into the
drain of a MOSFET having a resistance Rs in its source
is (ro + Rs + gmroRs). Hence find the output resistance
Rout1. Since the current sampled by the feedback network
is exactly equal to the output current, you can use the
feedback formula.
(e) If the voltage Vo is taken as the output, in which case
the amplifier becomes series–shunt feedback, what is
the value of the closed-loop voltage gain Vo/Vs? Assume
that RF has the original value you selected in (a). Note
that in this case RS2 should be considered part of the
amplifier and not the feedback network. The feedback
analysis will reveal that Aβ changes somewhat, which
may be puzzling given that the feedback loop did not
change. The change is due to the different approximation
used.
(f) What is the closed-loop output resistance Rout2 of the
voltage amplifier in (e) above?
11.52 Consider the circuit in Fig. P11.52 as a transconductance amplifier with input Vs and output Io. The transistor is
specified in terms of its gm and ro.
(a) Sketch the small-signal equivalent circuit using the
hybrid-π model of the MOSFET and convince yourself
that the feedback circuit is comprised of resistor RF.
(b) Find the A circuit and the β circuit.
(c) Derive expressions for A, β, (1+Aβ), Af , Ro, and Rof .
D 11.53 The transconductance amplifier in Fig. P11.53
utilizes a differential amplifier with gain μ and a very high
input resistance. The differential amplifier drives a transistor
Q characterized by its gm and ro. A resistor RF senses the
output current Io.
(a) For Aβ ≫ 1, find an approximate expression for the
closed-loop transconductance Af ≡ Io/Vs. Hence, select
a value for RF that results in Af ≃ 5 mA/V.
(b) Find the A circuit and derive an expression for A.
Evaluate A for the case μ = 1000 V/V, gm = 2 mA/V,
ro = 20 kΩ, and the value of RF you selected in (a).
(c) Give an expression for Aβ and evaluate its value and that
of 1+Aβ.
(d) Find the closed-loop gain Af and compare to the value
you designed for in (a) above.
(e) Find expressions and values for Ro and Rof . [Hint: The
resistance looking into the drain of a MOSFET with a
resistance Rs in its source is (ro +Rs +gmroRs).]
*11.54 It is required to show that the output resistance of the
BJT circuit in Fig. P11.54 is given by
Ro = ro + (Re || (rπ + Rb))(1 + gmro rπ/(rπ + Rb))
To derive this expression, set Vs = 0, replace the BJT with
its small-signal, hybrid-π model, apply a test voltage Vx to
the collector, and find the current Ix drawn from Vx and hence
Ro as Vx/Ix. Note that the bias arrangement is not shown. For
the case of Rb = 0, find the maximum possible value for Ro.
Note that this theoretical maximum is obtained when Re is so
large that the signal current in the emitter is nearly zero. In
this case, with Vx applied and Vs = 0, what is the current in
the base, in the gmVπ generator, and in ro, all in terms of Ix?
Show these currents on a sketch of the equivalent circuit with
Re set to ∞.
11.55 As we found out in Example 11.8, whenever the
feedback network senses the emitter current of the BJT,
the feedback output resistance formula cannot predict the
output resistance looking into the collector. To understand this
issue more clearly, consider the feedback transconductance
amplifier shown in Fig. P11.55(a). To determine the output
resistance, we set Vs = 0 and apply a test voltage Vx to the
collector, as shown in Fig. P11.55(b). Now, let μ be increased
to the point where the feedback signal across RF almost equals
the input to the positive terminal of the differential amplifier,
now zero. Thus the signal current through RF will be almost
zero. By replacing the BJT with its hybrid-π model, show that
Rout = rπ + (hfe + 1) ro ≃ hfe ro
where hfe is the transistor β. Thus for large amounts of
feedback, Rout is limited to a maximum of hfe ro independent
of the amount of feedback. This phenomenon does not occur
in the MOSFET version of this circuit, where the output
resistance can be theoretically made infinite.
11.56 For the feedback transconductance amplifier of
Fig. P11.56 derive expressions for A, β, Aβ, Af , Ro, and Rof .
Evaluate Af and Rof for the case of gm1 = gm2 = 4 mA/V,
RD = 20 kΩ, ro2 = 20 kΩ, RF = 100 Ω, and RL = 1 kΩ. For
simplicity, neglect ro1 and take ro2 into account only when
calculating output resistances.
D 11.57 For the feedback transconductance amplifier in
Fig. P11.57, derive an approximate expression for the
closed-loop transconductance Af ≡ Io/Vs for the case of Aβ ≫
1. Hence select a value for R2 to obtain Af = 100 mA/V.
If Q is biased to obtain gm = 1 mA/V, specify the value of
the gain μ of the differential amplifier to obtain an amount
of feedback of 60 dB. If Q has ro = 50 kΩ, find the output
resistance Rout. [Hint: Recall that for a MOSFET with a
resistance Rs in its source, the resistance looking into the drain
is (ro +Rs +gmroRs).]
11.58 All the MOS transistors in the feedback
transconductance amplifier (series–series) of Fig. P11.58 are
sized to operate at VOV = 0.2 V. For all transistors, Vt =
0.4 V and VA = 20 V.
(a) If Vs has a zero dc component, find the dc voltage at the
output, at the drain of Q1, and at the drain of Q2.
(b) Find an approximate expression and value for Af ≡
Io/Vs for the case Aβ ≫ 1.
(c) Use feedback analysis to obtain a more precise value
for Af.
(d) Find the value of Rout.
(e) If the voltage at the source of Q5 is taken as the output,
find the voltage gain using the value of Io/Vs obtained in
(c). Also find the output resistance of this series–shunt
voltage amplifier.
11.59 By setting Vs = 0 and breaking the feedback
loop, show that the loop gain of the amplifier circuit in
Fig. P11.58 is
Aβ = gm1,2 (ro2 || ro4) (RF || ro5)/(RF || ro5 + 1/gm5)
where gm1,2 is the gm of each of Q1 and Q2.
Feedback Transresistance
Amplifiers (Shunt–Shunt)
11.60 For the transresistance amplifier analyzed in Example 11.9, use the formulas derived there to evaluate Af , Rin, and
Rout when μ is one-tenth the value used in the example. That is,
evaluate for μ = 10^3 V/V, Rid = ∞, ro = 100 Ω, RF = 10 kΩ,
and Rs = RL = 1 kΩ. Compare to the corresponding values
obtained in Example 11.9.
11.61 Use the formulas derived in Example 11.9 to solve the
problem in Exercise 11.19. Show that the results are identical
to those given in the answer to Exercise 11.19.
11.62 By setting Is = 0, replacing the MOSFET with its
hybrid-π model, and breaking the feedback loop, determine
the loop gain of the feedback amplifier in Fig. E11.19. Hence
find the open-loop gain. Evaluate Aβ, β, A, and Af for
the numerical values given in Exercise 11.8. Why do the
results differ somewhat from those given in the answer to
Exercise 11.19?
11.63 The CE BJT amplifier in Fig. P11.63 employs
shunt–shunt feedback: Feedback resistor RF senses the output
voltage Vo and provides a feedback current to the base
node.
(a) If Vs has a zero dc component, find the dc collector current
of the BJT. Assume the transistor β = 100.
(b) Find the small-signal equivalent circuit of the amplifier
with the signal source represented by its Norton equivalent (as we usually do when the feedback connection at
the input is shunt).
(c) Find the A circuit and determine the value of A, Ri,
and Ro.
(d) Find β and hence Aβ and 1 + Aβ.
(e) Find Af, Rif, and Rof and hence Rin and Rout.
(f) What voltage gain Vo/Vs is realized? How does this value
compare to the ideal value obtained if the loop gain is
very large and thus the signal voltage at the base becomes
almost zero (like what happens in an inverting op-amp
circuit). Note that this single-transistor poor-man’s op
amp is not that bad!
D 11.64 The circuit in Fig. P11.64 utilizes a voltage
amplifier with gain μ in a shunt–shunt feedback topology with
the feedback network composed of resistor RF. In order to be
able to use the feedback equations, you should first convert
the signal source to its Norton representation. You will then
see that all the formulas derived in Example 11.9 apply here
as well.
(a) If the loop gain is very large, what approximate
closed-loop voltage gain Vo/Vs is realized? If Rs = 2 kΩ,
give the value of RF that will result in Vo/Vs ≃ −10 V/V.
(b) If the amplifier μ has a dc gain of 10^3 V/V, an input
resistance Rid = 100 kΩ, and an output resistance ro =
2 kΩ, find the actual Vo/Vs realized. Also find Rin and Rout
(indicated on the circuit diagram). You may use formulas
derived in Example 11.9.
(c) If the amplifier μ has an upper 3-dB frequency of 1 kHz
and a uniform −20-dB/decade gain rolloff, what is the
3-dB frequency of the gain Vo/Vs?
11.65 The feedback transresistance amplifier in Fig. P11.65
utilizes two identical MOSFETs biased by ideal current
sources I = 0.4 mA. The MOSFETs are sized to operate at
VOV = 0.2 V and have Vt = 0.5 V and VA = 16 V. The feedback
resistance RF = 10 kΩ.
(a) If Is has a zero dc component, find the dc voltage at the
input, at the drain of Q1, and at the output.
(b) Find gm and ro of Q1 and Q2.
(c) Provide the A circuit and derive an expression for A in
terms of gm1, ro1, gm2, ro2, and RF.
(d) What is β? Give an expression for the loop gain Aβ and
the amount of feedback (1+Aβ).
(e) Derive an expression for Af.
(f) Derive expressions for Ri, Rin, Ro, and Rout.
(g) Evaluate A, β, Aβ, Af, Ri, Ro, Rin, and Rout for the
component values given.
11.66 By setting Is = 0 and breaking the feedback loop,
find the loop gain of the feedback amplifier in Fig. P11.65.
If you have already solved Problem 11.65, compare results.
Which result do you think is more accurate, and why? For the
numerical values given in Problem 11.65, by how much (in
percent) do the two values of loop gain differ?
11.67 Analyze the circuit in Fig. E11.19 from first principles
(i.e., do not use the feedback approach) and hence show that
Af ≡ Vo/Is = −(Rs||RF)(gm − 1/RF)(ro||RF) / [1 + (Rs||RF)(gm − 1/RF)(ro||RF)/RF]
Comparing this expression to the one given in Exercise 11.19,
part (b), you will note that the only difference is that gm has
been replaced by (gm − 1/RF). Note that −1/RF represents
the forward transmission in the feedback network, which the
feedback-analysis method neglects. What is the condition then
for the feedback-analysis method to be reasonably accurate
for this circuit?
D 11.68 For the feedback amplifier in Fig. P11.68, select
a value for RF that results in a closed-loop gain Af ≡
Vo/Is ≃ −10 kΩ. Then, analyze the circuit to determine
the actual value of Af realized. As well, determine Rin and
Rout. Transistors Q1 and Q2 are operated so that gm1 =
gm2 = 4 mA/V and ro1 and ro2 can be neglected. Also,
RD1 = RD2 = 10 kΩ.
11.69 For the feedback transresistance amplifier in
Fig. P11.69, let VCC = −VEE = 5 V, RC = RE = RF = 10 kΩ.
The transistors have VBE = 0.7 V and β = 100.
(a) If Is has a zero dc component, show that Q1 and Q2
are operating at dc collector currents of approximately
0.35 mA and 0.58 mA, respectively. What is the dc
voltage at the output?
(b) Find the A circuit and the value of A, Ri, and Ro. Neglect
ro1 and ro2.
(c) Find the value of β, the loop gain, and the amount of
feedback.
(d) Find Af ≡ Vo/Is, the input resistance Rin, and the output
resistance Rout.
D **11.70 (a) Show that for the circuit in Fig. P11.70(a),
if the loop gain is large, the voltage gain Vo/Vs is given
approximately by
Vo/Vs ≃ −Rf/Rs
(b) Using three cascaded stages of the type shown in
Fig. P11.70(b) to implement the amplifier μ, design a
feedback amplifier with a voltage gain of approximately
–100 V/V. The amplifier is to operate between a source
resistance Rs = 10 kΩ and a load resistance RL = 1 kΩ.
Calculate the actual value of Vo/Vs realized, the input
resistance (excluding Rs), and the output resistance (excluding
RL). Assume that the BJTs have hfe of 100. [Note: In practice,
the three amplifier stages are not made identical, for stability
reasons.]
D 11.71 Negative feedback is to be used to modify the
characteristics of a particular amplifier for various purposes.
Identify the feedback topology to be used if:
(a) input resistance is to be lowered and output resistance
raised.
(b) both input and output resistances are to be raised.
(c) both input and output resistances are to be lowered.
11.72 The feedback amplifier of Fig. P11.72 consists of a
common-gate amplifier formed by Q1 and RD, and a feedback
circuit formed by the capacitive divider (C1, C2) and the
common-source transistor Qf. Note that the bias circuit for Qf
is not shown. It is required to derive expressions for Af ≡ Vo/Is,
Rin, and Rout. Assume that C1 and C2 are sufficiently small that
their loading effect on the basic amplifier can be neglected.
Also neglect ro. Find the values of Af, Rin, and Rout for the case
in which gm1 = 5 mA/V, RD = 10 kΩ, C1 = 0.9 pF, C2 = 0.1
pF, and gmf = 2 mA/V.
D *11.73 Figure P11.73 shows a shunt–shunt feedback
amplifier. The MOSFETs have Vtn = 0.6 V, VA = 20 V, and
μnCox = 200 μA/V2. The power supply VDD = 3.3 V, and
RL = 2 kΩ. The coupling capacitor CC can be assumed to be
very large.
(a) Perform a dc design to meet the following specifications:
ID1 = 100 μA, ID2 = 1 mA, IR2,R1 = 10 μA, VOV1 =
VOV2 = 0.2 V. Neglect the Early effect. Specify the values
required for I1, R1, R2, (W/L)1, and (W/L)2.
(b) Find an expression for β and hence an expression for the
ideal value of Vo/Vs.
(c) Find the value of Rs that results in Vo/Vs being ideally
−6 V/V.
(d) Find the A circuit and use it to determine the values of A,
Ri, and Ro.
(e) Find the value obtained for Vo/Vs.
(f) Find Rin and Rout.
Feedback Current Amplifiers (Shunt–Series)
11.74 For the feedback current amplifier in Fig. P11.47:
(a) Provide the A circuit and derive expressions for Ri and A.
Neglect ro of both transistors.
(b) Provide the β circuit and an expression for β.
(c) Find an expression for Aβ.
(d) For gm1 = gm2 = 5 mA/V, RD = 20 kΩ, RM = 10 kΩ, and
RF = 90 kΩ, find the values of A, β, Aβ, Af, Ri, and Rif.
(e) If ro2 = 20 kΩ and RL = 1 kΩ, find the output resistance
as seen by RL.
D 11.75 Design the feedback current amplifier of Fig.
11.27(a) to meet the following specifications:
(i) Af ≡ Io/Is = −100 A/A
(ii) amount of feedback ≃ 40 dB
(iii) Rin ≃ 1 kΩ
Specify the values of R1, R2, and μ. Assume that the amplifier
μ has infinite input resistance and that Rs = ∞. For the
MOSFET, gm = 5 mA/V and ro = 20 kΩ. What Rout is
obtained?
11.76 Consider the feedback current amplifier in
Fig. 11.27(a) (which was analyzed in Example 11.10). Let
Rs = Rid = ∞. By setting Is = 0 and breaking the feedback
loop at the gate of Q, find an expression for the loop gain
Aβ. Evaluate Aβ for the component values given in Example
11.10 and hence determine A and Af. Why do the results differ
somewhat from those found in Example 11.10?
11.77 The feedback current amplifier in Fig. P11.77 utilizes
two identical NMOS transistors sized so that at ID = 0.2 mA
they operate at VOV = 0.2 V. Both devices have Vt = 0.5 V
and VA = 10 V.
(a) If Is has zero dc component, show that both Q1 and Q2 are
operating at ID = 0.2 mA. What is the dc voltage at the
input?
(b) Find gm and ro for each of Q1 and Q2.
(c) Find the A circuit and the value of Ri, A, and Ro.
(d) Find the value of β.
(e) Find Aβ and Af.
(f) Find Rin and Rout.
*11.78 The feedback current amplifier in Fig. P11.78(a) can
be thought of as a “super” CG transistor. Note that rather than
connecting the gate of Q2 to signal ground, an amplifier is
placed between source and gate.
(a) If μ is very large, what is the signal voltage at the input
terminal? What is the input resistance? What is the current
gain Io/Is?
(b) For finite μ but assuming that the input resistance of the
amplifier μ is very large, find the A circuit and derive
expressions for A, Ri, and Ro.
(c) What is the value of β?
(d) Find Aβ and Af. If μ is large, what is the value of Af?
(e) Find Rin and Rout assuming the loop gain is large.
(f) The “super” CG transistor can be utilized in the cascode
configuration shown in Fig. P11.78(b), where VG is a dc
bias voltage. Replacing Q1 by its small-signal model, use
the analogy of the resulting circuit to that in Fig. P11.78(a)
to find Io and Rout.
*11.79 Figure P11.79 shows an interesting and very useful
application of feedback to improve the performance of the
current mirror formed by Q1 and Q2. Rather than connecting
the drain of Q1 to the gate, as is the case in simple current
mirrors, an amplifier of gain +μ is connected between the
drain and the gate. Note that the feedback loop does not
include transistor Q2. The feedback loop ensures that the
value of the gate-to-source voltage of Q1 is such that Io1 equals
Is. This regulated Vgs is also applied to Q2. Thus, if W/L of Q2
is n times W/L of Q1, Io2 = nIo1 = nIs. This current tracking,
however, is not regulated by the feedback loop.
(a) Show that the feedback is negative.
(b) If μ is very large and the input resistance of the amplifier
μ is infinite, what dc voltage appears at the drain of Q1?
If Q1 is to operate at an overdrive voltage of 0.2 V, what
is the minimum value that VBIAS must have?
(c) Replacing Q1 by its small-signal model, find an expression for the small-signal input resistance Rin assuming
finite gain but infinite input resistance for the amplifier
μ. Note that here it is much easier to do the analysis
directly than to use the feedback-analysis approach. For
large μ, what does Rin become?
(d) What is the output resistance Rout?
*11.80 The circuit in Fig. P11.80 is an implementation of a
particular circuit building block known as second-generation
current convoyer (CCII). It has three terminals besides
ground: x, y, and z. The heart of the circuit is the feedback
amplifier consisting of the differential amplifier μ and the
complementary source follower (QN, QP). (Note that this
feedback circuit is one we have encountered a number of
times in this chapter, albeit with only one source-follower
transistor.) In the following, assume that the differential
amplifier has a very large gain μ and infinite differential
input resistance. Also, let the two current mirrors have unity
current-transfer ratios.
(a) If a resistance R is connected between y and ground, a
voltage signal Vx is connected between x and ground, and z
is short-circuited to ground. Find the current Iz through the
short circuit. Show how this current is developed and its
path for Vx positive and for Vx negative.
(b) If x is connected to ground, a current source Iy is connected
to input terminal y, and z is connected to ground, what
voltage appears at y and what is the input resistance seen
by Iy? What is the current Iz that flows through the output
short circuit? Also, explain the current flow through the
circuit for Iy positive and for Iy negative.
(c) What is the output resistance at z?
*11.81 For the amplifier circuit in Fig. P11.81, assuming that Vs has a zero dc component, find the dc voltages at
all nodes and the dc emitter currents of Q1 and Q2. Let the
BJTs have β = 100. Use feedback analysis to find Vo/Vs and
Rin. Let VBE = 0.7 V.
**11.82 Figure P11.82 shows a feedback amplifier utilizing
the shunt–series topology. All transistors have β = 100 and
VBE = 0.7 V. Neglect ro except in (f).
(a) Perform a dc analysis to find the dc emitter currents
in Q1 and Q2 and hence determine their small-signal
parameters.
(b) Replacing the BJTs with their hybrid-π models, give the
equivalent circuit of the feedback amplifier.
(c) Give the A circuit and determine A, Ri, and Ro. Note that
Ro is the resistance determined by breaking the emitter
loop of Q2 and measuring the resistance between the
terminals thus created.
(d) Find the β circuit and determine the value of β.
(e) Find Aβ, 1+ Aβ, Af, Rif, and Rof. Note that Rof represents
the resistance that in effect appears in the emitter of Q2
as a result of the feedback.
(f) Determine Rin, Iout/Iin, and Rout. To determine Rout, use
VA2 = 75 V and recall that the maximum possible
output resistance looking into the collector of a BJT
is approximately βro, where β is the BJT’s β (see
Problem 11.55).
Section 11.7: The Stability Problem
11.83 An op amp designed to have a low-frequency gain
of 10^5 and a high-frequency response dominated by a
single pole at 100 rad/s acquires, through a manufacturing
error, a pair of additional poles at 20,000 rad/s. At what
frequency does the total phase shift reach 180°? At this
frequency, for what value of β, assumed to be frequency
independent, does the loop gain reach a value of unity?
What is the corresponding value of closed-loop gain at low
frequencies?
*11.84 For the situation described in Problem 11.83, sketch
Nyquist plots for β = 1.0 and 10−3. (Plot for ω = 0 rad/s, 100
rad/s, 10^3 rad/s, 10^4 rad/s, 2 ×10^4 rad/s, and ∞ rad/s.)
11.85 An op amp having a low-frequency gain of 10^4
and a single-pole rolloff at 10^3 rad/s is connected in a
negative-feedback loop via a feedback network having a
transmission k and a two-pole rolloff at 10^3 rad/s. Find the
value of k above which the closed-loop amplifier becomes
unstable.
11.86 Consider a feedback amplifier for which the open-loop
gain A(s) is given by
A(s) = 10,000 / ((1+s/10^4)(1+s/10^5)^2)
If the feedback factor β is independent of frequency, find the
frequency at which the phase shift is 180°, and find the critical
value of β at which oscillation will commence.
Section 11.8: Effect of Feedback on the
Amplifier Poles
11.87 A dc amplifier having a single-pole response with
pole frequency 10 Hz and unity-gain frequency of 1 MHz
is operated in a loop whose frequency-independent feedback factor is 0.1. Find the low-frequency gain, the 3-dB
frequency, and the unity-gain frequency of the closed-loop
amplifier. By what factor does the pole shift?
11.88 An amplifier has dc open-loop gain of 80 dB and a
single pole with 100-Hz frequency. It is utilized to design a
feedback amplifier with a 3-dB frequency of 10 kHz. What β
is needed? What is the dc closed-loop gain realized? Give an
expression for Af(s).
*11.89 An amplifier having a low-frequency gain of 10^4
and poles at 10^4 Hz and 10^5 Hz is operated in a closed
negative-feedback loop with a frequency-independent β.
(a) For what value of β do the closed-loop poles become
coincident? At what frequency?
(b) What is the low-frequency, closed-loop gain corresponding to the situation in (a)? What is the value of the
closed-loop gain at the frequency of the coincident poles?
(c) What is the value of Q corresponding to the situation in
(a)?
(d) If β is increased by a factor of 10, what are the new pole
locations? What is the corresponding pole Q?
D 11.90 A dc amplifier has an open-loop gain of 1000 and
two poles, a dominant one at 1 kHz and a high-frequency one
whose location can be controlled. It is required to connect
this amplifier in a negative-feedback loop that provides a dc
closed-loop gain of 10 and a maximally flat response. Find
the required value of β and the frequency at which the second
pole should be placed. What is the 3-dB frequency of the
closed-loop amplifier?
11.91 Reconsider Example 11.11 with the circuit in
Fig. 11.34, modified to incorporate a so-called tapered
network, in which the components immediately adjacent to
the amplifier input are raised in impedance to C/10 and 10R.
Find expressions for the resulting pole frequency ω0 and Q
factor. For what value of K do the poles coincide? For what
value of K does the response become maximally flat? For
what value of K does the circuit oscillate?
D 11.92 A feedback amplifier having a dc closed-loop
gain of 10 and a maximally flat second-order response with
a 3-dB frequency of 1 kHz is required. The open-loop
amplifier utilizes a cascade of two identical amplifier stages,
each having a single-pole frequency response. Find the
values required for β, the 3-dB frequency, and the dc gain
of each of the two amplifier stages. Give an expression
for Af(s).
11.93 Three identical inverting amplifier stages, each characterized by a low-frequency gain K and a single-pole
response with f3dB = 100 kHz, are connected in a feedback
loop with β = 1. What is the minimum value of K at
which the circuit oscillates? What would the frequency of
oscillation be?
Section 11.9: Stability Study Using Bode
Plots
11.94 Reconsider Exercise 11.26 for the case of the op amp
wired as a unity-gain buffer. At what frequency is |Aβ| = 1?
What is the corresponding phase margin?
11.95 Reconsider Exercise 11.26 for the case of a manufacturing error introducing a second pole at 10^3 Hz. What is now
the frequency for which |Aβ| = 1? What is the corresponding
phase margin? For what values of β is the phase margin 45°
or more?
11.96 For what phase margin does the gain peaking have a
value of 5%? Of 10%? Of 0.1 dB? Of 1 dB? Of 3 dB? [Hint:
Use the result in Eq. (11.82).]
11.97 An amplifier has a dc gain of 10^4 and poles at 10^5 Hz,
3.16 × 10^5 Hz, and 10^6 Hz. Find the value of β, and the
corresponding closed-loop gain, for which a phase margin
of 45° is obtained.
11.98 A two-pole amplifier for which A0 = 10^3 and having
poles at 1 MHz and 10 MHz is to be connected as a
differentiator. On the basis of the rate-of-closure rule, what is
the smallest differentiator time constant for which operation
is stable? What are the corresponding gain and phase
margins?
11.99 For the amplifier described by Fig. 11.37 and with
frequency-independent feedback, what is the minimum
closed-loop voltage gain that can be obtained for phase
margins of 90° and 45°?
Section 11.10: Frequency Compensation
D 11.100 A multipole amplifier having a first pole at 1 MHz
and a dc open-loop gain of 80 dB is to be compensated for
closed-loop gains as low as unity by the introduction of a
new dominant pole. At what frequency must the new pole be
placed?
D 11.101 For the amplifier described in Problem 11.100,
rather than introducing a new dominant pole we can use
additional capacitance at the circuit node at which the pole
is formed to reduce the frequency of the first pole. If the
frequency of the second pole is 20 MHz and if it remains
unchanged while additional capacitance is introduced as
mentioned, find the frequency to which the first pole must be
lowered so that the resulting amplifier is stable for closed-loop
gains as low as unity. By what factor is the capacitance at the
controlling node increased?
11.102 For the amplifier whose A(s) is depicted in
Fig. 11.38, to what value must the first pole frequency be
lowered to obtain stable performance for (a) β = 0.001 and
(b) β = 0.1?
11.103 Contemplate the effects of pole splitting by considering Eqs. (11.89), (11.93), and (11.94) under the conditions
that R1 ≃ R2 = R, C2 ≃ C1/10 = C, Cf ≫ C, and gm = 100/R,
by calculating ωP1, ωP2, and ωP′1, ωP′2. Comment on the results.
D 11.104 An op amp with open-loop voltage gain of 10^5 and
poles at 10^6 Hz, 10^7 Hz, and 10^8 Hz is to be compensated by
the addition of a fourth dominant pole to operate stably with
unity feedback (β = 1). What is the frequency of the required
dominant pole? The compensation network is to consist of an
RC low-pass network placed in the negative-feedback path
of the op amp. The dc bias conditions are such that a 1-MΩ
resistor can be tolerated in series with each of the negative and
positive input terminals. What capacitor is required between
the negative input and ground to implement the required
fourth pole?
D *11.105 An op amp with an open-loop voltage gain of
80 dB and poles at 10^5 Hz, 10^6 Hz, and 2 × 10^6 Hz is to be
compensated to be stable for unity β. Assume that the op
amp incorporates an amplifier equivalent to that in Fig. 11.40,
with C1 = 150 pF, C2 = 5 pF, and gm = 40 mA/V, and that
fP1 is caused by the input circuit and fP2 by the output circuit
of this amplifier. Find the required value of the compensating
Miller capacitance and the new frequency of the output pole.
**11.106 The op amp in the circuit of Fig. P11.106
has an open-loop gain of 10^5 and a single-pole rolloff with
ω3dB = 10 rad/s.
(a) Sketch a Bode plot for the loop gain.
(b) Find the frequency at which |Aβ| = 1, and find the
corresponding phase margin.
(c) Find the closed-loop transfer function, including its zero
and poles. Sketch a pole-zero plot. Sketch the magnitude
of the transfer function versus frequency, and label the
important parameters on your sketch.
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
    <div class=\"meta\">Sedra — Chapter 11 • Frequency Response</div>
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
    <div class=\"meta\">Sedra — Chapter 11 • Placeholder simulation page</div>
    <div class=\"placeholder\">Add your simulation, visualization, or interactive model here.</div>
  </div>
</body>
</html>
"""

CARD_TEMPLATE = """<article class=\"card\" data-tags=\"circuits-electronics sedra chapter-10 frequency-response\">
  <h3>Sedra — Chapter 11</h3>
  <p>Problem {num}: {title}</p>
  <div class=\"btn-row\">
    <a href=\"./Sedra/Sedra_ch11_prob_{num}.html\">OPEN THEORY</a>
    <a href=\"./Sedra/Sedra_ch11_prob_{num}_sim.html\">OPEN SIM</a>
  </div>
</article>"""

def parse_problems(raw: str):
    pattern = re.compile(r'(?m)^(?:[D*= ]+)?(11\.\d+)\s')
    matches = list(pattern.finditer(raw))
    problems = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        block = raw[start:end].strip()
        first_line = block.splitlines()[0]
        first_line = re.sub(r'^(?:[D*= ]+)?11\.\d+\s*', '', first_line).strip()
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
        title = f"Sedra Chapter 11 — Problem {num}"
        problem_text = html.escape(item["text"])
        theory_html = THEORY_TEMPLATE.replace("{title}", title).replace("{problem_text}", problem_text)
        sim_html = SIM_TEMPLATE.replace("{title}", title)
        theory_name = f"Sedra_ch11_prob_{num}.html"
        sim_name = f"Sedra_ch11_prob_{num}_sim.html"
        write_text(TARGET_DIR / theory_name, theory_html)
        write_text(TARGET_DIR / sim_name, sim_html)
        cards.append(CARD_TEMPLATE.replace("{num}", num).replace("{title}", html.escape(item["title"])))
    cards_html = "\n".join(cards)
    write_text(TARGET_DIR / "Sedra_ch11_cards.html", cards_html)
    print(f"Created {len(problems)} theory files, {len(problems)} sim files, and Sedra_ch11_cards.html in {TARGET_DIR}")

if __name__ == "__main__":
    build()
