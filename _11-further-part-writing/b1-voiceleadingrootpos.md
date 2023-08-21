---
layout: chapter
title: Lesson 11b - Voice-leading for Root Position Triads and Seventh Chords
abc: true
---

We can view the voicing rules (i.e. spacing, range, doubling, and voice-crossing) as our guidelines for creating the vertical aspect of this style of music, and our voice-leading rules (i.e. tendency tones, conjunct lines, and avoiding part-writing errors) as guidelines for creating the horizontal aspect of this style of music. By combining these ideas with a general knowledge of diatonic chord progressions, we can begin composing our first attempts at chorale-style music.

Before beginning, please remember that when composing in this style, you occasionally will need to bend, or even break, these rules to accommodate other musical goals. There is not a "right" or "wrong" hierarchy for the conventional rules of part-writing. For example, you might choose to accept parallel perfect 5ths if you are trying to create a particular melodic line that emphasizes stepwise motion. Or, you might decide to use voice-crossing of the inner voices to change the timbre and texture of a passage. So even the cleverest of composers may choose to eschew convention if it does not align with their musical goals, but for our beginning attempts, you should do your best to observe every rule in order to understand their importance and implementation.

## Reviewing our part-writing process

In [Unit 11a]({{ site.baseurl }}/11-further-part-writing/a1-funds-of-part-writing.html), we outlined a method for harmonizing a melody:
1. Identify the key
2. Determine your phrase
3. Choose a cadence to complete your phrase.
4. Create the rest of the diatonic progression beginning on tonic and ending with your cadence.
5. Compose a bass line based on your harmonization.
6. Fill in the alto and tenor voices.

And we employed the stylistic guidelines that we studied in Unit 10 to act as the framework for our part-writing.
- follow the standard harmonic progressions outlined by circle-of-fifths progressions
- correctly use cadences
- use functions such as tonic, dominant, and pre-dominant as general guides
- employ the smoothest possible voice-leading for each line
    - The bass can be slightly more disjunct than the upper parts, particularly when using root-position chords.
- do not cross voices
- avoid spacing or range errors
- avoid incorrect doubling
- resolve tendency tones correctly
- avoid unacceptable part-writing such as parallel perfect 5ths/8ves, contrary perfect 5ths/8ves, similar 5ths/8ves, and unequal 5ths

Remember that circle-of-fifths progressions work because the voice-leading taps into the primary functions of diatonic harmony. If you review [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html), you will remember that we created the harmonic flow chart by simply following good voice-leading between chords that have roots separated by a descending P5/ascending P4. Admittedly, long strings of root-position chords create unmelodic bass lines, but they still represent the strongest voicing for many sonorities. 

## Getting started

To give you a chance to create all four voices, we will now compose a four-part chorale using a circle-of-fifths progression. Because you now have harmonies and a bass line composed for you, you can use the same process as above but replace steps 3 and 4 (and 5 if given a pre-determined bass line from the harmony): 
- **Write a simple melody (soprano line)** 
    - Use mostly stepwise motion.
    - A good phrase will have an overall arc (upward or downward) with only one climax. 
    - Leaps of a fourth or more should resolve by stepwise motion in the opposite direction.

Try to create a clean and simple texture. Write the soprano line from the given first pitch, and then fill in the inner voices following the guidelines above.

{% capture ex1 %}X:1
T:Circle-of-fifths triadic progression
M:4/4
L:1
K:C
V:1
c| x| x| x| x|]
V:2 clef=bass
[C,]| [A,,]|[D,]| [G,,]| [C,]|]
w:C:I vi ii V I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

After you have completed your harmonization, make sure to double-check it for part-writing errors. If you feel good about your attempt, try changing your melody and trying again.

### Conclusion

After attempting this for the first time, most students are surprised at how relatively simple this process is once you get started. Your first harmonization from above was probably similar to this:

{% capture ex8 %}X:8
T:Circle-of-fifths triadic progression
M:4/4
L:1
K:C
V:1
[cE]| [cE]| [dF]| [dG]| [cE]|]
V:2 clef=bass
[C,G,]| [A,,A,]|[D,A,]| [G,,B,]| [C,C]|]
w:C:I vi ii V I{% endcapture %}
{% include abc-example.html number="8" abc=ex8 %}

