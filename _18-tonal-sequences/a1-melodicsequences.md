---
layout: chapter
title: 18a Lesson - Melodic Sequences
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
- single or multiple parts within each iteration

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
