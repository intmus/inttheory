---
layout: chapter
title: Lesson 6b - Establishing Diatonic Function through Voice Leading
abc: true
---

If we think back on our progression through the course thus far, we began by studying individual pitches, then combined those pitches into intervals, and then assembled those intervals sequentially and simultaneously to create melodies and chords respectively. Next, we studied a simplified version of counterpoint in order to examine how the combined vertical and horizontal aspects of music interact to create basic tonality. While counterpoint provides a framework for understanding harmony, it is primarily a study of how the horizontal aspect of music, melody, combines and *implies* harmony; it does not establish the vertical aspect of music, harmony, as a standalone concept. 

Therefore, we can use a simple counterpoint exercise to begin determining how harmony functions, because harmony is defined by the melodic tendencies of certain pitches within a diatonic scale.

## Implied harmony in two parts
<!-- When doing the following example, make sure that the class understands that each measure has the same two harmonies. It won't make sense to them otherwise. Also, after having listened to this once through and discussed the key and implied function with them, point out how they hear the first measure as having a major chord on the second beat even though there is no third or fifth. You can prove this to them by changing all of the Es to Ebs and then have them listen to it in minor. When you play the first measure again, they will now hear the second beat as having a minor third instead of a major third even though it's not there either time.-->

**Each measure of the next example implies the same two harmonies repeatedly--one on the first half note and the second on the second half note.**
- Which two harmonies do you think these measures imply? 
  - What are the Roman numerals and inversion figures for each measure?
  - Is there more than one option for any of the harmonies?
- Are all the intervals consonant? 
  - If not, to which chords do the dissonant intervals belong?  
- Do any particular chord members seem more important than the others? 
- Do any of these measures sound "weaker" than the others?

{% capture ex1 %}X:1
T:Implied harmonies from two voices
M:4/4
L:1/2
Q:1/4=80
K:C
V:1
Bc|| FE|| de|| Bc|| GE|| GG|]
V:2 clef=bass
"M3"G,"P8"C,|| "m7"G,"M3"C,|| "P5"G,"M3"C,|| "+4"F,"m6"E,|| "m6"B,,"M3"C,|| "M2"F,"m3"E,|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Conclusion

All of the two-voice progressions in the example imply harmonies of V moving to I in the key of C major, although you could make the argument that some of the implied harmonies are actually vii<sup>o</sup> instead of V<sup>7</sup>. The bass movement of the first three measures highlights V moving to I, but even once the bass movement changes, you should still hear the same progression of tension and release. 

From this, we may conclude that two voices--in this case a soprano line and a bass line--are enough to imply tonality. Furthermore, we can observe that the pitches within a V<sup>7</sup> chord pull toward resolving to the pitches of the I chord. One chord is stable and final, while the other wants to resolve to the stable and final chord.

This is *harmonic function*. A chord's function is a way of describing how it works within the context of tonal music.

## Harmonic functions in diatonic music

In this course, we will use a break harmonic function into three categories:
- *Primary* function
  - The foundation of creating tension and release in our tonal system. Every musical phrase must have chords that function in this category.
- *Secondary* function (Units 14 and 15)
  - These chords *borrow* primary function from a secondary key. 
- *Tertiary* function (Unit 11)
  - These chords *extend* the function of primary function chords.

For now, we will only focus on primary function chords. **Primary function** harmonies can be divided into three categories: *tonic*, *dominant*, and *pre-dominant*. 
- *Tonic* (**T**) harmonies feel stable and final.
  - This is primarily the I chord, but in some circumstances, this can include the vi chord.
- *Dominant* (**D**) harmonies are strong but unstable. They have a strong tonal gravity pulling toward a *tonic* harmony
  - This V and vii<sup>o</sup> chords are the most common dominant harmonies.
- *Pre-dominant* (**P**) harmonies are weak and unstable. Their tonal gravity pulls them toward *dominant* harmonies.
  - For our early discussions, you may consider this to be a broad category that includes all chords that do not function as either tonic or dominant. The most commonly used pre-dominant harmonies are ii, IV, and vi.  
  - Note that there is a difference between the words "pre-dominant" and "predominant".

### Some caveats on making assumptions based on this exercise

You may be tempted to make some definitive conclusions about voice-leading from looking at these examples--such as `ti` resolving to `do`, or `fa` resolving to `mi`--but be careful not to over-generalize with these ideas. If you make the assumption that `ti` always resolves to `do` without considering the context, you will make errors in situations where `ti` is not part of a dominant function. We will explore the true nature of tendency tones and their resolution in the next unit.

You may also notice that the chordal fifth is the least common chordal member in these examples, and as we will see when we begin voicing four-part harmony, the chordal fifth is indeed expendable. The root and third are best at implying a harmony, and the chordal seventh adds a strong resolution, whereas the fifth only provides a "fullness" to the chord. But not *all* chordal fifths are easily expendable, and sometimes composers will choose to imply/omit a chordal third (or even root!) given a particularly context. We will explore all of these ideas further in our part-writing studies.

## Cadences

Because of the importance of the V-I progression, we will introduce an important term in understanding harmony: the *cadence*. We will explore cadences further in the Unit 8, but for now, you may think of a cadence as a harmonic progression used to conclude a musical phrase. There are many types of cadences, but all of the progressions above are *authentic cadences*--cadences that have a V chord moving to a I chord. Bass movement is a key factor in determining the strength of a cadence. For example, measures 1 and 3 in the examples likely sound stronger to you than the last measure. The last measure not only lacks `sol` to `do` in the bass, it also does not have a tonic in the final chord. We will return to this idea when discussing cadences in detail in Unit 8a.