Because the chord progression provides a vertical framework and the focus on smooth voice-leading provides a horizontal framework, most of the process is simply following a pattern. This example is admittedly straightforward, because it relies entirely on root-position triads in a circle-of-fifths progression.

## Adding the seventh

In studying music theory, we will often spend more time discussing the exceptions to rules than the actual rule itself. And even though the general rule for resolving chordal sevenths--*chordal sevenths resolve down by step*--is fairly consistent, there are common situtations in which you will be forced to break this rule (e.g. pre-determined melodies, sequences, etc.) Make downward stepwise resolution your default until you are forced to choose otherwise. 

Try adding the following two seventh chords to our circle-of-fifths progression, making sure to pay attention to how your chordal thirds and sevenths are resolving. The first chord is fully voiced to force you into certain decisions, so you will need to start from the beginning rather than working your way backward.

{% capture ex2 %}X:2
T:Root-position part-writing with
T:seventh chords and root movement by P4/P5
M:4/4
L:1
K:C
V:1
[cE]| x| x| x| x|]
V:2 clef=bass
[C,G,]| [A,,]|[D,]| [G,,]| [C,]|]
w:C:I vi7 ii V7 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusion

The addition of seventh chords create problems to solve as you now must contend with additional tendency tones. The first arises between the second and third chords. If you simply choose the smoothest voice-leading possible for each voice going into the second chord, vi<sup>7</sup>, you will place the chordal seventh in the tenor voice. This locks the voice-leading of the tenor voice into resolving downward by step to the third of the following ii chord, and in turn, that chordal third has its own tendencies and should resolve upward by step to the the root of the next chord. This means that the initial placement on the vi<sup>7</sup> effectively locks the entire tenor voice into place. From there, our alto voice is predetermined, because we do not want to double the third of the ii chord, leaving us with only the closest D or A. If we were to move to the A, that would create parallel perfect 5ths with the bass voice, so we can only choose the D for the alto voice. To move to the next chord, if we do not alter our soprano voice, we are then forced to place a B in the tenor voice which creates a less melodic tenor line.

{% capture ex10 %}X:10
T:Root-position part-writing with
T:seventh chords and root movement by P4/P5
M:4/4
L:1
K:C
V:1
[cE]| [cE]| [dD]| [dF]| [cE]|]
V:2 clef=bass
[C,G,]| [A,,G,]|[D,F,]| [G,,B,]| [C,C]|]
w:C:I vi7 ii V7 I{% endcapture %}
{% include abc-example.html number="10" abc=ex10 %}


While this works, it leaves many strange voicings, such as the tripled roots of the ii and I chords as well as the unmelodic tenor line. There is a simpler option. It is easier to have the alto voice jump slightly to the the chordal seventh on the vi<sup>7</sup> which leads to the following progression.

{% capture ex9 %}X:9
T:Root-position part-writing with
T:seventh chords and root movement by P4/P5
M:4/4
L:1
K:C
V:1
[cE]| [cG]| [dF]| [dF]| [cE]|]
V:2 clef=bass
[C,G,]| [A,,A,]|[D,A,]| [G,,B,]| [C,C]|]
w:C:I vi7 ii V7 I{% endcapture %}
{% include abc-example.html number="9" abc=ex9 %}

Notice that the chordal third in the alto voice of the ii chord defies its tendency to resolve upwards to the root, and instead, uses static motion to become the chordal seventh of the V<sup>7</sup>. This is our first example of having to make a choice between two guidelines--is it better to prioritize smooth part writing or tendency tone resolution? In this case, the smooth voice-leading creates a fuller overall texture by allowing for less doubling and tripling, so I prefer that option. You could, however, prefer the other sound and prioritize your tendency tones.

## Exploring options

Of course, there are multiple chords in our circle-of-fifths progressions that have root movement by intervals other than 4ths and 5ths. Try harmonizing the following short chord progressions while observing our guidelines. Keep track of what types of root movement create the most issues while developing at least two possibilities for each of the progressions.

