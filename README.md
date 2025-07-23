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

## 🗂 Structure du projet

thesis/
├── main.tex                     ## Le fichier principal, qui appelle les chapitres, gère la structure globale, et compile tout.
├── preamble.tex                 ## Contient toutes les options de classe, packages, et réglages généraux.
├── thesis.bib                   ## Bibliographie au format BibTeX.
├── README.md                    ## Instructions pour compiler et structure générale du projet.
├── Makefile / compile.sh        ## Script pour compiler facilement.
├── figures/                     ## Contient les figures (par chapitre si nécessaire).
│   ├── chapitre1/
│   ├── chapitre2/
│   └── ...
├── chapters/                    ## Fichiers principaux de contenu (chapitres, intro, conclusion, annexes).
│   ├── intro.tex
│   ├── chapitre1.tex
│   ├── chapitre2.tex
│   ├── conclusion.tex
│   └── annexes.tex
├── tex/                         ## Fichiers auxiliaires LaTeX (macros, commandes, packages).
│   ├── macros.tex
│   ├── commands.tex
│   └── packages.tex
└── build/                       ## Répertoire généré automatiquement (.aux, .log, .pdf...). À ignorer via .gitignore.


## ⚙️ Compilation Manuscrit

### Méthode recommandée (avec `latexmk`)
Assurez-vous d'avoir `latexmk` installé :

```bash
latexmk -pdf main.tex 
```

Pour une compilation propre :
```bash
latexmk -C
```

Ou en ligne de commande classique

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Ou via le script qui demande si on veux trous compiler (les tikz aussi) et puis après compilation si on veux push sur ce git
```bash
./compile.sh
```

## ⚙️ Utilisation avec Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/THEMEZE/These-Memoire/main)

Cliquez sur le badge Binder pour lancer un environnement Jupyter avec ce dépôt.

## ⚙️ Utilisation avec Repl.it

- **Python**: [![Run on Repl.it](https://repl.it/badge/github/votre-utilisateur/quantum-mechanics-thesis)](https://repl.it/github/THEMEZE/These-Memoire?language=python3)
- **Julia**: [![Run on Repl.it](https://repl.it/badge/github/THEMEZE/quantum-mechanics-thesis)](https://repl.it/github/votre-utilisateur/These-Memoire?language=julia)
- **Fortran**: [![Run on Repl.it](https://repl.it/badge/github/THEMEZE/quantum-mechanics-thesis)](https://repl.it/github/votre-utilisateur/These-Memoire?language=fortran)

## ⚙️ Instructions de Compilation

### ⚙️ Python

Pour exécuter un script Python, utilisez la commande suivante :

```sh
python3 idée1/codes/python/idée1.py
```

# ⚙️ Git  Mise à jour
```bash
git add .
git commit -m "Mise à jour"
git push
```

## 🧰 Utiliser Git LFS (si tu dois quand même versionner ces fichiers)

```bash
brew install git-lfs
```

Installe Git LFS
```bash
git lfs install
```

Suit les fichiers .ipynb avec Git LFS
```bash
git lfs track "*.ipynb"
echo "*.ipynb filter=lfs diff=lfs merge=lfs -text" >> .gitattributes
```

Ajoute à nouveau les fichiers
```bash
git add .gitattributes
git add figures/06_Bipart/*.ipynb
git commit -m "Utilise Git LFS pour les fichiers volumineux"
git push
```
```bash
git lfs install
git lfs track "*.ipynb"
git add .gitattributes
git add figures/06_Bipart/*.ipynb
git commit -m "Track large notebooks with Git LFS"
git push
```

⚠️ Attention : tous les membres du projet devront avoir Git LFS installé localement.

## 🧹 Pour nettoyer un commit déjà envoyé (si tu as tenté un push auparavant avec un gros fichier)
Tu peux utiliser :
```bash
git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch figures/06_Bipart/bord_expansion_julia_2024-11-18.ipynb" \
--prune-empty --tag-name-filter cat -- --all
```
Puis :
```bash
git push origin --force
```





📌 Conseils
Modifier uniquement les fichiers dans chapters/ pour le contenu du manuscrit.
Ajouter les figures dans figures/chapitreX/ et les appeler dans les chapitres correspondants.
Les macros doivent être définies dans tex/macros.tex pour une meilleure lisibilité.
La bibliographie est définie dans thesis.bib et appelée automatiquement à la fin de main.tex.

📄 Licence
(Ce projet est privé / sous licence Creative Commons / à adapter selon les cas)

Dernière mise à jour : [jj/mm/aaaa]

- [x] #739
- [ ] <https://github.com/octo-org/octo-repo/issues/740>
- [ ] Add delight to the experience when all tasks are complete :tada:
