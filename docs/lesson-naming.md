# Lesson file naming conventions

Content is organized in to chapters, each represented by one directory of files, which become a Jekyll Collection. 
The chapters are given a name in the `_config.yml` under collections.

Each Chapter is split into multiple Topics, given a letter.
Each Topic is split into three Parts: Overview, Examples, and Lesson.

- Overview:
    Skeleton text that prepares the student to learn from the exemplars by hinting at specific concepts the student should explore
    Introduces the topic without actually defining the rules
- Exemplars:
    Images that will be used in class to introduce each concept
    Separate from topic overview text so that I can have them viewing these without looking at the text
- Lesson (concepts and rules):
    Editable space in which TA can take notes on class discussion
    Then I will turn these notes into prose
    This will function as the primary reference text as it will contain the rules of the concepts as explained by the class with my annotations and terminology

To ensure lessons sort in the correct order in the TOC and sidebar navigation, file names follow the convention:

`[chapter number][topic letter][section number]-[section abbreviation]-[title].md`

Where section number and abbreviation are `1-ov`, `2-ex`, or `3-tx`.
for example:

`1a1-ov-pitchesclefs.md`
