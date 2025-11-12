# 📚 Manuscrit de thèse – Étude de la dynamique hors-équilibre d'un gaz de boson unidimentionnel

Ce dépôt contient l'ensemble des fichiers LaTeX nécessaires à la compilation du manuscrit de thèse de doctorat.

## 🗂 Structure du projet

* `thesis/` — Répertoire racine du projet
    * `main.tex` — Fichier principal qui compile toute la thèse
    * `preamble.tex` — Définit la classe, les packages et les réglages globaux
    * `thesis.bib` — Bibliographie au format BibTeX
    * `README.md` — Instructions pour compiler et comprendre la structure
    * `Makefile` ou `compile.sh` — Script pour compiler automatiquement
    * `binder/`
		* `Project.toml`
		* `Manifest.toml`   # recommandé
    * `figures/` — Dossier des figures
		* `chapitre1/` — Figures du chapitre 1
        * `chapitre2/` — Figures du chapitre 2
        * `...` — Etc. pour les autres chapitres
    * `chapters/` — Contenu principal de la thèse
        * `intro.tex` — Introduction
        * `chapitre1.tex` — Premier chapitre
        * `chapitre2.tex` — Deuxième chapitre
        * `conclusion.tex` — Conclusion
        * `annexes.tex` — Annexes
    * `tex/` — Fichiers auxiliaires LaTeX
        * `macros.tex` — Définitions de macros
        * `commands.tex` — Commandes personnalisées
        * `packages.tex` — Chargement des packages
    * `build/` — Fichiers générés automatiquement à la compilation
        * À **ignorer** via `.gitignore`
    * `.vscode`/
        * `settings.json`   ← ⚙️ LTEX

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
```sh
[![Binder](https://mybinder.org/badge_logo.svg)](
  https://mybinder.org/v2/gh/<utilisateur>/<répertoire>/<branche>?filepath=<chemin/vers/notebook.ipynb>
)
```

Cliquez sur le badge Binder pour lancer un environnement Jupyter avec ce dépôt.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/THEMEZE/These-Memoire/main)

### 📊 Lancer le notebook Julia sur Binder

Cliquez ci-dessous pour exécuter le notebook Monte-Carlo en ligne via Binder :

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/THEMEZE/These-Memoire/HEAD?filepath=figures/04_GGE_Fluctuation/Monte-Carlo-Julia-Gge.ipynb)

> 💡 Requiert que le dépôt contienne un environnement Julia valide dans `binder/`.


### ⚙️Manifest.toml
```sh
cd chemin/vers/These-Memoire
julia
]          # <-- ne tape pas le crochet, appuie juste sur la touche ]
activate .
add IJulia
```

## ⚙️ Utilisation avec Repl.it

