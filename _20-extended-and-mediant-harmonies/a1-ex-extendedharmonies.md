---
layout: chapter
title: 20a Lesson - Extended Tertian Harmonies and Non-chord Tones
abc: true
---

To this point in the course, we have only studied harmony based on triads and seventh chords, but as we have shown in the units covering chromaticism, triads and seventh chords function in progressions due to the underlying voice leading in diatonic harmony. If we look at the construction of melodies and their interactions with vertical harmonies, we can find ways to expand the tertian stack to include extensions beyond seventh chords that function as chord tones. 

Let us start by analyzing the following "chorale" arrangement based on the famous tune *The Girl from Ipanema* composed by Antonio Carlos Jobim. Label each chord with leadsheet symbols and Roman numerals, while paying particular attention to labeling all non-chord tones. Note that measure 6 is particularly tricky, but you only need to look back into the previous unit for a way to understand that harmony. For that measure, you may want to consider the melody separately and enharmonically re-spell one pitch of the chorale chord.

{% capture ex1 %}X:1
T:Girl from Ipanema
T:4-part chorale
M:4/4
L:1/4
K:F
Q:1/4=120
V:1
g>e e/2d g/2-| g e/2e/2- e/2e/2 d/2g/2-| g e e d/2g/2-| g/2g/2 e/2e/2- e/2e/2 d/2f/2-|
f/2 d d/2- d/2d/2 c/2e/2-| e/2 c c/2- c/2c/2 B| zc3-| c4|]
V:2
[A4C]-| [A4C]| [G4=B,]-| [G4=B,]|
[G4B,]| [_D4B,]| [A,4C]-| [A,4C]|]
V:3 clef=bass
[F,,4E,]-| [F,,4E,]| [G,,4F,]-| [G,,4F,]|
w:F:
[G,,4F,]| [_G,,4_F,]| [F,,4E,]-| [F,,4E,]|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

How did you deal with the first measure of this tune? It is clearly an Fmaj7 chord, but the melody starts prominently on the ninth of the chord, and that G cannot be labeled as any kind of non-chord tone.

## Extended tertian harmony versus non-chord tones

The first measure of *The Girl from Ipanema* is a perfect example of functional extended harmonies and should help you begin creating a decision tree to determine whether a tone is a non-chord tone or a functional extension. Because the position of the `G` in the measure, it does not fit the standard non-chord tone patterns that we established early in the course. As you look at it further, it should be clear that this G is *functional*--it is critical to the texture and structure of this chord--so we must consider it a chord tone, making this harmony an F<sup>maj9</sup> chord. Measure 3 has a similar issue with the E in the melody over the G7

As we have discussed repeatedly in this course, harmonic analysis is the art of determining which pitches are functional to the harmony and which pitches are embellishment. As we move into an expanded view of tonal harmony, it is imperative that you are extremely familiar with the details of non-chord tones in Unit 9a, because these shapes will provide a foundation to help you begin determining what is functional. Simply put, if you cannot label a pitch as one of the possible non-chord tone shapes, then it is most likely a functioning chord tone. If there are more than four pitches for a given harmony that fall into this category, it means that you must consider the concept of extended tertian harmonies such as ninth chords.

Before you go further, you may wish to refresh yourself on the Roman numeral labeling conventions outlines in Unit 6a. In particular, the section that discusses the terms <sup>add</sup> and <sup>sub</sup> are important to our labeling of extended tertian harmonies.

## Identifying patterns

While most musicians have at least a passing familiarity with extended tertian harmonies in jazz and pop, they exist in all styles of tonal harmony. Analyze the following examples by labeling all chords with Roman numerals, inversion figures, and non-chord tones. After you attempt your analyses, read the commentary below each example.

{% capture ex2 %}X:2
T:Schubert, Deutsch Tanz, D. 420 no. 2
M:3/4
L:1/4
K:A
Q:1/4=150
V:1
c| d f B-| B ^A/2B/2c/2d/2| e a c-| c/2A/2G/2A/2B/2c/2|
d f B-| B ^A/2B/2c/2d/2| c/2e/2A/2c/2B/2G/2| A2:|]
V:2 clef=bass
z| E,[G,DE][G,DE]| E,[G,DE][G,DE]| E,[A,CE][A,CE]| E,[A,CE][A,CE]|
w:A:
E,[G,DE][G,DE]| E,[G,DE][G,DE]| [A,2C] [E,D]| [A,2C]:|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

