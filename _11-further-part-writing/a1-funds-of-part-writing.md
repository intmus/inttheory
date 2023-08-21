---
layout: chapter
title: Lesson 11a - Fundamentals of Part-writing
abc: true
---

## Introduction

Now that you have some guidelines in the form of stylistic rules, let's begin developing the process for composing your own part-writing. How would you go about harmonizing the following melody in a four-part chorale style? Before you begin, look at the example and make a list of all the things you would need to do to harmonize this melody.

{% capture ex1 %}X:1
T:Melody
M:4/4
L:1/4
K:C
V:1
cedf| gfed| c4|]
V:2 clef=bass
xxxx| xxxx| x4|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

In no particular order, you will need to determine: 
- Harmonies
- Harmonic rhythm
- Cadences
- Bass lines
- Inner voices
- Texture

To this point in the course, we have discussed each of these, but you have spent most of your assignments analyzing existing examples rather than creating your own music. 

And as a reminder, if you did not access our guide to part-writing in the last unit, you can find it here. [Part-Writing Error Checklist and Guide](https://docs.google.com/document/d/1s9Xd3LPqoaEevshTopxHzLX9jCzxVCZocOBLD_dceMU/edit?usp=sharing) We will continue referencing this for the rest of the unit, so you will probably want to print this out or open it in a separate window.

## Two important concepts to review before beginning

After looking at the list of concepts that are needed to harmonize a melody, you probably feel daunted and combining so many concepts into a single, coherent piece of music. So instead of bringing in every nuance to start, I'd like to draw your attention to two major concepts that will act as your overarching guides for managing your melodic (horizontal) and harmonic (vertical) choices. 

### CONCEPT 1 - Manage the horizontal aspect through melody and tendency tones

First, you should always prioritize making smooth, singable parts in this style. Your bass line will likely have more leaps if you prioritize root-position chords, but the upper three voices should predominantly use stepwise motion. Any leaps should be followed by stepwise motion in the opposite direction; not only does this make for singable, interesting melodies, but it also minimizes the possibility of issues such as voice crossing and spacing.

In Unit 7a, we showed that by studying the voice-leading of a simple V (or V<sup>7</sup>) to I progression, we can propose a broad set of voice-leading rules that explain circle-of-fifths diatonicism. Specifically:
- For chords that have roots separated by a P5:
    - The *seventh* of the first chord resolves to the *third* of the second chord.
    - the *third* of the first chord resolves to the *root* of the second chord.
    - If both chords are in root position, the bass voice moves from the *root* of the first chord to the *root* of the next chord.

This is the beginning of a *circle-of-fifths progression*: a progression in which each chord root follows the circle of fifths. 

### CONCEPT 2 - Manage the veritcal aspect through stylistic rules

Voice-leading governs the horizontal axis of music by shaping the melodies within each voice, but we need some basic rules to guide the vertical stacking of these melodies to make harmonies. A basic four-part chorale style employs the following four rules to act as general guidelines as a framework for combining voices.

- Range
    - Use the treble and bass staves as your guide. 
        - Your soprano should sit between the bottom line of the treble clef staff to a ledger line above the treble clef staff.
        - The alto voice can go as low two ledger lines below the treble clef staff and up to the top of the treble clef.
        - The tenor voice will typically range from the middle of the bass clef staff to three ledger lines above the bass clef staff.
        - The bass voice will range from the top of the bass clef staff to a ledger line below the bass clef staff.
- Spacing
    - Your upper three voices should never have more than an octave between adjacent voices. The soprano and tenor *can* be more than an octave apart though.
    - Your bass can be as more than an octave from the tenor. 
- Doubling
    - If you need to double a pitch, you can double (or even triple!) the root of most chords, and you should generally avoid doubling the chordal third and seventh in root-position chords. You can omit the chordal fifth if necessary, but the other pitches cannot be omitted entirely. 
- Voice-crossing
     - In our early attempts at part-writing, do not allow your voices to cross.

## A first attempt at part-writing

Let's use these two main concepts to try to harmonize the simple melody below with one harmony per pitch. Work through harmonizing the melody below, and take notes on each decision you have to make as your work through the process. If you get stuck, go back and look at the two major concepts to see if one of them gives you an idea how to proceed. And once you have finished, analyze your chorale to check for errors.

{% capture ex2 %}X:2
T:A first attempt at part-writing
M:4/4
L:1/2
K:C
V:1
[c] [A]| [B] [c]|]
V:2 clef=bass
x x| x x|]
w:C:{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusions

As you started, you hopefully realized that you had to make some important choices first such as choosing your key and cadences. By the end, you should have created a process similar to the following.

**To harmonize a melody in a four-part chorale style, you should:**
- **Identify the key**
    - Look for melodic patterns, starting pitches, and ending pitches for clues as to an implied key. 
- **Determine your phrase**
    - For the excerpt below, you have little room for decision making, but for a larger melody, try singing the phrase repeatedly and listen to your natural inclination for breaths or pauses. 
    - It can also be helpful to look for spots in which the rhythm slows naturally.
- **Choose a cadence** to complete your phrase.
    - Refer to [Unit 8a]({{ site.baseurl }}/08-cadences-phrasing/a1-cadences.html) to review the types of cadences.
- **Create the rest of the diatonic progression** beginning on tonic and ending with your cadence. (If not already provided.)
    - Beginning on tonic will establish your key center. Refer to [Unit 6b]({{ site.baseurl }}/06-intro-harmonic/b1-diafuncvoicelead.html) for a review of the three primary harmonic functions: tonic, dominant, and pre-dominant.
    - Refer to [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html) to determine a functional harmonic progression.
- **Compose a bass line** based on your harmonization.
    - This will resemble 1:1 counterpoint, so you can refer to [Unit 5b]({{ site.baseurl }}/05-counterpoint-embell-shapes/b1-cantfirmand1st.html).
    - It is okay for the bass line to be more disjunct than the other voices, so feel free to leave your chords in root position to make doubling simpler. 
    - You can alter one or more of these once you begin looking at how it interacts with your melody. Contrary motion against the soprano line is less likely to create issues.
- **Fill in the alto and tenor voices.**
    - Refer to the guidelines for voicing, range, and doubling in [Unit 10a]({{ site.baseurl }}/10-intro-harmonic/a1-voiceleadingerrors.html).
- When writing your parts, always **strive to have voice-leading that is as smooth as possible** by emphasizing stepwise motion.
    - As mentioned above, bass lines are the exception and will often have more leaps, especially when using root-position chords.
- **Check your work** 
    - Listen to your finished phrase repeatedly. It doesn't matter whether you play your phrase on piano or via musical notation software; it only matters that you listen to it.
    - Analyze your chorale for part-writing errors using the system we discussed in Unit 10.
    - Does your phrase sound convincing when played? If not, restructure your harmony and try again.

## Moving forward

Please do not be afraid of failing! This is a normal and important part of the learning process, so rather than be disappointed, try focusing on the parts that you do not like, and then analyze them for errors. Your first attempts may sound clunky and unconvincing, but you should be able to use the analytical tools that you have developed thus far to find mistakes. Iteration is key.

As you move the list above, you should realize that a four note melody such as this leaves little room for development, so it is easiest to stick with a simple ideas. Because `C` is in prominent positions at the beginning and end of the example, use C major for your key. And since the melody ends on the tonic, an authentic cadence would be easiest. With those two decisions made, everything else begins to fall into place.

To keep this simple, let's choose a perfect authentic cadence. This locks in the bass line for our last two notes, because we know that a PAC has a root position V and I chords at the end of the phrase. It is hopefully clear that the first pitch should start on the tonic chord to establish the key in our ear, which leaves only the second chord undetermined.

Because the chord that *follows* our undetermined chord is a dominant chord, it makes sense to use a pre-dominant chord, and the `A` in the melody would allow for either a ii chord or a IV chord. (If you are struggling to remember the standard diatonic chord progressions, please refer to Refer to [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html).)Let's choose an inverted ii chord to provide some variety.

{% capture ex3 %}X:3
T:A first attempt at part-writing
M:4/4
L:1/2
K:C
V:1
[c] [A]| [B] [c]|]
V:2 clef=bass
[C,] [F,] | [G,] [C,]|]
w:C:I ii6 V7 I
w:T P D T{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

You now can refer to the handout to see if we met some basic criteria:
- Our chords follow a standard progression.
- It establishes a key and then cadences in that key.
- The lines emphasize smooth voice-leading.

We are now ready to add inner voices, and we can use our voicing and doubling rules from Unit 6b to establish a first chord.

{% capture ex4 %}X:4
T:A first attempt at part-writing
M:4/4
L:1/2
K:C
V:1
[cE] [A]| [B] [c]|]
V:2 clef=bass
[C,G,] [F,,] | [G,,] [C,]|]
w:C:I ii6 V7 I
w:T P D T{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

And lastly, we can create the alto and tenor lines while observing the melodic guidelines from the handout.
- Individual lines should create smooth voice-leading using primarily stepwise motion.
- Resolve tendency tones as we studied in our voice-leading discussions (Unit 6b.)

Leading to...

{% capture ex5 %}X:5
T:A first attempt at part-writing
M:4/4
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,,A,] | [G,,G,] [C,G,]|]
w:C:I ii6 V7 I
w:T P D T{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

Of note, you may have tried to jump to a `D` for the first beat of the second measure in the tenor line, but this creates an unnecessarily disjunct tenor part. As we studied in Unit 6b, the chordal fifth can be ommitted on a seventh chord if the root is doubled.

Therefore, if we use only the tools that we have developed thus far in the course, we can already create a simple four-part chorale.

<!-- NO IDEA WHY THIS IS HERE. FIX LATER.

## Voicing a four-part progression

Let us return to the progressions from the last topic. We can now mix our voicing guidelines with our derived voice-leading rules to create a variety of progressions. 

There are two likely voicings for creating this next chord in the progression:

{% capture ex7 %}X:7
T:Two possible voicings for a ii chord
M:4/4
L:1/2
Q:1/4=100
K:C
V:1
[Fd]| [BG]| [c2G2]|| [FA]| [BG]| [c2G2]|]
V:2 clef=bass
[D,A,]| [G,D]| [C,2E2]|| [D,D]| [G,D]| [C,2E2]|]
w:C:ii V I ii V I{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

Some will prefer the sound of the first voicing, probably because they find the melodic shape in the soprano more interesting. Unfortunately, this voicing creates multiple issues. Not only are the parts more difficult to sing, particularly for the tenor voice, but the parallel perfect 5ths between the tenor and bass voices means that the tenor voice will meld into the bass voice and lose its independence. This doesn't sound too odd in a short excerpt like this, but in a longer passage, having parallel perfect 5ths will change the texture for brief moments in a noticeable way.

The second progression has less melodic variety, but it provides the smoothest, easiest voice-leading for each part with no voice-leading errors. If you add two more chords to the progression by following the circle-of-fifths progression we are creating, you should be able to add vi and then iii without much issue by following the pattern.

From this, we can demonstrate the process by which voice-leading creates one of the most fundamental progressions of all diatonic harmony, the circle-of-fifths progression.
  
{% capture ex8 %}X:8
T:A standard circle-of-fifths progression
M:4/4
L:1
K:C
V:1
[EG]| [EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[E,B,]| [A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:iii vi ii V I{% endcapture %}
{% include abc-example.html number="8" abc=ex8 %}
-->
