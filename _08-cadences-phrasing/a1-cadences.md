---
layout: chapter
title: Lesson 8a - Cadences
abc: true
---

After having developed voice-leading procedures in Unit 7a, you should now understand how the voice-leading between V and I contributes toward tension and release. This progression defines tonal harmony, and it is from this that we derive our three **primary functions**: tonic, dominant, and pre-dominant. While it is easy to memorize which chords belong to each of the primary functions, it is more important to understand how and why these functions work, because context can change a chord's function to any other function.
- *Tonic* function chords provide stability and closure. Most chords that do this contain the tonic pitch, hence the name.
- *Dominant* function chords pull strongly to *tonic* function chords. Their pull creates instability, but because they are only one chord removed from the end of the progression, most listeners will still associate them strongly with the end of a musical idea. The dominant chord can be considered the progenitor of this function, so all harmonies that pull to a tonic function can be described as a having a dominant function.
- Because the dominant function chord precedes the tonic function, the dominant function can be seen as the "doorway" through which all chords will pass as they move toward harmonic resolution. Therefore, all chords that have the goal of moving toward the dominant function are labeled as *pre-dominant* function. This will include a wide variety of chords, and when we introduce secondary and tertiary function chords later in the course, there will be a large amount of overlap between pre-dominant chords--a primary function--and those. We will discuss the implied semantics of primary, secondary, and tertiary chords as we learn them.
    - Some systems label *pre-dominant* functions as *subdominant*, because many include the fourth scale degree. We already use words such as "dominant" and "tonic" in a variety of ways (e.g. scale degrees, harmonic function, chord types, etc.), so we will be differentiating pre-dominant from subdominant to create slightly less confusion.

### Alleviating terminology confusion

Note that the two first primary functions--tonic and dominant--share terms with the older scale degree system (i.e. The system that we discussed in Unit 2a that uses terms such as mediant, submediant, supertonic, etc.) as well as certain commonly-used chord types such as dominant chords. Because students often confuse the meaning of these, this text will use the following style guide:
- When referring to scale degrees, I will always use the numbering system. (e.g. ^1, ^2, etc. OR "first scale degree", "second scale degree")
- When referring to harmonic function, I will always follow the terms "tonic" and "dominant" with the word "function".
- When referring to chords, I will use Roman numerals when possible. For example, rather than saying the dominant chord, I will refer to the V chord.

## Primary harmonic function

The three primary harmonic functions shape all musical phrases through tension and resolution, and no where is that more obvious than in studying how phrases end. *Cadences* are the term that we use to describe the harmonic progression at the end of a musical phrase. All cadences finish a phrase, but not all cadences provide closure and stability. In fact, some cadences are purposefully unsettled.

We will study the chords associated with classifying cadences, but it takes far more than a particular harmonic progression to create a cadence. In addition to chord progressions, cadences are affected by melodic shapes, melodic rhythm, harmonic rhythm, context, meter, and many other elements of music.

For this course, we will study five types of cadences:
- *perfect authentic cadence (PAC)*
- *imperfect authentic cadence (IAC)*
- *half cadence (HC)*
- *deceptive cadence (DC)*
- *plagal cadence (PC)*

*Take special care to remember the abbreviations in parentheses for each cadence type. These will be used repeatedly in your analyses.*

## Identifying cadences

For each cadence in the following examples, determine:
- what chord progressions are associated with each type of cadence.
    - *perfect authentic cadence*
    - *imperfect authentic cadence*
    - *half cadence*
    - *deceptive cadence*
    - *plagal cadence*
- what chord functions (i.e. tonic, dominant, pre-dominant) are used in each type of cadence.
- what chord tones are present in the soprano and bass.
- what other musical elements affect the phrase ending.

{% capture ex1 %}X:1
T:Standard cadences
T:Old hundredth psalm
M:4/4
L:1/4
Q:1/4=80
K:G
V:1
[GD]| [GD] [FD] [EB,] [DD]| [GB,] [AD] H[BD]
[BD]| [BD] [BG] [AF] [GG]| [cG] [BG] H[AF]
[GG]| [AF] [GB] [AF] [DG]| [EE] [FC] H[GB,]
[dD]| [BD] [GG] [AF] [cA]| [GB] [AF] H[GG]|| [G4C4]| [G4B,4]|]
V:2 clef=bass
[G,B,]| [G,B,] [A,D,] [E,G,] [B,,G,]| [E,G,] [D,F,] H[G,G,,]
w: _ _ _ _ _ _ _ IAC
[G,G,]| [G,G,] [G,D] [DD,] [E,B,]| [C,E] [G,,D] H[DD,]
w:  _ _ _ _ _ _ _ HC
[E,B,]| [D,D] [G,D] [D,D] [B,,G,]| [C,G,] [D,A,] H[G,E,]
w: _ _ _ _ _ _ _ DC
[G,B,]| [G,G,] [E,B,] [D,D] [A,,E]| [D/2B,,/2]-[D/2C,/2] [D/2D,/2]-[C/2D,/2] H[G,,B,]|| [C,4E,4]| [G,,4D,4]|]
w: _ _ _ _ _ _ _ _ _ PAC _ plagal{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

## Conclusions

Cadences close each musical idea and phrase, and we classify each cadence by certain characteristics of their voice-leading and harmonic progressions.

- **Authentic Cadence** - any cadence in which a dominant function harmony (i.e. V or vii<sup>o</sup>) resolves to I. There are two types of authentic cadences, so we always label any authentic cadence as one of these: 
    - **Perfect Authentic Cadence (PAC)**
        - Must have a V chord resolving to a I/i chord
        - Both the V chord and I/i chord are in root position
        - `Do` is in the soprano voice of the I/i chord 
    - **Imperfect Authentic Cadence (IAC)**
        - Any authentic cadence that does not fulfill all of the requirements for a PAC.
- **Half Cadence (HC)**
    - Any phrase that ends on a V chord.
- **Plagal Cadence (PC)**
    - Any phrase that ends in IV resolving to I
        - Commonly associated with "Amen" at the end of chorales
- **Deceptive Cadence (DC)**
    - Any phrase that ends with V resolving to vi/VI

### Phrygian half cadence

There is a special type of half cadence that is used often enough in certain musical styles that it has received a special name: the *Phrygian half cadence (PHC)*. This cadence only occurs in minor and must consist of a iv<sup>6</sup> resolving to a root-position V chord. We will not discuss this particular cadence often, but you should be aware of it and able to label it when you see it.

{% capture ex2 %}X:2
T:Phrygian half cadence
M:4/4
L:1
K:Eb
V:1
[FC]| [GD]|]
V:2 clef=bass
[CA,,]| [=B,G,,]|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}
