---
layout: chapter
title: Lesson 7a - Using Voice-leading to Create a Harmonic Progression
abc: true
---
<!-- Before teaching this lesson, make sure that they have attempted to resolve V7 to I in two voices in their previous homework as part of 6b. You can then use their findings from how the members of the V7 chord resolve to the I chord to move through this discussion more quickly. -->

We now have the analytical foundation and tools to begin studying harmonic *function*--how and why a chord works with other chords to build tonality. In this lesson, we will derive the basic aspects of function by studying how two major concepts from previous units are related:
1. *Scalar tendencies* - When written as a scale, diatonic collections are a sequence of five whole steps and two half-steps--the major scale, for example, is W-W-H-W-W-W-H--as shown in [Unit 2c]({{ site.baseurl }}/02-int-scales-keys/d1-keys.html). The inherent tension in the scale comes from the two half-steps, and we studied this by demonstrating that altering a single interval in a circle-of-fifths--more specifically, changing any of the P5 intervals to a d5--will always create a smaller cycle through seven diatonic pitches. This specific alteration creates the variation necessary for a diatonic collection, establishing `ti` and `fa`, and consequently creating the two scalar tendenices necessary for dominant and tonic  function.
2. *Voice-leading* - As shown in the two-part examples in [Unit 6b]({{ site.baseurl }}/06-intro-harmonic/b1-diafuncvoicelead.html), the progression from V<sup>7</sup> to I creates a strong and natural sense of resolution. There are many reasons we hear this progression as a strong cadence, but perhaps the strongest reason is the voice-leading between the V<sup>7</sup> and I chords--meaning the way in which individual pitches naturally pull toward each other. 

As a side note, the significance of cultural conditioning cannot be overlooked. A person who grows up listening to *any* style of music will be conditioned to hear the tendencies used in that music as a natural progression, and this holds true for those raised around music descended from the diatonic tradition. This does not change the importance of voice-leading in forming these progressions, but it is worth remembering the difference between laws, rules, and strategies discussed in the first reading from Unit 6.

The examples below demonstrate how these half-steps create this the foundation of diatonic harmony. If you understand the voice-leading principles that pull the V chord into the I chord, you can then extend these rules to create the basic progression from which all diatonic harmony evolves.

## Goals for this topic

The next five examples will help you begin creating the logic behind the voice-leading of standard diatonic harmonies. To use these, study each example before moving on to the next and form a hypothesis regarding the voice leading--i.e. which chord tones resolve or pull to other chord tones. Once you have developed a theory as to how and why the progression works, move to the next instruction to see if your hypothesis can be applied to create the next idealized harmony. If it cannot, alter your hypothesis to account for both examples. Continue this way until you have found voice-leading rules that account for all of the examples.

**This example has two idealized progressions of a V chord resolving to a I chord: one as triads and the other with a seventh chord.** 
- Study how each voice resolves. 
    - It is tempting to focus on which scale degree resolves to which scale degree (e.g. `ti` to `do`), but this does not provide a complete explanation. 
    - Instead focus on the how each chordal member resolves in the progression. This should include the chordal member to which it resolves and the interval necessary to do so.
        - Try to discern which chordal members have multiple options and which seem locked into a specific resolution.
- What pitches are doubled? Are any omitted?

{% capture ex1 %}X:1
T:Basic V to I progressions
M:4/4
L:1
Q:1/4=100
K:C
V:1
[BG]| [cG]|| [BF]| [cE]|]
V:2 clef=bass
[G,D]| [C,E]|| [G,D]| [C,C]|]
w:C:V I V7 I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

**The next example focuses on a simple triadic progression and follows the circle-of-fifths backwards to add a ii chord. Does this follow the voice-leading explanation that you created after looking at the first examples? If not, how does it differ? After you have studied this, try creating a voicing for a vi chord that would precede the ii chord.**

