---
layout: chapter
title: Lesson 2c - Identifying and Labeling Intervals
abc: true
---

To this point, we have discussed formal labeling systems for a single pitch, as well as how we can combine these pitches by whole and half steps to create scales. Our next step up the ladder of complexity will be develop a method to measure the distance between any two pitches, and we do this in Western music notation by looking at the distance between two pitches changes in function when in a scale. 

## Intervals

Any two-note combination is called a *dyad*, and the distance between the two pitches of a dyad is an *interval*. Intervals are the fundamental building blocks of melody and harmony. At their simplest, intervals need only measure the distance between two pitches, but there are many variables in music for which we must account.

### Goals for this topic

In the example below, each interval represents the concept stated at the beginning of its staff, but each measure *also* has an important intervallic relationship to the measures directly above and below it as labeled by the word in front of each row (staff line). Using these relationships and labels, develop explanations for how we find each of the following:
- the *size* of the interval between two pitches as represented by the Arabic numeral
- the *quality* of the interval as represented by the labels *perfect, major, minor, diminished, and augmented*
- which *sizes* can use which *qualities*
- the hierarchy of *qualities* for each *size*
- *chromatic* versus *diatonic* intervals
- *simple* versus *compound* intervals and how this affects classifying of *quality* and *size*
- how the *size* and *quality* change when the upper and lower pitches of an interval are inverted

### Important concepts

- _**Qualities**_: P = perfect, M = major, m = minor, A = augmented, d = diminished
- _**Diatonic vs Chromatic**_
  - All intervals in the examples below that are followed by a "d" in parentheses are diatonic intervals in the key of C major.
    - Note: We do not normally label diatonic intervals with a parenthetical "d". This label is solely for this exercise.
- **Inversions**
  - The bottom row of intervals are the inversions of each interval in the top row. For example, the M7 in the bottom row is the inversion of the m2 above it in the first row. 


