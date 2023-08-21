---
layout: chapter
title: 23b Lesson - Labeling Pitch-class Sets and Basic Manipulation
abc: true
---

For the rest of our introduction to post-tonal analysis, we will employ *integer notation* for *pitch classes*. Allen Forte first formalized this system in his seminal work, *The Structure of Atonal Music*, creating a broad analytical framework to compensate for the inadequacy of tonal analytical methods to address music that does not follow the structure and rules of diatonicism. His *set theory* is a specialized form of analysis that looks for intervallic patterns equally across all twelve chromatic pitches, rather than focusing on the relationship between a central pitch (i.e. tonic) and others. 

## Scratching the surface

*Set theory* is a broad field of theoretical study, and we will only introduce a few basic concepts in this unit. If you would like to explore this topic further--and if you intend to go beyond the undergraduate level of music study, you should have at least a passing familiarity with these concepts--I highly recommend that you read some of the many fine books written on the subject. My favorites include:
- *The Structure of Atonal Music* - Allen Forte
- *Introduction to Post-tonal Theory* - Joseph Straus
- *Basic Atonal Theory* - John Rahn

There have been numerous refinements and alterations to this method since the first publication of Forte's text in 1973, so this unit will attempt to distill the basics into a foundation that will make this sort of analysis more accessible.

## Notating unordered pitch-class sets

When we introduced pitch-class sets (pcs) in the previous topic, we did not formalize their notation, however, because we will study various levels of organization within pc sets, it is important to establish a standard form for writing an *unordered* pcs--a pitch class set that you have not organized according to a predetermined, formalized sorting method. For unordered pcs, you should always notate this using **parentheses with a comma between each pitch class**. The following are all examples of unordered pc sets:

- (0,8,5,t)
- (B-flat,C,G,D)
- (9,4)
- (0,t,3,e,6,7,8,9,2)
- (B,C,A,E,F,G,D)

You will notice that it doesn't matter if you use pitch names or integer notation; a pitch class set is any collection of pitch classes.

## Finding the ascending forms of pitch-class sets

We can then take each of these *unordered* pitch class sets and put them in an *ascending form*. This is notated the same way, but with an obvious order now applied.
- (0,5,8,t)
- (B-flat,C,D,G)
- (4,9)
- (0,2,3,6,7,8,9,t,e)
- (B,C,D,E,F,G,A)

For each of those five pitch-class sets, I've listed the ascending forms based on the first pitch class listed, but any pitch-class set will *always have as many ascending forms as there are pitch classes within the set*. Meaning that all tetrachords will have four ascending forms, and all pentachords will have five ascending forms, and so on, because we are able to create an ascending form built off of each pitch class. For example, the first pcs listed above would also have three additional ascending forms:
- (0,5,8,t) = ascending form built off of 0
- (5,8,t,0) = ascending form built off of 5
- (8,t,0,5) = ascending form built off of 8
- (t,0,5,8) = ascending form built off of t

At first glance, it seems silly that an "ascending" form would have bigger numbers before smaller numbers, but if you think of each of these numbers as pitches, it will make more sense. Is C higher than F? That depends on which octave you place the C and F; either could be higher. The only thing that matters when determining an ascending form is that you don't skip over a pitch class. In our example tetrachord, you can imagine the four pitches on a staff using fixed-zero notation (i.e. C, F, A-flat, and B-flat), and you should be able to see that each of these ascending forms creates the smallest arrangement of the pitches given the starting note.

