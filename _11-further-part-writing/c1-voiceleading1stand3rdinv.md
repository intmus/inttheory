---
layout: chapter
title: Lesson 11c - Voice-leading for First and Third Inversion Chords
abc: true
---

First-inversion and third-inversion chords are used to make smoother, more melodic bass lines, but in doing so, we put tendency tones--and all of the accompanying expectations--into the bass. Even though this seems more restrictive, first- and third- inversion chords actually allow more freedom in part-writing because:
- they remove the potential objectionable parallels that come from having the root in the bass.
- the upper voices have one less tendency tone to distribute and resolve correctly.

## Resolving tendency tones

Use the voicing and voice-leading guidelines discussed in the previous topic to harmonize the following progressions as a four-part chorale. Assuming that the progression follows the circle-of-fifths, what inversion should follow a first-inversion chord? What about the chord following a third-inversion? As always, make note of any difficulties that you encounter for the class discussion.

{% capture ex1 %}X:1
T:First- and third-inversion chords
T:in circle-of-fifths progressions
M:3/4
L:1/4
Q:1/4=70
K:C
V:1
[cE]xx| [cE]xx|| [cE]xx|]
V:2 clef=bass
[C,G,] [B,,] [C,]| [C,G,] [B,,] [C,]| [C,G,] [F,] [E,]|]
w:C:I V6 I I V6/5 I I V4/2 I6{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusions

With first and third inversion chords, we place either the chordal third or chordal seventh in the bass. Both of these chord tones are tendency tones, and tendency tones in outer voices follow fairly strict rules in this style. 

For first-inversion triads and seventh chords in circle-of-fifths progressions, the bass note should resolve up by step to the root of the following chord, meaning that the chord following a first-inversion chord will likely be in root position. For third-inversion seventh chords (there are no third-inversion triads), the chordal seventh in the bass should resolve down by step, and if it is a circle-of-fifths progression, the bass will resolve to the chordal third of the next chord making it a first-inversion chord.

Of course, these guidelines assume that we are harmonizing circle-of-fifths progressions. If you do not have roots that are separated by P4/P5, we can create guidelines using functional substitutions.

## Function over form (Part 2)

When harmonizing the the root-position deceptive progression from the previous topic, we discussed that you should treat the vi chord in a deceptive progression as a *functional substitution* for tonic. Because the vi chord acts as a tonic function when part of a deceptive progression, we double the scale degree that works best for the standard tonic chord, `do` of the I chord, rather than the general part-writing doubling rule for root position chords in which you would prefer to double the root. This means that in the deceptive progression, it is correct to break standard doubling convention and double the chordal third of the vi chord. Now that we are looking at first inversion voice-leading, we have another *functional substitution* to discuss.
- vii<sup>o</sup> is a dominant function, so therefore functions as V<sup>7</sup> chord without its root

Because of this, the vii<sup>o</sup> chord must follow different *doubling* rules in order to avoid poor voice-leading. With this in mind, try to harmonize the following progressions; first a simple I-V<sup>6/5</sup>-I progression, and then with an added root-position vii<sup>o</sup> chord. You will discover that:
- the two chords have all but one pitch in common.
- resolving a root-position vii<sup>o</sup> is extremely difficult and will require one voice to make consecutive jumps of a P5 to avoid issues due to tendency tone resolutions.**

{% capture ex2 %}X:2
T:Voicing a viio using functional substitution
M:4/4
L:1/4
Q:1/4=70
K:C
V:1
[cE] xx2|| [cE] xxx|]
V:2 clef=bass
[C,G,] [B,,] [C,2]|| [C,G,] [B,,] [B,,] [C,]|]
w:C:I V6/5 I I viio V6/5 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

Because the root position vii<sup>o</sup> triad is so difficult, it is rarely used. It is not possible to resolve a root-position vii<sup>o</sup> triad to a I chord without breaking at least one part-writing norm. A root-position vii<sup>o</sup> must either pass through another chord or be inverted to resolve directly to I.

As a general rule of thumb, any diminished triad (including the ii<sup>o</sup> in minor) will typically need to have the chordal third doubled, because the tension of the diminished fifth and its tendency tones.

## Function over form (Part 3)

The pre-dominant function presents an issue that the functional substitutions in tonic and dominant functions do not. To this point, we have considered the circle-of-fifths as the voice-leading foundation for diatonic harmony. In this case, the ii chord would be the "primary" pre-dominant function, and in many ways, this is true. The IV chord, however, holds a special place in harmony because of its role as the *subdominant*--the opposite pole of the dominant--as well as the high frequency throughout history of the I-IV-V-I progression.

Generally speaking, root position ii chords and root position IV chords are equally strong and follow standard doubling conventions. When the ii chord is in first inversion, however, it can be voiced as if it is the functional substitution of a root-position IV chord meaning that a ii<sup>6</sup> chord often takes its doubling from a root-position IV chord. (In the same way that a vii<sup>o</sup> chord takes its doubling from a V<sup>7</sup> chord.) Try this on the following progressions. (Make sure to consider the common direction and motion for upper voices tend to do when a root position IV chord moves to a V chord.)

{% capture ex3 %}X:3
T:Using functional substitutions for pre-dominants
M:4/4
L:1/4
Q:1/4=70
K:C
V:1
[cE]xxx| [cE]xxx|| [cE]xxx|]
V:2 clef=bass
[C,G,] [F,,] [G,,] [C,]| [C,G,] [F,,] [G,,] [C,]| [C,G,] [F,,] [G,,] [C,]|]
w:C:I IV V I I ii6 V I I ii6/5 V I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

