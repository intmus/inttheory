---
layout: chapter
title: 16c Lesson - Alternate modulatory methods
abc: true
---

## Secondary function pivot chord

In the following excerpt, try to apply the principles of a common chord pivot modulation. Is there a possible common chord? If not, is there an altered harmony that could be used to pivot? Make sure to look at the voice leading around the modulation.

{% capture ex1 %}X:1
T:Bach - Chorale no. 95 
T:(simplified)
M:4/4
L:1/4
K:Bb
Q:1/4=70
V:1
[dF] [eG] [fB] [fB]| [eA] [dB] [cA] H[cA]| [dB] [eG] [fF] [eG]| [cG] [cF] H[B2F]|
[cF] [dF] [eE] [eG]| [d_A] [dG] H[c2E]|]
V:2 clef=bass
[B,B,] [G,B,] [D,B,] [G,D]| [C,E] [D,F] [F,F] H[F,F]| [B,,F] [C,C] [D,A,] [G,B,]| [E,B,] [F,A,] H[B,,2D]|
w:Bb:
[F,A,] [D,=B,] [C,C] [E,C]| [F,C] [G,=B,] H[C,2G,]|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusions

We first hear the modulation on the second beat of the fifth measure. The B diminished triad is not diatonic to the original key of B-flat major but becomes the vii<sup>o</sup> chord of the new key of C minor. If you try to find a common chord pivot by looking at the chord before the modulation point (the place where you first hear the modulation), you will notice that the F major chord works in B-flat major, but not in the new key of C minor in which F minor is the diatonic iv chord. 

Even though there is no common chord pivot available, this excerpt still relies on the voice-leading and a functional progression to modulate. The listener expects the F major triad (m.5, beat 1) to resolve to a B-flat triad. Instead, Bach alters one pitch from the B-flat triad turning the B-flat triad into a B diminished triad, and thereby creates a pivot on a secondary function. This is a *secondary function pivot modulation*.

We label these using the same bracket system that we use for common chord pivot modulations, but one or both of the chords will be a secondary function. In this case, the top part of the bracket will contain "vii<sup>o6</sup>/ii", and the bottom part will containing "Cm: vii<sup>o6</sup>".

#### Secondary function pivot modulation principles

- Functions like all pivot modulations in that it relies on a functional progression on both sides of the pivot chord.
- Unlike common chord pivot modulations, there will not be a chord that is common to both keys before the modulation point. This then necessitates pivoting on a secondary chord.
- Typically occurs mid-phrase because of its reliance on a functional progression on both sides of the pivot.

## Phrase modulation (or direct modulation)

Analyze the following chorale excerpt. While you should be able to find a common chord pivot, how strong are the progressions on either side of the pivot? What aspect of the music mitigates the strangeness of these progressions? In other words, why doesn't this sound like a "bad" progression leading into the modulation point? (Hint: Even though our MIDI playback does not hold for the fermatas, you should consider that the choir would breathe after the natural resolution of that phrase. Play it on piano if you are able to simulate this.)

