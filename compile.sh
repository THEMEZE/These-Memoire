##!/bin/bash

# Script de compilation du manuscrit de thèse

# Demander si on veut tout compiler
read -p "Souhaites-tu tout compiler ? (o/n) " reponse_compile
if [[ "$reponse_compile" == "o" || "$reponse_compile" == "O" ]]; then
    python3 ./compilateurs/compil_tex.py
fi

TEXFILE="main"
OUTDIR="build"

echo "🛠 Compilation du manuscrit..."

mkdir -p "$OUTDIR"

#latexmk -pdf -output-directory="$OUTDIR" "$TEXFILE.tex"

latexmk -pdf -output-directory="$OUTDIR" "$TEXFILE.tex" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Compilation réussie. PDF généré dans $OUTDIR/$TEXFILE.pdf"
else
    echo "❌ Échec de la compilation."
fi

# Demander si on veut faire un git push
read -p "Souhaites-tu synchroniser (push) sur Git ? (o/n) " reponse_git
if [[ "$reponse_git" == "o" || "$reponse_git" == "O" ]]; then
    python3 ./compilateurs/synchroniser_git.py
fi

