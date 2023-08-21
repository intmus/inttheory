---
layout: chapter
title: Lesson 1b - Labeling Pitches
abc: true
---

## Pitch systems and an introduction to solfege

There are many methods for labeling pitches, and these vary based on language of origin, style of music, pedagogy, and analytical purposes. In this textbook, we will primarily reference the widely-used English-language notation system that employs seven letter names and accidentals. This system is discussed below and is sufficient for differentiating between pitches in diatonic tonality. (If the terms *diatonic* and *tonality* don't mean anything to you yet, don't worry; we'll cover those terms in later units.)

There are times, however, when we want to discuss the *relationships* within a tonal structure without tying ourselves to a particular tonal center. You already do this instinctively when you listen to music. If you have participated in any amount of music performance, you can likely tell the difference between a major and minor scale, simply by hearing them. You don't need to know the exact pitches, nor do you need to know the name of the primary pitch of the key. Instead, you intuit the relationships in pitch collection by hearing *the relative distance between pitches*. We will discuss our system for labeling intervals in the next unit, but to do so, we need a system that demonstrates the *relative* distances between pitches around a tonal center, without having to refer to the letter system and a key name. 

There are multiple pre-existing systems that define music in relative terms, but for this textbook, we will use *moveable-"do" solfege*, a system that evolved from some of the earliest methods of notation. In this system, we assign the *tonic* of the key (or in simpler terms, the first note of the key), to `do`, and then we assign each note above that pitch a similar Latin name based on its distance from `do`. For those of you familiar with the musical *The Sound of Music*, you probably already know the basic seven solfege. "Do, a deer, a female deer...and so on.

We will discuss this system in detail in the unit on scales, but until then, it will be helpful for you to refer to the following chart when necessary.

Scale degree | Solfege syllable | Raised | Lowered
 --- | --- | --- | ---
 ^1 | do | di | N/A
 ^2 | re | ri | ra
 ^3 | mi | N/A | me
 ^4 | fa | fi | N/A
 ^5 | sol | si | se
 ^6 | la | li | le
 ^7 | ti | N/A | te

### Accidentals

This course assumes that you have a basic knowledge of how to raise and lower pitches in standard music notation. If you need to review accepted usage of accidentals, please refer to the *Further Reading* section under [Discussion 1b]({{ site.baseurl }}/01-pitches-clefs//b2-labelingpitches.html).

## Enharmonic Equivalence and Pitch Classes

When studying tonal harmony, C-sharp and D-flat have unique functions and are *not* interchangeable, however, when considering their physical properties, there is no difference between these two pitches meaning that we consider these two pitches to be *enharmonically equivalent*. At its core, enharmonic equivalence is an easy concept: When two pitches sound the same--meaning that they share identical [frequencies](https://amazing-space.stsci.edu/resources/explorations/groundup/lesson/glossary/term-full.php?t=wavelength_and_frequency)--but have different note names (i.e. letters), we consider them to be enharmonically equivalent. 

If you were to group all pitches that are enharmonic equivalents, you create a *pitch class*; such as C-sharp, D-flat, and B-double-sharp. There are twelve pitch classes in traditional Western tonality. Every pitch has multiple enharmonic equivalents, but some are used less frequently due to the necessity for uncommon accidentals such as double-sharps and double-flats. Note that all but one pitch class has at least three enharmonic equivalents when using the five most common accidentals: *naturals, flats, sharps, double-flats, and double-sharps*. (The remaining pitch class only has two possible enharmonic equivalents, unless you were to use accidentals that would never appear in performable music such as triple-sharps or triple-flats.)

### Goals for this topic

In the example below, each measure contains two notes that are enharmonically equivalent. Using this example, determine:
- up to three *enharmonic equivalents* for every *pitch class* using flats, sharps, double sharps, and double flats.
    - Which one of the *pitch classes* only has two enharmonic equivalents when using the five most common accidentals?

### Accidentals and Enharmonic Equivalence

{% capture ex1 %}X:1
T:Enharmonic Equivalence
M:2/4
L:1/4
K:C
V:1 name="Treble Clef"
_B ^A |f ^e |^^E ^F |]
V:2 name="Alto Clef" clef="alto"
^G _A |B, _C |^^G, A,|]
V:3 name="Tenor Clef" clef="tenor"
^F, _G, |F, ^E, |D, ^^C,|]
V:4 name="Bass Clef" clef="bass"
_D, ^C, |^B,, C, |D, __E,|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusion

Using the example above, you can extrapolate which pitch classes have three enharmonic equivalents and which have two.

Two examples of complete enharmonic equivalent groups would be:
- A, B-double-flat, G-double-sharp
- B, C-flat, A-double-sharp

Each pitch in these groups belong to the same pitch class, because they share an identical frequency. Yet they function differently within the context of music, so we have multiple ways of labeling the same frequency.

This shows that the *letter* system employed in staff notation is the limiting factor in creating enharmonic equivalents within a pitch class. The pitch class that includes A-flat is isolated from its neighbors in such a way that there is no pitch that uses the letter *F* or *B* to create a third enharmonic equivalent when using only the five common accidentals. The interaction between the 7 letter names and 12 pitch classes is the basis for our musical notation system and will be critical in how we label intervals, chords, and scales.

{% capture ex2 %}X:2
T:Enharmonic Equivalence
T:Each measure contains all notes within a pitch class that are enharmonically 
T:equivalent using only the five most-common accidentals.
M:3/4
L:1/4
K:C
^B, C __D| ^^B, ^C _D| ^^C D __E| ^D _E __F|
^^D E _F| ^E F __G| ^^E ^F _G| ^^F G __A|
^G _A z| ^^G A __B| ^A _B __c| ^^A B _c|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

## **Labeling Octaves and Clef Relationships**

### ISO

When labeling pitches, we also need a way to refer to specific octaves or registers. We will be using the system used by the [International Standard Organization (ISO)](https://www.iso.org/standards.html). In this system, each pitch is given an Arabic numeral that designates its octave. For example, middle C is labeled as C4.

### Goals for this topic

Using the example below, determine:
- where C4 lies in each clef
- what the numeral refers to in the ISO system for labeling octaves
- how to describe the usage of this system to a non-musician

{% capture ex3 %}X:3
T:Pitches and Clefs
M:C
L:1/4
K:C
V:1 name="Treble Clef"
e a f b g ^c B|]
w: E5 A5 F5 B5 G5 C#5 B4
V:2 name="Alto Clef" clef=alto
E A F B G ^C B,|]
w: E4 A4 F4 B4 G4 C#4 B3
V:3 name="Tenor Clef" clef=tenor
E, A, F, B, G, ^C, B,,|]
w: E3 A3 F3 B3 G3 C#3 B2
V:4 name="Bass Clef" clef=bass
E, A, F, B, G, ^C, B,,|]
w: E3 A3 F3 B3 G3 C#3 B2{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

There are a few simple rules to label octaves using the ISO system.
- Notes are labeled using a pitch name and a number.
- The numbers represent an octave range and higher numbers equate to higher octaves.
- Each numbered octave starts on C, not A.
    - Each number ends on B.
    - Even if two notes are enharmonically equivalent, they can have different octave designations. For example, C-flat4 and B3 are enharmonically equivalent, but because they straddle the octave break between C and B, they are labeled as belonging to different octaves.

### Why is the ISO system based on C instead of A?

This is almost entirely related to the evolution of the musical notation system and how the non-accidental pitches (i.e. "white keys" of the keyboard) form a major scale. While this is a fascinating topic, it is somewhat beyond the purview of this chapter, but I hope you will explore this further on your own.
