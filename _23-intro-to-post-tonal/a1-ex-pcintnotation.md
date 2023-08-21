---
layout: chapter
title: 23a Lesson - Pitch-class integer notation
abc: true
---

Look at the following example. In both cases, the starting interval contains enharmonically equivalent pitches of a tri-tone. In the first measure it is notated as an A4, but in the second measure, it is notated as a d5. What harmony do you think is implied in these two measures? How does the choice of using D-flat or C-sharp change the resolution in a tonal context?

{% capture ex1 %}X:1
T:The importance of pitch notation in tonal harmony
M:2/2
L:1/2
K:C
V:1
Q:1/4=50
^C D|| z2|| _D C|]
V:2 clef=bass
G,^F,|| z2||G, _A,|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

In a tonal context, there is an important difference between enharmonically equivalent pitches such as D-flat and C-sharp. In the example above, the A4 between G and C-sharp implies the outward resolution of a V<sup>4/2</sup> to I<sup>6</sup> in the key of D major. In the second progression, changing the C-sharp to a D-flat creates a d5 that implies an inward resolution of a V<sup>6/5</sup> to I in the key of A-flat major. Clearly, the pitch notation system we use is designed to show harmonic movement in a tonal setting.

## Leaving tonality

As we move toward music that no longer relies on tonal harmony, the tools with which we notate analysis reflect the lack of a traditional tonal center. If a piece does not rely on the tonic and dominant relationship to provide tension and release, the importance of Roman numerals, scale degrees, and even pitch names becomes less useful. They are derived from a system that prioritizes seven pitches at a given time, so without that requirement, we need a method for demonstrating the relationships between all twelve chromatic pitches. 

Look at the following ornamented melody. The numbers below the staff denote the *pitch class* for each pitch. (Note that `t` = 10, `e` = 11) Each number is considered a *pitch class* (abbrev.: pc), and the system itself is called *pitch-class (pc) integer notation*. After studying this example, what can you determine about the pitch classes? How do you determine which pitches are in a pitch-class? Is this numbering built around a key center or just a particular pitch? While it should be obvious that this system would not be ideal for analyzing tonic and dominant centers, what kinds of information *does* this system demonstrate?

{% capture ex2 %}X:2
T:Happy Birthday in G major (a la R. Strauss)
M:3/4
L:1/4
Q:1/4=75
K:G
D/2>^D/2| E/2_E/2 D G/2^E/2| F2 (3D/2^C/2D/2| E D A/2^F/2| G2 D/2>D/2|
w:2 3 4 3 2 7 5 6 2 1 2 4 2 9 6 7 2 2
d/2_d/4c/4 B/2_B/4A/4 G| F/2=F/2 HE c/2>c/2| (3B/2^A/2B/2 G/2^G/2 =A/2_A/2| G2|]
w:2 1 0 e t 9 7 6 5 4 0 0 e t e 7 8 9 8 7{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusion

As you can see, pitch-class integer notation assigns a unique integer to all enharmonically equivalent pitches. This particular example is labeled in *fixed zero*, meaning that C=0, and every pitch is counted as half-steps from that point. This system is wonderful for showing intervals quickly, because each number is actually counting the number of half-steps away from zero. For fixed zero, D is two half steps away from zero, A is nine half steps away, and so on. Therefore, when you look at the numbers, you know that if the difference between two numbers is small, it is a small interval. Large distances equate to large intervals.

Look at the following chart for the pitch class of every pitch in fixed-zero pc integer notation. Note that this chart does not include double-sharps or double-flats, but *any pitch* can be included along with its enharmonic equivalents.

Pitch-class integer | Pitch 1 | Pitch 2
 --- | --- | ---
 0 | C | B-sharp
 1 | C-sharp | D-flat
 2 | D | --
 3 | D-sharp | E-flat
 4 | E | F-flat
 5 | F | E-sharp
 6 | F-sharp | G-flat
 7 | G | --
 8 | G-sharp | A-flat
 9 | A | --
 t (10) | A-sharp | B-flat
 e (11) | B | C-flat

## Movable-zero pc integer notation

Much like solfege, there is another system for labeling pitches in pc integer notation. Look at the following scales taken from Unit 21. Each scale is labeled using pc integer notation, but C no longer equals 0. First, figure out what scale is represented on each line, and then look at how the numbering system is adjusted. How are the numbers determined? What does having a *movable zero* demonstrate?

{% capture ex3 %}X:3
T:Scales labeled using movable-zero pc integer notation
M:4/4
L:1/4
Q:1/4=75
K:C
D E ^F G| A B ^c d|]
w:0 2 4 5 7 9 e 0
E ^F G A| B ^c d e|]
w:0 2 3 5 7 9 t 0
F _G ^G A| B c d _e| f|]
w:0 1 3 4 6 7 9 t 0{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

You can see that using movable-zero pc integer notation allows you to set 0 to the most important pitch for a given set of pitches, and then base every number around that pitch. In the first example, the D major scale labels D as the central pitch and then counts the half-steps away from that D. The second line assigns E as 0 to show the intervallic structure of the E dorian mode, and the last line assigns F as 0 to show the intervallic structure of an F HW octatonic scale. 

This does make it easy to see the intervals within each scale, but to be honest, standard interval labels (e.g. M2 and m3) do a similar job while also implying context. Movable-zero notation is actually best used for looking for patterns within subsets of pitches. Look at the next example which uses the exact same three scales, but instead of having only one zero, it assigns 0 to multiple pitches within the same scale. What patterns do you see emerge? Can you think of other ways to potentially use this?

{% capture ex4 %}X:4
T:Scales labeled using multiple zeros in pc integer notation
M:4/4
L:1/4
Q:1/4=75
K:C
D E ^F G| A B ^c d|]
w:0 2 4 5 0 2 4 5
E ^F G A| B ^c d e|]
w:0 2 3 5 0 2 3 5
F _G ^G A| B c d _e| f|]
w:0 1 3 4 0 1 3 4 0{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

By using movable zero to highlight certain collections of pitch classes, you can show intervallic patterns within these collections. For a major scale, there are two (0245) collections separated by a whole step. For a Dorian mode, there are two (0235) collections separated by a whole step. And for a HW octatonic scale, there are two (0134) collections separated by a whole step. What scale would two (0235) collections separated by a half-step create?

Any time we have a collections of pitch classes, this is called a *pitch-class set* (abbrev: pcs). A pitch-class set can be any number of pitches, and we call the number of pitches within a pcs its *cardinality*. Each cardinality has a special name shown in the chart below.

Number of pitch classes in the pitch-class set | Name
 --- | ---
 0 | empty set
 1 | monad
 2 | dyad
 3 | triad
 4 | tetrachord
 5 | pentachord
 6 | hexachord
 7 | septachord
 8 | octachord
 9 | nonachord
 10 | decachord
 11 | undecachord
 12 | aggregate

In the second scale example above, we used pc integer notation to show specific tetrachords within common scales. [0245] is often called the "major" tetrachord, [0235] is often called the "minor" tetrachord, and[0134] is often called the "diminished" or "octatonic" tetrachord. What tetrachord do you think is most associated with the whole-tone scale? What other scales make use of these tetrachords?

## Introduction to set theory

Pitch-class integer notation is really the beginning of *set theory*, a system that was first laid out by Allen Forte in *The Structure of Atonal Music*, and since been refined by many other theorists. Notably, Joseph Straus created a wonderful teaching method for set theory in his *Introduction to Post-Tonal Theory*. Both are amazing references and if you need to explore the topic further, I recommend that you start with these after reading through the set theory overview of Unit 22.