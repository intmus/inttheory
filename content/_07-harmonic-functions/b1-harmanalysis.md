---
layout: chapter
title: Lesson 7b - Performing a Harmonic Analysis
abc: true
---

Now that we have seen how the voice leading within circle-of-fifths progressions create a basic harmonic "outline", and we can use these patterns to ask the two fundamental questions of all harmonic analysis: 
- How are expectations created in the music?
- Which pitches are functional in creating these expectations?

Regardless of the complexity or era of a composition, if a theorist can answer these questions about a piece, they can analyze the qualities that define that style of composition. 

Students often think that "analyzing" a piece of music simply involves identifying and labeling each chord, but if that were the case, we should just use leadsheet symbols--they are flexible and do not require you to know anything more than pitches that are present at a given moment.  Roman numeral analysis provides a way for us to create *context*, because our ultimate goal in analyzing music is *to better understand how a listener perceives the music*. To explore this, we will go beyond Roman numerals and also provide an additional functional analysis for every chord, beginning with our basic functional labels from the last topic--tonic, dominant, and pre-dominant. Over time, you can begin to intuit how the movement in a chord affects its function, and through this we can make ourselves better performers, educators, and composers.

## A first attempt at harmonic analysis

Study the following chorale, and provide:
- a leadsheet symbol above every chord
- Roman numeral and inversion figure below every new harmony
- a functional analysis (i.e. T for tonic, D for dominant, or P for pre-dominant) below each Roman numeral 

As you go through this process, take notes of any questions you have and problems you solve, while paying particular attention to anything that you find difficult. Start by looking at the big picture, and do not get bogged down in trying to figure out every pitch and chord at first glance. If you get stuck, keep moving and return to the difficult sections after you have a feel for the piece as a whole. You should also consider starting with leadsheet notation until you are confident of the key of the piece; you can then return to add Roman numerals once you have more context.

{% capture ex1 %}X:1
T:Brahms-inspired chorale
T:Altered from “Die Wollust in den Maien”, WoO 34 no. 11
M:4/4
L:1/4
Q:1/4=80
K:G
V:1
[G/2D][B/2G]| [dG] [eG] [dF] [cF]| [BG] [AF] [BG] [dG]| [c2E] [A2F]| [G4]|]
V:2 clef=bass
[G,/2B,][G,/2D,]| [G,B,,] [A,C,] [A,D,] [DD,]| [DG,] [DD,] [DG,] [DB,,]| [C2C,] [C2D,]| [B,4G,,]|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Conclusions

 After working through the chorale, your issues could mostly be sorted into three basic categories:
- How often does the harmony change? (harmonic rhythm)
- Which pitches, if any, are omitted but implied by the context?
- Which pitches are functional (chord tones) or decoration (non-chord tones)?

### Harmonic rhythm

Before you can analyze a chord, you need to determine how often the chords change. This concept is called *harmonic rhythm*. It is different for every piece; sometimes it will be every beat as in the chorale above, but other pieces will have irregular patterns and/or many measures before new harmonies.

Determining harmonic rhythm is intuitively obvious to most musicians while listening, but can be difficult to illustrate during visual analysis because this is often a chicken-or-the-egg question: you need to know how often the chord changes to determine which pitches to include in the chord, but you also need to look at which pitches create chords to figure out how often the chord changes. Chorales are an easy place to start, because most often, they change chords in a consistent rhythm--in this case, every beat--and this creates an easy-to-see visual cue as each chord is stacked vertically and mostly homorhythmic. For more complicated textures, studying melodic patterns and bass lines is often enough to provide enough context for an educated guess. Bass-lines in particular will often sustain pitches and/or outline chords until the harmony changes, and this gives a clear indicator of probable harmonic rhythm. This becomes much easier as the student gains experience.

Once you have determined that the chords are changing every beat in this excerpt, you can add Roman numerals for each beat.

{% capture ex2 %}X:2
T:Brahms-inspired chorale
T:Altered from “Die Wollust in den Maien”, WoO 34 no. 11
M:4/4
L:1/4
Q:1/4=80
K:G
V:1
[G/2D][B/2G]| [dG] [eG] [dF] [cF]| [BG] [AF] [BG] [dG]| [c2E] [A2F]| [G4]|]
V:2 clef=bass
[G,/2B,][G,/2D,]| [G,B,,] [A,C,] [A,D,] [DD,]| [DG,] [DD,] [DG,] [DB,,]| [C2C,] [C2D,]| [B,4G,,]|]
w:I (6/4) (6) ii6/5 V (7) I V I (6) IV V7 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Omitted/implied chord tones

The chorale has a few incomplete chords, such as the downbeat of measure 3 and the downbeat of measure 4. If we do not have a full chord present, how do we determine the implied chord that a listener is likely to hear?

Let's examine the downbeat of measure 3. First, ask yourself what are all of the possible diatonic chords in the key of G major that contain both C and E? Those pitches would be the:
- root and third of the IV chord (C major triad or major seventh chord)
- third and fifth of the ii chord (A minor triad or minor seventh chord)
- fifth and seventh of the vii<sup>&oslash;7</sup> (F&sharp; half-diminished seventh chord)

With these options, we can look at which pitches are prioritized to see which of our three possibilities is most likely. We have already discussed that the root is the most likely chord tone to be doubled, and in this case the C is tripled. This strongly implies that the C is the root of the chord which would make this a IV chord. 

