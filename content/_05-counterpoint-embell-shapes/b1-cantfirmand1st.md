---
layout: chapter
title: Lesson 5b - Cantus Firmus and 1:1 Counterpoint
abc: true
---

Exercises in strict voice-leading, or species counterpoint, begin with a single, well formed musical line called the *cantus firmus* (fixed voice, or fixed melody; pl. *cantus firmi*). *Cantus firmus* composition gives us the opportunity to examine the following fundamental musical traits:

- smoothness  
- independence and integrity of melodic lines  
- variety  
- motion towards a goal

The "rules" of the style of counterpoint that we will study are compiled from important writings and treatises of the eighteenth century, most notably Johann Joseph Fux, so this style of counterpoint is typically referred to as *eighteenth century counterpoint*. As with all historical studies, especially those that are spread across a continent over decades, there are inconsistencies between systems and styles. We will look at a simplified version of contrapuntal writing to focus our thoughts on melodic interaction, however I urge you to complete a full study of counterpoint at some point in your musical development in order to properly explore this critical facet of music. Our discussion of this topic, however brief, aims to help you absorb the methodology of good counterpoint (voice-leading).

### Terms useful for discussing counterpoint

- Melodic intervals - intervals within a line (horizontal intervals)
- Harmonic intervals - intervals between lines (vertical intervals)

We will consider three types of melodic intervals:
- Movement by a 2nd is *stepwise* motion
- Movement by 3rd is a *skip* and typically implies a triad.
- Any movement of a 4th or larger is called a *leap* and has the most restrictions.

We use the terms *stepwise*, *skip*, and *leap* exclusively to describe melodic intervals, because each of these terms imply forward motion. Do not use these terms to describe harmonic intervals. For harmonic intervals, we use the types of motion (e.g. parallel, similar, etc.) combined with the size of the intervals (e.g. parallel 3rds, etc.)

### 1:1 Counterpoint (first species)

In first species counterpoint, we begin with a *cantus firmus* (new or existing) and compose a single new line--called the *counterpoint*--above or below the cantus firmus. That new line contains one note for every note in the cantus; both the cantus firmus and the counterpoint will consist of only whole notes. Thus, first species is sometimes called one-against-one or 1:1 counterpoint.

## Goals for this topic

Use the following examples of first-species (1:1) counterpoint to develop guidelines for writing in this style. Each of the following examples is in the major mode and has the counterpoint above the cantus firmus, but be aware that not all counterpoint is written this way; it is common to have the cantus firmus above the counterpoint or to compose in the minor mode. We are using a simplified structure as an introduction to the concepts.

**As you develop your rules for first-species counterpoint, look only at the *counterpoint (CP)* line; the *cantus firmus (CF)* was provided, so the counterpoint line was written by following the stylistic rules, not the cantus firmus.**

Generally, your rules should be divided into three categories:
- Constructing a *melodic line* and *melodic intervals*
    - Length
    - Starting and ending pitches
    - Approaching the final note
    - Repeated pitches
    - Melodic intervals
        - Leaps
        - Resolutions following leaps
    - Range
    - Climax (position in melody and frequency)
- Acceptable *harmonic intervals*
    - Valid harmonic intervals
        - Particularly starting and ending intervals
    - Approaching perfect intervals
    - Approaching the final pitch
    - Number of times that an interval size can be used consecutively
        - Differentiate between perfect and imperfect consonances
- Acceptable *motion between lines*
    - Acceptable types of motion

**Note that these examples are taken from a counterpoint random generator and lack some of the elegance that human-composed counterpoint tends to have.**

