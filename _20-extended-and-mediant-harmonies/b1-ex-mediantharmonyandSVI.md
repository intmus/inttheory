---
layout: chapter
title: 20b Lesson - Mediant harmony and Simplified Voice-leading Intervals
abc: true
---

As discussed repeatedly in this course, diatonic harmony and its progressions work because of the strength of the voice-leading. To prove this, let's listen to the following standard progression. As you listen, pay special attention to the voice-leading. Do you consider this progression to have strong voice-leading? If so, what makes it strong? If not, what makes it weak and what could strengthen it?

{% capture ex1 %}X:1
T:Basic diatonic progression
M:4/4
L:1
K:C
V:1
[EG]| [EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[C,C]| [A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:I vi ii V I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

Most students when presented with these questions determine that the strength of the progression comes from four things:
- The overall smoothness of the voice-leading in the upper voices 
- The "pull" from certain tendency tones toward another
- The strong, repetitive pattern of the bass voice
- The stability of resolutions by ascending P4/descending P5

Between any two chords with roots separated by descending P5, there is one common tone and two voices that resolve by step. The large leaps of the bass line contrast the smoothness of the upper voices and create a sense of movement, but if we remove the bass voice, we can clearly see (and hear) the smooth voice-leading between these chords while still using complete chords. (The tenor voice has been written in treble clef to make it easier to see the voice-leading. Its octave is not altered.)

{% capture ex2 %}X:2
T:A simplified basic diatonic progression
M:4/4
L:1
K:C
V:1
[CEG]| [CEA]| [DFA]| [DBG]| [EcG]|]
w:C:I vi6 ii V6/4 I6{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

By quantifying this aspect of voice-leading--the "smoothness" between two chords--we can study how this aspect of voice-leading strengthens a progression. In the simplified progression above, count the half-steps necessary to move between each of the two chords. Which chords have the smoothest voice-leading? Which are the most disjunct? Does this line up with what you would have expected?

## Simplified Voice-leading Intervals (SVI)

Counting the half-steps necessary for resolution in idealized voice-leading will be helpful to us as we explore more advanced harmonic concepts, because it gives us a tool to quantify something that is relatively subjective--what makes good voice-leading. We will call this process Simplified Voice-leading Intervals (SVI). You can do this between any two chords by:
- Writing both chords next to each other in closed position.
- Inverting one of the chords to minimize the distance necessary to resolve the two chords.
- Counting the half-steps necessary to resolve the progression.

When counting the half-steps in the the above progression, you hopefully found that the movement from ii to V was the "weakest" voice-leading and required four half-steps to resolve. The next strongest resolutions were vi to ii and V to I. Both of these resolutions require only three half-steps. But in a surprise twist, the winner of the smoothest voice-leading in the above progression, was not a circle-of-fifths progression at all; it was the I chord moving to the vi chord to start the progression. This happens because it has *two* common tones rather than just the one associated with chords that have roots separated by P5.

## Mediant harmony

Let's take this one step further. Before reading on, take a moment to find the SVI between a **C major triad** and all triads that are **diatonic to C major or C minor**.* Rank them in order of smoothest voice-leading to least.

Of all those chords, you should find that the lowest SVI--and therefore the smoothest voice leading--between a C major triad and the other triads is the one half-step necessary to create E minor, the mediant. In the next closest category (two half-steps), there are three chords: A minor (the submediant), A-flat major (the borrowed submediant), and F minor (the borrowed subdominant). Of the four smoothest chords, three are chords whose roots are separated by a third.

Anytime a progression has two chords whose roots are separated by a M3 or a m3, we call this *mediant harmony*. Do not confuse mediant harmony with tertian harmony; tertian harmony is any harmony that uses chords built by stacking thirds and exists independently of the distance between chordal roots in a progression. 

Rather than the structured rules and tendency tones of standard diatonic harmony, mediant harmony relies solely on the smoothness of voice-leading between two chords to create progression. And because of its flexibility, it creates interesting new colors and progressions within a framework that relies on tonal structures such as triads and seventh chords.

## Finding and labeling mediants

For any major or minor triad, there are eight possible mediant chords: one major and one minor chord for each of the four mediant pitches. For example, the four mediant pitches for C are E (mediant), E-flat (borrowed mediant), A (submediant), and A-flat (borrowed submediant). Each of these four pitches can have either a major or minor chord built off of it for a total of eight possible mediant chords.

Before looking at the completed chart below, find the SVI for each of the eight possible chords. After you group the mediants by SVI, also note how many common tones there are between the C major and each chord.

### Conclusions

All mediant harmonies for a C major triad:

Diatonic mediants | Chromatic mediant | Doubly chromatic mediants
 --- | --- | ---
 E minor | E major | E-flat minor
 A minor | A major | A-flat minor
 -- | E-flat major | --
 -- | A-flat major | --

There are three categories of mediants. The following descriptions compare describe the relationship to any major or minor chord:

*Diatonic mediants* (2 possible chords) 
- Have two common tones
- Have the opposite chord quality
- Have an SVI of 1 or 2
- Found as the diatonic mediant chord and submediant chord

*Chromatic mediants* (4 possible chords)
- Have one common tone
- Have the same chord quality
- Have an SVI of 2 or 3
- Found as:
    - EITHER the diatonic mediant chord and submediant chord *from the parallel minor/major mode* (2)
    - OR the triads built by *changing the chord quality* of the diatonic mediant chord and submediant chord (For C major, E minor become E major and A minor becomes A major)

*Doubly chromatic mediants* (2 possible chords) 
- Have zero common tones
- Have the opposite chord quality
- Have an SVI of 3 or 4
- Found by changing the chord quality of the diatonic mediant chord and submediant chord *from the parallel mode*

## Using SVI in Analysis

Listen to the following progression. It will not sound like a standard diatonic progression, but at the same time, it will likely sound like a convincing modulation from a C major chord to a B-flat major chord. You may even hear the last two chords as a cadence. Is it possible for you to analyze this using normal Roman numeral analysis?

{% capture ex3 %}X:3
T:Mediant progression
M:4/4
L:1
K:C
V:1
[CEG]| [C_E_A]| [CF_A]| [CFA]| [DFA]| [DF_B]|]
w:Cmaj Abmaj Fmin Fmaj Dmin Bbmaj{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

In this progression, Roman numerals cease to have a meaningful role because the chords do not follow standard function, nor are we able to identify a sequence with a stable repetitive pattern as we did in our unit on sequences. What good is using Roman numerals if a iii chord can function directly before the tonic chord? You *could* label this passage as beginning in C major and moving through I-bVI-iv, and you would then need to pivot on the F major chord to become the V chord in B-flat major. You could even analyze the D minor chord as just the arrival of the B-flat major triad with a retardation on the A.

But none of this truly explains why this works. This passage uses small, smooth alterations in voice-leading to create a sense of motion. To be clear, it is always preferable to analyze a passage using standard diatonic function (i.e. primary, secondary, and tertiary function) or a sequence if either is possible; there is no need to overcomplicate your analyses. But in passages like the one above--those that function due to an interesting but irregular pattern of voice-leading--you should include an SVI number in place of your standard functional analysis (i.e. T,D, or P). 

## Labeling SVI

To label chords that function through their voice-leading, you should place an SVI number inside of box below your Roman numerals and between the pair of chords. This replaces your standard functional analysis. You should still write the correct Roman numerals under each chord in order to show the pitches of the written chord, but SVI explains why the non-standard function works in the same way that labeling passing or cadential chords shows tertiary functions.

Key | Chord 1 | Chord 2 | Chord 3 | Chord 4 | Chord 5 | Chord 6
 --- | --- | --- | --- | --- | --- | ---
 C: | I [SVI:2] | bVI6 [SVI:2] | iv6/4 [SVI:1] | IV6/4 [SVI:2] | ----- | -----
 Bb: | ----- | ----- | ----- | V6/4 [SVI:2] | iii [SVI:1] | I

## The limits of SVI

As with all tools, you must be careful with how you use Simplified Voice-leading Intervals and mediant harmony. For example, when looking at diatonic progressions, the order in which the chords appear matters as much as the smoothness of the voice-leading. If you try to resolve V to ii, you have created a regression that will likely sound displeasing to someone familiar with tonal harmony. Also, many would say that adding a seventh to a chord (e.g. V becoming V7) strengthens the progression, because we have added a second tendency tone and therefore more tonal gravity between the two chords. But if you were to only look at SVI, adding the seventh would *weaken* the progression because it adds an extra half-step of resolution. In general, SVI is most useful when looking at non-standard tonal progressions.
