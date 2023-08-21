---
layout: chapter
title: 23d Discussion - PC Set Inversion
abc: true
---

# Class discussion

## PC Set Inversion

How do you find the inversion of the number?
- you take the number and go that many around the given pitch. 
  - if we are inverting over 0, the inversion of 3 is -3. 
- -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

What if we apply Mod 12 to this idea?
- 1 2 3 4 5 6 7 8 9 t e 0 1 2 3 4 5 6  7 t e 
  - we get the same idea by mirroring numbers over the clock, putting the mirror down the line between 0 and 6.
- the inversions of each number are:
  - 1 e, 2 t, 3 9, 4 8, 5 7, 6 6.
- if you're using the clock for inversion, you can move the mirror axis to any number and treat it the same.

#### Ex: C major triad
What is the pitch class set for a C major triad?
(0,4,7). 
What is the inversion? 
(0,8,5).
  - the normal form of the inversion is [5,8,0].
  
The chord made is a F minor triad, because we directly flipped the intervals around C. 
### Transposition and Inversion
When you have to transpose and invert a PC set, the formula is TnI().
#### Which is correct? 
1. Transpose
  - ex: T4I(1,5,6)
    - (5,9,t)
2. Invert
    - (7,3,2)
3. Find normal form
    - [2,3,7]
    
**OR**
1. Invert 
- ex: T4I(1,5,6)
    - (e,7,6)
2. Find normal form
    - [6,7,e]
3. Transpose
  - next we transpose by adding n (4) to each interger. 
   - [t,e,3]

The SECOND OPTION is correct. 
By transposing first, it changes the axis you invert over.
You have to invert first, THEN transpose. 
You have to wait to find normal form until AFTER you invert the PC set. 

Shortcut:
- subtract n by each interger, then set it in normal form.
    - ex: T9I(4,3,1)
      - 9-4=5
      - 9-3=6
      - 9-1=8
    - so our PC set is (5,6,8), and normal form is [5,6,8]
    
 ### Set Class 
 Think of pitch class, it is a combination of pitches, thus a PC set.
 So set class, is a collection of pitch class sets.
 
 Heirarchy:
 - pitch class (1)
 - pitch class set (1,4,7)
 - set class (1,4,7);(2,5,8);(3,6,9);(4,7,t);(5,8,e);(6,9,0); etc...

A set class for (0,4,7), a major triad, all of its transpositions and inversions create 24 PC sets, making one large set class. 
This includes all major and minor triads in interger notation. 
- a way to decrease a set class is using a symmetrical chord

# Further reading

## From *Open Music Theory*

### Inversion

Inversion, like transposition, is often associated with motion that connects similar objects. You need to be able to (1) invert a collection of pitches and (2) determine the inversional relationship between two collections of pitches.

[![](/images/postTonal/inversion.png)](/images/postTonal/inversion.png)

This passage above from Debussy's "Sunken Cathedral" is an example. Just as was the case in the [transpositionally-related passages][transposition], these two gestures have the same intervallic content—and so, our ears recognize them as very similar. (Debussy underscores that similarity by giving both of the gestures the same rhythmic setting.) Unlike transposition, however, the interval content of these two gestures is not *arranged* in the same way.

[![](/images/postTonal/inversionallyRelated.png)](/images/postTonal/inversionallyRelated.png)

Both have the same intervals, but the {A,D,E} collection has the +5 on the bottom instead of on the top.

Inverting something is a two-step process, performed *in this order*: (1) Reflect the pitch classes in an object around the 0-6 axis of symmetry, and then (2) transpose it. I'll illustrate first on a clock, and then show you an easier way:

[![](/images/postTonal/invertingWithAClock.png)](/images/postTonal/invertingWithAClock.png)

Fortunately, there is a much quicker way to invert a pitch or collection of pitches! Given any collection of pitch classes and a _TnI_, simply subtract the the pitch classes from _n:_

[![](/images/postTonal/differences.png)](/images/postTonal/differences.png)

Conversely, to determine the _TnI_ that relates two collections of pitch classes, find a common value to which they all sum. That is the _n_ in _TnI:_

[![](/images/postTonal/sums.png)](/images/postTonal/sums.png)
