---
layout: chapter
title: 17a Lesson - An introduction to mode mixture
abc: true
---

When first studying tonal harmony, the seemingly endless options for musical progression is daunting, so it can be helpful to look through the lens of rigid structure. Because of this, we have studied harmonic function thus far through the diatonic framing of separate major and minor keys, however in most tonal music, the relationship between modes is more fluid. 

## Mode mixture (modal interchange)

Look at the following chart of the chords of parallel major and minor keys. Compare the chords built off each diatonic scale degree. (e.g. I to i, ii to ii<sup>o</sup> How many of these chords match qualities? Does this fit with your perception of distantly-related keys as we defined in the previous unit?

C major | Chord | Chord | C minor
 --- | --- | --- | ---
 I | C maj | C min | i
 ii | D min | D dim | ii<sup>o</sup>
 iii | E min | E-flat maj | III
 IV | F maj | F min | iv
 V | G maj | G maj | V
 vi | A min | A-flat maj | VI
 vii<sup>o</sup> | B<sup>o</sup> | B<sup>o</sup> | vii<sup>o</sup>

You will notice that the only common chords are the dominant function chords, and even these *require* alteration in minor to share function and qualities. So if we think about this as we did when discussing modulations, these keys should have little in common. On the other hand look at the following basic progressions in both keys. Do these look unrelated? How does the voice-leading differ between the two? How many chromatic pitches are required to make the second progression function?

{% capture ex1 %}X:1
T:Variations between parallel major and minor
M:4/4
L:1/2
Q:1/2=60
K:C
V:1
[cE] [cE]| [dF] [BF]| [c2E]|]
[K:Eb] [cE] [cE]| [dF] [=BF]| [c2E]|]
V:2 clef=bass
[K:C] [C,G,] [A,,A,]| [D,A,] [G,,G,]| [G,2C,2]|]
w:C:I vi ii V7 I
[K:Eb] [C,G,] [A,,A,]| [D,A,] [G,,G,]| [G,2C,2]|]
w:c:i VI iio V7 i{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusion

Even at a glance, you should see that the voice-leading in these two progressions is identical with the only differences between the two resulting from the altered pitches in the key signature. In particular, the resolution from the sixth scale degree to the fifth scale degree is strengthened in minor, because the resolution becomes a half-step between le and sol.

## Borrowing from the parallel minor

When studying the voice-leading of these two parallel modes, they seem almost interchangeable.

And they are.

Alter the following progression in C major to "borrow" either the VI or ii<sup>o</sup> chords from minor. What chordal members do you have to alter for each chord? What scale degrees are these? When you play it back does it sound acceptable? What if you alter both chords? Does this make it more or less jarring?

{% capture ex2 %}X:2
T:Borrowing chords from the parallel minor
M:4/4
L:1/2
Q:1/2=60
K:C
V:1
[cE] [cE]| [dF] [BF]| [c2E]|]
V:2 clef=bass
[K:C] [C,G,] [A,,A,]| [D,A,] [G,,G,]| [G,2C,2]|]
w:C:I vi>bVI ii>iio V7 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusions

To borrow either ii<sup>o</sup> or VI from minor, you must alter the sixth scale degree for both, and the VI also requires an altered third scale degree. Regardless of which chord you alter--or both--the progression is functional and convincing. Borrowing from the parallel minor mode darkens the progression without changing any of the voice-leading functions. Also, take note of how the roots of chords are affected. The ii chord has a root of `re` in either the major or minor mode and changes only in quality from a D minor to a D diminished chord. The vi chord undergoes a more substantial change, because not only does its quality change from minor to major, but it does this by changing the actual root of the chord from `la` to `le`. Forgetting to alter the root when borrowing chords from different modes is one of the most common mistakes that students make when studying borrowed chords in mode mixture, so always check your roots before building the chord.

Perhaps more importantly than even understanding which chords can be borrowed, you must look at how they function. In this example, we are borrowing chords directly from a circle-of-fifths progression. *They are still fulfilling their diatonic function, because the voice-leading is tendencies are the same regardless of mode.* As with all Roman numeral analysis, its purpose is to explain the function and provide context for a progression. So even though the quality of this ii chord has changed and is no longer diatonic, the meaning of the Roman numeral doesn't change unless you alter it with further information such as labeling it as a passing or pedal chord. If you put ii<sup>o</sup> without further explanation, you are saying that it still has a pre-dominant function in this context.

## Further borrowing from the parallel minor

The next progression is a longer example containing multiple cadences. Try borrowing each chord individually from the parallel minor. Which chords work and which don't? Once you have an idea of which chords function best, try combining these into a single progression. How many chords can you borrow before it simply sounds as if its in minor? 

{% capture ex3 %}X:3
T:More borrowing from the parallel minor
M:4/4
L:1/2
Q:1/4=90
K:C
V:1
[c2E]| [dF] [BF]| [c2E]| [cF] [dF]| [c2E]|]
V:2 clef=bass
[C,2G,]| [F,,A,] [G,,G,]| [A,,2C]| [A,,A,] [B,,A,]| [C,2G,]|]
w:C:I ii6 V7 vi IV6 vii%7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