In this excerpt (D.420 no. 2), the melody in the first measure arpeggiates a B minor triad, but this is superimposed over an obvious E<sup>7</sup> in the left hand. Your first instinct should be to try to treat one of the outer pitches of the possible chord tones as a non-chord tone, either the E (to create a G# diminished seventh chord) or the F# (to leave the E<sup>7</sup>). Both would be functionally sound acting as a dominant function in the key, however, both the E and F# are in prominent positions -- the E is present throughout the measure, and the F# is not only the high point of the measure, but it is approached and left by a leap. Because both pitches are functional and unable to be identified as a non-chord tone, this is an example of a *ninth chord*. 

For our course, we will label the harmony as V<sup>7add9</sup>. There are many systems for labeling extended harmonies using Roman numerals, but this will allow us to continue using our methods for labeling inversions. For example, if this chord had the chordal third in the bass, we could label it as V<sup>6/5add9</sup>. And if this chord did *not* have a chordal seventh at all, we would label it as V<sup>add9</sup>, which denotes a major triad with an added ninth (and no seventh).

{% capture ex3 %}X:3
T:Schubert, Deutsch Tanz, D. 366 no. 4
M:3/4
L:1/4
K:C
Q:1/4=135
V:1
E| ^G2 G/2G/2| A A A| B2 B/2B/2| c c c|
^G2 G/2G/2| A A A/2e/2| e/2d/2 d/2c/2 c/2B/2| A2|]
V:2
E| F/2E/2F/2E/2F/2E/2| E E E| F/2E/2F/2E/2F/2E/2| E E E|
F/2E/2F/2E/2F/2E/2| E E E| F F ^G| A2|]
V:3 clef=bass
z| [B,D] E, [B,D]| [A,C] E, [A,C]| [^G,D] E, [^G,D]| [A,C] E, [A,E]|
w:a:
[B,D] E, [B,D]| [A,C] E, [C,A,]| [D,A,] [D,B,] [E,D]| [A,2C]|]{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

This piece is written for piano, but I separated the right hand into two voices to highlight the possibility of a ninth. You can make many of the same arguments for this excerpt as we did in the first: the ninth above this E<sup>7</sup> in measures 1, 3, and 5 is in a prominent position and present throughout the measure. The difference is its melodic role. This ninth can easily be explained as an accented neighbor tone. You must decide when listening to this piece if you hear this F as functional or embellishing. I hear it as an embellishment rather than a functioning chord tone.

{% capture ex4 %}X:4
T:Schumann, Dichterliebe, op. 48 no. 9
M:3/8
L:1/8
K:F
Q:1/8=90
V:1
z| z3| z3| z3| z z A|
A2 A| d>dd| f3| e2 A| d2 d|]
V:2
G/2A/2| B/2A/2G/2e/2d/2^c/2| d/2a/2g/2f/2e/2d/2| e/2d/2^c/2d/2e/2f/2| e/2^c/2A/2B/2G/2A/2|
B/2A/2G/2e/2d/2^c/2| d/2a/2g/2f/2e/2d/2| e/2d/2^c/2d/2e/2f/2| e/2^c/2A/2c/2d/2e/2| f/2e/2d/2a/2g/2f/2|]
V:3 clef=bass
z| A,,[G,/2B,^CE][G,/2B,CE][G,B,CE]| A,,[A,/2DF][A,/2DF][A,DF]| A,,[^G,/2=B,F][G,/2B,F][G,B,F]| A,,[A,/2^CE][A,/2CE][A,CE]| 
w:d:
A,,[G,/2B,^CE][G,/2B,CE][G,B,CE]| A,,[A,/2DF][A,/2DF][A,DF]| A,,[^G,/2=B,F][G,/2B,F][G,B,F]| A,,[A,/2^CE][A,/2CE][A,CE]| D,,[F,/2A,D][F,/2A,D][F,A,D]|]{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

This final excerpt is similar to the first excerpt in that chord in measures 1 and 5 emphasizes the root of the V chord (the A) by placing it alone in the left hand on the downbeat, but clearly stacks a vii<sup>o7</sup> on the second and third eighth notes of the measure. It would be possible to consider the A as a pedal tone throughout the first eight measures and only analyze this measure as a vii<sup>o7</sup>, but when I listen to it, the A is in too prominent a position and I hear it as defining the function of the chord. Because of this, I would label both of the measures a V<sup>7add9</sup> chords.