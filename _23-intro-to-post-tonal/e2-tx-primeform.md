---
layout: chapter
title: 23e Discussion - PC Set Prime Form
abc: true
---

# Class discussion


Prime form is useful for making pitch class sets easy to compare with other pitch class sets. 

Prime form is also another way we can say that pitch class sets are related. Now we can say they are related by transposition, inversion, and/or same prime form. 

## Prime Form
Prime form is the way we classify types of PC sets.
- commonly how we describe a PC set that creates a major triad, minor triad, etc...

#### Ex: (2,6,9)
Take (2,6,9) and align it to 0. (0,4,7) major triad.
Invert (0,4,7) to (0,8,5) minor triad.
Normal form for (0,8,5) is [5,8,0].
Take the normal form and realign it back to 0 (037).
- prime form is written in parenthesis without commas between the intergers

#### Ex: (4,t,8,3)
What are our order options?
- (3,4,8,t) / 7
- (4,8,t,3) / 11
- (8,t,3,4) / 8
- (t,3,4,8) / 10

So our normal form is [3,4,8,t].
Take the normal form and set it on zero: [0,1,5,7].
NOW invert the original normal form. 
  - [3,4,8,t] to (9,8,4,2).
  - find the inversion's normal form:
    - (2,4,8,9) / 7
    - (4,8,9,2) / 10
    - (8,9,2,4) / 8
    - (9,2,4,8) / 11
   - our normal form for the inversion is [2,4,8,9].
   
And set the inversion's normal form on zero [0,2,6,7].
NOW you compare the two normal forms on zero. 
  - [0,1,5,7] and [0,2,6,7]
  - first you find the smallest interval between the first and 4th intergers (in this case it is the same).
  - then you check the interval between the first and 3rd intergers (in this case the first option has a smaller interval).

**Our prime form is (0157).**

# Further reading

## From *Open Music Theory*

### Set class relationships

Lots of concepts in pitch-class set theory are best viewed along a sliding scale of "concreteness" or "abstractness." A concept like _pitch_, for example, is very concrete, while _pitch class_ is somewhat more abstract. We can perform a pitch, but we can't really perform a pitch class. We've seen similar examples in the intervallic realm. Ordered pitch intervals are associated with a very specific sound (e.g., +15); unordered pitch-class intervals (e.g., interval class 1) are less vivid or real. A basic concept in pitch-class set theory is that these levels of concreteness and abstractness encompass not only pitch and interval, but groups of pitch classes as well. These groups of pitch classes are called _pitch-class sets_.

We've already seen sets of pitch-classes, though we haven't really been calling them that. When we extract a group of notes from a passage of music and put them in "[normal order][1]," that group of notes is a pitch-class set. As we've seen in class, one very interesting way of looking at a lot of post-tonal music is by studying the [transpositional][2] and [inversional][3] relationships between pitch-class sets. In the short example below (from Bartók's "Subject and Reflection") you'll notice that the right hand of the two passages is _T5_-related, as is the left-hand. Within each passage, the right and left hands are _T8I _and _T6I_ related, respectively.

[![](/images/postTonal/subjecdtAndReflection.png)](/images/postTonal/subjecdtAndReflection.png)

_In order for a pitch-class set to be transpositionally or inversionally related to some other pitch class set, they must share the same collection of intervals_. This is most easily grasped by remembering that all major and minor triads have the same interval content (M3, m3, and P5). Major triads are transpositionally related to one another, while major and minor triads are inversionally related to one another. The same observation applies in Bartók's "Subject and Reflection." The four pitch-class sets in those two passages all have the same intervallic content and that's why we can label transpositional and inversional relationships between them.

All pitch-class sets that are transpositionally and inversionally related belong to the same _set class_, and they are represented by the same _prime form_. We follow a simple process to put a pitch-class set in prime form:

1. Put the pitch-class set in normal order.
2. Transpose it so that the first pitch class is 0.
3. Invert the results from step 2 (any inversion will work) and put the result in normal order.
4. Transpose it so that the first pitch class is 0.
5. Compare the results of steps (2) and (4). Prime form is the most compact version.

The example below walks demonstrates using the motive from Bartók's "Subject and Reflection."

[![](/images/postTonal/primeForm.png)](/images/postTonal/primeForm.png)

### Prime form

_Analytically_, the concept of set class is useful because it can show coherence in a composition. Bartók's "[Subject and Reflection][1]," for example, uses the (02357) set class nearly exclusively—though it appears in many transpositions and inversions.

_Theoretically_, the concept is useful because it provides a prism through which we can begin to study the _possibilities_ provided to us by the twelve pitch-class universe. For almost 500 years, composers mostly used only a small subset of those possibilities (triads, seventh chords, and so forth). Set class lists reveals all of the other possibilities. They also give us hints as to why tonal composers used only a small portion of them and suggest entire worlds organized through other means. Fortunately for us, we don't need to create such a list because many others have! A particularly good list is found [here][2], and I'll give you another to keep in class.

Most of these set-class lists are organized similarly. Set classes that have the same number of notes in them (we say that they have the same "cardinality") are grouped together: trichords (three-note pitch-class sets) sit together, as do nonachords (nine-note pitch-class sets), and so on. 

[![](/images/postTonal/trichordsAndNonachords.png)](/images/postTonal/trichordsAndNonachords.png)

Prime form for each set class is show in parenthesis. The "Forte Number" (3-1, 9-1, etc.), often adjacent to the prime form, was given to each set class by the famous music theorist [Allen Forte][4], who was one of the first to describe the set class list.

### Interval Class Vector##

The interval class vector next to each set class's prime form is particularly valuable. Think of it as a numeric representation of the "intervallic flavor" of each set class. IC vectors have six places <_ _ _ _ _ _> that are placeholders for interval classes 1–6. If a set class has a single interval class 1, it will have the digit 1 in the interval class vectors first placeholder. The IC vector <001110>, for example describes a trichord with 1 interval class 3, 1 interval class 4, and 1 interval class 5; that is, the major or minor triad, set class (037)!