Almost every chord can be substituted for its minor counterpart in this progression without changing its function. The pre-dominant and tonic functions can all be borrowed without altering their function, although altering the tonic functions quickly changes the sense of whether we are operating in the major or minor mode.

There are two chords that cannot be borrowed. The first is the minor v chord; if you borrow this, you undermine the fundamental core of diatonic tonality, so it sounds as if someone simply played a wrong note. The other non-borrowable chord for this progression is the major VII chord that would be built off of B-flat. Both of these chords demonstrate the importance of the resolution from the leading tone to the tonic to establish dominant and tonic function. This is the basis for tonal harmony.

Of note, you *can* borrow the vii<sup>o7</sup> from minor because it still has a leading tone.

## Borrowing from the parallel major

The next example uses the same progression in minor. Alter one chord at a time to borrow it from the parallel major, and pay careful attention to which scale degrees you are altering. Which progressions sound acceptable to you? How does the voice-leading change when starting in minor? Pay careful attention to any enharmonically equivalent resolutions.

{% capture ex4 %}X:4
T:Borrowing from the parallel major
M:4/4
L:1/2
Q:1/2=60
K:Eb
V:1
[c2E]| [dF] [=BF]| [c2E]| [cF] [dF]| [c2E]|]
V:2 clef=bass
[C,2G,]| [F,,A,] [G,,G,]| [A,,2C]| [A,,A,] [=B,,A,]| [C,2G,]|]
w:c:i iio6 V7 VI iv6 viio7 i{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

## Roman numeral notation of mode mixture

It is because of mode mixture that we have followed strict guidelines when labeling Roman numerals to this point. By having each part of a Roman numeral describe an isolated chord tone, we are able to accurately describe even borrowed chords.

Chordal member | Default implied pitch | To raise by semitone from default | To lower by semitone from default
 --- | --- | --- | ---
 root | diatonic scale degree* | sharp symbol in front of Roman numeral** | flat symbol in front of Roman numeral**
 third | based on case of Roman numeral | upper case (M3) | lower case (m3)
 fifth | P5 above root | add <sup>+</sup> after Rom num | add <sup>o</sup> after Rom num
 seventh | m7 above root | add <sup>M</sup> before inversion figure | add <sup>o</sup> before inversion figure***

* - Because a raised leading tone is necessary for *diatonic* function in minor, it is not necessary to show the raised root of the vii<sup>o</sup> chord in the Roman numeral (i.e. #vii<sup>o</sup>). This is the only chord in this system for which you have to make an assumption regarding an altered pitch. This also means that in minor, there are two possible chords that will have different roots but not have Roman numeral alterations. The assumed diatonic chord, vii<sup>o</sup> built off of the leading tone `ti`, as well as the the naturally occurring VII chord, built off of the subtonic `te`.
* 
 ** - For clarity's sake, we **always** use a sharp or flat symbol to show that we are raising or lowering the root, even if you are actually adding a natural.

 *** - Because the diminished <sup>o</sup> implies the interval of a d5 AND a d7, you must use the half-diminished symbol if you wish to alter the fifth but leave the chordal seventh as a m7 above the root.

Test your knowledge of this by writing the correct borrowed chords for every diatonic chord in a parallel major and minor. You may use the following chart as a model. With all of these make sure that you build the chord off of the correct root. For example, students often forget that to build a major VI chord in major, the root is altered thereby changing the entire chord. (In C major for example, the borrowed bVI chord is *not* an A major triad.)

Roman numeral in major | Borrowed from parallel minor | Roman numeral in minor | Borrowed from parallel major
 --- | --- | --- | ---
 I || i |
 ii || ii<sup>o</sup> |
 iii || III |
 IV || iv |
 V || V |
 vi || VI |
 vii<sup>o</sup> || vii<sup>o</sup> |

## Commonly used mode mixture

As you discovered above, certain chords do not sound good -- or function at all -- when borrowed. Because of this, there are a few chords that are borrowed most often.

Because of voice-leading resolutions, it is easiest to borrow chords while in major. The most commonly borrowed chords in major are:
- vii<sup>o7</sup> (requires lowered ^6)
- iv (requires lowered ^6)
- ii<sup>&oslash;7</sup> (requires lowered ^6) 
- ii<sup>o</sup> (requires lowered ^6)
- bVI (requires lowered ^6 and ^3)
- bVII (requires lowered ^7)
    - Be careful to look at the function of this chord. Label it as V/III if it resolves to a borrowed bIII chord. Label it as bVII if it resolves in any other way.
- bIII (requires lowered ^7 and ^3)

Minor is more limited due to voice-leading limitations, but the following chords are commonly borrowed:
- I (requires raised ^3)
    - This is often used to end a minor piece in Baroque and Classical music. It is used often enough that it has a unique name: the Picardy (Picardie) third
- IV (requires raised ^6)
    - Commonly results when used in first inversion to create a scalar bass line of sol-la-ti-do
- #vi (requires raised ^6 and ^3)
    - Commonly results when used in root position to create a scalar bass line of sol-la-ti-do
