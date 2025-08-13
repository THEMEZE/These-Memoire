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

def compile_latex_index_bibtex(path):
    compile_latex(path + ".tex")      # 1ère passe LaTeX
    compile_index(path + ".idx")      # makeindex
    compile_bibtex(path)              # bibtex
    compile_biblatex(path)              # bibtex
    compile_latex(path + ".tex")      # 2e passe LaTeX
    compile_latex(path + ".tex")      # 3e passe LaTeX (pour les refs/bib à jour)

def clean_auxiliary_files(tex_path):
    tex_path = Path(tex_path)
    base = tex_path.with_suffix('')
    directory = base.parent
    stem = base.name

    extensions = [
        ".aux", ".idx", ".ilg", ".ind", ".log",
        ".maf", ".out", ".toc", ".bbl", ".blg"
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
    #"./figures/06_Bipart/Figures.tex",
    #"./figures/06_Bipart/Shema.tex",
    #"./figures/06_Bipart/Shemas_2.tex",
    #"./figures/07_Dipolaire/Figures.tex",
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

