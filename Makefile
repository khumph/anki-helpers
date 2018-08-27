include config.mk

## all          : Generate .csvs for import to Anki
.PHONY : all
all : add

## format       : Convert inputs .mds to .csvs
.PHONY : format
format : $(OUTPUT_CSVS)

$(OUTPUT_CSVS) : format.py $(IN_MD) 
	python $^ $(SOURCES) $(TAGS)

## add          : Add .csvs to Anki
.PHONY : add
add : format
	osascript add-to-anki.scpt $(shell find . -not -empty -name "*.csv" | python card-types.py)

## reformat     : Remove [latex] tags, convert [$] tags
.PHONY : reformat
reformat : reformat.py $(IN_MD)
	python $< < $(IN_MD)

## clean        : Remove auto-generated files
.PHONY : clean
clean :
	rm -f $(OUTPUT_CSVS)

## trash-in     : Trash input .md, create empty one
.PHONY : trash-in 
trash-in : 
	trash $(IN_MD)
	touch $(IN_MD)
	make clean

## help         : Show arguments and what they do
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
