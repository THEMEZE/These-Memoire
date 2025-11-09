# from pypdf import PdfReader, PdfWriter
# import os

# # PDF source
# input_pdf = "main.pdf"

# # Dictionnaire avec les parties à extraire et leur plage de pages (1-indexée)
# parts = {
#     "Titre" : , 
#     "Sommaire": (1, 2),
#     "Introduction": (3, 6),
#     "1. Modèle de Lieb-Liniger et approche Bethe Ansatz": (7, 28),
#     "2. Relaxation et Équilibre dans les Systèmes Quantiques Intégrables : Une Approche par la Thermodynamique de Bethe": (29, 46),
#     "3. Dynamique hors-équilibre et hydrodynamique généralisée": (47, 60),
#     "4. Fluctuation de la distribution de rapidité dans des état d'équilibre": (61, 82),
#     "5. Dispositif expérimental": (83, 106),
#     "6. Étude du protocal de bi-partition : Mesure de distribution de rapidités locales rho(x,θ) pour des systèmes hors équilibre": (107, 124),
#     "7. Mise en place d'un confinement longitudinale dipolaire": (125, 150),
#     "Conclusion": (151, 151),
#     "Annex A - Action de P et H sur l'état de Bethe": (153, 156),
#     "Annex B - Réduction GHD vers transport d’Euler": (157, 158),
#     "Annex C - Dérivation alternative des fluctuations de rho": (159, 164),
#     "Annex D - Propriétés des facteurs d'homothétie": (165, 166),
#     "Annex E - Polarisabilité dynamique et potentiel dipolaire optique": (167, 172),
#     "Annex F - Moment tensoriel J=1/2": (173, 174),
#     "Résumé" :  , 
# }

# # Répertoire de sortie
# output_dir = "pdf_decoupes"
# os.makedirs(output_dir, exist_ok=True)  # ✅ crée le dossier s'il n'existe pas

# # Charger le PDF
# reader = PdfReader(input_pdf)

# # Créer un PDF pour chaque partie
# for name, (start, end) in parts.items():
#     writer = PdfWriter()
#     for i in range(start - 1, end):  # PyPDF est 0-indexé
#         writer.add_page(reader.pages[i])
    
#     # Remplacer caractères interdits dans les noms de fichiers
#     safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in name)
    
#     output_path = os.path.join(output_dir, f"{safe_name}.pdf")
#     with open(output_path, "wb") as f:
#         writer.write(f)
    
#     print(f"{name} -> {output_path} créé avec succès ✅")


from pypdf import PdfReader, PdfWriter
import os

# ============
# 📄 PDF source
# ============
input_pdf = "main.pdf"

# =============================
# 🧩 Parties à extraire (1-indexées)
# =============================
parts = {
    "Titre": 1,
    "Sommaire": 2,
    "Introduction": 4,
    "1. Modèle de Lieb-Liniger et approche Bethe Ansatz": 8,
    "2. Relaxation et Équilibre dans les Systèmes Quantiques Intégrables : Une Approche par la Thermodynamique de Bethe": 30,
    "3. Dynamique hors-équilibre et hydrodynamique généralisée": 48,
    "4. Fluctuation de la distribution de rapidité dans des états d'équilibre": 62,
    "5. Dispositif expérimental": 84,
    "6. Étude du protocole de bi-partition : Mesure de distribution de rapidités locales rho(x,θ) pour des systèmes hors équilibre": 108,
    "7. Mise en place d'un confinement longitudinal dipolaire": 126,
    "Conclusion": 152,
    "Annex A - Action de P et H sur l'état de Bethe": 153,
    "Annex B - Réduction GHD vers transport d’Euler": 157,
    "Annex C - Dérivation alternative des fluctuations de rho": 159,
    "Annex D - Propriétés des facteurs d'homothétie": 165,
    "Annex E - Polarisabilité dynamique et potentiel dipolaire optique": 167,
    "Annex F - Moment tensoriel J=1/2": 173,
    "Résumé": 175,
}

# =========================
# 📁 Répertoire de sortie
# =========================
output_dir = "pdf_decoupes"
os.makedirs(output_dir, exist_ok=True)

# =========================
# 🔍 Lecture du PDF
# =========================
reader = PdfReader(input_pdf)
nb_pages = len(reader.pages)

# =========================
# 🧮 Conversion auto des numéros en plages
# =========================
titles = list(parts.keys())
starts = list(parts.values())
ranges = {}

for i, title in enumerate(titles):
    start = starts[i]
    if i < len(starts) - 1:
        end = starts[i + 1] - 1  # la page juste avant la suivante
    else:
        end = nb_pages  # dernière section jusqu’à la fin
    ranges[title] = (start, end)

# =========================
# ✂️ Découpage automatique
# =========================
for name, (start, end) in ranges.items():
    writer = PdfWriter()
    for i in range(start - 1, end):  # PyPDF est 0-indexé
        writer.add_page(reader.pages[i])
    
    # Nom de fichier sécurisé
    safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in name)
    
    # Sauvegarde
    output_path = os.path.join(output_dir, f"{safe_name}.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"✅ {name} -> pages {start}-{end} -> {output_path}")

print("\n🎉 Tous les PDF ont été créés avec succès !")
