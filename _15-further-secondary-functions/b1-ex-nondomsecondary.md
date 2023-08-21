---
layout: chapter
title: 15b Lesson - Non-dominant Function Secondary Chords
abc: true
---

Secondary chords can be extended beyond the dominant function, creating further tonicization of a chosen chord.

## Extending toniczation

For the following chorale, provide leadsheet symbols and a Roman numeral analysis. There are multiple chromatically-altered chords, some of which cannot be explained as secondary dominant or secondary leading-tone chords. And while it might be tempting to label a minor v chord in your analysis, that doesn't explain what the listener is hearing. Instead focus on looking for "pockets" of tonality, in which you might be able to explain a progression easier through the lens of another key. 

As with all analysis, you should never dwell too much on an individual chord in your first attempt. If you get stuck, just move to the next chord. It is helpful to start with leadsheet symbols when working with chromatic harmony, because it allows you to label chords by their construction before worrying about each chord's function and relationships.

{% capture ex1 %}X:1
T:Other secondary functions
M:4/4
L:1/2
K:C
Q:1/2=60
V:1
[c/2E][B/2F][cE]| [dG][eG]| [dF][dF]| [c2E]|]
V:2 clef=bass
[C,/2G,][D,/2G,][C,G,]| [_B,D,][A,^C,]| [A,D,][G,,B,]| [C,2G,]|]
w:C:{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusion

At first glance (and hearing), the G minor triad seems starkly out of place. We have seen minor v chords in previous examples, but in each case, they followed the defined conventions of one of our alternate functions such as a passing or pedal functions. Here, the minor v chord does not fit the typical voice-leading of tertiary functions--it does not create the passing bass line typical of passing chords, nor does it have an obvious pedal voice--so we need to examine the context of this example. 

The chord following the G minor triad is a clear V<sup>6/5</sup>/ii which then resolves to a ii chord. If you look through your leadsheet symbols, you can see a pattern that extends backwards if you continue thinking in the key of ii (D minor). In the key of ii, a G minor chord is a diatonic iv chord, which would make this a iv-V-i progression in that key. Therefore, the correct labeling of this example is iv<sup>6/4</sup>/ii -- V<sup>6/5</sup>/ii -- ii. Without a stable cadence, we have not changed keys, but this progression clearly emphasizes and extends our pre-dominant harmony.

{% capture ex3 %}X:3
T:Other secondary functions
M:4/4
L:1/2
K:C
Q:1/2=60
V:1
[c/2E][B/2F][cE]| [dG][eG]| [dF][dF]| [c2E]|]
V:2 clef=bass
[C,/2G,][D,/2G,][C,G,]| [_B,D,][A,^C,]| [A,D,][G,,B,]| [C,2G,]|]
w:C:I V4/3 I iv6/4/ii V6/5/ii ii V7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

## Secondary or diatonic?

Because of the nature of diatonic progressions, there is a great deal of crossover between non-dominant secondary functions and the actual diatonic chords of a key. Provide a Roman numeral analysis of the following chorale, paying particular attention to the second chord. Is it diatonic or a secondary function?

{% capture ex2 %}X:2
T:Ambiguous secondary functions
M:4/4
L:1
K:C
V:1
[cE]| [cE]| [dA]| [dF]| [cE]|]
V:2 clef=bass
[C,G,]| [A,,A,]| [^F,,C]| [G,,B,]| [C,G,]|]
w:C:{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Conclusion

The second chord, the A minor triad, is clearly a vi chord in the key of C major. It is worth noting however, that because this chord is followed by a secondary dominant, this chord also functions perfectly in the secondary key as a non-dominant secondary function. The third chord is a  V<sup>7</sup>/V which tonicizes the key of G major. If you extend this key backwards, the A minor chord functions as a ii/V chord.

You do not need to label this as anything other than a vi chord in C major, because it is fulfilling its standard diatonic function in every way. However, this further illustrates how fluid harmony can become when thinking of the relationships between keys and voice-leading.
