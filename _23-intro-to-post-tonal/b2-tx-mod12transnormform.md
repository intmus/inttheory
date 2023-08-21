---
layout: chapter
title: 23b Discussion - Labeling Pitch-class Sets and Basic Manipulation
abc: true
---

Post Tonal Music

When descussing post tonal music, we can’t use our normal letter names to talk about pitches anymore, because we aren’t working in any specific key. We will now label each note with a number (zero through eleven) starting with C as 0. A pitch class is all of the possible enharmonic equivalents of a note, labeled with a number. The numbers that we label pitch classes with are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, t, and e. We substitute t and e for 10 and 11 because when we put pitch classes together, we will need to be able to differentiate these numbers from 0 and 1.

Pitch Class Sets

If we were to label scales using pitch classes, they would look like a string of numbers. For example, a major scale would be “0 2 4 5 7 9 e”. Any group of pitches is called a pitch class set. If we label the major scale using four-note pitch class sets, it would look like this: “0 2 4 5 0 2 4 5”. This shows that the major scale is actually two groups of four notes (0 2 4 5) that are the same. 

Ascending Form

Let's put this pitch class set into ascending form: 4692. The most basic and easiest way to put this set into ascending form would be by putting each number into ascending order: 2469. This is one version of ascending form, but we can also put the pitch "2" at the end of the set, and it will still be in an ascending order: 4692. This is still in ascending form because we don’t skip any tones as we move up. This is a way to invert chords. The other two ascending forms are 6924, and 9246. 


Modulo 12

Usually when we count up, we count up to 10 before we start over. In serialism, we will think in base 12, or mod 12. This means that once we have numbers 12 or over, we can subtract 12 to find what number they are equivalent to (0 = 12). Think of it like military time. If the time is 13:00 and we need to translate that to what it would be in standard time, we would subtract 12 (13 - 12 = 1) 1:00 pm.

Transposition

Transposition in music is really just adding or subtracting the pitches by specific intervals. Therefore, if we want to transpose a pitch class set, we can simply add or subtract a number from all pitch classes in the set.


# Class discussion 2021

**Refresher: what is a pitch class (pc)?**
- A number to represent all enharmonic equivalents of a pitch. We use 0 to e
- Remember 10 and 11 are represented as t and e

**Refresher: what is a pitch class set (pcs)?**
- A collection of pitch classes. Each group size has a different name (refer to the chart in 22b)

**Notating pitch class sets**
- Many of the examples on your homework will be *unordered* pitch class sets. Despite this name, we need a standard system for writing these so we can easily make them *ordered* later.
- Undordered pc sets are notated with parantheses around the set and commas between each pc. Examples: (0,1,5,t) and (Bb,C,D,G). Like two points on a graph are notated before you actually graph them.

**Modulo 12 arithmetic**
- 12 is the magic number in this system! Everything is based around 12. Just like how you know that the clock resets when you go from noon to 1 P.M., the number above e/11 in this notation roll back around to 0, 1, 2, etc.
- If you have a number above 12, you subtract 12 from it to get the number that's actually within the bounds of our system.

**Notating transposition**
- We are solely in fixed zero now.
- We have the pitch class set (E,F,G,Bb). Using traditional transposition methods, transpose up a P4 to get (A,Bb,C,Eb)
- If we convert our first pcs to integer notation, we get (4,5,7,t). Add 5 to each number (subtracting 12 from any numbers over e), and we have (9,t,0,3). Convert the second set back to note names, and you will find it's the same as the second set the first time we transposed in our traditional method.
- The numbers in integer notation represent intervals from 0. 5 = P4 because F is a P4 (5 half steps) from C (0)
- You would notate this process like this: T5(E,F,G,Bb) = (A,Bb,C,Eb) OR T5(4,5,7,t) = (9,t,0,3). T5 just means that we are transposing by adding 5, and it is fixed to the front of the original set to show that it is the one we're manipulating.

**Transposing downward**
- Same process as above, but instead of adding numbers we subtract them!
- In Mod12, you can also add 12 to a negative number to get a pc within the bounds of our notation system.

**Normal form/normal order**
- Normal form/order is an ascending arrangement of a pcs where the outside interval is smallest. This is very different from tertian harmony, where we're concerned with stacking in thirds.
- Let's use (1,7,t). Think about this process like using a clock face: you can only go clockwise, which means you can shuffle which nubmer is first in the set as long as the set remains in the same order. You can have (7,t,1) but you can't have (1,t,7) because t is out of ascending order.
- We can have (1,7,t,), (7,t,1), or (t,1,7). We're looking for the smallest outside interval, which we do by subtracting the last integer from the first one in the set. t-1=9, 1-7=6, and 7-t=9. Since the middle one has the smallest interval, the normal form for (1,7,t) is [7,t,1].
- Square brackets and commas denote normal form.
- *Always* put things in ascending form before you put them in normal or prime form. This form allows us to go through the process of finding the smallest outside interval, so it's important that we start out using it.

