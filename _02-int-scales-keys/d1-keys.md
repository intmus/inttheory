---
layout: chapter
title: Lesson 2d - Key Signatures
abc: true
---

As discussed in the previous topics, scales represent a pitch collection, centered around a tonic pitch. Because we can transpose these pitch collections to center around any pitch-class, we create twelve unique pitch centers--called *keys*--and even more if we include enharmonic equivalents. (Some argue that there are fifteen key centers, one for each key signature. Theoretically speaking, there as many keys as we have pitch names, but we can leave that argument for another time.) Because writing accidentals for every pitch would be clunky and difficult to read, we use a system of *key signatures*--a shorthand collection of flats or sharps at the beginning of each staff--to give performers a simple way of knowing which pitches in the key are raised and lowered.

## Key signatures

Diatonic music is built around perfect intervals, although as we will see below, introducing one non-perfect interval to a series of perfect intervals creates the major scale and consequently diatonic tonality. Because of this non-perfect interval, key signatures follow a very simple pattern that can be reversed whether you are raising or lowering pitches.

### Goals for this topic

In the examples below, you will find sets of three keys. Use these to find:
- the order of sharps and flats
    - including any mnemonic devices to remember these
    - and the intervallic structure of the order of sharps and flats
- what differentiates *diatonic* and *chromatic* pitches
- a method for determining the *relative* and *parallel* minor keys from a major key
    - as well as the *relative* and *parallel* major keys from a minor key

#### A caveat

Please remember from our discussion of scales and modes that any *scale* that shares a tonic note is considered to be one key. Even though this may contradict your intuitive thoughts, this means that G major and G minor are considered the same **key**! Instead, we call them *modes* of each other, not different keys. While somewhat pedantic, this will help our discussions of modulation and mode mixture once we begin studying chromatic harmony.

### Keys that use sharps and the minor keys that are related to them

Accidentals are added to the key signature from left to right, so using the examples below, you can compare the relation of the tonic to the newly added sharps to develop an order in which you would add more sharps to a key signature. 

Pay particular attention to which **scale degrees** are affected in each key as sharps are added. Is it the same scale degree in each key? How is this related to the tonic? If you continue the pattern, are you able to discern the name of the next key and which accidentals are added? You should also be able to determine the relationship between a major key and its parallel and relative minors.

{% capture ex1 %}X: 1
T:3 major scales that use sharps
M:4/4
L:1/8
K:G clef=bass
G,,A,, B,,C, D,E, F,G, ||[K:D] D,E, F,G, A,B, CD||[K:A] A,,B,, C,D, E,F, G,A,|]
w: G maj _ _ _ _ _ _ D maj _ _ _ _ _ _ A maj{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}


{% capture ex2 %}X: 2
T:3 natural minor scales that use sharps
T:Each of these minor keys is a *relative* minor to the major key listed in parentheses
M:4/4
L:1/8
K:G clef=bass
E,,F,, G,,A,, B,,C, D,E, ||[K:D] B,,C, D,E, F,G, A,B,||[K:A] F,,G,, A,,B,, C,D, E,F,|]
w: E min (G maj) _ _ _ _ B min (D maj) _ _ _ _ F-sharp min (A maj){% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}


{% capture ex3 %}X: 3
T:3 more natural minor scales
T:Each of these minor keys is a *parallel* minor to the major key listed in parentheses
M:4/4
L:1/8
K:Bb clef=bass
G,,A,, B,,C, D,E, F,G, ||[K:F] D,E, F,G, A,B, CD||[K:C] A,,B,, C,D, E,F, G,A,|]
w: G min (G maj) _ _ _ _ D min (D maj) _ _ _ _ _ _ A min (A maj){% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Keys that use flats and the minor keys that are related to them

Use these examples to determine the order of flats in the same way. As before, pay particular attention to which **scale degrees** are affected in each key as flats are added. Is it the same scale degree in each key? How is this related to the tonic? If you continue the pattern, are you able to discern the name of the next key and which accidentals are added? You should also be able to determine the relationship between a major key and its parallel and relative minors.

{% capture ex4 %}X: 4
T:3 major scales that use flats
M:4/4
L:1/8
K:Bb clef=bass
B,,C, D,E, F,G, A,B,|| [K:Eb] E,F, G,A, B,C DE|| [K:Ab] A,,B,, C,D, E,F, G,A,|]
w: B-flat maj _ _ _ _ _ E-flat maj _ _ _ _ _ A-flat maj{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}


{% capture ex5 %}X: 5
T:3 natural minor scales that use flats
T:Each of these minor keys is a *relative* minor to the major key listed in parentheses
M:4/4
L:1/8
K:Bb clef=bass
G,,A,, B,,C, D,E, F,G,|| [K:Eb] C,D, E,F, G,A, B,C|| [K:Ab] F,,G,, A,,B,, C,D, E,F,|]
w: G min (B-flat maj) _ _ _ C min (E-flat maj) _ _ _ F min (A-flat maj){% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}


{% capture ex6 %}X: 6
T:3 more natural minor scales
T:Each of these minor keys is a *parallel* minor to the major key listed in parentheses
M:4/4
L:1/8
K:Db clef=bass
B,,C, D,E, F,G, A,B,||[K:Gb] E,F, G,A, B,C DE||[K:Cb] A,,B,, C,D, E,F, G,A,|]
w: B-flat min (B-flat maj) _ _ E-flat min (E-flat maj) _ _ A-flat min (A-flat maj)(A maj){% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

## Conclusions

In the next topic, we will discuss how the overtone series creates our perception of pitch, tonality, and music as a whole. But for now, we can observe that one aspect of the overtone series, the circle-of-fifths, plays a critical role in defining diatonic function and key signatures. The order of sharps and flats follows a series of ascending perfect 5th intervals for sharps and a descending perfect 5ths for flats.
- Order of sharps: F - C - G - D - A - E - B
- Order of flats: B - E - A - D - G - C - F

Note that the two orders are simply reversed sequences of each other. 

### Tips for finding major key signatures

Your ultimate goal for key signatures should be the ability to instantly recall all key signatures from memory, but there are two common tricks that you can use to find the major key implied by any key signature.

1. For any key signature with two or more flats, the name of the key is the *second to last flat* when reading from left to right. For example, in a key signature with four flats, the four flats from left to right are B-flat, E-flat, A-flat, and D-flat. The second to last flat is A-flat, so A-flat major is the implied major key of this key signature.
2. For any sharp key signature, you can go up a half-step (minor 2nd) from the last sharp to find the tonic of the implied major key. For example, in a key signature with four sharps, the sharps are F-sharp, C-sharp, G-sharp, and D-sharp when read from left to right. The last sharp is D-sharp and a minor 2nd above D-sharp is E-natural. So E major is the implied major key of this key signature.

Of course, these tricks do not work for C major (no sharps or flats) or F major (one flat), but you should be able to remember those two keys.

### Tips for finding minor key signatures

You can combine the two tricks above with your knowledge of relative major and minor keys to quickly find the implied minor key of a key signature, because relative major and minor keys *share a key signature*. For example, if you know that a key signature of four sharps implies E major, you can go to the sixth scale degree of E major to find the tonic of the relative minor--in this case, C#. Therefore, E major and C-sharp minor both share a key signature of four sharps.
