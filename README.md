# Anki helpers

This is a rough group of scripts to make entering cards into Anki easier and faster by allowing you to create cards using your text editor of choice, and specify certain card attributes with text shortcuts.

These scripts format cards into a .csv file (fields separated by semicolons) which can be imported into Anki. The applescript can then do most of the work of actually importing them them to Anki.

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
Remarks field (not present in default anki setup, but recommended)

---

character indicating card type 2
;
Front of card 2
;
Back of card 2
;
Remarks field 2

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


---

b
;
Who is Billy's favorite superhero?
;
Batman
;
He also likes Magneto from X-men

---
```

A field for Sources and tags can be specified in the Makefile, which will be added to all notes.

Implemented characters indicating card types are:
1. `b` for Basic
2. `r` for Basic (and reversed)
3. `c` for Cloze
4. `o` for [Cloze (overlapping)](https://ankiweb.net/shared/info/969733775)

The applescript just executes keyboard commands, so it requires Anki to remain in the foreground while running. It also therefore requires the most user monitoring and input.