**Breaking ties for ordering pitch class sets**
- What do we do if we do all our subtracting and end up with two of the same result??
  - Go one more number in from the right with the remaining possibilities to break the tie! Obviously there was no tie to break with (1,7,t), but if we wanted to break the tie between the two 9 answers we would go 7-1=6 and 1-t=3 respectively.

**Developing a method for normal form using (3,e,5,2,8)**
- Put in ascending order: (2,3,5,8,e). Any ascending order is fine, but I usually start with the smallest number on the left because it makes sure I don't get mixed up
- Get all our different ascending forms:
  - (2,3,5,8,e)
  - (3,5,8,e,2)
  - (5,8,e,2,3)
  - (8,e,2,3,5)
  - (e,2,3,5,8)
- Subtract the outside numbers (last number - first number):
  - e-2=9
  - 2-3=e
  - 3-5=t
  - 5-8=9
  - 8-e=9
- Subtract the next smallest intervals for the tiebreakers (second to last number - first number):
  - 8-2=6
  - 3-8=7
  - 5-e=6
- Subtract the next smallest intervals for the second tiebreakers (third to last number - first number):
  - 5-2=3
  - 3-e=4
-The normal form for this pentachord is [2,3,5,8,e]. Remember that we're subtracting the same number every time--we're just changing what we're subtracting it *from*

Completely symmetrical pitch class sets don't have a normal form, so we would just write it in ascending form with the smallest number at the bottom.
  
# Further reading

## From *Open Music Theory*

### Transposition

In post-tonal music, transposition is often associated with motion: Take a chord, motive, melody, and when it is transposed, the aural effect is of *moving* that chord, motive, or melody in some direction. That’s the effect here, in two disconnected passages from Debussy's, *La cathédrale engloutie*:

[![](/images/postTonal/transposition.png)](/images/postTonal/transposition.png)

The opening motive — comprising the notes B, D, E, or {11, 2, 4} — is transposed four semitones higher in m. 18, representing the cathedral’s slow ascent above the water. Transposing something preserves its intervallic content, and not only that, it preserves the specific arrangement of that thing’s intervals. When we hear the passage at m. 18 above, we recognize its relationship to the passage in m. 1 because the same intervals return, but starting on a different pitch.

Transposition is an operation — something that is *done* to a pitch, pitch class, or collection of these things — or alternatively a *measurement* — representing the distance between things. We represent it as *Tn*, where *n* represents the ordered pitch-class interval between the two things. To transpose something by *Tn*, add *n* to every element in that thing (mod 12). Given the collection of pitch classes in m. 1 above and transposition by *T4*:

[![](/images/postTonal/t4.png)](/images/postTonal/t4.png)

The result is the pitch classes in m. 18. *T4* {11, 2, 4} = {3, 6, 8}.

Alternatively, to determine the transpositional relationship *between* two things, subtract the first thing from the second. If the numbers that result are all the same, the two things are related by that *Tn*.

[![](/images/postTonal/t4Measurement.png)](/images/postTonal/t4Measurement.png)

This is how I arrived at the *T4* arrow label in the musical example above, by “subtracting” the pitch class integers of m. 1 from the pitch-class integers in m. 18.

### Normal Form

Normal order (sometimes called normal form) has a lot in common with the concept of triad “root position.” Among other things, root position is a standard way to order the pitch-classes of triads and seventh chords so that we can classify and compare them easily. Normal order does the same, but in a more generalized way so as to apply to chords containing a variety of notes and intervals.

Normal order is the most compressed way to write a given collection of pitch classes. Often, you’ll be able to determine normal order intuitively using a keyboard or a clockface, but it’s good to learn a process that will always give you the correct answer.

1. Write as a collection of pitch classes (eliminating duplicates) in ascending order and within a single octave. There are many possible answers.
2. Duplicate the first pitch class at the end. 
3. Find the largest ordered pitch-class interval between adjacent pitch classes.
4. Rewrite the collection beginning with the pitch class to the right of the largest interval and write your answer in square brackets.

For example, given {G-sharp4, A2, D-sharp3, A4}:

1. *Write as a collection of pitch classes (eliminating duplicates) in ascending order and within a single octave.* {8,9,3}
2. *Duplicate the first pitch class at the end.* {8,9,3,8}
3. *Find the largest ordered pitch-class interval between adjacent pitch classes.* In this case, the largest interval is between "9" and "3."
4. *Rewrite the collection beginning with the pitch class to the right of the largest interval and write your answer in square brackets.* [3,8,9]

Occasionally you’ll have a tie in step 3. In these cases, write the ordering implied by each tie and calculate the interval from the first to the penultimate pitch class. The ordering with the smallest interval is the normal order.
