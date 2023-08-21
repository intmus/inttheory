---
layout: chapter
title: 23c Lesson - Finding the Normal Form of a PCS
abc: true
---

In studying tonal music, you quickly learn that any melody or chord can be transposed to start on 12 different pitches, and we will still hear those as related as long as the *relative* interval structure remains intact. In order to make comparing pitch-class sets possible, we need some way to ensure that we are comparing like intervallic patterns. You can imagine how difficult it would be to make sense of multiple pc sets if each set was in a random order. For this, we use *normal form*.

## Normal form (normal order)

Reducing a pitch-class set to its normal form, also called normal order, is similar to the way in which we analyze chords in standard diatonic harmony. For example, how would you condense the following open voicing of a seventh chord to its simplest form? When reducing it, make sure to retain its inversion.

{% capture ex1 %}X: 1
T:C major seventh chord
T:in an open voicing
M:4/4
L:1
K:C
V:1
[BG]|]
V:2 clef=bass
[E,C]|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

Most people will reduce this to a closed-position chord such as the following, because it shows every pitch and the inversion in the smallest space possible. This makes it easy to see the intervals and construction of the chord:

{% capture ex2 %}X: 2
T:C major seventh chord
T:in a closed voicing
M:4/4
L:1
K:C
V:1
[EBGc]|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

*Normal form* (or *normal order*) applies the same principles for organizing pitches to pc sets as you did when rearranging this seventh chord. **Normal form is an ascending arrangement of a pc set in which the outside interval is smallest.** For example, take the following pc set and arrange it so it fills the smallest space possible. 

(1,7,t)

More precisely, find the ascending order that has the smallest interval between the outside pitch classes. As discussed above, you should know that a triad has three ascending forms, so you should use that as your starting point. You may use any method that works, but common methods include checking each interval using mod12, notating the pitches on a staff, or even drawing the pitches on a clock face to visualize the shortest distance. As you work through this, consider the speed and efficacy of each method that you try.

### Conclusions

For your first attempt at this basic trichord, you will probably find it easiest to translate the pitches into standard pitch letters, and then just treat it as a triad. In this case, the pitches D-flat, G, and B-flat form a G diminished triad, so you can quickly tell that the normal form for this should be:

[7,t,1]

**Remember that when notating a pc set in normal form, we use brackets, not parentheses.** Parentheses with commas imply an unordered or ascending form. This notation method is outlined by Joseph Straus in his *Introduction to Post-Tonal Theory*.

## Breaking "ties" for ordering pcs

Before we create a full integer-based system for finding normal form, we need to understand one more issue. With many pitch class sets, it is possible that there are multiple arrangements that have the same interval between the outside pitches. Try putting the following trichord into normal form.

(0,5,7)

If you arrange this on a staff in all possible ascending orders, you get:

{% capture ex3 %}X: 3
T:Three possible arrangements of (0,5,7)
M:4/4
L:1
K:C
V:1
[CFG]| [FGc]| [Gcf]|]{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Conclusion

After looking at this on the staff, it is obvious that you can eliminate the last arrangement, but how do you choose between the first two which both have an outer interval of 7 (P5)? In pcs theory, the first tie-breaker is looking at the distance between the lowest pitch and the second highest pitch. In the above example, the second interval for the first arrangement is 5 (P4), but the second interval for the second arrangement is only 2 (M2). In this case the normal form this trichord is [0,2,7].

## Developing a method for normal form

But how could we find normal form without relying on our familiarity with the traditional musical notation system? And what happens when we have a more complicated and ambiguous pc set? Imagine a more complicated set that doesn't translate into a traditional tonal structure like a triad or seventh chord. What difficulties do you imagine there will be? Do you have a method that seems to get a quick and reliable result? Which seems the most consistent?

Let's try to create a step-by-step process by using a more difficult example. The following pentachord has multiple ties and will require you to work through multiple levels. Try to develop this method without using a staff or clock faces. While working through this, how many permutations in ascending order are there for a this set? How does that number relate to the cardinality for any set? Remember that each tie is broken by measuring the first pitch against the next closest pitch.

(3,e,5,2,8)

### Conclusion

With a large set such as this pentachord, it is difficult to quickly parse the normal form.

1. **Put the pcs in an ascending form.** It does not matter on which pitch you start, only that the pitches are ascending. You can imagine this using a clock face--each pitch class must go in the order it would if you move clockwise around the clock without skipping any pitch classes. For this pentachord, let's start with:
    1. (2,3,5,8,e)
2. **List every possible ascending arrangements of the pc set.** There will always be the same number of arrangements as there are members of the pc set, because each integer will have *one* ascending arrangement with it as a starting pitch class. For a pentachord, there will always be five possibilities, and for this particular pc set, they are:
    1. (2,3,5,8,e)
    2. (3,5,8,e,2)
    3. (5,8,e,2,3)
    4. (8,e,2,3,5)
    5. (e,2,3,5,8)
3. **Subtract the first number *from* the last number for each ascending arrangement.** This will give you the interval between the outer pitch classes expressed as a number of half-steps. If the last number is smaller than the first number, you must use mod12 to convert it. For most students, it is easiest to add 12 to the smaller number before subtracting, but after you have practiced, you can apply this to the result if you'd like. For example above: 
    1. (2,3,5,8,e) | e-2 = 11-2 = *9*
    2. (3,5,8,e,2) | 2-3 (requires mod 12) = 14-3 = *11*
    3. (5,8,e,2,3) | 3-5 (requires mod 12) = 15-5 = *10*
    4. (8,e,2,3,5) | 5-8 (requires mod 12) = 17-8 = *9*
    5. (e,2,3,5,8) | 8-e (requires mod 12) = 20-11 = *9*
4. **The normal form is the ascending arrangement with the smallest outer interval. If you have multiple arrangements with the same outer interval, you must proceed to the first tie-breaker.** In our above example, we have three options with an outer interval of 9 (M6). (At this point, we have eliminated the two arrangements that had the larger outer intervals of 10 and 11.) We must compare each of the tied arrangements against each other to determine which example has the *next* smallest outer interval. You can do this easily by subtracting the second-to-last number from the first number, so for our remaining three with the outer interval of 9, we get:
    1. (2,3,5,8,e) | 8-2 = *6*
    4. (8,e,2,3,5) | 3-8 (requires mod12) = 15-8 = *7*
    5. (e,2,3,5,8) | 5-e (requires mod12) = 17-11 = *6*
5. **If there is still a tie, repeat the process for the remaining ascending orders, but using the third-to-last pitch class for your subtraction.** Sometimes, this can move through multiple tie-breakers, so just continue moving inward through the arrangements. The previous example still had a tie between the first and last arrangement, so we have to go one last round:
    1. (2,3,5,8,e) | 5-2 = *3*
    5. (e,2,3,5,8) | 3-e (requires mod12) = 15-11 = *4*
6. **Once you have only one smallest interval, you have found the normal form for that pc set.** Remember that you must change your notation to include square brackets once you have determined normal form. For our example above, our normal form is:
    1. [2,3,5,8,e]

Note that there cannot be a definitive normal form for symmetrical sets such as diminished seventh chords, augmented triads, and whole-tone scales. For these, it is simplest to list the lowest integer first.
