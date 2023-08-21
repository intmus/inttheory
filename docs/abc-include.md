# How to use abcjs include

In page yml header add `abc: true` to pull in the necessary js files.
For example:

```
---
layout: page
title: ABC include demo
abc: true
---
```

Where you want to add an ABC editor, use the `abc-example.html` include, `{% include abc-example.html number="1" abc=ex1 %}`. 
The include must have two variables, `number` and `abc`. 
- `number` must be a unique number on the page, used to make each ABC editor separate.
- `abc` is the ABC notation. To create the `abc` variable, quote the notation inline, or use a Liquid capture statement before the include and use the captured variable in the include.

> String variables can be passed to the include, however they must be quoted with `'` or `"`. 
> Since ABC notation uses both quote symbols (e.g. `clef="alto"` and `a'`), it can not be reliably quoted inline.
> Incorrect quoting will cause Liquid errors that prevent Jekyll from building the site.

For example:

```
{% include abc-example.html number="1" abc='X: 1
M: 4/4
L: 1/8
K: Emin
|:D2|EB{c}BA B2 EB|~B2 AB dBAG|FDAD BDAD|FDAD dAFD|' %}
```

```
{% capture ex2 %}X:1
T: Enharmonic Equivalence
T: Each measure contains two notes that are enharmonically equivalent.
M:2/2
L:1/2
K:C
V:1 name="Treble Clef"
_B ^A |f ^e |^^E ^F |]
V:2 name="Alto Clef" clef="alto"
^G _A |B, _C |^^G, A,|]
V:3 name="Tenor Clef" clef="tenor"
^F, _G, |F, _E, |D, ^^C,|]
V:4 name="Bass Clef" clef="bass"
_D, ^C, |^B,, C, |D, ^^E,|]{% endcapture %}
{% include abc-example.html number="2" abc=ex2 %}
```

Important points:
- the capture has a unique variable name (e.g. `ex1`), that is repeated in the include without quotes (e.g. `abc=ex1`).
- the 1st line of the ABC notation starts on the same line as the capture
- the last line of the ABC notation has the endcapture tag
- be careful of extra whitespace and blank lines as they will cause abcjs errors
- every tune *must* have a value for `M:` and `K:` or there will be abcjs or midi playback errors 
