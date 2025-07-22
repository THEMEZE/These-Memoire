##!/bin/bash

# Script de compilation du manuscrit de thèse

#python ./compilateurs/compil_tex.py

TEXFILE="main"
OUTDIR="build"

echo "🛠 Compilation du manuscrit..."

mkdir -p "$OUTDIR"

latexmk -pdf -output-directory="$OUTDIR" "$TEXFILE.tex"

#latexmk -pdf -output-directory="$OUTDIR" "$TEXFILE.tex" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Compilation réussie. PDF généré dans $OUTDIR/$TEXFILE.pdf"
else
    echo "❌ Échec de la compilation."
fi