To double check that assumption, we can see if a IV chord makes sense in the progression by referring to the chord progression chart that we built in the last topic (and copied below). If we look at the *function* of a possible IV chord in the context of chords on either side of it, we know that a pre-dominant chord would fit well between the tonic and dominant chords in this spot. A I chord can resolve to any chord, and a IV chord moves easily to a V chord.

| (*unnamed*) | (*unnamed*) | pre-dominant | dominant | tonic |
--- | --- | --- | --- | --- |
| iii | vi | ii | V | I |
| | | IV | vii<sup>o</sup> | |

By employing a knowledge of standard progressions, a theorist can look at a given harmony and decide which pitches support a harmonic progression that is *likely* to be heard by a listener, even if those tones are not present. For this purpose, it will be helpful for you to add a row of functional analysis below your Roman numerals so that you can easily see what your Roman numerals imply to an experienced analysis. If we combine these, we get a finished analysis that will look like this:

{% capture ex3 %}X:3
T:Brahms-inspired chorale
T:Altered from “Die Wollust in den Maien”, WoO 34 no. 11
M:4/4
L:1/4
Q:1/4=80
K:G
V:1
[G/2D][B/2G]| [dG] [eG] [dF] [cF]| [BG] [AF] [BG] [dG]| [c2E] [A2F]| [G4]|]
V:2 clef=bass
[G,/2B,][G,/2D,]| [G,B,,] [A,C,] [A,D,] [DD,]| [DG,] [DD,] [DG,] [DB,,]| [C2C,] [C2D,]| [B,4G,,]|]
w:I (6/4) (6) ii6/5 V (7) I V I (6) IV V7 I
w:T - - P D - T D T - P D T{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Chord tones versus non-chord tones

The above example had no tones that did not belong directly to the harmony, but as you know, most musical textures are not as straight forward as the example above. So one of the most difficult issues to tackle in harmonic analysis is determining *which pitches are functional*. 
- Which pitches define how the listener "hears" the music?
- Which pitches could be removed without changing the basic effect?
- Which pitches are added solely to provide variety?

Let's use the initial sketch of our analysis to look at a more complex version of the same excerpt.

**Analyze the following embellished version chorale from above. Which notes are not necessary for the harmonic function? How would you describe their motion? If you are struggling to determine whether it belongs or not, try referring to your the harmonic outline that you built in the previous topic [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html). Does the voice-leading--i.e. how each chordal member resolves--work with the rules that you established in Unit 7a if you do not have a non-chord tone?**

{% capture ex4 %}X:4
T:Embellished version of chorale
T:(Divided across four staves)
M:4/4
L:1/4
Q:1/4=80
K:G
V:1
G/4A/4B/4c/4| [d] [e] [d] [c]| [B] [A] [B] [d]| [c]-[c/2][B/2] [A2]| [G4]|]
V:2
[D/2][G/2]| [G] [G]-[G/2][F/2] [F]| [G] [F] [G] [G]| [E2] [F2]| [G4]|]
V:3 clef=bass
[B,/2][G,/2]| [G,] [A,] [A,] [D]| [D/2]>[E/2] [D/2]>[E/2] [D] [D]| [C2] [C2]| [B,4]|]
V:4 clef=bass
[G,/2][D,/2]| [B,,] [C,] [D,] [D,/2][E,/4][F,/4]| [G,] [D,] [G,/2][D,/2] [B,,]| [C,2] [D,][D,,]| [G,,4]|]{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

As you attempted to analyze this decorated chorale, were you able to see and hear the basic framework from the first phrase of the basic version that you first analyzed? If so, it should have allowed you to figure out both the harmonic rhythm as well as which pitches were added as embellishment. 

The harmonic rhythm stayed the same; one chord per quarter note, even though the voices were often filled more notes, so your harmonic analysis would not change for this arrangement. Therefore, the *functional* pitches of any piece of music are the essential notes that if removed, would noticeably alter the way the listener hears the harmony. 

As we progress in our analyses, you will find that there are a number of factors which influence a listener's perception of functional pitches (i.e. chord tones) and non-functional (non-chord tomes) pitches such as: 
- Which pitches are in strong metric positions (e.g. strong beats or sustained notes)? 
- Are certain pitches given preference through methods such as repetition? 
- Is one pitch more dissonant against the other chord tones? 
Differentiating between chord tones and non-chord tones is the key to deciding a chord's function.

When we study non-chord tones in detail in Unit 9, we will be able to clearly differentiate and label these from our chord tones, but for now, it is enough to know that they exist and are an important part of analysis.

## Before moving forward...

Hopefully, these examples have allowed you to start grasping the difference between *labeling* chords and understanding their *functions*. Even without much guidance, you can use your knowledge of musical fundamentals--intervals, chords, melodic lines, etc.--to create a sketch of the harmonic underpinnings of this chorale.

We use chorales to begin studying analysis because of the vertical nature of the writing. Every chord in this composition is aligned to where it can be easily parsed by sight, and almost every tone is functional. As we look at music from a variety of styles, we will always have the tool of reducing music to its simplest texture--one that likely resembles a chorale voicing--in order to further our understanding of the phrase and shape of our interpretations.
