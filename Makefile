include config.mk

## add       : Add notes to anki using AnkiConnect
.PHONY : add
format : add.py $(IN_MD) 
	python $^ $(SOURCES) $(TAGS)

## reformat     : Remove [latex] tags, convert [$] tags
.PHONY : reformat
reformat : reformat.py $(IN_MD)
	python $< < $(IN_MD)

## trash-in     : Trash input .md, create empty one
.PHONY : trash-in 
trash-in : 
	trash $(IN_MD)
	touch $(IN_MD)

## help         : Show arguments and what they do
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
