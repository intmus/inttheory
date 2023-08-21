---
layout: chapter
title: 18a Lesson - Tonal Sequences
abc: true
---

In music, a sequence occurs when a musical pattern is established then repeated at various transpositions. Sequences can be any combination of the following categories:
- melodic, harmonic, or both
- ascending or descending
- diatonic or chromatic
- single or multiple parts within each repeated segment

Sequences work because they rely on one of the most fundamental human characteristics: our ability to identify patterns. All music relies on a listener's familiarity with the tendencies within a style, but these tendencies can be broken if a composer is able to create a new pattern to guide the listener. Once a musical pattern is established, it will sound "right" to a listener, even if this pattern defies standard tonal conventions.

## Terminology of a sequence

For our discussions, we must differentiate between the overall pattern of the sequence and the individual segments within the sequence. We will use the term *sequence* to refer the whole, but we will use the word *iteration* to discuss an individual segment within the sequence. You can think of the iteration as one complete "building block" that is transposed repeatedly to create the sequence.

## Melodic sequences

We will begin studying sequences by looking at melodic sequences because they demonstrate the basic principles without the complications of multiple voices. Look at the following melodic patterns; each one contains a few iterations at the beginning of a melodic sequence. Complete the pattern through the designated ending pitch and then discuss the repetition using the following terms:
- ascending or descending
- diatonic or chromatic
- intervals of transposition
- length of pattern
- single or multiple parts within each repetition

Of note, when describing melodic sequences to another person, you can assume that the reader is looking at the music and therefore can see the entire first iteration. This means that you should not have to describe pattern of the iteration.  Instead, we focus our description on *how the pattern is transposed*, not on describing the intervals within the *initial* segment.

