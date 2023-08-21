---
layout: chapter
title: 22b Lesson - Advanced rhythm and meters
abc: true
---

In Unit 4, we discussed the two most common classifications of meter: simple and compound. In this lesson, we will add two more advanced classifications as well as discuss the idea of how beat and division relationships can be used to combine them.

## Asymetric (irregular) meters

In the example below, each line shows a metric pattern of of a meter that we have not yet defined in our studies so far. These meters are grouped in pairs, so the first two lines are related, the third and fourth lines are related, and the fifth and sixth lines are related. (The 1/1 time signature is just a placeholder and has nothing to do with these meters.) How would you label these ? Can your knowledge of simple and compound meters apply to these? What rhythmic value gets the beat for each line?

{% capture ex1 %}X:1
T:Patterns in asymetric meters
M:1/1
L:1/8
Q:1/4=110
K:C
cG cGG| cG cGG| cG cGG|]
cGG cG| cGG cG|cGG cG|]
cG cG cGG| cG cG cGG| cG cG cGG|]
cG cGG cG| cG cGG cG| cG cGG cG|]
cG cGG cGG| cG cGG cGG| cG cGG cGG|]
cGG cGG cG| cGG cGG cG| cGG cGG cG|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## 5/8, 7/8, and 8/8 meters

In the patterns above, the beaming and pitch patterns show clear groupings of division, but if we use these grouping to define our beats, we realize that each measure is a mixture of a simple and compound beats--some are grouped in two while others are grouped in three. Any meter in which the beats have varying lengths is considered to be an *asymetric meter* or *irregular meter*.

### 5/8

The first two lines of the above example will be labeled as 5/8. The first line has five eighth notes in each measure but alternates between groups of two then three. The second line reverses the order of the grouping to three then two, but the number of divisions (eighth notes) remains the same. Therefore, 5/8 meters have **two** beats of unequal length -- a quarter note and a dotted quarter note. The quarter note has a division of two eighth notes, and the dotted quarter note has a division of three. 

The exception to this is when the tempo is slow enough that the eighth note becomes the beat, in which case, this meter becomes a simple quintuple meter with each eighth note divided into two sixteenth notes. When discussing an asymetric meter such as this with other musicians, it is often helpful to describe it using groupings of twos of threes. The first line below is "two plus three", and the second line is "three plus two". Try conducting along with both of these.

{% capture ex2 %}X:2
T:Patterns in 5/8 meters
M:5/8
L:1/8
Q:1/4=110
K:C
"two plus three"cG cGG| cG cGG| cG cGG|]
"three plus two"cGG cG| cGG cG|cGG cG|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### 7/8

Lines 3 and 4 of the first example will be labeled as 7/8. Lines 3 and 4 are similar to Lines 1 and 2 in that they have irregular groupings of two and three eighth notes, but instead of consisting of five eighth notes, each measure has a total of seven. Because they are grouped into groups of two and three, 7/8 meters have **three** beats of unequal length--two quarter notes and one dotted quarter note. Also like 5/8, the exception to this is when the tempo is slow enough that the eighth note becomes the beat, in which case, this meter becomes a simple septuple meter with each eighth note divided into two sixteenth notes. 

The beat groupings can come in any order as shown below. Try conducting along with these.