{% capture ex1 %}X:1
T:First species (1:1) examples
T:Each system is a new example.
M:4/4
L:1
K:C
V:1 name=CP1
c| B| A| e| d| c| F| G| B| c|]
w:P8 M6 M3 M3 m3 P8 m6 m3 M6 P8
c| B| c| F| G| A| f| e| c| B| c|]
w:P8 M6 P5 m3 m3 M6 m3 P8 m6 M6 P8
c| d| c| d| A| B| d| f| e| d| c|]
w:P8 m3 m6 P8 M3 M3 M6 m3 M3 m3(m10) P8
c| g| f| c| d| a| g| d| e| B| c|]
w:P8 m3 m6 m3 P5 M3 M6 m6 M3 M6 P8
V:2 clef=bass name=CF
C,| D,| F,| C| B,| C| A,| E| D| C|]
C,| D,| F,| D,| E,| C,| D,| E,| E| D| C|]
C,| B,,| E,| D,| F,| G,| F,| D,| C,| B,,| C,|]
C,| E,| F,| A,| G,| F,| G,| F,| E,| D,| C,|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Conclusions

As you develop your counterpoint rules, your observations will naturally separate into three categories mentioned above: 
- rules within a single melody (the horizontal aspect of the music)
- rules for comparing the intervals between the two melodies (the vertical aspect of the music)
- and rules for studying the motion between the line. 

To plut this simply, there are rules for melody, harmony, and voice-leading.

### Melodic intervals and structure

These are some general guidelines for each of the *melodic* aspects of 1:1 counterpoint.
- First species counterpoint typically has 8 to 14 pitches.
- As a general rule, use stepwise motion as much as possible.
    - Thirds or other leaps can form triads, and this can create a non-functional implied harmony. 
- The final note should be approached by stepwise contrary motion.
    - Therefore one voice will have the seventh scale degree (`ti`) and the other will have the second scale degree (`re`).
- There are generally no repeated pitches
    - Meaning that static and oblique motion do not occur in first species because they both require at least one voice to repeat pitches
- The line should have a clear high (or low) point.
    - Repeating the highest pitch--or lowest if the contour arcs downward--undermines the climax. A strong melody will have a clear beginning, middle, and end, so having multiple climaxes muddies this journey.
- Leaps should be used sparingly, because too many leaps imply certain types of harmony that were not common in this style.
    - Leaps should always be aproached and left by step, preferably in contrary motion.
    - You may sometimes leap to or from the climax. 

### Harmonic intervals and structure

- 1:1 counterpoint will likely start and end on a perfect octave (or unison) of the tonic pitch, although a perfect fifth can be used to begin the counterpoint if necessary.
- In this style of counterpoint, perfect intervals should only be approached by contrary or oblique motion, although oblique motion is not allowed in first species. (You can use oblique in the later species.)
- You should only use consonant intervals in first species, which you can review from [the previous topic]({{ site.baseurl }} /05-counterpoint-embell-shapes/a2-introcounterpoint.html).

To be clear, this means that the acceptable consonant intervals in first species are:
- **Perfect**: Perfect fifths and octaves
- **Imperfect**: Major and minor thirds and sixths

### Motion Between Lines in First Species

Types of motion
- contrary - no restrictions
- parallel - some restrictions
- similar - some restrictions
- static - not allowed
- oblique - not allowed

In first species, an individual line cannot repeat a pitch, so this eliminates both static and oblique motion entirely. Contrary motion is the easiest motion to use because it has almost no restrictions. Parallel and similar motion are less common but still regularly used; you will need to pay careful attention to avoid creating part writing errors with both of these. 

### Errors in motion

- parallel perfect octaves and perfect fifths
    - Parallel perfect octaves and fifths are always unacceptable. Repeating the same pitch in this manner blurs the independence of the lines and becomes too similar to monophony.
- contrary perfect octaves and perfect fifths
    - Unacceptable contrary octaves and fifths occur when two identical perfect intervals occur consecutively in contrary motion. This is a way of trying to hide parallel perfect octaves or fifths by using contrary motion. 
- similar/direct/hidden octaves and fifths
    - Unacceptable similar motion occurs when you approach a perfect fifth or octave in similar motion from any interval. Approaching a perfect interval by similar motion makes it more difficult to hear the interval and will make it difficult to continue writing your counterpoint without creating more errors. Similar octaves or fifths are also referred to as direct octaves/fifths or hidden octaves/fifths; I prefer the term "similar octaves/fifths" because it describes the motion accurately.