{% capture ex1 %}X:1
T:Melodic sequences
M:2/2
L:1/8
Q:1/4=70
K:C
CDEC DEFD| x8| x8| x4c4||
cBcG BABF| AGAE x4| x8| x4C4||
cBcG B^AB^F| _BA_BF x4| x4G4||
c'gae fcdA| x6C2||
c'bc'g a^gae| fefc x4| x8| x4C4||
cBcG AGAE| dcdA BABF| x8| x8| g8||{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusions

The terminology for describing sequences should be familiar because each term is used in a similar manner across all aspects of music, however, each term has some specific connotations when applied to sequences.
- When discussing sequences of any kind, the terms "ascending" and "descending" describe the direction of the transpositions, not necessarily each interval within the pattern.
- The interval(s) of transposition is found by comparing the relationship between the first pitch of each iteration. As long as you know the starting pitches of each iteration, you should be able to extract the entirety of the sequence by using the intervalic structure from the *first* iteration.
- The overall length of a melodic sequence will likely be apparent at a glance, but determining the length of the individual iterations can involve some amount of subjectivity. Some sequences can be viewed as a having varying intervals of transposition--e.g. down a 3rd, up a 4th, down a 3rd, up a 4th, and so on--and in these cases, you will need to determine which level of iteration best represents the sequence. For example, in the pattern of down by a 3rd then up by 4th as seen in the last line of the above examples, you may label both transpositions for an iteration that lasts two beats OR group those together to create a larger iteration that repeatedly goes up by 2nd every measure. In general, I choose the larger iteration to make my analyses easier to read unless I feel that there is a motivic reason to differentiate the smaller divisions.

The discussion of chromatic and diatonic sequences, however, requires clarification.
- A true **diatonic pattern** only uses notes within the key signature so they do not require a quality when discussing the transposition. For example, it is incorrect to describe a diatonic pattern using, "The pattern repeats in ascending *major* 3rds," because diatonic patterns will have a mix of major 3rds and minor 3rds depending on which scale degree the iteration starts. Instead, we would say, "The pattern is transposed in diatonic ascending 3rds," because this tells the reader to go up a 3rd and use whatever note is in the key signature.
- Conversely, **chromatic patterns** *do* require a quality on the transposition for the interval, because the pattern repeats *exactly* using the same intervals from the initial iteration. If we isolate the third sequence from the melodic examples (see example below), we have a fixed intervallic pattern -- in this case, descending m2, ascending m2, descending P4 -- that is then repeated by transposing that *exact intervallic pattern* down a m2. In short, a chromatic pattern is assumed to transpose every part of the pattern exactly at a fixed interval(s) unless otherwise noted.

{% capture ex10 %}X:10
T:Strict chromatic sequence
M:2/2
L:1/8
Q:1/4=70
K:C
cBcG B^AB^F| _BA_BF A^GAE| _AG_A_E G4||{% endcapture %}
{% include abc-example.html number="10" abc=ex10 %}

The fifth example above is the most difficult to complete and classify, because it mixes elements from both diatonic and chromatic sequences. It has a diatonic transposition, but each iteration can only be defined by a fixed intervallic structure. So we would describe this as a diatonic sequence that descends in 3rds, while each iteration is four pitches with the intervals of descending m2, ascending m2, and descending P4. Notice that the interval of transposition is found by comparing the first pitches of each iteration, *not* the interval between the last pitch of an iteration to the first pitch of the next iteration.

{% capture ex11 %}X:11
T:Diatonic transposition with a chromatic pattern
M:2/2
L:1/8
Q:1/4=70
K:C
c'bc'g a^gae| fefc d^cdA| B^AB^F G^FGD| E^DEB, C4||{% endcapture %}
{% include abc-example.html number="11" abc=ex11 %}

## Harmonic sequences

When two or more melodic sequences are combined, they create a harmonic sequence that can supplant standard harmonic function and conventions. As mentioned in the introduction, sequences work because they establish a pattern for the listener and then fulfill this new goal. Look at the following example of a two voice pattern. The first bar establishes tonic, and then a sequence begins in the second measure. After listening to it, discuss with your classmates whether it *sounds* functional. If you were going to describe this to another person, how would you describe it? Once you finish your discussion, propose a harmonic progression that fits the melody.

{% capture ex2 %}X:2
T:A two voice sequence
M:4/4
L:1/2
K:C
V:1
c f-| f e-| e d-| d c-| c B| c2|]
V:2 clef=bass
C, A,| G, G,| F, F,| E, E,| D, D,| C,2|]
w:C:{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

While there are some variations on how you could harmonize this sequence, it is possible to make a chord progression that has diatonic chords with roots separated by a P5. I have suggested a version of this below. Using my progression, try adding a third voice as an alto line. As you do this, remember that the sequential pattern will not start until the second measure, so the first measure can just fill out missing chord tones. Your line does not have to have all stepwise motion like the outer two voices do, but it should follow some sort of repeating pattern.

{% capture ex3 %}X:3
T:Harmonizing a two voice sequence
M:4/4
L:1/2
K:C
V:1
c f-| f e-| e d-| d c-| c B| c2|]
V:2 clef=bass
C, A,| G, G,| F, F,| E, E,| D, D,| C,2|]
w:C:I IV6 V7 I6/4 IVM7 viio6/4 iii7 vi6/4 ii7 V6/4 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

The next example uses my suggested alto voice. It provides the required missing chord tones for each chord in this progression.

{% capture ex4 %}X:4
T:Filling in the sequence
M:4/4
L:1/2
K:C
V:1
[cE] [fc]| [Bf] [ec]| [Ae] [Bd]| [Gd] [Ac]| [cF] [GB]| [E2c2]|]
V:2 clef=bass
C, A,| G, G,| F, F,| E, E,| D, D,| C,2|]
w:C:I IV6 V7 I6/4 IVM7 viio6/4 iii7 vi6/4 ii7 V6/4 I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

In your classification of the two-voice progression above, you likely described each line individually (e.g. descending diatonic 2nds that last one whole note), or you may have described the intervals between the two lines for each measure (e.g. a diatonic 7th resolving to diatonic 6th, then repeating after transposing down a diatonic 2nd). Neither of these is sufficient, however, once we add a third voice.

Instead, we classify *harmonic* sequences by describing the movement of the *roots* of each chord. We do *not* label harmonic sequences by inversions or the bass line. If we were to identify sequences by bass lines, all sequences that created a particular style of bass line (e.g. descending by stepwise motion) would be grouped together, even if they shared no harmonic similarities. (You can see this concept in the next two examples below.) Taking this into account, the description of the sequence in the example above would be:
- A diatonic harmonic sequence with root-movement by descending 5th that alternates between root-position seventh chords and second-inversion triads.

## Complex harmonic sequences

The above sequence has only one interval and direction in its root movement pattern, a descending P5. Similar to the final example of the melodic sequences above, though, it is also possible for harmonic sequences to have two or more parts within each repetition. Look at the example below, and classify it using our terms from above:
- ascending or descending
- diatonic or chromatic
- intervals of transposition
- length of pattern
- single or multiple parts within each repetition