{% capture ex3 %}X:3
T:Patterns in 7/8 meters
M:7/8
L:1/8
Q:1/4=110
K:C
"2+2+3"cG cG cGG| cG cG cGG| cG cG cGG|]
"2+3+2"cG cGG cG| cG cGG cG| cG cGG cG|]
"3+2+2"cGG cG cG| cGG cG cG| cGG cG cG|]{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### 8/8

Lines 5 and 6 of the first example will be labeled as 8/8. Lines 3 and 4 are similar to Lines 1 and 2 in that they have irregular groupings of two and three eighth notes, but each measure now has a total of eight. Because they are grouped into groups of two and three, 8/8 meters have **three** beats of unequal length--one quarter note and two dotted quarter notes. As with all irregular meters, the exception to this is when the tempo is slow enough that the eighth note becomes the beat, in which case, this meter becomes a simple septuple meter with each eighth note divided into two sixteenth notes. 

Note the similarity to 7/8; both of these assymetric meters have three beats, but where 7/8 has two quarter notes, 8/8 has two *dotted* quarter notes. The beat groupings can come in any order as shown below. Try conducting along with these.

{% capture ex4 %}X:4
T:Patterns in 8/8 meters
M:8/8
L:1/8
Q:1/4=110
K:C
"2+3+3"cG cGG cGG| cG cGG cGG| cG cGG cGG|]
"3+3+2"cGG cGG cG| cGG cGG cG| cGG cGG cG|]
"3+2+3"cGG cG cGG| cGG cG cGG| cGG cG cGG|]{% endcapture %}
{% include abc-example.html number="4" abc=ex4 %}

## More asymetric meters

Any grouping of eighth notes can be turned into an asymetric meter if it has groupings of unequal beats. Look at the following for more examples. How many beats are in each of these meters? If a meter shares a time signature with a common meter (simple or compound), how do these differ and what visual cues can you use to differentiate them? Can you think of other possibilities?

{% capture ex5 %}X:5
T:More asymetric meters
M:9/8
L:1/8
Q:1/4=110
K:C
"2+2+2+3"cG cG cG cGG| cG cG cG cGG| cG cG cG cGG|]
[M:11/8]"3+3+3+2"cGG cGG cGG cG| cGG cGG cGG cG| cGG cGG cGG cG|]
[M:12/8]"3+3+2+2+2"cGG cGG cG cG cG| cGG cGG cG cG cG| cGG cGG cG cG cG|]{% endcapture %}
{% include abc-example.html number="5" abc=ex5 %}

## Mixed meters, polymeters, and polyrhythms

*Mixed meters, polymeters, and polyrhythms* are commonly used terms that are often confused. Look at the examples below, and try to come up with definitions that seperate them as cleanly as possible. 

{% capture ex6 %}X:6
T:Mixed meter (changing meter)
M:5/8
L:1/8
Q:1/4=110
K:C
cG cGG| [M:6/8]cGG cGG| [M:3/4]cG cG cG| [M:4/4]cG cG cG cG|]{% endcapture %}
{% include abc-example.html number="6" abc=ex6 %}

{% capture ex7 %}X:7
T:Polymeter
M:3/4
L:1/4
Q:1/4=90
K:C
V:1
c G E| c G E| c G E| c G E|]
V:2
[M:4/4]C E G c| C E G c| C E G c|]{% endcapture %}
{% include abc-example.html number="7" abc=ex7 %}

{% capture ex8 %}X:8
T:Implied polymeter
M:3/4
L:1/4
Q:1/4=90
K:C
V:1
c G E| c G E| c G E| c G E|]
V:2
C E G| c C E| G c C| E G c|]{% endcapture %}
{% include abc-example.html number="8" abc=ex8 %}

{% capture ex9 %}X:9
T:Polyrhythm
M:2/4
L:1/8
Q:1/4=110
K:C
V:1
cG cG| cG cG| cG cG|]
V:2
(3EGG (3EGG| (3EGG (3EGG| (3EGG (3EGG|]{% endcapture %}
{% include abc-example.html number="9" abc=ex9 %}

### Exploring the inbetween

{% capture ex10 %}X:10
T:Polymeter or polyrhythm?
M:3/4
L:1/8
Q:1/4=110
K:C
V:1
cG cG cG| cG cG cG| cG cG cG|]
V:2
[M:6/8]EGG EGG| EGG EGG| EGG EGG|]{% endcapture %}
{% include abc-example.html number="10" abc=ex10 %}


## Metric modulation

## Asymetric beat divisions

quintuplets, setuplets