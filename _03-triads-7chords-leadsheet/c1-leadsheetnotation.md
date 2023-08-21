---
layout: chapter
title: Lesson 3c - Leadsheet Notation
abc: true
---

In looking at triads and seventh chords, we have only learned how to label and classify these musical objects without specifying a particular root. A major triad or a dominant seventh chord can be built off any of the twelve pitch-classes, and each of the pitch-classes have multiple options depending on which enharmonic equivalent you choose as the root.  

*Leadsheet notation* is a commonly-used system that allows us to label specific triads and seventh chords--including any inversions and alterations. This is also sometimes referred to as *slash-chord notation*, *jazz chord symbols*, or *pop chord symbols*. This system for labeling chords is most commonly seen in jazz and pop music, but it is useful to all musicians because it is an efficient system for communicating chords *of any complexity*.

Even after we introduce Roman numeral analysis and harmonic function in Unit 6, we will continue to use leadsheet notation to provide a harmonic overview of complex analyses before we try to assign harmonic function and relationships. For example, if we have a C major triad and an F major triad and no other context, we cannot be sure of their key and function, so Roman numeral notation is not very useful. For those with a knowledge of diatonic function, it would seem most likely that these two chords belong to F major, but they could also exist diatonically in the keys of C major, D minor, A minor, as well as various modes. When analyzing harmonically ambiguous functions, it is critical to have a shorthand for labeling chords that is separate from the key, so that we can create a harmonic overview rather than re-analyzing each chord every time we re-contexualize a section of music.

### Labeling triads

Using the examples below:
- determine the standard methods for labeling all chord qualities
    - match these to our current labels (e.g. Major minor (Mm) chords are the same as a dominant seventh chord which is then labeled as...)
- determine the method for denoting inversions
    - match these inversions to their corresponding inversion figures for both triads and seventh chords

