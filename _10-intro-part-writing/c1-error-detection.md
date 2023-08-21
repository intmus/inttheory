---
layout: chapter
title: Lesson 10c - Error detection
abc: true
---

We have now studied the full array of part-writing errors for four-part chorale style compositions. Because there are so many possible errors, it can feel overwhelming to begin looking for errors, and it is easy to miss errors in long examples. I have developed a method for systematically identifying part-writing errors, and it not only helps to limit errors, it also helps students to understand the vertical and horizontal interactions that create part-writing errors.

Follow the steps from the list below when searching for errors. The next page gives specific examples of how to use this methodology for numbers 5 through 8.

1. *Voice-crossing*
    - Exception: alto and tenor may cross briefly if musically necessary
2. *Spacing*: In a four-part texture, are the top three voices within an octave of the adjacent voices?
3. *Range*
4. *Doubling* 
5. *Similar 5ths and 8ves*
    - Follow the soprano line looking for leaps
    - When a leap is found, look to see if there is similar motion in the bass (not parallel)
    - Determine the interval between the outer voices of the second chord. - If this interval is either a P5 or P8, there is a similar 5th or 8ve.
6. *Parallel Perfect 5ths and 8ves*
    - Determine the interval between each pitch horizontally (melodically -- NOT within each chord (vertically)
    - If one of the new vertical stacks of four intervals (numbers only) contains two matching numbers, check to see if the intervals within each chord (vertically) are P5s or P8s.
      - With triads, P5s must always have the root of the chord on the bottom of a major or minor chord. No other combination or chord can produce a P5.
       - P8s must come from doubled voices moving to doubled voices
    - If there are two consecutive P5s or P8s, those are parallel 5ths or 8ves.
7. *Unacceptable Unequal 5ths*
    - Should be found while looking for parallel 5ths using same method as above.
    - When completing step 2, if a d5 moves to a P5 and it involves the bass line, this is unacceptable unequal 5ths
8. *Contrary Perfect 5th and 8ves*
    - After the first part of the parallel perfect 5ths/8ves instructions, look for inverted pairs of numbers (e.g. 2 and 7, 3 and 6, 4 and 5) within each number stack
    - If one of the new vertical stacks contains one of these inversion pairs, check to see if the intervals within each chord (vertically) are P5s or P8s.
    - With triads, P5s must always have the root of the chord on the bottom of a major or minor chord. No other combination or chord can produce a P5.
    - P8s must come from doubled voices moving to doubled voices
    - If there are two consecutive P5s or P8s, those are contrary 5ths or 8ves.


We have already practiced finding errors in voicing:
1. *Voice-crossing*
    - Exception: alto and tenor may cross briefly if musically necessary
2. *Spacing*: In a four-part texture, are the top three voices within an octave of the adjacent voices?
3. *Range*
4. *Doubling* 

Finding part-writing errors is considerably more time-consuming, and it can be easy to miss errors if you do not approach it systematically. I have created a system that uses horizontal intervals to make it simpler and more consistent to find the four major part-writing errors. Use the examples below to explore the concepts, and then apply these on your homework.

## Finding similar fifths and octaves

As mentioned in the previous topic, the restrictive rules of *similar fifths and octaves* make these the simplest of the part-writing errors to find.

- *Similar 5ths and 8ves*
    - Follow the soprano line looking for skip of a 3rd or more
    - When a skip is found, look to see if there is similar motion in the bass (not parallel)
    - Determine the interval between the outer voices of the second chord. - If this interval is either a P5 or P8, there is a similar 5th or 8ve.

**Practice on this example.**

{% capture ex1 %}X:1
T:Similar octaves (S8)
M:4/4
L:1/2
K:C
V:1
[Ge] [AA]| [FA] [FB]| [c2E2]|]
V:2 clef=bass
[C,C] [CA,,]| [F,,C] [DG,,]| [C2C,2]|]
w:C:I vi IV V7 I{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Finding unacceptable parallels

- *Parallel Perfect 5ths and 8ves*
    - Determine the interval between each pitch horizontally (melodically -- NOT within each chord (vertically)
    - If one of the new vertical stacks of four intervals (numbers only) contains two matching numbers, check to see if the intervals within each chord (vertically) are P5s or P8s.
      - With triads, P5s must always have the root of the chord on the bottom of a major or minor chord. No other combination or chord can produce a P5.
       - P8s must come from doubled voices moving to doubled voices
    - If there are two consecutive P5s or P8s, those are parallel 5ths or 8ves.

**Practice these steps on the following two examples, even though it is fairly easy to find the parallel motion in these two examples visually.**

{% capture ex2 %}X:2
T:Parallel perfect octaves (PP8)
M:4/4
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,A,] | [B,G,] [C,C]|]
w:C:I ii6 V7 I{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

{% capture ex3 %}X:3
T:Parallel perfect fifths (PP5)
M:4/4
L:1/2
K:C
V:1
[cE] [AF]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [D,A,] | [DG,] [C,C]|]
w:C:I ii V7 I{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

## Finding unacceptable unequal fifths

Unacceptable unequal fifths will be found inadvertently while looking for parallel fifths and octaves using the steps outline above. Specifcally:

- *Unacceptable Unequal 5ths*
    - Should be found while looking for parallel 5ths using same method as above. Unequal fifths have parallel motion in that it is a fifth moving to a fifth; the only difference is the quality of the two intervals change.
    - When completing step 2, if a d5 moves to a P5 and it involves the bass line, this is unacceptable unequal 5ths

**Practice on the next example.**

{% capture ex4 %}X:4
T:Unacceptable unequal fifths (UU5)
M:4/4
L:1/2
K:C
V:1
[cE] [Fd]| [dF] [cG]|]
V:2 clef=bass
[C,C] [D,A,] | [B,,G,] [E,C,]|]
w:C:I ii V6/5 I{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

## Finding unacceptable contrary motion

{% capture ex5 %}X:5
T:Contrary perfect octaves (CP8)
M:4/4
L:1/2
K:C
V:1
[cE] [AD]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [F,A,] | [B,G,] [C,C,]|]
w:C:I ii6 V7 I{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}


