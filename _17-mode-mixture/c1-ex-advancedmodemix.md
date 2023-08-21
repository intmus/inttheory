---
layout: chapter
title: 17c Lesson - Advanced mode mixture
abc: true
---

## Extending mode mixture

Please watch this wonderfully-made video on modal interchange -- another name for mode mixture -- created by Myles Yang for his Native Construct YouTube channel. In it, he demonstrates possible mode mixture beyond parallel major and minor modes. If you are not familiar with modes beyond major and minor (Ionian and Aeolian), please review Unit 2. You can also quiz yourself on modes at [musictheoryfundamentals.com](http://musictheoryfundamentals.com/MusicTheory/modes.php).

<iframe width="560" height="315" src="https://www.youtube.com/embed/1dRA28cdt5c?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

This video does a great job of explaining the concept of mode mixture, but as he mentioned near the end of the video, he is only "scratching the surface". Having watched the video, you probably feel that you understand the extended *concept* of mode mixture, but if you were asked to compose a progression and melody using this advanced language of mode mixture, do you feel that you would be able to implement it? Where would you start? Why did he choose these particular chords? How did he know where they would sound convincing? In short, this video explains the questions of "what is it?", but it does not approach the questions of "why it works" or "how it works".

To begin exploring this, use the score below to try voicing one of the progressions taken from the video. Take risks, and break the "rules" as you try this. You must use the chord progression below, but you may alter the bass and soprano lines if you would like. You may also add as many or as few of the pitches as you need. Are you able to make this progression sound as pleasing as it does in the video? If not, what are the factors making this difficult? From a technical viewpoint, is it lack of knowledge or is it the medium (MIDI keyboard)? From a musical viewpoint, what aspects make the biggest improvement when you alter them?

{% capture ex1 %}X:1
T:Sample mode mixture
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[e] [f]| [f] [f]| [e2]|]
V:2 clef=bass
[C,] [_B,,]| [F,,] [D,]| [C,2]|]
w:C:I bVII IVM7(#11) ii%7 I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusions

Even though this is an entirely new style of progression, you can focus on the fundamentals of voice-leading to guide you. For example:
- Resolve tendency tones correctly
- Write smooth individual voices
- Allow more spacing in your voices when writing in the lowest range
- Avoid objectional parallels when possible
- Don't double tendency tones

If you do these things, it is fairly easy to write smooth soprano and bass lines and then work your way backward through the progression to create something such as this:

{% capture ex4 %}X:4
T:Voiced sample mode mixture
T:(inversions not notated in Roman numerals)
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[GC] [_BD]| [AE] [_AC]| [G2C]|]
V:2 clef=bass
[C,E,] [_B,,F,]| [B,,F,] [D,F,]| [C,2E,]|]
w:C:I bVII IVM7(#11) ii%7 I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

## Functional mode mixture

As you have hopefully come to realize, all tonal harmony--even the chromatic alterations--rely on voice-leading to create a sense of natural progression, and each harmony can be viewed through the lens of how it functions. From this, we derive primary harmonic functions such as tonic, dominant, and pre-dominant as well as embellishing functions such as passing, pedal, and cadential. Even the exceptions to these can be viewed as functional substitutions (e.g. deceptive progressions).

At its core, mode mixture borrows altered tones from parallel modes, thus altering chord *qualities*, but retains standard chord function. If a diatonic chord would have a pre-dominant function, altering an individual tone by a half-step will not alter the function. It creates color and often *strengthens* the voice-leading by changing whole-step resolutions into half-step resolutions. Moreover, if a chord functions as an embellishing chord such as a passing or pedal chord, then it will retain that function even if one or two pitches are borrowed from a parallel mode. 

Even seemingly inexplicable choices can be explained, such as the ii<sup>&oslash;7</sup> from the chord progression above, if you look at the voice-leading and compare it to standard diatonic function.
1. The ii<sup>&oslash;7</sup> is inserted into the position where we would normally expect a dominant function.
2. If you compare the pitches within ii<sup>&oslash;7</sup> to the pitches of vii<sup>o7</sup>, you will realize that three of the pitches are the same (D, F, and A-flat) and the remaining pitch only changes by a half-step (B to C). In this progression, the C works best when it acts as an anticipation of the tonic chord, and this strengthens the voice-leading resolutions of ii<sup>&oslash;7</sup>. Therefore, the ii<sup>&oslash;7</sup> can be viewed as a dominant function chord.

With this in mind, look at the following reduction of an excerpt from Mahler's Symphony No. 2. How would you explain each of these borrowed chords? How do they function? Is this similar to the progression from above?

{% capture ex2 %}X:2
T:Mahler Symphony No. 2, Mvt. I
T:Simplified reduction
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[G3EC] _B/2>_A/2| [G3EC] _G/2>F/2| [G3EC] _E/2>_D/2|
[G3EC] _B,/2>_A,/2| [G2EC] z2| [G2EC] z2| [Eceg] [_E3c_eg]|]
V:2 clef=bass
(3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [B,DF]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [_A,_D]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [_A,F,]|
(3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 C,/2z/2 [B,,D,F,]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 [C,2E,G,]| (3C,/2G,,/2C,/2 (3C,/2G,,/2C,/2 [C,2E,G,]| [C,,4C,]|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

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

Measures 2 and 3 follow the same pattern of placing a non-chord tone on beat 4, followed by descending stepwise motion into a chord tone. In this case though, the resulting chord is a D-flat major triad. While we could consider this further mode mixture as a borrowed II chord from the Phrygian mode, it will be easier to wait until the next Unit to discuss Neapolitan chords.

## Chromatic non-chord tones versus mode mixture

Analyze the following two chord progressions. What factors help you decide how to label each chord? Which tones are chromatic passing tones, and which create new harmonies?

{% capture ex3 %}X:3
T:Mode mixture or non-chord tones?
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[cE] [cF] [cF] [cE]|| 
GA A/2_A/2G|]
V:2 clef=bass
[C,G,] [C,A,] [C,_A,] [G,C,2]|| 
[C,E] [C,F] [C,F] [C,E]|]
w:C:{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

Chromatic passing tones often create harmonies that could be considered borrowed chords, but the determining factor should always be its function. If the resulting borrowed chord does not sound as a defined function (e.g. tonic, dominant, pedal, etc.), then the pitch should be classified as a passing tone. If the chord operates as a functional substitution (tonic, dominant, pre-dominant), then it is better to label it as a borrowed chord. If each member of the chord functions solely for smooth voice-leading purposes, then it should be labeled as a borrowed chord with an alternate function such as a passing or pedal chord.

In the example above, most will hear the first iteration as a I-IV-iv-I progression. The chromatic tone of the iv chord on beat 3 is present for the entirety of the beat and fits the harmonic rhythm of one chord per quarter note. Considering beats 2 and 3 as one chord would allow you to label the A-flat as a chromatic passing tone, but the A-flat is present long enough to make this difficult to hear as such. Conversely, the A-flat in the second measure is only present for an eighth note and occurs in a weak position. In this case, the A-flat is a clear chromatic passing tone and would not be labeled as a borrowed iv chord.
