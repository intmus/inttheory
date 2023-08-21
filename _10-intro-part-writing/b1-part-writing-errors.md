---
layout: chapter
title: Lesson 10b - Part-writing Errors
abc: true
---

## Part-writing

The term *part-writing* can imply many things depending on its context, but for our purposes, this will be our first attempt to combine the fundamentals of melody (counterpoint) and harmony (voice-leading derived from circle-of-fifths progressions) into functional music using diatonic tonality. 

By applying the various rules and techniques that we have studied thus far, we will be able to:
- Propose a functional harmonization for a melody
- Compose a melody given a harmonic progression
- Provide a four-voice arrangement of independent melodic lines that function harmonically together

Units 10 and 11 will help you solidify this process. First, we will establish a reference model by looking at the rules--and resulting errors from breaking those rules--that occur when writing in a four-voice structure. We will then apply these guidelines to our own attempts to compose basic four-voice chorales in order to better understand the voice-leading principles of diatonic music.

We will be referring to this handout, [Part-Writing Error Checklist and Guide](https://docs.google.com/document/d/1s9Xd3LPqoaEevshTopxHzLX9jCzxVCZocOBLD_dceMU/edit?usp=sharing), for the next two units, so you may want to print this out or open it in a separate window.

## Why part-writing?

Before we begin, I would like to address a question that I have received many times from students. Why do we study part-writing rather than just analysis, particularly in a strict style that is not applicable to all modern styles of composition?

For our purposes, the study of basic part-writing is the simplest way to learn *how* voice-leading creates harmony. Even though most of its rules are archaic--and perhaps more damning is that a modern student's ear is unlikely to dislike certain style characteristics (e.g. parallel perfect fifths)--four-voice composition is the most direct way to study every aspect of how music functions: voice-leading, chord progressions, voicing chords, chordal structure, tendency tones, melodic construction, and so on.

We could attempt to focus on only one style of modern music--whether pop, jazz, classical, or otherwise--but because each is a fully developed, complex language, you would still need to learn basic harmonic movement before beginning to write in that style. And because each of these musics has its roots in diatonic harmony, an understanding of basic chorale style part-writing will allow you to study and develop a process to analyze *all* of these styles, rather than focusing your studies into only one area and being ignorant of the others.

In short, focus on the *process* of the part-writing rather than trying to memorize every rule as if it is unbreakable. Even within a style, rules are guidelines, so an inflexible mindset will lead to nothing but frustration. Once you have grasped the basics of part-writing, you will have advanced another step toward the goal of improving your musicianship.

## Traditional errors

In the last [topic]({{ site.baseurl }}/10-intro-harmonic/a1-voiceleadingerrors.html), we first looked at some basic rules for voicing a chord in a four-part chorale style. These rules included:
- Voice-crossing
    - In this style, voices generally should not cross
    - Exception: alto and tenor may cross briefly if musically necessary
- Spacing
    - In this style, the top three voices--soprano, alto, and tenor--should always be within an octave of the adjacent voices. To be more specific, there can never be more than an octave between *soprano* and *alto*, and there can never be more than an octave bteween *alto* and *tenor*. 
    - There **can** be more than an octave between *bass* and *tenor*.
    - There **can** be more than an octave between *soprano* and *tenor*, and this creates two different types of voicings.
        - A *closed voicing* has **less** than an octave between *soprano* and *tenor*. 
        - An *open voicing* has **more** than an octave between *soprano* and *tenor*.
- Range
    - Each part must stay within the typical range for that voice/instrument?
- Doubling
    - You can double the root of a chord when possible.
    - For triads, you may double the fifth instead of the root if necessary.
        - This is actually preferable if the triad is in second inversion.
    - Do not double the chordal third because *if it is a tendency tone*--meaning that it has a desired resolution based on voice leading (e.g. the chordal third in a circle-of-fifths progression). If this is doubled, it will force you to choose between the incorrect resolution of a tendency tone or unacceptable parallel voices.
        - Additionally, the third should usually be the least present chord tone for a triad to sound balanced.
    - Do not double the chordal seventh because *it is a tendency tone*. Just as with the chordal third tendency tone, doubled chordal sevenths will force you to choose between the incorrect resolution of a tendency tone or unacceptable parallel voices.
    - **Do not** double the chordal fifth of a seventh chord. This would require omitting the root, third, or seventh, and none of these are expendable.

## Part-writing errors

**An important caveat**: Before you begin examining each of the four errors below, please remember two things:
1. All voice-leading errors *must occur within the same two voices*. 
      - Due to the effects of consistently doubling roots, there will almost always be consecutive perfect octaves and perfect fifths between two triads, but this is not *parallel*. For example, a root position C major triad moving to a root position G triad likely will have two voices on C in the first chord and two voices on G in the second chord, if standard doubling practices are observed. This is fine as long as its not in the *same* two voices in both chords (e.g. soprano and bass both have C and then both have a G).
2. Each of the four primary categories of part-writing errors are *symptoms* of voice-leading issues. If you understand the underlying voice-leading issues of each of these errors, you can find them more easily and avoid them in your own part-writing. 

Once you are comfortable with the descriptions of each of the errors below, try to fix each of the errors and listen to the playback. What do you have to change? Do you have to alter the harmony? Voice-leading? Voicing? In trying to fix it, do you just create further errors?

## Parallel perfect fifths and perfect octaves (PP5, PP8)

Part-writing errors result from poor voice-leading. For example, look at the progression below and try to find our first major error: *parallel perfect octaves* (PP8). The name of the error should be enough of a clue as to what you are searching for, and once you have found it, look to see if a voicing rule (e.g. spacing, doubling, etc.) has been broken. If the voicing error is not fixed, is there any way to avoid the parallel octaves without incorrectly resolving a tendency tone?

{% capture ex1 %}X:1
T:Parallel perfect octaves (PP8)
M:4/4
Q:1/4=80
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,A,] | [B,G,] [C,C]|]
w:C:I ii6 V7 I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