{% capture ex1 %}X:1
T:Intervals
M:1/4
L:1/4
K:C
V:1 name=Harmonic
[AA]| [_BA]| [ce]| [_e_B]| [D_A]| [^dF]| [CB]| [^f^F]||
w: P1(d) m2 M3(d) P4 d5 A6 M7(d) P8
V:2 name=Melodic
B/2_B/2| B/2A/2| c/2^e/2| e/2_B/2| _D/2_A/2| F/2_d/2| ^C/2B/2| f/2^F/2||
w:A1 _ M2(d) _ A3 _ A4 _ P5 _ m6 _ m7 _ d8 
V:3 name=Simple
[CC]| [_B^A]| [^c_e]| [_eB]| D/2^A/2| d/2F/2| [C__B]| [^fF]||
w: P1(d) d2 d3 d4 A5 _ M6(d) _ d7 A8
V:4 name=Compound clef=bass
[D,_D]| [^B,A,,]| [C,_E]| [_E_B,,]| _A,/2_D,,/2| F,,/2_D/2| ^B,/2C,,/2| [FF,,]||
w:d8 A9 m10(d) P11 P12 _ m13 _ A14 _ P15(d)||
V:5 name=Inversions
[Aa]| [_B,A]| [cE]| [_E_B]| [d_A]| [^df]| [Bc]| [^f^f]||
w: P8 M7 m6(d) P5 A4 d3 m2 P1{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Conclusions

Our goal when measuring intervals is intrinsically tied to the tonal system that we use, diatonic harmony. The simplest way to measure the distance between two intervals would be to measure the distance by counting the number of the shortest possible intervals--in this case, a half-step (minor second)--between two pitches. While easily understandable, this method does not relate to our concept of tonality. Instead, counting half-steps creates *interval-classes* in which intervals are considered equal regardless of the pitches. For example, the interval of `G` to `D-flat` has six half-steps which is identical to the interval from `G` to `C-sharp`. Both even use the same pitch-classes, however, if you put those into the context of the scales from the previous unit, you will hopefully associate these two intervals with different key centers. (`G` to `D-flat` is strongly associated with the key of A-flat major/minor, whereas `C-sharp` to `G` likely implies D major/minor.) The context of these two intervals is critical in determining their function in tonal harmony, so we use a system that differentiates between the two.

In a diatonic labeling system, every interval has a *size* and a *quality*. For example, in a minor second, labeled `m2`, the **m** indicates the *quality* of the interval and the **2** indicates the *size* of the interval. Let's look at how we find *size* first.

### Interval size

Interval *size* can be determined by considering either:
- lines and spaces
- letter names

Both these methods will correctly identify interval size, although counting letter names yields results without requiring the presence (or visualization) of a staff. Do not forget that you must include both letters when counting. (e.g. The ascending interval from A to C is a third, because you must count A (1), B (2), and C (3).)

This means that any interval that has the same two letters, regardless of accidentals or key signatures, will always have the same *size*. Using our previous example, the *size* of the interval between `G` and `D-flat` is a fifth: G (1), A (2), B (3), C (4), and D (5). We can change the bottom note to any other `G` (`G-sharp, G-flat`, etc.) and the top note to any other `D` (`D-sharp, D-natural`, etc.), but the *size* of that interval will **always** be a fifth. Yet if we exchange the `D-flat` for its enharmonic equivalent, `C-sharp`, we alter the letters and turn the *size* of the interval into a fourth.

### Interval quality

In the Western music notation system, interval *quality* is difficult to examine without beginning to think about our concept of tonality and keys, because it is designed to describe tonal intervals. It is easiest to understand *qualities* of intervals by comparing them to the major scale, so we will look at that below. If you do not yet feel comfortable with scales, however, you may look at the [Further Reading]({{ site.baseurl }}/02-int-scales-keys/a2-intervals.html) of this topic to find a useful method from the writers of *Open Music Theory*.

The most common and straightforward method for learning interval *quality* compares the interval to a major scale:

1. Find the size of the interval by counting through the letter between the two pitches. 
  - Remember that you must include the starting and ending pitches in your counting.
  - Remember that size is independent of quality, so none of the following steps will affect the interval size.
1. To being finding the quality of the interval, consider the bottom pitch of the interval as the tonic of a major scale.
1. If the top pitch of the interval is a note that naturally exists in the major scale built off the lower pitch, it is either a major or perfect interval, depending on the *size* of the interval.
  - Unisons, fourths, fifths, and octaves occur naturally in the major scale as *perfect* intervals.
  - Seconds, thirds, sixths, and sevenths occur naturally in the major scale as *major* intervals.
1. Any alteration from the basic major and perfect intervals can then be labeled by looking at the direction of alteration and the number of half-steps that the interval was altered.
  - If the original interval is *perfect*:
    - Raising the interval by a half-step creates an *augmented* interval.
    - Lowering the interval by a half-step creates a *diminished* interval.
  - If the original interval is *major*:
    - Raising the interval by a half-step creates an *augmented* interval.
    - Lowering the interval by a half-step creates a *minor* interval.
    - Lowering the interval by a 2 half-steps creates a *diminished* interval.

#### Quality hierarchies

From this, our interval can be grouped into two distinct hierarchies:
- The "Perfect" intervals - Interval *sizes* of 1, 4, 5, and 8 can only have the *qualities* of perfect (P), augmented (A), or diminished (d).
- The "Major/minor" intervals - Interval *sizes* of 2, 3, 6, and 7 can only have the *qualities* of major (M), minor (m), augmented (A), or diminished (d).

Note that even though *perfect* intervals use a different hierarchy than *major/minor* intervals, both hierarchies share the terms *diminished* and *augmented*. 

#### Interval quality practice

Let's practice some examples using this method:
- `C` to `E`:
  - Counting the letter names confirms that the *size* is a third - C (1), D (2), E (3)
  - If we consider the lower pitch, `C`, as the tonic of a major scale, we can use the C-major scale to find that the naturally occurring `E` in the key of C major is `E-natural`.
  - Because this is an interval size of a third, we must use the *major* hierarchy, so therefore, `E-natural` would be a **major third *(M3)** above C.
- `D` to `G-sharp`
  - Counting the letter names confirms that the *size* is a fourth - D (1), E (2), F (3), G (4)
  - By setting the lower pitch, `D`, as a tonic, we can use the D-major scale to find that the naturally occurring `G` in the key of D major is `G-natural`. Therefore, `G-natural` is a perfect 4th above D, because all naturally occurring intervals in a major scale are either perfect or major depending on their size.
    - Because `G-sharp` is one half-step above the *perfect* interval, we go one step up the "perfect" hierarchy to find that this interval is an **augmented fourth (A4)**.
- `F` to `E-double-flat`
  - Counting the letter names confirms that the *size* is a seventh (F, G, A, B C, D, E = 7)
  - By using the lower pitch, `F`, as `do`, we can use the F-major scale to find that the naturally occurring `E` in the key of F major is `E-natural`.
  - Because this is a seventh, we must use the *major* hierarchy, so therefore, `E-natural` would be a M7 above F.
  - Because `E-double-flat` is two half-steps below the *major* interval, we go two steps down the major hierarchy to find that this interval is an **diminished seventh (d7)**.


### Melodic vs. Harmonic

Melodic and harmonic intervals are one of the simplest concepts to understand, although the describing them can be problematic. At first, students often describe harmonic intervals as occurring "at the same time" while melodic intervals occur "at different times". While this is a simple explanation, we must be careful in how we apply the terms *interval* and *pitches*. The interval is the space between the two pitches, therefore, the interval cannot occur "at the same time" or "at different times". The pitches can occur simultaneously or consecutively, but the interval always exists as a fixed measurement. This is how we can label harmonic and melodic intervals using the same system.

I recommend that we think of intervals as existing on either a horizontal or vertical axis, because we can visualize axes (as in the plural of axis) easily on musical staff notation. If two pitches occur "at the same time", they will be aligned vertically on a staff. If two pitches occur consecutively, they will represent unique points on a horizontal line that runs parallel to the lines of the staff. This may seem overly technical, but it is an important distinction.

A final note: melodic intervals can have two modifiers attached to them, *ascending* or *descending*. Ascending intervals start with the lower of the two pitches, whereas descending intervals start on the the higher pitch. Harmonic intervals cannot be ascending or descending.
 
### Simple vs. Compound

Simple intervals include any interval that is equal to or smaller than an octave. Compound intervals are any interval larger than an octave.

To label compound intervals, we count letter names as we do for simple intervals. We can find a compound interval by adding 7 to any simple interval. For example, a 2nd becomes a 9th. A 4th becomes an 11th. An 8ve (octave) becomes a 15th.

Conversely, if we see a compound interval, we can find its simple equivalent by subtracting 7. A 12th is a 5th plus an octave. A 10th is a 3rd plus an octave.

You may ask why we don't add eight considering that we are adding an octave. The answer lies in how we find the *size* of intervals. When we find interval *size*, we count the letter names *and include the starting pitch*. When we add an octave, we have already used the top note so we are missing one letter. For example, a fifth from A to E includes the letters `A B C D E`. If we add an octave, the first `E` was already included in the first interval of the 5th, so we are only adding seven letters `F G A B C D E`.

### Chromatic vs. Diatonic

The difference between chromatic and diatonic is probably the most straightforward of interval classifications in usage, but it has a level of nuance that students often miss and causes confusion later. Simply put, *diatonic* intervals contain only pitches that belong to the **current** tonality, whereas *chromatic* intervals contain at least one pitch that does not belong to the current tonality. 

Of course, this relies on you knowing what the current tonality is. In many situations, this means that you can find chromatic pitches, and therefore chromatic interals, wherever you find a note with an accidental. So if the key signature matches the current tonality--for example, the key signature has two sharps and the tonality is D major--any pitch that does not have an accidental is a *chromatic* pitch and all intervals formed with that pitch would be chromatic intervals.

### Inversions

An easy way to think of inverted intervals is to consider an inversion to be an interval in which one pitch is fixed and the other is transposed by one octave toward the fixed pitch.

#### Inverting size

To determine the *size* of an inverted interval, it is easiest to simply memorize the interval pairs, so:
- 4 inverts to 5 and vice versa
- 3 inverts to 6 and vice versa
- 2 inverts to 7 and vice versa
- 1 inverts to 8 and vice versa

Each of these pairs adds up to nine, so if you ever forget or doubt your memorization, you can find an inversion by simply subtracting the interval size from 9. For example, if there is a written 3rd, subtract 3 from 9 to find that the inversion of a 3rd is a 6th. Note that for compound intervals, you must use subtract from 16 or use negative numbers and absolute values. Because of this, it is easier to reduce compound intervals to a simple interval before inverting.

#### Inverting quality

To find the qualities of inverted intervals, you simply need to memorize three pairs:
- diminished becomes augmented and vice versa
- major becomes minor and vice versa
- perfect becomes perfect and vice versa

We will explore the mathematical underpinnings of why inversions form these pairs in Unit 23.