{% capture ex3 %}X:3
T:Short chord progressions
T:Treat each measure as a separate progression
M:4/4
L:1/4
K:C
V:1
cxxx|| cxxx|| cxxx|| cxxx|]
V:2 clef=bass
[C,] [F,,] [G,,] [C,]|| [C,] [F,,] [G,,] [A,,]|| [C,] [D,] [F,] [G,]|| [C,] [D,] [G,,] [C,]|]
w:C:I IV V7 I I IV V vi I ii IV V I ii7 V7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusions

When you were harmonizing these short progressions, which chord progression presented the most issues? For most, it will likely be when the progressions that have root-movement by 2nd, particularly a progression like IV-V-vi. Let's examine this by isolating a common example of this movement, V moving to vi. In this progression, the V is acting according to its standard dominant function, but the vi chord has replaced the I chord in the position where a tonic chord usually appears. This progression represents a *functional substitution* in which vi is now acting as the tonic function. (This concept has application within the dominant and pre-dominant functions as well, but we need to explore first-inversion chords in the next topic, 11b, before we are ready for that discussion)

### Function over Form (Part 1)

A *functional substitution* can, and often should, inform your voice-leading. When a root-position V chord precedes a root-position vi chord, we must choose to prioritize either our *doubling* conventions or our *part-writing* conventions. More specifically, do we want to double the third or do we want to end up with parallel perfect 8ves/5ths? We can demonstrate this by looking at two nearly identical progressions. Harmonize the following two progressions; first with the standard tonic function (i.e. V to I) and then with the functional substitution (i.e. V to vi.) Even though the I chord and vi chord have two common tones--the first and third scale degrees--you will have to make very different choices to avoid voice leading errors.

{% capture ex4 %}X:4
T:Using a functional substitution for a deceptive cadence
M:3/4
L:1/4
Q:1/4=60
K:C
V:1
[cE][B][c]| ] [cE][B][c]|]
V:2 clef=bass
[C,G,] [G,,] [C,]| [C,G,] [G,,] [A,,]|]
w:C:I V I I V vi{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

When attempting this deceptive cadence, you hopefully realized that you cannot allow the tenor voice to remain on G and then resolve to A because it creates parallel octaves with the bass voice. Because the vi chord acts as a replacement for a I chord when it is part of a deceptive cadence, we double the scale degree that works best for a I chord, `do`, rather than the standard doubling of the root, `la` or fifth, `mi`. In this progression, it is correct to break standard convention for doubling and double the chordal third of the vi chord. This doubling should now be your permanent convention for deceptive cadences.
- When V goes to vi, the vi chord is replacing the tonic function and therefore functions as a I<sup>sub6</sup>

So for the above example, a better approach would be to alter the melody to allow for a doubling of the chordal third of the vi chord.

{% capture ex11 %}X:11
T:Using a functional substitution for a deceptive cadence
M:3/4
L:1/4
Q:1/4=60
K:C
V:1
[cE][dG][cE]|]
V:2 clef=bass
[C,G,] [G,,B,] [A,,C]|]
w:C:I V vi{% endcapture %}
{% include abc-example.html number="11" abc=ex11 %}

### Root movement by 2nd

The other difficult resolution in the previous example was when the root position IV chord moved to the V chord. We do not have a *functional substitution* to provide a doubling exception here, so instead you must be careful about how you resolve the voices. Harmonize the following progression without altering the given pitches, and pay particular attention to the direction that the upper voices resolve as you avoid part-writing errors.

{% capture ex5 %}X:5
T:Root movement by 2nd
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[cE] [c] xx|]
V:2 clef=bass
[C,G,] [F,,] [G,,] [C,]|]
w:C:I IV V I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

#### Conclusion