Listen to the following example, and try to locate the parallel perfect fifths aurally before you look through the parts. Once you have identified the voices that contain the PP5, try singing the upper of the two voices, and then listen to the example again. Do you have a difficult time differentiating the upper voice from the lower of these two voices?

{% capture ex2 %}X:2
T:Parallel perfect fifths (PP5)
M:4/4
L:1/2
Q:1/4=80
K:C
V:1
[cE] [AF]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [D,A,] | [DG,] [C,C]|]
w:C:I ii V7 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusions

PP8 and PP5 undermine the independence of lines, so you should always avoid them in this style. Unacceptable parallel fifths and octaves occur when two voices have consecutive perfect fifths/octaves and move in parallel motion. It is not parallel perfect fifths/octaves if the intervals change voices. (e.g. The first P8/P5 is between the soprano and tenor, but the second P8/P5 is between the soprano and alto.)

In the first example, there are two examples of parallel perfect octaves:
- between the soprano and tenor moving from ii<sup>6</sup> to V<sup>7</sup>
- between the soprano and tenor moving from V<sup>7</sup> to I

There is a larger underlying issue, however, because a doubling rule was broken on the V<sup>7</sup>. Because the third was doubled, you are forced to choose between incorrectly resolving one of the leading tones or undermining the independence of the two voices by locking them into consecutive perfect octaves.

{% capture ex7 %}X:7
T:Parallel perfect octaves (PP8)
M:4/4
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,A,] | [B,G,] [C,C]|]
w:C:I ii6 V7 I{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

In the second example, there are two examples of parallel perfect fifths:
- between the bass and tenor from I to ii
- between the bass and tenor moving from ii to V<sup>7</sup>

{% capture ex8 %}X:8
T:Parallel perfect fifths (PP5)
M:4/4
L:1/2
K:C
V:1
[cE] [AF]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [D,A,] | [DG,] [C,C]|]
w:C:I ii V7 I{% endcapture %}
{% include abc-example.html number="8" abc=ex8 %}

Parallel perfect fifths and octaves undermine the independence of the individual voices. If you repeatedly listen to the the PP5 example repeatedly, you will find it difficult to distinguish the tenor voice from the bass voice. This effect would be even more pronounced if the chords were tuned using just intonation, because the upper note will blend into the overtone series of the lower note.

In summary, you may never have parallel perfect octaves or parallel perfect fifths in this style of music. Please note that for an interval to be considered *parallel*, the interval must occur consecutively in the *same* two voices. For example, if your first P8 is between the bass and alto, the second P8 must also be in the bass and alto. If you find a P8 between the bass and tenor on the second chord, this is acceptable because it does not undermine the independence of the voices.

## Contrary perfect fifths and octaves (CP5, CP8)

Our next part-writing error, *contrary perfect fifths* and *contrary perfect octaves* (CP5 or CP8) are simply an attempt to cover up parallel perfect fifths and parallel perfect octaves by displacing one voice by an octave. The next two examples attempt to fix the errors from the first two examples on this page by displacing one voice of the parallel perfect intervals. Identify these by comparing them to the previous example (i.e. P) Notice that it creates multiple voicing and spacing errors as well as nearly unsingable parts!

{% capture ex3 %}X:3
T:Contrary perfect octaves (CP8)
M:4/4
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,A,] | [B,G,] [C,C,]|]
w:C:I ii6 V7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}


{% capture ex4 %}X:4
T:Contrary perfect fifths (CP5)
M:4/4
L:1/2
K:C
V:1
[cE] [AF]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [D,,A,] | [D,G,,] [C,C]|]
w:C:I ii V7 I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

