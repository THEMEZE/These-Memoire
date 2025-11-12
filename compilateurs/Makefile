# Makefile pour compiler la thèse avec latexmk

TEXFILE = main
BUILD_DIR = build

.PHONY: all clean veryclean view

all:
	latexmk -pdf -output-directory=$(BUILD_DIR) $(TEXFILE).tex

view:
	open $(BUILD_DIR)/$(TEXFILE).pdf

clean:
	latexmk -c -output-directory=$(BUILD_DIR)

veryclean: clean
	rm -f $(BUILD_DIR)/$(TEXFILE).pdf

#📌 Astuce macOS : open ouvre le PDF dans l'application par défaut (Preview, Skim, etc).