{% capture ex1 %}X:1
T:Leadsheet notation of triads
M:2/4
L:1/2
K:C clef=bass
"Bb+ (or Bbaug)"[_B,,D,^F,]| "Bb"[_B,,D,F,]| "Bbmin (or Bb-)"[_B,,_D,F,]| "Bbdim (or Bbo)"[_B,,_D,_F,]||{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Labeling seventh chords

{% capture ex2 %}X:2
T:Leadsheet notation of seventh chords
T:Everything other than the chord's root is typically written in superscript
T:---------------
M:2/4
L:1/2
K:C
"Dmaj7"[D^FA^c]| "D7"[D^FAc]| "Dm7 (or Dmin7)"[DFAc]| "D\/o7 or Dm7(b5)"[DF_Ac]| "Do7(or Ddim7)"[DF_A_c]||
w: major~seventh dominant~seventh minor~seventh half~diminished fully~diminished{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Labeling inversions

{% capture ex3 %}X:3
T:Inversions in leadsheet notation
T:---------------
M:2/4
L:1/2
K:C
"D7"[D^FAc]| "D7/F#"[d^FAc]| "D7/A"[d^fAc]| "D7/C"[D^FAC]|
w:root~position first~inversion second~inversion third~inversion
w:7~(7/5/3) 6/5~(6/5/3) 4/3~(6/4/3) 4/2~(6/4/2){% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

## Conclusions

### Basic leadsheet notation

The general naming system that we have used thus far allows us to talk about general categories of triads and seventh chords, but does not allow us to specify the exact root of a chord. Leadsheet notation is a shorthand method written above the staff that specifies a chord's root and quality. Leadsheet notation never had a centralized authority, so over many decades, it evolved various ways to denote the same chord qualities.

Leadsheet notation consists of a note name followed by a number of abbreviations and symbols. The note name denotes the root of the chord, and is most commonly an upper-case letter regardless of the chord's quality. Some systems use a lower-case letter for minor chords, but this is less common and is problematic for letters that have similar upper-case and lower-case versions such as `c`. (And of course can be exacerbated if the writer's penmanship is poor.) For our course, I will always use an upper-case root in my leadsheet notation.

The chord quality shorthand can vary greatly, so I have listed the most common possibilities below for chords with a root of C. Within each chord quality, I have listed the possible notations in my order of preference--again taking student penmanship into account. Clarity should be valued above brevity.

- Major Triad: C (no shorthand necessary, just a capital root name)
- Minor Triad: Cmin, Cm, C-
- Augmented Triad: Caug, C<sup>+</sup>
- Diminished Triad: Cdim, C<sup>o</sup>

- Major major (major seventh chord): Cmaj<sup>7</sup>, C<sup>M7</sup>, C<sup>&Delta;</sup>
- Major minor (dominant seventh chord): C<sup>7</sup>
- Minor minor (minor seventh chord): Cmin<sup>7</sup>, Cm<sup>7</sup>, C-<sup>7</sup>
- Diminished minor (half-diminished seventh chord): C<sup>&oslash;7</sup>, C<sup>&oslash;</sup>, Cmin<sup>7(b5)</sup>
- Diminished diminished (fully-diminished seventh chord): Cdim<sup>7</sup>, C<sup>o7</sup>

### Inversions in leadsheet notation

We are also able to show chord inversions in leadsheet notation by using *slash-chords*. To use slashchords, you use standard standard leadsheet notation followed by a slash (/) and then the *bass* note. This allows you to show any inversion. For example:

- C<sup>7</sup>/E is a C dominant seventh chord in first-inversion.
- C<sup>7</sup>/G is a C dominant seventh chord in second-inversion.
- C<sup>7</sup>/B&flat; is a C dominant seventh chord in third-inversion.

### Extensions and Using Sub vs. Add

Using the example below, you should:
- define *extended harmonies* by contrasting the chords below from the chords above
- find the key factor in determining a *sus* chord
- understand the difference between using *sub* and *add* in your leadsheet notation

{% capture ex4 %}X:4
T:Labeling extensions in leadsheet notation
T:---------------
M:2/4
L:1/2
K:C
"D13"[D^FAcegb]| "D6/9"[D^FAeB]^c/2| "Dsus7"[DGAc]| "D9 or D7(add9)"[D^FAce]| "Dm7(add b5)"[DF_a=Ac]| "Dm7(sub b5)"[DF_Ac]||
w:_ _ implied{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

## Conclusions

### Extended harmonies in leadsheet notation

As tertian harmony evolved from its earliest roots, some composers began adding pitches to chords beyond the chordal seventh. We will use the term *extended harmony* to refer to these chords, but in common usage, this term can also encompass chords that do not adhere to standard triad and seventh chord structures. 

For chords that extend beyond the seventh chord, we typically use the terms *ninth* for the second scale degree, *eleventh* for the fourth scale degree, and *thirteenth* for the sixth scale degree, because these extensions are a continuation of stacked thirds continuing above the seventh chord. A Cmin<sup>11</sup> implies that it has the normal minor seventh chord with both the diatonic ninth and eleventh added above it. 

As with standard leadsheet notation for seventh chords, if you have a number alone, it always implies a dominant seventh chord with extensions. A C<sup>13</sup> is a dominant seventh chord built on the root C with extensions up to the thirteenth. The only notable exception to this rule is the <sup>6/9</sup> chord; the shorthand in this case implies a major seventh even though there is no signifier other than the two numbers.

### *Sus* chords

As we move into studying the ways that composers embellish their music later in the course, we will study *suspensions*--a note that *does not belong to a chord*, but instead adds extra tension and color before resolving downward by step. In modern music however, there exists a standalone chord called a sus chord, which resembles the non-chord tone suspension of previous eras, but because the sus chord can be used without resolution, it has its own leadsheet notation. 

Csus

Any time that you see the abbreviation *sus* added to a chord in leadsheet notation, this implies that there is no chordal third. Instead, you will use the diatonic pitch that is a fourth above the *root*. So for a Csus, you will replace the E that would normally be present in a C major triad with an F. This would not change even if the bass note was altered; it will always replace the chordal third with the step above it. Any further alterations are best handled using...

### *Sub* and *Add*

The two commands *sub* and *add* are useful when writing leadsheet notation of non-standard chords. Admittedly, these will not be used much in diatonic harmony, but understanding their usage now will help when we move into chromatic harmonies.

Because triads and seventh chords are built in thirds, every third above the root has a predetermined quality based on the chord quality and root. If you would like to alter one of those chordal members, you can use the *sub* followed by an altered chordal member to imply that you are *replacing* that chordal member. For example, the alternate method for half-diminished seventh chords comes from this. Because a diminished triad is a minor triad with a lowered fifth chordal member, you could use the leadsheet notation for a minor seventh chord and substitute a lowered 5th. This would look like:

Cmin<sup>7(sub b5)</sup>

Admittedly, this method for notating half-diminished seventh chords is common enough that it is not required to use "sub" in this particular example, but this is still an excellent example of the proper way to use the sub command.

*Add*, on the other hand, does not alter any of the chordal members, but instead adds an extra chord tone. If you would like to add a raised ninth to a dominant 7th chord without altering the third, you could use:

C<sup>7(add#9)</sup>

If you master these two commands in your leadsheet notation, it is possible to denote any combination of altered pitches and substitutions for even the most complicated music. Of course, this assumes that the music still has at least its basic roots in tertian harmony, but even through the current day, almost all Western music does.