In the first example, there are two examples of parallel perfect octaves:
- between the soprano and tenor moving from ii<sup>6</sup> to V<sup>7</sup>
- between the soprano and tenor moving from V<sup>7</sup> to I

In the second example above, the CP5s occur between bass and tenor voices between:
- the I chord and ii chord
- the ii chord and the V<sup>7</sup> chord

Contrary perfect 5ths/8ves occur when two voices have consecutive perfect fifths/octaves and move in contrary motion. Contrary fifths and octaves occur when trying to mask parallel perfect fifths and octaves, so they will exhibit most of the traits of PP5/PP8 including the fact that the intervals must occur between the same two voices If the interval changes voices, it does not undermine the independence of the voices.

## Unacceptable unequal fifths (UU5)

The last two common part-writing errors have specific clauses tied to them that specify which voices are acceptable and unacceptable. The first, *unacceptable unequal fifths* (UU5), must occur between the bass voice and one of the upper voices. In the following example, find the *unacceptable unequal fifths* where a d5 moves to a P5. What is wrong with the voice-leading here?

{% capture ex5 %}X:5
T:Unacceptable unequal fifths (UU5)
M:4/4
L:1/2
K:C
V:1
[cE] [Fd]| [dF] [cG]|]
V:2 clef=bass
[C,C] [D,A,] | [B,,G,] [E,C,]|]
w:C:I ii V6/5 I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

### Conclusions

Unacceptable unequal fifths are one of the easier part-writing errors to understand, because we are actually focusing on only one voice-leading issue. And because it is limited to certain voices, it is relatively easy to find compared to parallel and contrary fifths/octaves which are not acceptable between any voices.

For this course, we will consider a d5 moving to a P5 *unacceptable* unequal fifths, but we will consider a P5 moving to a d5 as *acceptable*--a P5 to a d5 does not require poor resolutions of tendency tones. Remember that these errors are best thought of as symptoms of the actual problem. In this case, the real issue is that the only two notes in a diatonic key that can form a d5 are `ti` and `fa`, and as discussed many times in this course, these two notes imply a dominant harmony that wants to resolve inward with `ti` moving to `do` and `fa` moving to `mi`. For a d5 to be followed by a P5, it would mean that `fa` must resolve to `sol`--or less commonly, `ti` resolving to `la` as part of a deceptive progression--which is poor voice-leading and therefore the error we are trying to avoid. There are some stricter versions of chorale part-writing that do not allow any form of unequal fifths.

## Similar perfect fifths or octaves (SP5, SP8)

The final common part-writing has many names, but we will use the term *similar perfect fifths or octaves*. The term *similar* can also be replaced with "direct", "hidden", or "exposed". I prefer the term *similar* because it describes the motion like the other categories, but I also think that *exposed* does a fine job describing the effect. (I dislike the term *hidden* because students often confuse this with contrary fifths (or octaves), because the goal of contrary fifths is to "hide" parallel fifths.) Of all the part-writing errors discussed in this unit, *similar perfect fifths or octaves* have the most restrictions. The conditions are:
- They can only occur between the soprano and the bass voices.
- They require a skip of a third or more in the soprano voice.
- The two voices must move in similar (not parallel) motion.
- The second interval must be a P5 or P8.

If any one of these conditions are *not* met, then this error does not exist. Look at the following example to find an example of SP8. Once you have found it, look at the voice-leading around it. What does it do to spacing? Does it create more errors? Unacceptable similar octaves and fifths also often create melodies that imply different harmonies. To demonstrate, sing the melody alone. Do you hear it as C major or a different key?

{% capture ex6 %}X:6
T:Similar octaves (SP8)
M:4/4
L:1/2
K:C
V:1
[Ge] [AA]| [FA] [FB]| [c2E2]|]
V:2 clef=bass
[C,C] [CA,,]| [F,,C] [DG,,]| [C2C,2]|]
w:C:I vi IV V7 I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

### Conclusions

As described above, similar perfect fifths/octaves have the highest number of restrictions in place. They can only occur when 1) the soprano and bass voices 2) move in similar motion to a 3) perfect fifth/octave, and 4) the soprano voice has a skip of a third or larger. You can see an example of this between the first two chords in the above example.

Similar fifths/octaves are sometimes called "exposed" fifths/octaves, and both of these terms demonstrate a key feature about the part-writing error. Obviously, they must move in similar motion, but the term "exposed" highlights the fact that these must occur between the outer voices. By having similar motion to a perfect interval in the outer voices, it creates the impression of a parallel perfect interval. Most importantly, the leap in the soprano typically creates a poor soprano line in which the melody outlines/implies an unintentional harmony. In the example above, if you sing the melody line without the harmony it outlines an A minor triad instead of C major triad.