{% capture ex2 %}X:2
T:Adding the ii chord
M:4/4
L:1
Q:1/4=100
K:C
V:1
[FA]| [BG]| [cG]|]
V:2 clef=bass
[D,D]| [G,,D]| [C,E]|]
w:C:ii V I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

**The next example adds the vi chord. Were you able to correctly construct this using your voice-leading rules? Is it more accurate to explain the voice-leading of the progression using chordal members or scale degrees? If you continue around the circle-of-fifths, what would the voicing for the next chord be?**

{% capture ex3 %}X:3
T:Adding the vi chord
M:4/4
L:1
Q:1/4=100
K:C
V:1
[EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:vi ii V I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

**Again, we ask the same questions. Were you able to correctly add the iii chord using your voice-leading rules? Is it more accurate to explain the voice-leading of the progression using chordal members or scale degrees?**

{% capture ex4 %}X:4
T:Adding the iii chord
M:4/4
L:1
Q:1/4=100
K:C
V:1
[EG]| [EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[E,B,]| [A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:iii vi ii V I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

As we look at implied harmony in two-voice counterpoint, we can demonstrate that simple voice-leading is all that is necessary to *imply* diatonic function. If we take that further, we should be able to create the fundamentals of harmonic progression using the voice-leading inherent in diatonic systems.

Beginning theory students often learn two general rules of thumb for voice-leading:
- `ti` resolves to `do`
- `fa` resolves to `mi`

This is helpful to begin thinking about voice-leading in the most basic of ways, but it only applies to a specific, albeit common, set of circumstances that arise in common practice harmony--the V<sup>7</sup> to I progression. In contrast to those rules, look at the following two-voice outline of one of the most common progressions in tonal music.

{% capture ex6 %}X:6
T:Implied harmonies from two voices
M:4/4
L:1/2
Q:1/4=80
K:C
V:1
cA| Bc|]
V:2 clef=bass
E,F,| G,C,|]
w:C:I6 IV V I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

In this common progression, the bass voice moves `fa` to `sol`, and it sounds acceptable to almost anyone's ear. From this alone, you should infer that there is far more detail necessary to understand voice-leading.

So instead, you must base your general rules around *chordal members* and their resolutions, rather than scale degrees and their resolutions. Specifically:
- For chords that have roots separated by a P5:
  - The *third* of the first chord resolves to the *root* of the second chord.
  - The *seventh* of the first chord, if present, resolves to the *third* of the second chord.
  - If both chords are in root position, the bass voice moves from the *root* of the first chord to the *root* of the next chord.

Before moving on, take a moment to check these rules against the finished example from above, copied below for your convenience.

{% capture ex7 %}X:7
T:Adding the iii chord
M:4/4
L:1
Q:1/4=100
K:C
V:1
[EG]| [EA]| [FA]| [BG]| [cG]|]
V:2 clef=bass
[E,B,]| [A,,C]| [D,D]| [G,,D]| [C,E]|]
w:C:iii vi ii V I{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

You can also alter this example to include seventh chords in order to apply the chordal seventh resolutions, but we will do that in the next topic.

## Adding IV and vii<sup>o</sup>

**Beyond the iii chord, the voice-leading runs into an issue with harmonic function. While it is possible to continue this pattern through these two chords, in tonal harmony, the IV and vii<sup>o</sup> chords actually function most often as if they are extensions of the ii<sup>7</sup> and V<sup>7</sup> chords respectively. Look at the following example to see voice-leading using both of these chords. The first measure uses the ii<sup>7</sup> and V<sup>7</sup> chords as part of a diatonic progression, but the second progression substitutes the IV for the ii<sup>7</sup> chord and the vii<sup>o</sup> chord for the V<sup>7</sup> chord. After looking at this example, explain why IV and vii<sup>o</sup> function similarly to ii<sup>7</sup> and V<sup>7</sup>.**

*Please note that to demonstrate how closely related these chords are, many voice-leading rules of common practice harmony are broken in this example--most notably the parallel octaves between the soprano and bass between vii<sup>o</sup> and I. This is for demonstration purposes only, do not assume that this is standard voice-leading for IV or vii<sup>o</sup>. We will discuss the rules of voice-leading in this style when we study part-writing in Units 10 and 11.*

{% capture ex5 %}X:5
T:Adding the IV and viio chords
M:4/4
L:1
Q:1/4=100
K:C
V:1
[Fc]| [BF]| [cE]|| [Fc]| [BF]| [cE]|]
V:2 clef=bass
[D,D]| [G,,D]| [C,C]|| [A,,C]| [B,,D]| [C,C]|]
w:C:ii7 V7 I IV6 viio I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