Now that we are dealing with root movement of an interval other than a perfect fourth, you cannot solely rely on simple voice leading guidelines such as "chordal third moves upward by step to the root of the following chord." While this will still hold true when moving from V to I in this example, the the IV and V chords are separated by a 2nd. So if you solely rely on smooth, stepwise voice-leading, you will likely create objectionable parallel movement between the two chords. For example, when composing he soprano line as you move from the IV to the V chord, you cannot choose `re`, because this creates parallel perfect 5ths against the bass. So you must choose to move to the leading tone instead which locks your soprano line into `C - C - B - C`. From there, you will have to use some small skips in your other voices to resolve every voice in the smoothest possible way. There are a few different options for this progression, but you likely ended up with something like this.

{% capture ex12 %}X:12
T:Completed root movement by 2nd
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[cE] [cF] [BD] [cE]|]
V:2 clef=bass
[C,G,] [F,,A,] [G,,G,] [C,G,]|]
w:C:I IV V I{% endcapture %}
{% include abc-example.html number="12" abc=ex12 %}

## Common exceptions

### Third to third
There are some commonly used exceptions to our general part-writing conventions. For example, when a chord progression has a root that moves down by P5, we expect the chordal third to resolve up by step to the root of the following chord. However, if you need to change the texture of your part-writing to be more or less compact, you may choose to have the chordal third leap to the following chordal third which changes the entire voicing possibilities of the two chords. (Note that you can only use this on the leading tone if it is in an inner voice.) 

As you can see in the example below, the third of the V chord leaps to the third of the I chord. It is awkward to sing, but it allows the chords to transition for an open voicing (more than an octave between soprano and tenor) to closed voicing (less than an octave between soprano and tenor). This kind of resolution should be used sparingly.

{% capture ex6 %}X:6
T:Chordal third to chordal third
M:4/4
L:1/4
Q:1/4=60
K:C
V:1
[eG] [dG] [c2G]|]
V:2 clef=bass
[C,C] [G,,B,] [C,2E]|]
w:C:I V I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

### Frustrated leading tone

Another common exception is called the *frustrated leading tone*. While not considered ideal voice-leading, you can occasionally choose to resolve the leading tone by skipping downward to the root of the tonic chord, **if the leading-tone is in an inner voice**. This can solve doubling issues if you are trying to fix an incomplete triad by adding the chordal fifth. You can see examples of this in the tenor voice in the following two progressions. Notice that this allows you to create a deceptive cadence without having to double the chordal third of the vi chord.