{% capture ex6 %}X:6
T:Contrary perfect fifths (CP5)
M:4/4
L:1/2
K:C
V:1
[cE] [AF]| [BF] [cE]|]
V:2 clef=bass
[C,G,] [D,,A,] | [D,G,,] [C,C]|]
w:C:I ii V7 I{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

- *Contrary Perfect 5th and 8ves*
    - After the first part of the parallel perfect 5ths/8ves instructions, look for inverted pairs of numbers (e.g. 2 and 7, 3 and 6, 4 and 5) within each number stack
    - If one of the new vertical stacks contains one of these inversion pairs, check to see if the intervals within each chord (vertically) are P5s or P8s.
    - With triads, P5s must always have the root of the chord on the bottom of a major or minor chord. No other combination or chord can produce a P5.
    - P8s must come from doubled voices moving to doubled voices
    - If there are two consecutive P5s or P8s, those are contrary 5ths or 8ves.

## Needles in a haystack

The following excerpt from Bach's Chorale no. 4 (“Es ist das Heil uns Kommen her”, mm. 9-10) has only one example of a part-writing error discussed above. Given his ability, it is safe to assume that he did this intentionally, so our goal is not to judge whether his part-writing was correct, only to see if you can use the methods above to find the error. He also chose to cross voices for a moment, but this is intentional and hidden in the inner voices. 

NOTE: When one voice moves more quickly than the others, you must compare the intervals created on *both* sides to the vertical stacks of the other three voices.

{% capture ex7 %}X:7
T:Find the error
M:4/4
L:1/4
Q:1/4=60
K:E
V:1
[EG]| [DF] [CA] [B,G] [B,F]| [CC] [B,D] H[B,E]|]
V:2 clef=bass
[E,B,]| [B,B,,] [E/2C,/2]-[E/2D,/2] [EE,] [B,,/2D/2]-[B,,/2B,/2]| [F,A,,] [F,B,,] H[G,E,,]|]
w:E:{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

## Conclusions

[Part-Writing Error Checklist and Guide](https://docs.google.com/document/d/1s9Xd3LPqoaEevshTopxHzLX9jCzxVCZocOBLD_dceMU/edit?usp=sharing)

When we practice voice-leading, we are really studying melodic intervals, the horizontal aspect of music. And because all part-writing errors are symptoms of poor voice-leading, this method finds part-writing errors by systematically comparing at the melodic intervals within each voice. It can be difficult at first to understand the method when only reading about it, but if you take the time to walk through each step above, you should be able to understand the process. It should not only teach you to identify the motion and tendencies behind the errors, but it also ensures that you will have a way to consistently double-check your work.