### Conclusions

It is possible to continue our voice-leading pattern backwards to add the last two diatonic chords, IV and vii<sup>o</sup>, but these chords actually function differently. Instead, the IV and vii<sup>o</sup> chords function similarly to their two functional counterparts, ii<sup>7</sup> and V<sup>7</sup>. The logic is fairly simple, if you remove the root from a ii<sup>7</sup> chord, `D-F-A-C` in C major, you are left with a IV chord, `F-A-C`. Likewise, if you remove the root from a V<sup>7</sup> chord, you are left with a vii<sup>o</sup> chord. By this logic, the IV and vii<sup>o</sup> chords often use alternative voice leading, because their tendency tones are not necessarily tied to the chordal thirds and sevenths. 

When we add these to our harmonic progression flowchart, we get our basic outline for harmonic progressions.

| (*unnamed*) | (*unnamed*) | pre-dominant | dominant | tonic |
--- | --- | --- | --- | --- |
| iii | vi | ii | V | I |
| | | IV | vii<sup>o</sup> | |

Using just this flowchart, you can build basic chordal progressions for a given melody by harmonizing the pitches with the correct progressions. Please note that the I chord can comfortably jump back to anywhere in the progressions.

## Adding in Exceptions

There are a few common exceptions that should be added to this progression flowchart. We will discuss how these are used as we work through their appropriate topics (e.g. cadences, chordal substitutions), but for now, please add them to your list of possible progressions.
- *lateral progressions* - chords that have the same function can move to each other
    - V can move to vii<sup>o</sup>, and vii<sup>o</sup> can move to V
    - ii can move to IV, and IV can move to ii.
- *deceptive progressions* - V can move to vi 
    - This is most commonly used at the end of a phrase. In this case, vi is "replacing" a I chord and assuming a tonic function, so it must be used  and voice carefully. See [Unit 8a]({{ site.baseurl }}/08-cadences-phrasing/a1-cadences.html) for a full explanation of cadences.
- *plagal progressions* - IV can go to I
    - This is most commonly used at the end of a phrase, and in this case, IV is "replacing" the V chord. This is another cadence, so it must be prepared properly. It is better to avoid using this progression in the middle of a phrase, so in your early attempts at part-writing, do not attempt to use this.
- UNCOMMON: vi can move to V
    - There are instances where vi will move to V, but in these cases, it is best to think of the vi chord as taking on a tonic function. In your early part-writing, do not use this progression, because like V moving to vi--a much more common progression--this progression is likely to result in poor voice-leading.
- RARE: iii can move to IV
    - It is difficult to use this without creating multiple voice-leading issues, so in your early attempts at part-writing, do not attempt to use this.

## Changes in Minor

Minor follows all of the same progressions and exceptions, but the chord qualities change to match the naturally occurring pitches in the key signature. Please remember that minor keys must have a major V chord and diminished vii chord to function diatonically. This means that both of these chords are built using the raised seventh scale degree, even though this isn't necessarily implied by the Roman numeral of the vii<sup>o</sup>.

| (*unnamed*) | (*unnamed*) | pre-dominant | dominant | tonic |
--- | --- | --- | --- | --- |
| III | VI | ii<sup>o</sup> | V | i |
| | | iv | vii<sup>o</sup> | |
