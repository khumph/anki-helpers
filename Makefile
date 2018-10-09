IN_MD=input.md

## add       : Add notes to anki using AnkiConnect
.PHONY : add
add : add.py $(IN_MD)
	python3 $^

## trash     : Trash input .md, create empty one
.PHONY : trash 
trash : 
	trash $(IN_MD)
	touch $(IN_MD)

## help      : Show arguments and what they do
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