{% capture ex5 %}X:5
T:A multi-part sequence
M:4/4
L:1/2
K:C
V:1
[eG] [Bd]| [cE] [GB]| [AC] [EG]| [AF] [BD]:|
V:2 clef=bass
C G,| A, E,| F, C,| F, G,:|
w:C:I V vi iii IV I IV V{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

Hopefully you were able to identify that the sequence only covers the first three measures, the final measure is simply a way to allow the pattern to repeat smoothly. For the sequence, there are two possibilities to describe it. You could consider each measure a pattern in which case you would say that this is a diatonic sequence that descends by 3rd. If you consider the pattern to be a half note, though, it has multiple parts. It is a diatonic sequence of triads that moves down by 4th and then up by 2nd. Either is correct, but they have different uses. The larger iteration makes for a cleaner, simpler analysis, but the smaller iteration communicates a more detailed explanation of the pattern. Choose the method that best suits your needs.

How does your description of the sequence change if we change some of the voices to alter the chords' inversions as in the example below?

{% capture ex6 %}X:6
T:Using inversions to create a smooth bass line
M:4/4
L:1/2
K:C
V:1
[eG] [Gd]| [cE] [EB]| [AC] [CG]| [AF] [BD]:|
V:2 clef=bass
C B,| A, G,| F, E,| F, G,:|
w:C:I V6 vi iii6 IV I6 IV V{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

## Commonly used sequences

#### Seventh chords following the circle-of-fifths

While any sequence that establishes a pattern and has clear voice-leading can function, there are common sequences that many composers have relied upon. We discussed the first of these in [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html) when exploring the voice-leading that creates the strong pull of the standard circle-of-fifths progression. Now that we understand the nature of sequences, look at each voice here as a melodic sequence. Does this change your view of standard voice-leading practices? Can you come up with a sequence description for this progression?

{% capture ex7 %}X:7
T:Circle of fifths sequence of triads
M:4/4
L:1
K:C
V:1
[GE]| [EG]| [EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[C,C]| [E,B,]| [A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:I iii vi ii V I{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

#### Parallel 6 chords

Sequences can also be used to explain how non-diatonic progressions function in a diatonic context. One common sequence occurs when first-inversion chords are used in succession to create a stepwise bass line. A *parallel 6 sequence* is any sequence with repeated first-inversion triads, most commonly moving downward by step. Notice that this does not create objectional parallel voices as long as the root of the chord stays above the chordal fifth. If these two voices are inverted, the result will contain parallel perfect fifths. To label a sequence of parallel six chords, label each chord with its Roman numeral and inversion figure and then place a bracket under the entire sequence with a label of "parallel six sequence."

{% capture ex8 %}X:8
T:Parallel 6 chords
M:4/4
L:1/2
K:C
V:1
[eg] [gd]| [fc] [eB]| [dA] [cG]| [BF] [cE]|]
V:2 clef=bass
C B,| A, G,| F, E,| D, C,|]
w:C:I V6 IV6 iii6 ii6 I6 viio6 I{% endcapture %}
{% include abc-example.html number="8" abc=ex8 %}

#### The Pachelbel sequence

Another of the most commonly used sequences is known as the Pachelbel sequence.

{% capture ex9 %}X:9
T:Pachelbel's sequence
M:4/4
L:1/2
K:C
V:1
[eG] [Bd]| [cE] [GB]| [AC] [EG]| [AF] [BD]:|
V:2 clef=bass
C G,| A, E,| F, C,| F, G,:|
w:C:I V vi iii IV I IV V{% endcapture %}
{% include abc-example.html number="9" abc=ex9 %}

This sequence takes its name from the German Baroque composer, Johann Pachelbel, who composed a canon using this sequence as its foundation. Since then, the harmonic progression has become a common structure on which to build multiple styles of music. The comedian Rob Paravonian satired many of these takes in his now famous "Pachelbel Rant". **(Caution: contains language not suitable for all ages)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/JdxkVQy7QLM" frameborder="0" allowfullscreen></iframe>

Further to our discussion of the importance of patterns in music, please view the following TED Talk by Dr. Scott Rickard. He used mathematics to try to create music without any repetition, and the results are...interesting.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RENk9PK06AQ" frameborder="0" allowfullscreen></iframe>
