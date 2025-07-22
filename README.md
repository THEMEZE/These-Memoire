# 📚 Manuscrit de thèse – [Titre de la thèse]

Ce dépôt contient l'ensemble des fichiers LaTeX nécessaires à la compilation du manuscrit de thèse de doctorat.

## 🗂 Structure du projet

thesis/
├── main.tex. 					## Le fichier principal, qui appelle les chapitres, gère la structure globale, et compile tout.
├── preamble.tex					## Contient toutes les options de classe, packages, et réglages généraux. Il appelle souvent packages.tex et macros.tex.
├── thesis.bib					## Bibliographie au format BibTeX.
├── README.md					## Instructions pour compiler et structure générale du projet.
├── Makefile (ou compile.sh)		## Script pour compiler facilement (avec latexmk ou pdflatex).
├── figures/						## Contient les figures (par chapitre si nécessaire).
│   ├── chapitre1/				## Tous les chapitres et annexes.
│   ├── chapitre2/
│   └── ...
├── chapters/
│   ├── intro.tex
│   ├── chapitre1.tex
│   ├── chapitre2.tex
│   ├── conclusion.tex
│   └── annexes.tex
├── tex/						## Sous-dossier pour les fichiers LaTeX auxiliaires (macros, commandes perso, etc).
│   ├── macros.tex
│   ├── commands.tex
│   └── packages.tex
└── build/ (généré automatiquement)	## Répertoire temporaire pour les fichiers .aux, .log, .pdf, etc. Peut être ignoré par Git.

thesis/
├── main.tex ## Le fichier principal, qui appelle les chapitres, gère la structure globale, et compile tout.
├── preamble.tex ## Contient toutes les options de classe, packages, et réglages généraux.
├── thesis.bib ## Bibliographie au format BibTeX.
├── README.md ## Instructions pour compiler et structure générale du projet.
├── Makefile (ou compile.sh) ## Script pour compiler facilement (avec latexmk ou pdflatex).
├── figures/ ## Contient les figures (par chapitre si nécessaire).
│ ├── chapitre1/
│ ├── chapitre2/
│ └── ...
├── chapters/
│ ├── intro.tex
│ ├── chapitre1.tex
│ ├── chapitre2.tex
│ ├── conclusion.tex
│ └── annexes.tex
├── tex/ ## Fichiers auxiliaires LaTeX (macros, commandes, etc.)
│ ├── macros.tex
│ ├── commands.tex
│ └── packages.tex
└── build/ ## Répertoire généré automatiquement (.aux, .log, .pdf...). À ignorer via .gitignore.

## ⚙️ Compilation

### Méthode recommandée (avec `latexmk`)
Assurez-vous d'avoir `latexmk` installé :

```bash
latexmk -pdf main.tex

Pour une compilation propre :
latexmk -C

Ou en ligne de commande classique

pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

Ou via le script
./compile.sh

📌 Conseils
Modifier uniquement les fichiers dans chapters/ pour le contenu du manuscrit.
Ajouter les figures dans figures/chapitreX/ et les appeler dans les chapitres correspondants.
Les macros doivent être définies dans tex/macros.tex pour une meilleure lisibilité.
La bibliographie est définie dans thesis.bib et appelée automatiquement à la fin de main.tex.

📄 Licence
(Ce projet est privé / sous licence Creative Commons / à adapter selon les cas)

Dernière mise à jour : [jj/mm/aaaa]
# These-Memoire
# These-Memoire