- **Python**: [![Run on Repl.it](https://repl.it/badge/github/votre-utilisateur/quantum-mechanics-thesis)](https://repl.it/github/THEMEZE/These-Memoire?language=python3)
- **Julia**: [![Run on Repl.it](https://repl.it/badge/github/THEMEZE/quantum-mechanics-thesis)](https://repl.it/github/THEMEZE/These-Memoire?language=julia)
- **Fortran**: [![Run on Repl.it](https://repl.it/badge/github/THEMEZE/quantum-mechanics-thesis)](https://repl.it/github/THEMEZE/These-Memoire?language=fortran)

### Fluctuation 
- **Julia**: [![Run on Repl.it](https://repl.it/badge/github/THEMEZE/quantum-mechanics-thesis)](https://repl.it/github/THEMEZE/These-Memoire/figures/04_GGE_Fluctuation/Monte-Carlo-Julia-Gge.jl?language=julia)

## ⚙️ Instructions de Compilation

### ⚙️ Python

Pour exécuter un script Python, utilisez la commande suivante :

```sh
python3 idée1/codes/python/idée1.py
```
### ⚙️ Julia
```sh
julia figures/04_GGE_Fluctuation/Monte-Carlo-Julia-Gge_Pluto.jl
```

#### Pluto
Voici un guide pas à pas pour transformer ton script en *notebook Pluto* interactif, tout en gardant la rigueur scientifique.
##### 🧰 1. Installation de Pluto
```sh
julia
import Pkg
Pkg.add("Pluto")
```

##### ▶️ 2. Lancer Pluto
```sh
using Pluto
Pluto.run()
```


```sh
julia figures/04_GGE_Fluctuation/Monte-Carlo-Julia-Gge.jl
```

# ⚙️ Git  Mise à jour
```bash
git add .
git commit -m "Mise à jour"
git push
```

```bash
#!/bin/zsh

# === Configuration ===
THRESHOLD=50M  # fichiers plus gros que 50MB
LOGFILE="git_lfs_add.log"

# Installer LFS si pas déjà fait
git lfs install

# Trouver tous les fichiers >50MB
echo "Recherche des fichiers > $THRESHOLD..." | tee -a $LOGFILE
find . -type f -size +$THRESHOLD | while read f; do
    echo "Ajout à Git LFS : $f" | tee -a $LOGFILE
    git lfs track "$f"
    git add "$f"
done

# Ajouter le fichier .gitattributes créé/modifié par LFS
git add .gitattributes

# Commit
git commit -m "Ajout automatique des fichiers > $THRESHOLD dans Git LFS"

# Push
git push
```

```bash
THRESHOLD=50M
LOGFILE="git_lfs_add.log"
git lfs install
echo "Recherche des fichiers > $THRESHOLD..." | tee -a $LOGFILE
find . -type f -size +$THRESHOLD | while read f; do
    echo "Ajout à Git LFS : $f" | tee -a $LOGFILE
    git lfs track "$f"
    git add "$f"
done
git add .gitattributes
git commit -m "Ajout automatique des fichiers > $THRESHOLD dans Git LFS"
git push
```


# Sauvegarde type Time Machine en bash

Ce script lance une sauvegarde incrémentale avec `rsync` (`./compilateurs/backup_these.sh`)  :

```bash
#!/bin/bash
#!/bin/bash

# === Configuration ===
SRC="/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire"
DEST="/Volumes/NO NAME/These_Memoire"
LOGFILE="/Volumes/NO NAME/backup_these.log"

# Créer un dossier de destination horodaté pour garder les anciennes versions
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DEST_TIMESTAMPED="${DEST}_${TIMESTAMP}"

# === Sauvegarde ===
echo "=== Sauvegarde lancée $(date) ===" >> "$LOGFILE"

# Crée une copie horodatée
rsync -avh "$SRC/" "$DEST_TIMESTAMPED/" >> "$LOGFILE" 2>&1

echo "=== Sauvegarde terminée $(date) ===" >> "$LOGFILE"

```

# Si problème avec .pynb (car trop lourd) : 

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


## ✅ Solution : Réécrire l’historique pour supprimer complètement ces gros fichiers

1. Installe le paquet BFG Repo-Cleaner (plus rapide que filter-branch) :
```bash
brew install bfg
```

2. Sauvegarde ton dépôt :
```bash
cp -r These_Memoire These_Memoire_backup
```

3. Supprime les fichiers problématiques de l’historique :
Depuis le dossier de ton dépôt :
```
bfg --delete-files bord_expansion_julia_2024-11-24.ipynb
bfg --delete-files bord_expansion_julia_2024-11-18.ipynb
bfg --delete-files box_expansion_julia_final_2_2024-03-13.ipynb
```

4. Nettoie le dépôt :
```
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

5. Force le push (⚠️ dangereux si d'autres personnes travaillent dessus) :
```bash
git push origin --force
```

🧹 Bonus : Ajouter à .gitignore pour éviter de recommencer
Ajoute ceci dans .gitignore :
```bash
figures/06_Bipart/*.ipynb
```
ou
```bash
echo "figures/06_Bipart/*.ipynb" >> .gitignore
git add .gitignore
```

## ✅ Objectif : Forcer le push de la version actuelle sans les gros .ipynb

🛠️ Étapes claires et testées :
1. Supprime les gros fichiers du suivi Git
Assure-toi qu’ils ne sont plus suivis (même s’ils sont dans ton dossier local) :
```bash
git rm --cached figures/06_Bipart/bord_expansion_julia_2024-11-24.ipynb
git rm --cached figures/06_Bipart/bord_expansion_julia_2024-11-18.ipynb
git rm --cached figures/06_Bipart/box_expansion_julia_final_2_2024-03-13.ipynb
```
2. Ajoute un fichier .gitignore pour éviter qu’ils reviennent
```bash
echo "figures/06_Bipart/*.ipynb" >> .gitignore
git add .gitignore
```
3. Réécris l’historique pour effacer les fichiers trop gros
Installe BFG si ce n’est pas fait :
```bash
brew install bfg
```
Puis dans le dossier de ton dépôt :
```bash
bfg --delete-files bord_expansion_julia_2024-11-24.ipynb
bfg --delete-files bord_expansion_julia_2024-11-18.ipynb
bfg --delete-files box_expansion_julia_final_2_2024-03-13.ipynb
```
4. Nettoie les résidus Git
```bash
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```
5. Force le push vers GitHub
```bash
git push origin --force
```
⚠️ Attention :
-- Le --force va écraser l’historique distant, donc si quelqu’un d’autre bosse dessus, il faut le prévenir.

-- Tu ne pourras plus récupérer les gros .ipynb via GitHub, donc garde-les bien localement ou ailleurs.


## 🗂 Structure du projet
```bash
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
