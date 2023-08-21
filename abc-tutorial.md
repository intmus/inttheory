---
layout: page
title: ABC Notation Tutorial
abc: true
---

### Overview of ABC Notation

[ABC notation](http://abcnotation.com/) is a text-based system created by Chris Walshaw for recording musical notation. 
Due to its simple but powerful interface, developers have been able to create software that renders ABC notation into standard musical notation while also providing editable, instant playback. 
This website uses [abcjs](https://github.com/paulrosen/abcjs), a javascript package developed by Gregory Dyke and Paul Rosen.

### Known Technical Issues

You may view our [Known Technical Issues]({{ site.baseurl }}/known-technical-issues.html) page if you are having technical difficulties with any portion of the website.
Chrome browser has the most complete support for abcjs functionality.

### Introducing the Editor

Interactive examples are embedded in the text using an ABC editor powered by [abcjs](https://github.com/paulrosen/abcjs). 
It would be overwhelming to try to learn **all** the commands and entry nuances of our ABC javascript editor, so instead, we recommend that you just play with some examples to see how it works.
Try playing with the two basic examples below to see what a change in the textbox does to the music.

When you click on an object in the music, it will highlight the appropriate text in the editor.
If you place your cursor in the editor's textbox, it will highlight the corresponding object in the music.
After you have tried to play with it for a bit, continue reading below for a basic overview of the editor functions.
(**Once you make *many* changes, the editor may lock. To fix this, hit the reset button below the editor to continue. If you'd like to save your changes and continue, you simply need to copy your all the text in the textbox, and then paste it over the old text after you hit reset.**)

{% capture ex1 %}X: 1
T:Happy Birthday
M:3/4
L:1/4
Q:1/4=90
K:G
D/2>D/2| E D G| F2 D/2>D/2| E D A| G2 D/2>D/2| 
d B G| F E c/2>c/2| B G A| G2|]{% endcapture %}
{% include abc-example.html number="1" abc=ex1 %}

{% capture ex2 %}X: 2
T:Happy Birthday
M:3/4
L:1/4
Q:1/4=90
K:G
V:1 clef=bass
D,/2>D,/2| E, D, G,| F,2 D,/2>D,/2| E, D, A,| G,2 D,/2>D,/2| 
d, B, G,| F, E, c,/2>c,/2| B, G, A,| G,2|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}

### Basic Entry

Each piece of music is entered in two parts: the header and the body.

The header contains all the information needed to setup musical notation such as clefs, keys, and time signatures.
Each component in the header will consist of an abbreviation, a colon, and an instruction.
The abbreviation tells the editor **what you are editing** and the instruction tells the editor **what to do**.
For example, `M: 4/4` will give you a meter of 4/4.
Note that the `X:` field is a place-holder necessary for the website implementation and does not affect the musical notation.

The body contains the actual musical notes as well as bar lines and repeats.
- Note names are entered as letter names.
- Accidentals:
    - Put a `^` before the letter to add a sharp to the pitch. (F-sharp is written `^F`)
      - Add two `^` for a double-sharp. `^^`
    - Put a `_` before the letter to add a flat to the pitch. (E-flat is written `_E`)
      - Add two `_` for a double-flat. `__`
    - Put a `=` before the letter to add a natural to the pitch (E-natural is written `=E`)
- Octaves of pitches are determined by two factors:
    - An upper-case `C` denotes C4 (middle C), and a lower-case `c` denotes C5.
    - To alter these in either direction, you can add an apostrophe `'` after the letter to raise it an octave, or you can add a comma `,` after a letter to lower it an octave.
      - The simplest way to get C3 is to add a comma after an upper-case "C" - `C,`
      - You could also write C3 by adding two commas to a lower-case "C" - `c,,`
      - The simplest way to notate C6 is a lower-case "c" with an apostrophe - `c'` - but you could also write it by affixing two apostrophes after an upper-case "C" - `C''`
- Rhythms and note length
    - In your header, you will set a default note length with the command L.
      - If you set a default note length of a quarter note `L: 1/4` in your header, all pitches will default to a quarter note length.
    - To lengthen a note, add a number **after** the pitch name and the editor will multiply your note length by that amount.
      - If you set a default note length of a quarter note `L: 1/4` in your header, but would like a half-note, you only need to add a `2` after a note name. If you add a `3`, you will get a dotted half-note. If you add a `4` after a note name, you will get a whole note. Etc.
    - To shorten a note, add a back-slash and a number **after** the pitch name and the editor will divde your note length by that amount.
        - If you set a default note length of a quarter note `L: 1/4` in your header, but would like an eighth-note, you only need to add a `/2` after a note name. If you add a `/4` after a note name, you will get a sixteenth-note. Etc.
- Beaming is controlled by adding or subtracting spaces between notes.
- Barlines must be manually added using a pipe, `|`.
- You can start a new system by hitting enter and continuing your note-entry on the following line.
- Blank lines indicate the end of a song. Avoid blank lines in the editor!

## Adding Voices and Changing Clefs

The last basic function that you may want to use is adding voices and changing clefs.
Both of these are done using the "voice" `V:` option.
Take the following example:

{% capture ex3 %}X:3
T:Happy Birthday
T:for String Quartet
M:3/4
Q:1/4=90
L:1/4
K:C
V:1 name=Violin
G/2>G/2| A G c| B2 |
w: Hap-py birth-day to you
V:2 name=Violin
E| F G2| G2|
V:3 name=Viola clef=alto
C| B,2 E| D2|
V:4 name=Cello clef=bass
C,| F, E,/2-D,/2 C,| G, G,,|{% endcapture %}
{% include abc-example.html number="3" abc=ex3 %}

### Have fun

Try creating new music at the [ABC Playground]({{ site.baseurl }}/abc-playground.html).
Use Chrome browser for the full functionality, allowing you to enter ABC, render notation, play music, and download MIDI. 
Click the "print" button to print out your rendered notation or save as PDF.

### Existing Tutorials

Because ABC notation is a well-established notation standard, there are many websites that offer excellent tutorials on how to enter music using this method.
If you would like to learn more about the advanced capabilities of ABC Notation, please visit:

- [**Steve Manfsfield's ABC Notation tutorial**](http://www.lesession.co.uk/abc/abc_notation.htm) - an excellent place to start
- [**ABC Notation Home Page**](http://abcnotation.com/) - good help forums
- [**ABC Standard Notation Wiki**](http://abcnotation.com/wiki/abc:standard:v2.1#abc_tutorials) - very detailed
- [**Paul Rosen's and Gregory Dyke's explanation of their javascript, abcjs**](https://abcjs.net/#how)
