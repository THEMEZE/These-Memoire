import subprocess
from pathlib import Path

import time

def compile_latex(tex_path):
    tex_path = Path(tex_path)
    cwd = tex_path.parent
    filename = tex_path.name
    if not tex_path.exists():
        print(f"❌ Fichier LaTeX introuvable : {filename}")
        return
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", filename],
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ LaTeX compilé : {filename}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur compilation LaTeX : {filename}")

def compile_index(idx_path):
    idx_path = Path(idx_path)
    if not idx_path.exists():
        print(f"⚠️ Aucun .idx trouvé pour {idx_path.stem}, index ignoré.")
        return   
    cwd = idx_path.parent
    filename = idx_path.name
    try:
        subprocess.run(
            ["makeindex", filename],
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Index généré : {filename}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur makeindex : {filename}")

import subprocess
from pathlib import Path

def compile_indices(tex_path):
    """
    Compile l'index (.idx) et les acronymes (.acn) générés par LaTeX.
    """
    tex_path = Path(tex_path)
    stem = tex_path.stem
    cwd = tex_path.parent

    # --- Index classique ---
    idx_file = cwd / f"{stem}.idx"
    if idx_file.exists():
        try:
            subprocess.run(
                ["makeindex", idx_file.name],
                cwd=cwd,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"✅ Index généré : {idx_file.stem}.ind")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur makeindex sur {idx_file.name}")
    else:
        print(f"⚠️ Aucun .idx trouvé pour {stem}, index ignoré.")

    # --- Acronymes glossaries ---
    acn_file = cwd / f"{stem}.acn"
    acr_file = cwd / f"{stem}.acr"
    alg_file = cwd / f"{stem}.alg"
    ist_file = cwd / "acronyms.ist"  # généré automatiquement par glossaries

    if acn_file.exists():
        try:
            cmd = [
                "makeindex",
                "-s", str(ist_file) if ist_file.exists() else "acronyms.ist",
                "-t", str(alg_file),
                "-o", str(acr_file),
                str(acn_file)
            ]
            subprocess.run(
                cmd,
                cwd=cwd,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"✅ Acronymes générés : {acr_file.name}")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur makeindex sur {acn_file.name}")
    else:
        print(f"⚠️ Aucun .acn trouvé pour {stem}, acronymes ignorés.")

def compile_acr(idx_path):
    idx_path = Path(idx_path)
    if not idx_path.exists():
        print(f"⚠️ Aucun .idx trouvé pour {idx_path.stem}, index ignoré.")
        return
    cwd = idx_path.parent
    filename = idx_path.name
    filename = idx_path
    try:
        subprocess.run(
            ["makeglossaries", filename],
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Acr généré : {filename}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur Acr : {filename}")
        
def compile_acr(tex_path):
    """
    Compile les acronymes/glossaires d'un fichier .tex donné.
    """
    tex_path = Path(tex_path)
    #if not tex_path.exists():
    #    print(f"⚠️ Fichier introuvable : {tex_path.name}, acronymes ignorés.")
     #   return

    cwd = tex_path.parent
    stem = tex_path.stem  # nom du fichier sans extension
    #p = Path("./main.tex")
    #print(p.exists())  # doit retourner True
    #print(p.stem)      # doit retourner "main"

    try:
        subprocess.run(
            ["makeglossaries", stem],
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Acronymes/glossaires générés pour : {stem}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur lors de la génération des acronymes : {stem}")



def compile_bibtex(tex_stem):
    tex_stem = Path(tex_stem)
    cwd = tex_stem.parent
    stem = tex_stem.name
    aux_file = cwd / f"{stem}.aux"
    if not aux_file.exists():
        print(f"⚠️ Aucun .aux trouvé pour {stem}, bibtex ignoré.")
        return
    try:
        subprocess.run(
            ["bibtex", stem],
            cwd=cwd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ BibTeX compilé : {stem}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur BibTeX : {stem}")
        
def compile_biblatex(tex_file, show_output=False):
    """
    Compile la bibliographie BibLaTeX d'un fichier .tex donné.

    Args:
        tex_file (str or Path): Chemin vers le fichier .tex
        show_output (bool): Affiche stdout/stderr de Biber si True
    """
    tex_file = Path(tex_file)
    cwd = tex_file.parent
    stem = tex_file.stem
    aux_file = cwd / f"{stem}.aux"

    if not aux_file.exists():
        print(f"⚠️ Aucun fichier .aux trouvé pour {stem}, compilation BibLaTeX ignorée.")
        return

    try:
        subprocess.run(
            ["biber", stem],
            cwd=cwd,
            check=True,
            stdout=None if show_output else subprocess.DEVNULL,
            stderr=None if show_output else subprocess.DEVNULL
        )
        print(f"✅ BibLaTeX compilé : {stem}")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur lors de la compilation BibLaTeX : {stem}")

def compile_biblatex(tex_file, show_output=False):
    """
    Compile la bibliographie BibLaTeX d'un fichier .tex donné.

    Args:
        tex_file (str or Path): Chemin vers le fichier .tex
        show_output (bool): Affiche stdout/stderr de Biber si True
    """
    tex_file = Path(tex_file)
    cwd = tex_file.parent
    stem = tex_file.stem
    aux_file = cwd / f"{stem}.aux"

    if not aux_file.exists():
        print(f"⚠️ Aucun fichier .aux trouvé pour {stem}, compilation BibLaTeX ignorée.")
        return

    try:
        result = subprocess.run(
            ["biber", stem],
            cwd=cwd,
            check=True,
            stdout=None if show_output else subprocess.DEVNULL,
            stderr=None if show_output else subprocess.DEVNULL
        )
        print(f"✅ BibLaTeX compilé avec succès pour : {stem}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la compilation BibLaTeX pour {stem}")
        if show_output:
            print(e)

def compile_latex_index_bibtex(path):
    compile_latex(path + ".tex")      # 1ère passe LaTeX
    #compile_index(path + ".idx")      # makeindex
    #compile_indices(path + ".acn")
    compile_acr(path)
    #compile_bibtex(path)              # bibtex
    compile_biblatex(path)#, show_output=True)            # biblatex
    compile_biblatex(path)            # biblatex
    compile_latex(path + ".tex")      # 2e passe LaTeX
    compile_latex(path + ".tex")      # 3e passe LaTeX (pour les refs/bib à jour)
    compile_latex(path + ".tex")      # 3e passe LaTeX (pour les refs/bib à jour)

def clean_auxiliary_files(tex_path):
    tex_path = Path(tex_path)
    base = tex_path.with_suffix('')
    directory = base.parent
    stem = base.name

    extensions = [
        ".aux", ".idx", ".ilg", ".ind", ".log",
        ".maf", ".out", ".toc", ".bbl", ".blg",
        ".acn" ,".acr" , ".alg", ".ist", ".bcf",
        ".run.xml", ".fdb_latexmk", ".fls", ".glg",
        ".glo", ".gls", ".synctex.gz", ".mtc",
    ] + [f".mtc{i}" for i in range(15)]

    deleted_files = []

    for ext in extensions:
        file = directory / (stem + ext)
        if file.exists():
            file.unlink()
            deleted_files.append(file.name)

    if deleted_files:
        print(f"🧹 Fichiers auxiliaires supprimés : {', '.join(deleted_files)}")
    else:
        print(f"🧼 Aucun fichier auxiliaire à supprimer pour {tex_path.name}")

# === CONFIGURATION ===

tex_files = [
    #"/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/Outils/Mind-Map-main/mind_map.tex",
    #"/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire_19_07_2025/BiPart/Figures/Figures.tex",
    #"/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire_19_07_2025/BiPart/Figures/Shema.tex",
    #"/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire_19_07_2025/BiPart/Figures/Shemas_2.tex",
    #"../These_Memoire_19_07_2025/Figures/Figures.tex",
    #"./figures/01_LL_BA/Figures.tex",
    #"./figures/02_GGE_TBA/Figures.tex",
    #"./figures/03_GHD/Figures.tex",
    #"./figures/04_GGE_Fluctuation/Figures.tex",
    #"./figures/05_Disp_Exp/Figures.tex",
    #"./figures/05_Disp_Exp/Figures_2.tex",
    #"./figures/06_Bipart/Figures.tex",
    #"./figures/06_Bipart/Shema.tex",
    #"./figures/06_Bipart/Shemas_2.tex",
    #"./figures/07_Dipolaire/Figures.tex",
    #"./figures/official_template_phd_universite-paris_saclay_2/Modele_These_UParisSaclay_2022.tex",
    # Ajoute ici les .tex à compiler seuls
]



tex_idx_bib_files = [
    #"/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire_19_07_2025/These_Memoire",
    "./main",
    # Ajoute ici les .tex (SANS .tex à la fin) à compiler avec index+bibtex
]

# === BOUCLE PRINCIPALE ===

if __name__ == "__main__":
#    while True:
    flag = True
    while flag :
        try:
            for tex_file in tex_files:
                compile_latex(tex_file)
                clean_auxiliary_files(tex_file)
            for tex_idx_bib_file in tex_idx_bib_files:
                compile_latex_index_bibtex(tex_idx_bib_file)
                clean_auxiliary_files(tex_idx_bib_file + ".tex")
        except Exception as e:
            print(f"💥 Erreur inattendue : {e}")
        flag = False
        # Pause entre les compilations (10 minutes)
        #time.sleep(600)