{% capture ex4 %}X: 4
T:Tetrachords represented in ascending forms
T:using the (0,5,8,t) collection in fixed-zero (C=0)
M:4/4
L:1
K:C
V:1
[CF_A_B][F_A_Bc][_A_Bcf][_Bcf_a]|]
w:0 5 8 t{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

It may help you to compare ascending form to traditional tertian harmony. When looking at seventh chord, you know that there are four inversions--root position, 1st inversion, 2nd inversion, and 3rd inversion. And if you were to write out each of these inversions in its simplest form, you would end up with a representation of the seventh chord in four different ways--one for each pitch in the chord. The ascending forms of pitch class sets are the same; there is one ascending form built off of a each pitch class within the set.  

## Modulo 12 arithmetic

Before we begin using integer notation to study pitch classes and pitch-class sets, we must establish our first mathematical method for manipulating pitches. Our standard counting system is based around ten and its multiples (ones, tens, hundreds, thousands, etc.), but music uses twelve equally-spaced pitches. Because of this, we must figure out a way to count, and create equivalency, around the number 12. For this, we use modulo 12 (mod12) arithmetic. You already use modulo 12 arithmetic every time you count time in hours, assuming that you use a 12-hour system. For example, if it is 11:00 and you have a meeting in three hours, what time is your meeting? From experience, you understand that when you reach 12, you must reset your counting to find the meeting's start time at 2:00--not 14:00. Again, this assumes that you are not using a 12-hour clock cycle, not 24-hour.

This is exactly how pitch-class integer notation works, although the system begins numbering on 0 instead of 12. In this system, each time you pass 11, you begin again at zero, therefore making every multiple of 12 equal to zero. Complete the following chart to show the first two equivalencies for every number in this system. Can you create a method to quickly find any level of equivalency? What would happen if you crossed below zero?

Pitch-class integer | First equivalency | Second equivalency
 --- | --- | ---
 0 | 12 | 24
 1 | 13 | 25
 2 | 14 | --
 3 | -- | --
 4 | -- | --
 5 | -- | --
 6 | -- | --
 7 | -- | 31
 8 | -- | --
 9 | -- | --
 t (10) | -- | --
 e (11) | 23 | --

### Conclusion

While it is easy to complete this chart by simply counting sequentially downward within each column, it is still useful in that it demonstrates the continuum that is mod12 arithmetic. All whole integers can be represented by an integer between 0 and 11, giving us exactly one integer for every possible pitch class in the chromatic system.

Pitch-class integer | First equivalency | Second equivalency
 --- | --- | ---
 0 | 12 | 24
 1 | 13 | 25
 2 | 14 | 26
 3 | 15 | 27
 4 | 16 | 28
 5 | 17 | 29
 6 | 18 | 30
 7 | 19 | 31
 8 | 20 | 32
 9 | 21 | 33
 t (10) | 22 | 34
 e (11) | 23 | 35

This also works in moving backward. Using basic arithmetic, it is easy to understand that 12 - 5 = 7. But because 12 is equivalent to 0 in mod12, this also means that 0 - 5 = 7. This is correct, but it skips an step in demonstrating how. 
- 0 - 5 = -5
- You must then convert -5 into an integer between 0 and 11 using multiples of 12. Therefore, -5 + 12 = 7.

This shows that any whole integer, whether positive or negative, can be converted to an integer between 0 and 11. You could create a similar chart to the one above for negative integers.

Pitch-class integer | First negative equivalency | Second negative equivalency
 --- | --- | ---
 0 | -12 | -24
 1 | -11 | -23
 2 | -10 | -22
 3 | -9 | -21
 4 | -8 | -20
 5 | -7 | -19
 6 | -6 | -18
 7 | -5 | -17
 8 | -4 | -16
 9 | -3 | -15
 t (10) | -2 | -14
 e (11) | -1 | -13

## Transposition using integer notation

Fixed-zero integer notation assigns the following integers to pitch-classes:

 Pitch-class integer | Pitch 1 | Pitch 2
 --- | --- | ---
 0 | C | B-sharp
 1 | C-sharp | D-flat
 2 | D | --
 3 | D-sharp | E-flat
 4 | E | F-flat
 5 | F | E-sharp
 6 | F-sharp | G-flat
 7 | G | --
 8 | G-sharp | A-flat
 9 | A | --
 t (10) | A-sharp | B-flat
 e (11) | B | C-flat

This is relatively simple to memorize, but it is more important to consider what these numbers truly represent. Consider the following pitch-class set:

`(E, F, G, B-flat)`

First, transpose these pitches up a P4 using our traditional intervallic method for transposition, and as you do this, pay careful attention to the process that you use for transposing. Do you think of each pitch as part of a key? If so, what scale degree do you use for each pitch? Do you count half-steps? Do you find the first pitch and then as the base for finding the rest of the intervals?

Next:
- Convert this pitch-class set into integer notation *using fixed-zero*
- Then add 5 to each number
- For any resulting number greater that 11, convert that number to its lowest possible integer using mod12 from above. 
    - For example, if you were to get 13, you would need to subtract 12 to get 1.
- Convert this new set of integers into pitch letter names. 

Did you get the same result as when you transposed the pitches using the traditional method for pitch transposition? If so, why does this work? What do the numbers for integer notation *actually* represent? (Hint: it is not the assigned pitches.)

## Notating transposition

Hopefully, you came to the same result using both methods of transposition. The pc set becomes (4,5,7,t), and then when you add 5 to each integer it becomes (9,t,12,15). All numbers greater than 11 must be reduced by mod12, so the set becomes (9,t,0,3). When these numbers are converted back into pitch letter names *using fixed-zero*, you get (A,B-flat,C,E-flat) which is exactly a P4 above the original pc set.

This works, of course, because *the numbers in integer notation actually represent the number of half-steps above a given pitch*. When using fixed zero, each integer represents that many half-steps above C. From this, we derive the following chart, although if you have already memorized the integers for fixed-zero notation, you can always "reverse engineer" this chart using your knowledge of intervals within the C major scale.

 Pitch-class integer | Interval 1 | Interval 2 | Interval 3
 --- | --- | --- | ---
 0 | unison | d2 | A7
 1 | m2 | (augmented unison) | --
 2 | M2 | d3 | --
 3 | m3 | A2 | --
 4 | M3 | d4 | --
 5 | P4 | A3 | --
 6 | A4 | d5 | --
 7 | P5 | d6 | --
 8 | m6 | A5 | --
 9 | M6 | d7 | --
 t (10) | m7 | A6 | --
 e (11) | M7 | (diminished unison) | --

 When notating transposition, we write T<sub>n</sub> where n = the interval by which you will transpose. The example above would be notated:

 T<sub>5</sub>(E, F, G, B-flat) = (A,B-flat,C,E-flat)

 OR using integer notation
 
 T<sub>5</sub>(4,5,7,t) = (9,t,0,3)

## Transposing downward

Any positive integer implies a transposition upward, so a negative integer is used to transpose downward. For example, perform the following transposition:

T<sub>-3</sub>(4,5,7,t)

This example is simple enough because each of the integers is easily reduced by -3 to create (1,2,4,7). However, try the following:

T<sub>-5</sub>(4,5,7,t)

In this example, 4 - 5 = -1. What does -1 equal? Because we use mod12, you can simply add 12 to this number to find its simplest equivalency.

-1 + 12 = 11

Just as you must reduce any number greater that 11 to an integer between 0 and 11, you must also increase any number less than 0. Therefore the set above is:

T<sub>-5</sub>(4,5,7,t) = (e,0,2,5)