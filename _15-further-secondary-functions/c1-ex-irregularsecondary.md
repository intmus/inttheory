---
layout: chapter
title: 15c Lesson - Irregular Usage of Secondary Chords
abc: true
---

## Voice-leading exceptions for secondary dominants

In Unit 17, we will discuss how repeated patterns and sequences in voice-leading can override standard voice-leading practices. We can preview one such example by looking at seventh chords that require "incorrectly" resolved chordal thirds and sevenths. To demonstrate this, harmonize the excerpt below paying attention to the chordal resolutions between the ii<sup>7</sup> and V<sup>4/3</sup> chords. Which voices must use non-standard resolutions to accommodate the progression?

{% capture ex1 %}X:1
T:Harmonizing consecutive seventh chords
M:4/4
L:1/2
K:C
V:1
[c] [B]| [c2]|]
V:2 clef=bass
[D,] [D,]| [C,2]|]
w:C:ii7 V4/3 I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusion

In order to use complete chords, the chordal third of the ii<sup>7</sup> chord must remain static to become the chordal seventh of the V<sup>7</sup>:

{% capture ex5 %}X:5
T:Harmonizing consecutive seventh chords
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[cF] [BF]| [c2E]|]
V:2 clef=bass
[D,A,] [D,G,]| [C,2G,]|]
w:C:ii7 V4/3 I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}


## Secondary dominant chord cycles

Because secondary dominant chords are so closely related to diatonic circle-of-fifths progressions, you may apply the same principle to repeated series of secondary dominant seventh chords. Try the same voice-leading on the following example. What changes? How does this affect accidentals within the bar.

{% capture ex2 %}X:2
T:Harmonizing consecutive seventh chords
T:with a secondary dominant chord
M:4/4
L:1/2
K:C
V:1
[c] [B]| [c2]|]
V:2 clef=bass
[D,] [D,]| [C,2]|]
w:C:V7/V V4/3 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusion

You may keep the same resolutions that you used in the diatonic example above--the chordal third of the first chord becomes the chordal seventh of the following chord. The static motion in the alto voice is altered though, because you must resolve down by half-step now that the chordal third has been raised.

{% capture ex6 %}X:6
T:Harmonizing consecutive seventh chords
T:with a secondary dominant chord
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[c^F] [B=F]| [c2E]|]
V:2 clef=bass
[D,A,] [D,G,]| [C,2G,]|]
w:C:V7/V V4/3 I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

## Series of secondary dominants

Unsurprisingly, this concept can be extended to encompass the entirety of the diatonic circle-of-fifths progression. Begin by harmonizing the following standard progression.

{% capture ex3 %}X:3
T:Consecutive secondary dominant chords
M:4/4
L:1/2
K:C
V:1
[cE] [c]| [d] [d]| [c2]|]
V:2 clef=bass
[C,G,] [A,,]| [D,] [G,,]| [C,2]|]
w:C:I vi7 ii7 V7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

This progression is nearly identical to the progression we used in Unit 14 to introduce secondary dominant chords by altering the ii chord. We then altered the vi chord from the same progression in Unit 15a in order to demonstrate tonicization of chords other than V. Because the voice-leading is so similar, secondary dominant functions can lead into *each other* creating series of secondary dominant chords. In the example above, alter your voicing of the ii7 chord to create a V7/V chord and alter the vi7 chord to create a V7/ii creating a progression of:

I - V7/ii - V7/V - V7 - I

### Conclusions

This progression now simply extends your seventh chord resolutions from the examples above, although the fixed soprano line forces you to use an incomplete chord on your V7/ii.

{% capture ex7 %}X:7
T:Consecutive secondary dominant chords
M:4/4
L:1/2
Q:1/4=80
K:C
V:1
[cE] [^cG]| [d^F] [d=F]| [c2E]|]
V:2 clef=bass
[C,G,] [A,,A,]| [D,C] [G,,B,]| [C,2C]|]
w:C:I V7/ii V7/V V7 I{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

Therefore, secondary dominant chords can be substituted freely within a circle-of-fifths progression.

## Deceptive resolutions of secondary dominant functions

There is a less common resolution of secondary dominant chords that relies on the voice-leading from a deceptive cadence. Analyze the following example, and you will notice that at first glance, the progression does not follow our established progressions between the second and third chords. To understand this, you must think in the *tonicized* key. What key would this chromatic chord *normally* tonicize? If you were in that key, how would label the progression between these two chords? It is helpful to use leadsheet symbols here.

{% capture ex4 %}X:4
T:Deceptive resolutions of secondary dominant functions
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[cE] [BD]| [AC] [GD]| [G2C]|]
V:2 clef=bass
[C,G,] [E,^G,]| [F,A,] [B,F,]| [C2E,]|]
w:C:I V7/vi IV V4/2 I6{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

In this progression, the E7 chord is likely to function as the dominant in the key of A major/minor. But instead of resolving to an A minor chord--the diatonic vi of the current key of C major--it resolves to an F major triad. At first this seems nonsensical, but if you thinkn of the tonicization in the key of A minor, you will realize that this is a common progression in that key--a deceptive progression of V7 to VI. This also neatly explains why the F major chord has a double chordal third, the standard doubling in a deceptive progression for the VI chord. In labeling this in our secondary key, you do not need to label anything further, but feel free to use the abbreviation of "dec" in parentheses between the two chords if you would like to make a note of this uncommon use of secondary dominants.

In short, if you find a root-position secondary dominant chord that does not resolve to its normally tonicized chord, check to see if it instead resolves to a diatonic chord with a root that is a step (M2/m2) above the root of the secondary dominant. If so, this is a deceptive resolution in a secondary key, so you should still label the secondary dominant in the secondary key.

Remember that all deceptive progressions create difficult voice leading in four-part harmony, particularly if both chords are triads. Please refer to the voice-leading guidelines for this progression in Unit 11 if you would like to review.
