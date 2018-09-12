# Anki helpers

This is a group of scripts to make entering cards into [Anki](https://apps.ankiweb.net/) easier and faster by allowing you to create cards using your text editor of choice, and specify certain card attributes with text shortcuts.

The `add.py` script format notes into a CSV-like format, then uses the [AnkiConnect](https://foosoft.net/projects/anki-connect/index.html) add-on to add them into Anki (you must have the AnkiConnect add-on installed in Anki, and the Anki application open).

Running

```bash
make help
```

will display all the things that can be made.

In general, the makefile expects an `input.md` file in the project folder that contains cards formatted as follows:

```markdown
character indicating card type 1
;
Front of card 1
;
Back of card 2
;
Remarks field (not present in default Anki setup, but recommended)
;
Sources field (not present in default Anki setup, but recommended)
;
Tags 1

---

character indicating card type 2
;
Front of card 2
;
Back of card 2
;
Remarks field 2
;
Sources field 2
;
Tags 2

---
```

For example,

```markdown
r
;
Capital of Kansas
;
Topeka
;
;
Wikipedia
;
tag1


---

b
;
Who is Billy's favorite superhero?
;
Batman
;
He also likes Magneto from X-men
;
;
tag2 tag3

---
```

Implemented characters indicating card types are:

1. `b` for Basic
2. `r` for Basic (and reversed)
3. `c` for Cloze
4. `o` for [Cloze (overlapping)](https://ankiweb.net/shared/info/969733775)
