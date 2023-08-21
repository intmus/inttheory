---
layout: chapter
title: Lesson 1a - Pitches and Clefs
abc: true
---

<!--Hi Future Sean! I hope you've had a great summer. I know that you've forgotten how to commit, add, and push as well as all the other basics, but a while ago, you installed an VS code extension to make this easier. It will probably work on this new repository, but if not, you'll need to set it up by clicking on the gear in the lower left corner, choose Extensions, and click on "Git add commit push" to set it up. 

Once it's running properly, you can use ctrl + s to save changes, and then ctrl + alt + p to automatically git add, git commit, and git push without having to log in every gd time. You'll need to add a description, but that's not too bad. 

You're welcome! And if it doesn't work, just have Evan fix it like you always do lol -->

## A Starting Place

In this course, we will study music through the lens of a few of its most basic components: melody, harmony, and rhythm. There are other building blocks of music, such as texture, orchestration, and lyrics, but we will focus on melody, harmony, and rhythm because the unique ways in which a muscial genre combines these three concepts will help us understand the *least* intuitive rules and strategies that define the style. Or more simply put: we will establish a framework for understanding the parts of music that are most difficult to study.

While much of our beginning examples will study the widely-used standards of Western art music from the Renaissance through the Romantic eras, any music that that grew out of this tradition--including almost all popular music today--can be better understood using the tools we use in analyzing tonal harmony. As such, when possible, we will analyze music from a wide variety of styles and genres to better test the tools that we use to study.

### Before you begin

By the time most musicians begin formally exploring music theory, they likely are familiar with basic music notation--treble and bass clefs, staves, ledger lines, and accidentals--due to time spent performing. If you are uncomfortable with any of aspect of these concepts, you can review by reading the explanations under the *Further Reading* section of [Discussion 1a]({{ site.baseurl }}/01-pitches-clefs/a2-pitchesclefs.html).

## Clefs

Even though most college music students are familiar with reading music, most are partial to the clef associated with their primary instrument or voice-part. It is vital that musicians be fluent in not only the two most common clefs--treble and bass--but also with two additional clefs: alto clef and tenor clef. Alto and tenor clefs are often used by instruments such as viola, cello, trombone, and bassoon. They alleviate the use of ledger lines in the extreme registers of an instrument and appear regularly in even the most elementary music.

### Exploring clefs

Treble clef is sometimes referred to as the *G-clef*, and bass clef as the *F-clef*.
Alto and tenor clefs are known as *C-clefs*. 
So let's piece together the notes and octave relationships between the clefs as well as why the clefs have these alternate names. 

In the examples below: 
- the treble and alto clefs are in unison
- the tenor and bass clefs are in unison 
- the treble/alto clefs are separated from the the tenor/bass clefs by one octave
- middle C rests on the first ledger line below the treble clef staff

Knowing this, use these examples to find:
- the order of pitch names for each clef's lines and spaces.
- why treble clef is a G-clef, why bass clef is an F-clef, and why alto and tenor clefs are C-clefs.
- where middle C is on each clef.
- any tips or tricks that may help in differentiating and reading clefs.

{% capture ex1 %}X: 1
T: Pitches and Clefs
M: 4/4
L:1/4
K:C
V:1 name="Treble Clef"
E A F B G ^C G,|]
w: E A F B G C# G
V:2 name="Alto Clef" clef="alto"
E A F B G ^C G,|]
w: E A F B G C# G
V:3 name="Tenor Clef" clef="tenor"
E, A, F, B, G, ^C, G,,|]
w: E A F B G C# G
V:4 name="Bass Clef" clef="bass"
E, A, F, B, G, ^C, G,,|]
w: E A F B G C# G{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

### Conclusion

Clefs have secondary names because each clef is centered around the pitch in its name. The bass clef's dots surround an F, and the two C-clefs are centered on middle C. Treble clef, however, not only encircles the G at the center of its spiral, but it evolved from a stylized *G*. For a short and fun article on the evolution of clefs, I suggest reading Jimmy Stamp's [The Evolution of the Treble Clef](http://www.smithsonianmag.com/arts-culture/the-evolution-of-the-treble-clef-87122373/) from the Smithsonian website.

The octave relationship for each clef is the most important thing you can remember from this discussion, and the easiest way to demonstrate this is to look at where middle C sits on each clef. Below, you can see the note names for the lines and spaces of each clef, and middle C is highlighted at the beginning of each staff.

{% capture ex2 %}X: 2
T:Pitch Names for Each Clef
M:C
L:1/4
K:C
V:1 name="Treble Clef"
C | E G B d f| F A c e|]
w: midC E G B D F F A C E
V:2 name="Alto Clef" clef="alto"
C | F, A, C E G| G, B, D F|]
w: midC F A C E G G B D F
V:3 name="Tenor Clef" clef="tenor"
C | D, F, A, C E| E, G, B, D|]
w: midC D F A C E E G B D
V:4 name="Bass Clef" clef="bass"
C | G,, B,, D, F, A,| A,, C, E, G,|]
w: midC G B D F A A C E G{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

{% capture ex3 %}X:3
T:Middle C in each clef
M:C
L:1
K:C
C| [K:clef=alto]C| [K:clef=tenor]C| [K:clef=bass]C|]{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

From these two examples, it is easy to see the necessity of clefs. Ledger lines are an important notation tool, but too many ledger lines becomes difficult to read quickly. Therefore, each clef highlights a specific range that can be written without employing ledger lines. Alto clef is typically thought of as a lower extension for treble clef; it adds the visual space of seven steps from treble clef. Tenor clef is a higher extension for bass clef and adds the visual space of five steps from bass clef. Of course, alto and tenor clef have similar ranges and one of the other could likely be eliminated with little issue--alto clef is visually seven steps from either treble or bass clef making it a middle ground for both--but because both of these clefs have been widely used for more than a century, it is necessary for all musicians to be familiar with reading them.

### Tips and tricks

When asked about their methods, past students suggested working on clefs via:
- Memorization - The most widely used method uses flash cards or other repetitive devices to practice identifying notes on each clef to ensure a quick and efficient memorization.
- Relative note identifications - Some students remember one important note for each clef and then visually "count" through the alphabet upward or downward to find pitches in unfamiliar clefs. For example, you could memorize where C sits in each clef and count steps (letter names), or you could expand that concept to memorize how thirds are stacked to move around more quickly. While this is a reasonable method for familiarizing yourself with clefs, it will ultimately be too slow and inconsistent to be practical.
- The final suggestion was to determine the visual relationship of your weaker clefs to your strongest clef, and then use this to read in the new clef. 
    - For example, if you are primarily comfortable in treble-clef, you could remember that alto-clef moves all of the pitches down by a step relative to treble clef. (This ignores octave displacement, of course.) In this case, if you read alto clef as a treble clef but *up* a step, this compensates and gives you a quick visual method for reading the clef. 
        - To demonstrate this method: if a note head is on the line where B would be in treble clef, you could "translate" that pitch into alto clef by moving up a step (or letter name) to find that it is C. 
    - You would then need to find the visual relationships for each clef, because each will have a different visual distance and direction compared to your primary clef.
    - Like the relative note identification method above, this could be slow and inconsistent, but if one regularly transposes, this could be used effectively.