{% capture ex7 %}X:7
T:Frustrated leading tone
M:3/4
L:1/4
Q:1/4=60
K:C
V:1
[eG] [dF] [cE]|| [eG] [dF] [cE]|]
V:2 clef=bass
[C,C] [G,,B,] [C,G,]|| [C,C] [G,,B,] [A,,A,]|]
w:C:I V7 I I V7 vi{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

## Overall conclusions for root-position part-writing

When first asked to compose a simple chorale, it is easy to feel paralyzed as you consider all of the rules and guidelines that you have learned. Luckily, if you develop an order to process the guidelines, they greatly simplify the part-writing process. It is much simpler to write a melody when you only have one or two options for the next pitch!

As stated above, you should use smooth voice-leading when possible, making it a high priority in your decision-making process. But what constitutes "smooth" voice-leading? The simple answer is that stepwise, or sometimes static, motion is preferred, although this is only one decision point to consider. When you are creating a line, you will need to balance stepwise motion against avoiding errors. For our simple chorale-style, we are not using non-chord tones yet, so your next pitch must be a chord-tone. This means that you must also consider the notes that are already present such as the bass line or melody in order to ensure that you form a complete harmony and avoid errors. When you add in doubling and range limitations, you can usually narrow your options to one pitch. 

You should also understand that while there are some general guidelines for resolving tendency tones, there are no simple rules that are unbreakable. At its most basic, `ti` resolves up by step, and `fa` resolves down by step. When part-writing, however, this is too simplistic a view. For example, `fa` often moves upward by step to `sol`, either as part of an ascending scalar melodic line or in the bass line when a pre-dominant chord (i.e. IV or ii<sup>6</sup> moves to a root-position V chord. A more advanced part-writer may think that `ti` and `fa` are tendency tones when they are part of a V<sup>7</sup> chord, so therefore, the rule for tendency tones should be that *chordal thirds* resolve up by step and *chordal sevenths* resolve down by step. This is a better rule, but it also falls apart when we leave circle-of-fifths progressions (chords with roots separated by a descending P5). When a IV chord moves to a V chord, it is impossible for the third to move *up by step* to the root of the V chord. For now, the easiest rule for tendency tones is:
- *Chordal thirds* resolve up by step and *chordal sevenths* resolve down by step *when part of a circle-of-fifths progression*.

### Our part-writing process

As a review, here are our finalized methods for part-writing in a four-part chorale style:

### If given a melody:

- **Identify the key**
    - Look for melodic patterns, starting pitches, and ending pitches for clues as to an implied key. 
- **Determine your phrase**
    - In a short excerpt such as many of your assignments, you will have little room for decision making, but for a larger melody, try singing the phrase repeatedly and listen to your natural inclination for breaths or pauses. 
    - It can also be helpful to look for spots in which the rhythm slows naturally.
- **Choose a cadence** to complete your phrase.
    - Refer to [Unit 7c]({{ site.baseurl }}/07-harmonic-functions/c1-cadences.html) to review the types of cadences.
- **Create the rest of the diatonic progression** beginning on tonic and ending with your cadence. (If not already provided.)
    - This will establish your key center. Refer to [Unit 6b]({{ site.baseurl }}/06-intro-harmonic/b1-diafuncvoicelead.html) for a review of the three primary harmonic functions: tonic, dominant, and pre-dominant.
    - Refer to [Unit 7a]({{ site.baseurl }}/07-harmonic-functions/a1-diaprogcirclefifths.html) to determine a functional harmonic progression.
- **Compose a bass line** based on your harmonization.
    - This will resemble 1:1 counterpoint, so refer to [Unit 5b]({{ site.baseurl }}/05-counterpoint-embell-shapes/b1-cantfirmand1st.html).
    - It is okay for the bass line to be more disjunct than the other voices, so feel free to leave your chords in root position to make doubling simpler.
    - Contrary motion against the soprano line is preferred.
- **Fill in the alto and tenor voices.**
    - Refer to the rules for voicing, range, and doubling in [Unit 6c]({{ site.baseurl }}/06-intro-harmonic/c1-voiceleadingerrors.html).
- When writing your parts, always **strive to have voice-leading that is as smooth as possible** by emphasizing stepwise motion.
    - As mentioned above, bass lines are the exception and will often have more leaps, especially when using root-position chords.

### If given a harmonic progression (and likely a bass line):

- **Remember to check your key**
    - Even though you have been given the key in this case, make sure to follow the guidelines for this mode (i.e. major or minor). 
- **Determine your phrases via cadences**
    - In longer examples, you will need to identify your cadences before moving to the next step. You can look for spots in which the harmonic rhythm slows naturally.
    - Refer to [Unit 7c]({{ site.baseurl }}/07-harmonic-functions/c1-cadences.html) to review the types of cadences.
- **Write a simple melody (soprano line)** 
    - Use mostly stepwise motion.
    - A good phrase will have an overall arc (upward or downward) with only one climax. 
    - Leaps of a fourth or more should resolve by stepwise motion in the opposite direction.
- **If the harmony does not give you a predetermined bass line, compose a bass line.**
    - This will resemble 1:1 counterpoint, so refer to [Unit 5b]({{ site.baseurl }}/05-counterpoint-embell-shapes/b1-cantfirmand1st.html).
    - It is okay for the bass line to be more disjunct than the other voices, so feel free to leave your chords in root position to make doubling simpler.
    - Contrary motion against the soprano line is preferred.
- **Fill in the alto and tenor voices.**
    - Refer to the rules for voicing, range, and doubling in [Unit 6c]({{ site.baseurl }}/06-intro-harmonic/c1-voiceleadingerrors.html).
- When writing your parts, always **strive to have voice-leading that is as smooth as possible** by emphasizing stepwise motion.
    - As mentioned above, bass lines are the exception and will often have more leaps, especially when using root-position chords.

 I next asked them to add two seventh chords along with the rule that the *chordal seventh should resolve down by step*.
