---
layout: chapter
title: 23d Lesson - PC Set Inversion
abc: true
---

Transposition is the most commonly used set manipulation, but there is a second commonly used function that is of equal importance to understanding pc sets.

## Inversion

When first studying tonal harmony, we discussed the scale degree names in pairs: dominant/subdominant, mediant/submediant, subtonic/supertonic. For each of these pairs, there is a duality to their naming in that they share a relationship centered around the tonic pitch. For example, the dominant is a P5 *above* the tonic where the subdominant is a P5 *below* the tonic. They are mirrored around the central pitch, and therefore represent an *inversion* of each other.

In set theory, we can perform this same operation using intervals (i.e. numbers of half-steps). Take a moment to think about how to translate the concept of inversion from traditional intervals (e.g. P5,M3) into pitch-class integers. What kind of results do you expect for integer notation? Remember that to find an inversion of any musical pitch, you need two pieces of information: the starting pitch class and the pitch class *around* which you will invert. 

## Visually inverting pitch classes

Depending on the central pitch used to invert, pitch-class integer notation can make inversion relatively easy. It does not require you to understand a specialized pitch and interval system like traditional notation. Instead, it only requires basic mathematical functions. 

Before tackling the mathematical approach to inverting pitch-class integers, let's visually explore inversion using the pitch class continuum below. For simplicity's sake, let's start by centering our inversions around C/0. To visually find an inversion, pick a letter/integer on the chart below. Count the number of steps it takes to reach C/0, and then continue past C/0 for the same number of steps. (You can think of it as balancing the scale.) Of course, you will find that each positive integer is paired with its negative integer; 5 becomes -5, 8 becomes -8, etc. If you were to create a chart showing all inversion pairs as letter names, what patterns do you notice about the pairings? For example, how does the 7/-7 pair compare to the 5/-5 pair? Also, what is the inversion for C/0? Why?

-e | -t | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | e
 --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
 C# | D | D# | E | F | F# | G | G# | A | A# | B | C |  C# | D | D# | E | F | F# | G | G# | A | A# | B

### Conclusions

Your first chart should have 12 pc sets, although two of them are technically only one pitch name -- C/0 and F#/6 end up inverting on top of themselves. However, as you look at the pairs, do you see a pattern? How many *unique* pc sets are there if you only look at pitch letter names?

Inversion Pair 1 | Inversion Pair 2
 --- | ---
 C | C
 C# | B
 D | A#
 D# | A
 E | G#
 F | G
 F# | F#
 G | F
 G# | E
 A | D#
 A# | D
 B | C#

As you hopefully can see, there are only six *unique* inversion pairs once you eliminate duplicates by examining pitch letters. For example, 5 and -5 are F and G respectively, but 7 and -7 are G and F respectively. This creates a phenomenon that we will refer to as inversion pairs. Anytime that you are using fixed-zero notation (C=0), you can simply memorize these six pairs as written above and always have access to all inversions. If you change your center point, however, it will change the pairs. You can see this by shifting all of the letters in the above number line in either direction. As soon as you assign zero to a different center pitch, you have to create a new chart of inversion pairs. You can see what would happen if we shifted all of the letters one space to the left, making C# our new zero (C#=0):

 -e | -t | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | e
 --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
 D | D# | E | F | F# | G | G# | A | A# | B | C |  C# | D | D# | E | F | F# | G | G# | A | A# | B | C

Any function that may involve inversion is the main reason that we employ fixed-zero notation: the calculations are easier if you can memorize only one set of inversion pairs.

## Applying Mod12

When we were to only look at the pitch-class *integers* in the above pairings, we still have 12 unique pc sets because negative numbers differentiate the sets. But we also know that in dealing with pitch-class integers, we can represent *any* integer as a pitch class between 0 and 11 using Mod12. (This is also a visual demonstration of how *octave equivalency* works.) If you look at the chart below, you can see what happens when we apply Mod12 to a series of integers; it creates a continuously repeating set of integers between 0 and 11, which means that inversion is as simple as memorizing the six pairs above as long as you are using fixed-zero as your inversion axis--the specific pitch class around which we are inverting.

-e | -t | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | e
 --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | e | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | e

 This means that the inversion pairs when inverting around zero (and 6) are:

 Inversion Pair 1 | Inversion Pair 2
 --- | ---
 0 | 0
 1 | e
 2 | t
 3 | 9
 4 | 8
 5 | 7
 6 | 6

Because mod12 creates a continuously repeating series of 12 integers, you may use the visual aid of a clock to help you find inversions. First, draw a clock (with 0 in the place of 12). Then draw a line between 0 and 6; this line will represents the center around which you will invert your pitches. To find your inversion pairs, connect the integers by a line that is perpendicular to the center line (i.e. integers that are directly across the line), and you will see that you create the same set of inversion pairs above. If you were to move your center line to connect a different set of opposites, say 2 and 8, what would this represent?

## Finding inversions mathematically

As with transposition, we have shorthand to represent inversion. To show the inversions around zero used to create the chart above we would write:

T<sub>0</sub>I (0,1,2,3,4,5,6) = (0,e,t,9,8,7,6)

As you can see, each pitch class in the result is just the inversion of the corresponding pitch class in the original pc set. If you were to put the result in normal form you would get (6,7,8,9,t,e,0).

What if you wanted to invert *and* transpose a pc set? Try inverting and transposing the following pc set, but do it two different ways to see if you get the same results:
- Transpose first, then invert
- Invert first, then transpose

T<sub>4</sub>I(1,5,6)

Did you get the same result either way? If not, why are they different? Which do you think is correct? Why?

## The shortcut

Inverting first will always give you the correct answer, because in that case you are inverting *around zero* and then transposing. If you transpose first, you are actually inverting around a different axis. You can think of this easily using the clock face. If you invert first, you invert around the 0/6 axis and then you transpose the result. If you transpose first, you move the axis of transposition, and then you invert around that.

Luckily there is a mathematical shortcut for inverting around zero and transposing. Look at the following correctly solved examples. Do you see a simple way to find the answers given only the numbers in the formula? It may be helpful to think of the original number series that we used at the top of the page, before we converted it using mod12. To make it easier to find the shortcut, the results have purposely *not* been put into normal form, although you should always do so after inverting.

T<sub>t</sub>I(2,6,7) = (8,4,3)

T<sub>5</sub>I(2,6,7) = (3,e,t)

T<sub>9</sub>I(2,6,7) = (7,3,2)

T<sub>0</sub>I(2,6,7) = (t,6,5)

### Conclusion

To quickly invert and transpose, just subtract each member of your pitch class from `n` in the formula `T<sub>n</sub>I`. So in the first example above, n = t.

T<sub>t</sub>I(2,6,7) = (8,4,3)

If you subtract each pitch class from the inversion interval, which is t (or 10) in this case, you will get the resulting set.

- 10-2 = 8
- 10-6 = 4
- 10-7 = 3

You should get in the habit of putting these into normal form after inversion. If you transpose a pc set in normal form, it will still be in normal form. If you invert a pc set in normal form, you will have to find normal form again. Usually, the normal form of an inverted set the reverse order, but there are certain situations in which this will not be the case. You should always double-check your normal form to be sure.