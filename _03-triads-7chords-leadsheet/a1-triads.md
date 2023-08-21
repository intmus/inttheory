---
layout: chapter
title: Lesson 3a - Triads
abc: true
---

When discussing key signatures in Unit 2d, we demonstrated that a series of repeating P5 intervals will eventually cycle through all twelve pitch classes. And if we insert a diminished 5th at any point, we can "shortcut" back to six pitches earlier--and in doing so, we create a new looping set of intervals that also happens to be a diatonic collection of seven pitches. 

We can further demonstrate this effect by stacking them on top of each other to create basic harmonies. Listen to the next example which stacks diatonic 5ths--meaning 5ths that only use the pitches in this key--to create a series of perfect 5ths. As you listen, you will probably hear each of these dyads as having an "open" or "undefined" sound. Feel free to experiment using the text entry box below the example to see if you can insert a note into those open 5ths that creates a pleasing sound. 

{% capture ex1 %}X:1
%%staffsep 100%
T:Diatonic 5ths in the Major Scale
M:C
L:1/2
K:C
[CG] [DA]| [EB] [Fc]| [Gd] [Ae]| [Bf] [cg]||
w:P5 P5 P5 P5 P5 P5 d5 P5{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

As you probably noticed, you can create a variety of interesting harmonies, but the ones that felt the most familiar occurred when you placed a pitch in each 5th that divided them equally. And in doing so, you created the basic harmonic structure for all diatonic music: *the triad*.

## Building diatonic triads

All diatonic triads have exactly three unique pitches, although chordal members may be doubled and certain chord members can occasionally be omitted (and therefore implied) depending on the context. We name the chord members by the distance above the bottom pitch **when the chord is stacked in thirds**:
- the lowest pitch is called the *root* of the chord
- the pitch that is a 3rd above the root is called the *chordal third*
- the pitch that is a 5th above the root is called the *chordal fifth*

This can be confusing to beginning theory students, because we refer to intervals, scale degrees, and chordal members using the same ordinal numbers--thirds, fifths, etc.--and most often do not use the word "chordal". As you become more experienced in describing these things, you will be able to discern the meaning from context, but if you would like to avoid confusion for now, you can preface the ordinal number with the word "chordal" until you are comfortable. 

### A note on terminology

As dyads have two pitches, the word "triad" implies *any* collection of three pitches. In diatonic music, however, we use this word to refer to a certain intervallic structure, so until we reach the unit on post-tonal harmony, you may assume that the word "triad" refers to the stacked thirds of diatonic harmony.

## Triad qualities

In the study of the evolution of music, you will find that early harmony focused on perfect intervals similar to this example, but diatonic harmony as we know did not take root until music began regularly using a third chordal member. By stacking two intervals of a third, we create a *triad*, which contains not only the two thirds, but also the interval of a fifth between the outer pitches. Any harmonic system which relies on stacking thirds is called *tertian harmony*.

{% capture ex2 %}X:2
%%staffsep 100%
T:Diatonic triads in the Major Scale
M:C
L:1/2
K:C
[CEG] [DFA]| [EGB] [FAc]| [GBd] [Ace]| [Bdf] [ceg]||
w:M m m M M m d{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

Triads are important to almost all of Western music and form the basic unit in diatonic (key-based) harmony. While our ultimate goal is to describe how triads *function* harmonically, it is important that we are able to identify the structure of triads themselves independent of their diatonic functions, so we will begin by studying their intervallic structure.

Using the next example:
- determine what role each chord member -- root, third, and fifth -- plays in determining the quality of a triad
- find all three intervals contained in a *root-position* triad for each chord quality

{% capture ex3 %}X:3
T:Triad qualities
M:2/4
L:1/2
K:C clef=bass
"Augmented (A)"[_B,,D,^F,]| "Major (M)"[_B,,D,F,]| "Minor (m)"[_B,,_D,F,]| "diminished (d)"[_B,,_D,_F,]||{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

Your first goal should be to come up with a way to define each triad's *quality*. To begin, you may classify triadic qualities by dividing them into two groups based on the defining chord members of the triads.

When looking at a diatonic triad in root position:
- If the chordal fifth is either a diminished or augmented fifth, then the triad is labeled as *diminished* or *augmented* respectively.
    - Diminished triads always have a minor 3rd between the root and chordal third.
    - Augmented triads always have a major 3rd between the root and chordal third.
- If the chordal fifth is a perfect fifth, the chordal third determines whether a triad is *major* or *minor*.
    - Major triads have a M3 above the root.
    - Minor triads have a m3 above the root.

From this, we can create a couple of simple groupings based on the chord members:
- Between root and chordal 3rd
  - Augmented and major triads always have a M3 (or inversion)
  - Minor and diminished triads always have a m3 (or inversion)
- Between root and chordal fifth
  - Major and minor triads always have P5 (or inversion)
  - Diminished triads always have a d5 (or inversion)
  - Augmented triads always have an A5 (or inversion)

Therefore, if a triad is in root position, you can determine triad qualities by the measuring the intervals of the stacked thirds.

- Major: M3 + m3
- Minor: m3 + M3
- Diminished: m3 + m3
- Augmented: M3 + M3

Please note that when looking at the thirds contained in our four standard triads, *only* M3 and m3 intervals are used. By stacking those you can create a d5 or A5, but you will never use a d3 or A3.

## Triad inversions and their labels

Because triads have three pitches, there are three possible configurations that depend on which note of the triad is in the lowest voice. We will call these *inversions*, but they are sometimes referred to as *positions*. The system that we use to label inversions relies on the intervals within the triad.

Using the next example, you should:
- determine the naming conventions of inversions
- know the shorthand method for labeling inversions
- develop a method for determining the chord quality of a triad that is not presented in root position (stacked as two thirds on top of each other.)
- find the rest of the interval *sizes* between chord members of a triad (Hint: This may involve moving some chord members up or down an octave)
    - thirds (2)
    - fourth (1)
    - fifth (1)
    - sixths (2)
- relate these interval sizes to our system for labeling triad inversions
    - provide inversion figures for root position, first-inversion, and second-inversion triads

NOTE: Because ABC notation is not capable of using superscript, the inversion figures in the next example are notated as fractions. If you were to write these by hand or use music notation software, you would notate all inversion figures in superscript as stacked numbers without a dividing line. For example, a major chord in first inversion would be written as M<sup>6</sup>

{% capture ex4 %}X:4
T:Triad inversions
T:1) Inversion names are listed above the staff
T:2) Inversion figures are listed below the staff
T:---------
M:2/4
L:1/2
K:C
"Root-position"[_Bdf]| "First-inversion"[_BDF]| "Second-inversion"[_BdF]||
w:5/3 6~(6/3) 6/4{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

From the simple presentation of the above example, you should have realized that you cannot identify the inversion of the chord until you know the root. The simplest method for finding the root for any triad is to re-arrange the pitches until you have a triad that is stacked using only thirds. To be clear, this means no fourths, no sixths, and everything within a octave. You can even eliminate any duplicate pitches. Once you have this simplified arrangement of pitches, you can easily determine the root and quality of the chord using the method above. 

For inversions, it is not necessary to know each interval within a triad, but instead, you only need to identify the chordal member in the bass.

- Root position: 5/3
  - the root of the chord is in the bass
  - The `5` and `3` refer to the simple intervals above the bass 
- First inversion: 6/3 (shortened to 6)
  - the 3rd of the chord is in the bass
  - The `6` and `3` refer to the simple intervals above the bass
- Second inversion: 6/4
  - the 5th of the chord is in the bass- The `6` and `4` refer to the simple intervals above the bass

Of note, there are six different possible intervals in a triad, depending on the inversion: two thirds, two sixths, one fourth, and one fifth. These intervals always exist between the same two chord members.
- The thirds exist between the root/third and third/fifth.
- The sixths appear when you invert either of the thirds, so between the third/root and fifth/third.
- The fifth always exists between root/fifth.
- The fourth is the inversion of the fifth, so between fifth/root.

### Triad voicings

Now that you understand the basic of triads and their inversions, we have to account for the variety of ways that they appear in music. When analyzing music, you must account for doubled pitches, implied harmonies, and a variety of spacings across the range of the performers; all of which can make it difficult to find the basic structure of the triad when looking at a musical score. 

We will start by dealing with the issue of spacing, and to do so we must understand how the *inversion* interacts with the chord's *voicing*. 

Look at the following example, and compare the closed and open voicings listed there. You should:
- be able to succinctly describe the differences
- create a process to convert any inverted and/or open-voiced triad into a root-position triad in closed voicing

{% capture ex5 %}X:5
T:Triad voicings
M:2/4
L:1/2
K:C
V:1
"Closed"z| "Closed"[_BF]| "Open"[_Bf]| "Open"[fdF]|
V:2 clef=bass
[_B,,D,F,_B,]| [D]| [_B,,D]| [F,_B,]|{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

### Conclusions

As students develop the process for finding any inversion, they usually work through the following ideas:
- Attempt #1: Open voicing is spread out.
  - True, but this is a subjective measure. What constitutes "spread out"?
- Attempt #2: Closed voicings use only simple intervals and open positions have compound intervals.
  - This is interesting in that it works if the chord only has no repeated pitches, but does not hold up if a chord has repeated notes or more than four distinct pitches.
- Attempt #3: - Closed voicings contain all chord members within one octave. 
    - This is almost there , but does not explain how a chord with more than four pitches can be in closed position.
- Attempt #4: Open voicing skips one of the voices.
  - This definition is also very close, but the term "voices" is problematic because "voices" is used ambiguously and does not relate directly to a chord.

A complete definition combines these ideas.
- Closed voicing stacks all pitches of a chord in an ascending order and does not skip a chordal member.
- Open voicings can have chord members stacked in any order and skip chord members. 
    - All open voicings will cover more than one octave because of this.

### *Root* versus *bass*

Understanding the difference between the terms *root* and *bass* is the last piece of information necessary to find the quality of any chord; students often confuse the two. The term *bass* **always** refers to the lowest voice of any chord. The *root* is the lowest member of the chord **if the chord is in root position**, meaning that the triad is stacked as two thirds. If a chord is in root position, the *root* and *bass* will be the same pitch, however if a triad is in first or second inversion, the *root* and *bass* will be different pitches.

### Finding a chord quality while inverted

Combining a knowledge of inversions and voicings is critical in correctly identifying chord qualities. Teachers often suggest to students that they can find chord qualities by putting a chord in root position, but a chord in root position can be spread across multiple staves and still difficult to parse. We really mean that they should put the chord in root position *and* closed voicing. This allows the student to look at the interval qualities and determine the quality of the triad based on their knowledge of triadic interval structures.

I also suggest that you look at the method for identifying triads from the *Open Music Theory*. You can find this listed under the [Further Reading]({{ site.baseurl }}/03-triads-7chords-leadsheet//a2-triads.html) for this topic.