While it is certainly possible to voice the pre-dominant function chords in these progressions following standard doubling conventions, it can create less than appealing voicings for the ii chord, particularly in its triad form. When in first inversion, you may choose to double the third of the ii, in which case, it is acting as a functional substitution of a root-position IV chord. 

{% capture ex5 %}X:5
T:Using functional substitutions for pre-dominants
M:4/4
L:1/4
Q:1/4=70
K:C
V:1
[cE][dF][BD][cE]|]
V:2 clef=bass
[C,G,] [F,,A,] [G,,G,] [C,G,]|]
w:C:I ii6 V I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

## Passing chords

Thus far, we have only described a chord's function using the *primary* functions of tonic, dominant, and pre-dominant. We now add a new category of functions called *tertiary* functions. We will discuss all varieties of tertiary function in Unit 11d, but we need to introducte our first type of tertiary function, the *passing chord*, because of its prevalence in first- and third-inversion part-writing. (If you are wondering why we are skipping over secondary functions, we will cover those in Unit 14.) A *passing chord* is a chord that is inserted between two other chords to create stepwise motion within a voice, usually in the bass line. You can consider *passing* a function that removes a chord's standard function (i.e. tonic, dominant, and predominant), and instead extends the function of the chords on either side. 

Let's see how this works by attempting an example that seemingly breaks all of our harmonic progressions norms. When you first look at the progression below, you should immediately notice that a V chord resolves to a IV chord--which does not follow our harmonic flowchart of primary functions. While this is generally true, there is something happening here that requires you to look at the bigger picture. Try to harmonize the following progression using your best voice-leading, and as you do so, pay particular attention to the motion within each voice. You will notice that there is no tenor voice in the first chord, so you may try multiple options to see if you can find a solution for a tenor voice that fulfills all guidelines thus far.  

{% capture ex4 %}X:4
T:Passing chords
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[cE][d][c][d]| [c]4|]
V:2 clef=bass
[C,][B,,][A,,][G,,]| [C,]4|]
w:C:I V6 IV6 V7 I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

### Conclusions

In the example above, the melodic, stepwise motion of the bass line traps us into making some difficult harmonic choices. We want to end on a PAC, which means that as we extend the progression backward, we don't have any choices that would follow our standard harmonic flowchart of primary functions. (Please refer to Unit 7a if you need a refresher on primary functions in diatonic harmony.) We can use a pre-dominant function on beat 3 to lead to our dominant function chord on beat 4, but there are no primary function harmonies that lead to a pre-dominant that also incorporate the leading tone of the bass line. (Of note, the I<sup>M7</sup> is not used in this style of composition; you are welcome to try it and you will notice that it doesn't sound too out of place, but we would analyze this as two beats of a I chord with a passing tone (non-chord tone) on the second beat of the bass line.)

The solution is to use another dominant chord on beat 2. Even though we would not normally have a dominant harmony resolve to a IV chord, in this case, the IV chord is not functioning as a IV chord with its typical primary function as a pre-dominant chord. Instead, it has taken on a *tertiary function* as a *passing chord*. Look at the voice-leading within each voice of this completed example:

{% capture ex6 %}X:6
T:Passing chord extending dominant function
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[cE][dD][cF][dF]| [cE]4|]
V:2 clef=bass
[C,G,][B,,G,][A,,A,][G,,B,]| [C,C]4|]
w:C:I V6 IV6 V7 I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

If you were to ignore the fact that beat 3 forms a standard triad, you can assign each voice on beat 3 to a standard non-chord tone label, as if it were not part of a harmony.
- The soprano voice is a neighbor tone between the two Cs.
- The alto voice is an anticipation of the F on beat 4. (Or simply a chord tone if you consider this to be the chordal 7th of the V<sup>7</sup>.)
- The tenor voice is a passing tone between beats 2 and 4.
- And most importantly, the bass voice is a passing tone between beats 2 and 4.
So even though a V chord does not usually resolve to a IV chord, in this particular case, it only *looks* as if it is resolving to a IV chord. In reality, each voice is simply moving through a non-chord tone...which happens to form a standard triad on beat 3. So instead of trying to label the IV chord as having a standard function, you would say that it's function is extending the dominant function on either side of it.

So when this happens, we still want to acknowledge that the chord exists, but we also want to note that it is no longer a primary function. We will discuss the notation of of tertiary functions more in the next topic, but for now, label them using their standard Roman numeral and inversion figure, but put the Roman numeral inside of parentheses with a label of "pass" directly beneath it. Note that passing chords--meaning chords who create passing motion in one or more voices--act as if they are a group of non-chord tones. You may even think of them as "non-chord tone chords" if that helps. A listener will hear this progression as an extension of the dominant function, not as an alternating dominant/pre-dominant/dominant pattern. Any inversion of a chord can be classified as a passing chord as long as it creates stepwise motion in one or more voices--usually the bass voice--and it is common for many first- and third-inversion chords function this way.

You may also notice that we have an unusual doubling on the IV<sup>6</sup> chord, but once we discuss second inversion chords in the next unit, we will be able to update the guidelines for doubling chord tones to more closely reflect what exists in music.
