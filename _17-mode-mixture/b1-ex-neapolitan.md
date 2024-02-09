---
layout: chapter
title: 17b Lesson - bII chords (Neapolitan)
abc: true
---

Analyze and listen to the following short progressions. There are three progressions in major and then three similar progressions in the parallel minor. Start your analysis with leadsheet symbols and then provide Roman numerals. (You may want to refer back to Unit 17a to review the finer points of using the Roman numeral system.) In each progression below, there is a chromatic chord that will stand out. What is its function in each case? (e.g. tonic, passing, etc.) If you were to compare it to a diatonic or chromatic chord that normally fulfills this function, which chord shares the most commonalities with it? (Hint: Think about the inversion and choice of doubled notes.) Does it seem most "at home" in major or minor?

{% capture ex1 %}X:1
T:Standard progressions in major using the bII
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[cE] [cE]| [_dF] [BF]| [c2E]|]
[cE] [cE]| [_dF] [c/2E][B/2F]| [c2E]|]
[cE] [_dF]| [c_E] [BD]| [c2E]|]
V:2 clef=bass
[K:C] [C,G,] [A,,A,]| [F,,_A,] [G,,G,]| [G,2C,2]|]
w:C:
[C,G,] [A,,A,]| [F,,_A,] [G,,/2G,][G,,/2G,]| [G,2C,2]|]
w:C:
[C,G,] [F,,^G,]| [^F,,A,] [G,,G,]| [G,2C,2]|]
w:C:{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

{% capture ex2 %}X:2
T:Standard progressions in minor using the bII
M:4/4
L:1/2
Q:1/4=90
K:Eb
V:1
[cE] [cE]| [_dF] [=BF]| [c2E]|]
[cE] [cE]| [_dF] [c/2E][=B/2F]| [c2E]|]
[cE] [_dF]| [cE] [=BD]| [c2E]|]
V:2 clef=bass
[C,G,] [A,,A,]| [F,,A,] [G,,G,]| [G,2C,2]|]
w:c:
[C,G,] [A,,A,]| [F,,A,] [G,,/2G,][G,,/2G,]| [G,2C,2]|]
w:c:
[C,G,] [F,,^G,]| [^F,,=A,] [G,,G,]| [G,2C,2]|]
w:c:{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusions

As you labeled the chords, you probably noticed that you had a chord that could only be explained as the borrowed II chord from the Phrygian mode. In each case, it was acting as a pre-dominant chord and followed the rules of a standard ii chord. This bII chord is used often enough that it earned a special name: the Neapolitan chord. The origin of the chord's moniker (Neapolitan) is disputed, but recently, one could make a case for calling this the "Batman" chord; it has been featured prominently in almost every modern Batman theme. Composers love to use this chord to add darkness to a progression.

## Neapolitan chords (bII)

You may label the Neapolitan chord using standard Roman numeral notation (bII) as discussed in the mode mixture unit (Unit 17a), but it is also common to substitute an upper-case "N"--short for Neapolitan--in your Roman numerals. For voice-leading purposes, the chord may sometimes have an enharmonically equivalent pitch--such as the `G#` shown in the third and sixth progressions--but we still always analyze this as a bII chord.

The above examples are three of the most common ways in which you should approach and leave a Neapolitan chord:
- Directly to the V chord, most often the V<sup>7</sup>
- Into a cadential 6/4 progression
- Into a vii<sup>o7</sup>/V

As you observed in the example, the bII chord is most commonly used as a pre-dominant function. In this case, you can make the argument that it is most similar to a pre-dominant ii chord, because it has the same scale degrees of ^2, ^4, and ^6, with a lowered ^2 and ^6. While this is true, if you look at the common doubling and inversion of the Neapolitan chord--first inversion with a doubled third--it may be easier for you to consider the Neapolitan as a functional substitution for a borrowed iv chord. This ensures correct doubling and voice-leading tendencies. Look at the chords side-by-side in below, and you will notice there is only a half-step difference between the two chords.

{% capture ex3 %}X:3
T:bII6 and iv
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[F_A_d] [F_Ac]|]
w:c:bII6 iv{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

Perhaps the most important reason for this doubling is that it solves two major part writing errors that occur for root-position bII chords:
1. *Resolving to V* - The root of the bII chord is a tendency tone and should not be doubled as we do for many chords. The flatted second scale degree pulls strongly downward, and when going directly to a V chord, it will resolve downward by an interval of a diminished 3rd to the third of the V chord. Of course, the chordal third of the V chord is also a tendency tone, so you would create multiple parallel perfect octaves if you were to double the root of the Neapolitan. 
2. *Resolving to a cadential 6/4 or a vii<sup>o7</sup>/V* - Not only is the root a tendency tone, the chordal fifth of this chord (^b6) also wants to resolve downward. If the bII chord resolves to either a cadential 6/4 or a vii<sup>o7</sup>/V, the movement between the root and chordal fifth would create parallel perfect fifths. By using a first inversion triad and placing the chordal third in the bass, you are free to move the root above the chordal fifth in your voicing.

You may use a Neapolitan chord as a pre-dominant function in any progression in which you could use a minor iv chord. In minor, there is only one chromatic pitch (^b2), but in major, you will need to lower both ^2 and ^6.

## Neapolitan chords as dominant chords

In the orchestral reduction below, how is the Neapolitan chord different from the above examples? What is its function here? If it is not a pre-dominant as above, then what chord from this new function shares the most commonalities with it?

{% capture ex4 %}X:4
T:Mahler Symphony No. 2, Mvt. I
T:Simplified reduction
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[g3GEC] _B/2>_A/2| [g3GEC] _G/2>F/2| [g3GEC] _E/2>_D/2|
[g3GEC] _B,/2>_A,/2| [G2EC] z2| [G2EC] z2| [Eceg] [_E3c_eg]|]
V:2 clef=bass
(3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [B,DF]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [_A,_D]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [_A,F,]|
(3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [B,,D,F,]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 [C,2E,G,]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 [C,2E,G,]| [C,,4C,]|]{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

Each Beat 4 of the first four measures of this passage has a colorful chord that contrasts the stateliness of the C major triad of the first three beats. In measure 1, the B-natural against the B-flat is not a typo; this dissonance is intentional. If you listen to the right-hand of this reduction alone, you will hear a clear descending melody in which the borrowed B-flat begins the `te` - `le` - `sol` melodic tendency that we associate with melodic minor.

{% capture ex5 %}X:5
T:Mahler Symphony No. 2, Mvt. I
T:Simplified reduction - right hand only
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[G3EC] _B/2>_A/2| [G3EC] _G/2>F/2| [G3EC] _E/2>_D/2|
[G3EC] _B,/2>_A,/2| [G2EC] z2| [G2EC] z2| [Eceg] [_E3c_eg]|]{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

Underneath that B-flat, however, is B diminished triad, and when the B-flat moves downward to the A-flat, we hear a a clear borrowed vii<sup>o7</sup>, which makes the B-flat an appogiatura. This figure is repeated down an octave in measure 4.

Measures 2 and 3 follow the same pattern of placing a non-chord tone on beat 4, followed by descending stepwise motion into a chord tone. In this case though, the resulting chord is a D-flat major triad--our bII (Neapolitan) chord.