{% capture ex2 %}X:2
T:Bach - Chorale - Erkenne mich, mein Huter
T:(simplified)
M:4/4
L:1/4
K:E
Q:1/4=65
V:1
[EG]| [Ec] [EB] [A/2E][A/2F] [GE]| [FE] [FD] H[GE] [Fd]| [Ee] [eG] [dG] [dF]| H[c3E]|]
V:2 clef=bass
[E,B,]| [A,A,] [B,G,] [C,/2C][D,/2B,] [B,E,]| [A,,C] [B,,B,] H[E,B,] [D,^B,]| [G,C,] [E,C] [G,C] [^B,G,,]| H[C,3C]|]
w:E:{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusions

Because you first hear the modulation on beat 4 of the measure 2, it would make sense to pivot on the previous chord (the fermata), an E major triad. Pivoting on this chord would give you a modulation bracket with a "I" on top and "c#: III" on bottom. The issue is that the modulation point is a B-sharp diminished triad, which is the ii<sup>o6</sup> in the key of C-sharp minor. III-ii not a diatonically functional progression, so this is not a pivot chord modulation.

The crucial factor for this modulation is that it occurs across two phrases. The first phrase clearly ends on an IAC in E major, and the following chord immediately begins the new key. A modulation that relies on the phrase is called a *phrase modulation* or *direct modulation*.

Because there is no pivot chord in these types of modulations, we label phrase modulations without a bracket. Simply put the upper- or lower-case letter for the new key followed by a colon and the first chord in the new key. For this excerpt, the Roman numeral for beat 4 of the measure 2 would be: *C#m:ii<sup>o6</sup>*. 

Because phrase modulations are the only modulations we label without a bracket, you should know that if you choose to label a modulation that is not a direct modulation without using a modulation bracket, someone reading your analysis will assume that you misunderstood the modulation.

#### Phrase modulation principles

- Occurs when a modulation begins abruptly after a phrase ending.
- May or may not have a possible pivot chord, but it will create a non-functional progression between the last chord of the first phrase and the first chord of second phrase.

## Common-tone modulation

The last type of common modulation relies on a non-harmonic principle. Look at the following excerpt from a Schubert Lied. This is noticeably more advanced harmonic language than anything we have studied to this point, so there are certain harmonies (e.g. beat 2 of measure 2, beat 1 of measure 6) that we will not study until a later unit. As you listen to this however, you should have a strong sense of D minor until the dramatic modulation in measure 10. What ties the two chords in measure 10 together? If you need help, try isolating the voice part by deleting the piano staves. (To do this quickly, delete everything from `V:2`and below in the textbox. You can hit the "Reset" button below the textbox to restore the example to its original form.)

{% capture ex3 %}X:3
T:Schubert - Wehmut
M:2/2
L:1/4
K:F
Q:1/8=60
V:1
z4| z4| D D/2D/2 A> A| d>e ^c>c| ^c>c c c| d>A A>A| e>d e>d| A2 z ^c| 
d>A A/2>A/2 A/2=B/2| ^c2- c/2c/2c/2c/2| ^c>^A ^G/2=B/2A/2G/2| ^F3 z|]
V:2
[D2A,F,] [A2EA,]| [FDA,][FD^G,] [^C2A,]| [D2A,F,] [A2EA,]| [dAD][d^GD] [A2^cE]| [^cBG]>[cBG][cBG][cBG]| [d2A^F] [d2A=F]| [e^cAG]>[dAF] [ecAG][dAF]| [^cAE]>[cBG][cBG][cBG]| 
[d2A^F] [d2A=F]| [^c2AE] [^c2B^E^C]| [^c2^A^F^C] [^c2^E^G=B,]| [^c3^F^A,] z|]
V:3 clef=bass
[D,2D,,] [C,2C,,]| [B,,2B,,,] [A,,2A,,,]| [D,2D,,] [C,2C,,]| [B,,2B,,,] [A,,2A,,,]| [A,,4A,,,]| [A,,4A,,,]| [A,,2A,,,][A,,2A,,,]| [A,,2A,,,] [A,,A,,,][A,,A,,,]|
w:d:
[A,,2A,,,][A,,2A,,,]| [A,,2A,,,][^G,,2^G,,,]| [^F,,2^F,,,] [^C,2^C,,]| [^F,,3^F,,,] z|]{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

The excerpt begins in D minor but modulates to F-sharp major by the end. These are distantly related keys, so a common chord pivot modulation would be difficult. Instead, Schubert emphasizes a particular common tone in the melody and upper voice of the piano: the C-sharp. This pitch is the seventh scale degree in D minor and the fifth scale degree in F-sharp major.

By accentuating a particular pitch that is common to two keys, a composer can bridge seemingly impossible gaps in the tonal language. In this particular example, the C-sharp was accentuated by placing prominently in the melody, but composers will often take this a step further and completely isolate the pitch without any accompaniment. Regardless of texture, a common-tone modulation functions by emphasizing a particular pitch.

**To label a common-tone modulation**, we use a bracket similar to a pivot modulation. Instead of using chord symbols, however, we use scale degrees. For the Schubert common-tone modulation above, the top of the bracket would contain "^7", and the bottom of the bracket would contain "F#:^5". (Remember that when writing the scale degree "caret mark", you should place the caret *above* the numeral, not beside it as shown in an online text such as this.)

#### Common-tone modulation principles

- Functions by accentuating a particular pitch that is common to both keys.
- The pitch may be isolated entirely or just accentuated through normal musical means such as register, doubling, voicing, dynamics, etc.

## Final note

Some modulations may fall into more than one of these categories. In these cases, let your ear be the deciding factor. Focus on the basic premise of each modulation and decide which most closely describes your perception of the composer's intent. 
