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


# from pypdf import PdfReader, PdfWriter
# import os

# # ============
# # 📄 PDF source
# # ============
# input_pdf = "main.pdf"

# # =============================
# # 🧩 Parties à extraire (1-indexées)
# # =============================
# parts = {
#     "Titre": {"page" : 1 , "pages" : "1-1" , "nb_pages" : 1},
#     "Blanc": {"page" : 2 , "pages" : "2-2" , "nb_pages" : 1},
#     "Acronymes" : {"page" : 3 , "pages" : "3-4" , "nb_pages" : 2},
#     "Sommaire": {"page" : 5 , "pages" : "" , "nb_pages" : ""},
#     "Introduction": {"page" : 7 , "pages" : "" , "nb_pages" : ""},
#     "1. Modèle de Lieb-Liniger et approche Bethe Ansatz": {"page" : 9 , "pages" : "" , "nb_pages" : ""},
#     "2. Relaxation et Équilibre dans les Systèmes Quantiques Intégrables : Une Approche par la Thermodynamique de Bethe":  {"page" : 29 , "pages" : "" , "nb_pages" : ""},
#     "3. Dynamique hors-équilibre et hydrodynamique généralisée":  {"page" : 45 , "pages" : "" , "nb_pages" : ""},
#     "4. Fluctuation de la distribution de rapidité dans des états d'équilibre":  {"page" : 57 , "pages" : "" , "nb_pages" : ""},
#     "5. Dispositif expérimental": {"page" : 77 , "pages" : "" , "nb_pages" : ""},
#     "6. Étude du protocole de bi-partition : Mesure de distribution de rapidités locales rho(x,θ) pour des systèmes hors équilibre":  {"page" : 99 , "pages" : "" , "nb_pages" : ""},
#     "7. Mise en place d'un confinement longitudinal dipolaire": {"page" : 115 , "pages" : "" , "nb_pages" : ""},
#     "Conclusion": {"page ": 137 , "pages" : "" , "nb_pages" : ""},
#     "Annex A - Action de P et H sur l'état de Bethe":  {"page" : 139 , "pages" : "" , "nb_pages" : ""},
#     "Annex B - Réduction GHD vers transport d’Euler": {"page" : 143 , "pages" : "" , "nb_pages" : ""},
#     "Annex C - Dérivation alternative des fluctuations de rho": {"page" : 145 , "pages" : "" , "nb_pages" : ""},
#     "Annex D - Propriétés des facteurs d'homothétie": {"page" : 151 , "pages" : "" , "nb_pages" : ""},
#     "Annex E - Polarisabilité dynamique et potentiel dipolaire optique": {"page" : 153 , "pages" : "" , "nb_pages" : ""},
#     "Annex F - Moment tensoriel J=1/2": {"page" : 157 , "pages" : "" , "nb_pages" : ""},
#     "Bibliographie": {"page" : 159 , "pages" : "" , "nb_pages" : ""},
#     "Résumé": {"page" : 165 , "pages" : "" , "nb_pages" : ""},
#     "Blanc": {"page" : 166 , "pages" : "" , "nb_pages" : ""},
# }

# # # =========================
# # # 📁 Répertoire de sortie
# # # =========================
# # output_dir = "pdf_decoupes"
# # os.makedirs(output_dir, exist_ok=True)

# # # =========================
# # # 🔍 Lecture du PDF
# # # =========================
# # reader = PdfReader(input_pdf)
# # nb_pages = len(reader.pages)

# # # =========================
# # # 🧮 Conversion auto des numéros en plages
# # # =========================
# # titles = list(parts.keys())
# # starts = list(parts.values())
# # ranges = {}

# # for i, title in enumerate(titles):
# #     start = starts[i]
# #     if i < len(starts) - 1:
# #         end = starts[i + 1] - 1  # la page juste avant la suivante
# #     else:
# #         end = nb_pages  # dernière section jusqu’à la fin
# #     ranges[title] = (start, end)

# # # =========================
# # # ✂️ Découpage automatique
# # # =========================
# # for name, (start, end) in ranges.items():
# #     writer = PdfWriter()
# #     for i in range(start - 1, end):  # PyPDF est 0-indexé
# #         writer.add_page(reader.pages[i])
    
# #     # Nom de fichier sécurisé
# #     safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in name)
    
# #     # Sauvegarde
# #     output_path = os.path.join(output_dir, f"{safe_name}.pdf")
# #     with open(output_path, "wb") as f:
# #         writer.write(f)
    
# #     print(f"✅ {name} -> pages {start}-{end} -> {output_path}")

# # print("\n🎉 Tous les PDF ont été créés avec succès !")


# # ========== Output folder ==========
# output_dir = "pdf_decoupes"
# os.makedirs(output_dir, exist_ok=True)

# # ========== Load PDF ==========
# reader = PdfReader(input_pdf)
# total_pages = len(reader.pages)

# # ========== Infer missing ranges ==========
# titles = list(parts.keys())

# for i, title in enumerate(titles):
#     entry = parts[title]

#     page = entry["page"]
#     pages = entry["pages"]
#     nb = entry["nb_pages"]

#     # --- Case 1 : pages="x-y" ---
#     if isinstance(pages, str) and re.match(r"\d+-\d+", pages):
#         start, end = map(int, pages.split("-"))
#         entry["page"] = start
#         entry["nb_pages"] = end - start + 1
#         continue

#     # --- Case 2 : pages empty but nb_pages known ---
#     if pages == "" and isinstance(nb, int) and nb > 0:
#         start = page
#         end = page + nb - 1
#         entry["pages"] = f"{start}-{end}"
#         continue

#     # --- Case 3 : pages empty and nb_pages empty ---
#     if pages == "" and nb == "":
#         start = page
#         if i < len(titles) - 1:
#             next_title = titles[i + 1]
#             next_page = parts[next_title]["page"]
#             end = next_page - 1
#         else:
#             end = total_pages  # last section

#         entry["pages"] = f"{start}-{end}"
#         entry["nb_pages"] = end - start + 1

# # ========== Extraction ==========
# for title, entry in parts.items():
#     start, end = map(int, entry["pages"].split("-"))

#     writer = PdfWriter()
#     for i in range(start - 1, end):  # zero-indexed
#         writer.add_page(reader.pages[i])

#     safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
#     output_path = os.path.join(output_dir, f"{safe_name}.pdf")

#     with open(output_path, "wb") as f:
#         writer.write(f)

#     print(f"✔ {title} → pages {start}-{end} → {output_path}")

# print("\n🎉 Tout est découpé automatiquement !")



# from pypdf import PdfReader, PdfWriter
# import os
# import json
# import re
# from tabulate import tabulate  # pip install tabulate

# # ============
# # 📄 PDF source
# # ============
# input_pdf = "main.pdf"

# # ============
# # 🧩 Sections
# # ============
# parts = {
#     "Titre": {"page": 1, "pages": "1-1", "nb_pages": 1},
#     "Blanc": {"page": 2, "pages": "2-2", "nb_pages": 1},
#     "Acronymes": {"page": 3, "pages": "3-4", "nb_pages": 2},
#     "Introduction": {"page": 7, "pages": "", "nb_pages": ""},
#     "Sommaire": {"page": 5, "pages": "", "nb_pages": ""},
#     "1. Modèle de Lieb-Liniger et approche Bethe Ansatz": {"page": 9, "pages": "", "nb_pages": ""},
#     "2. Relaxation et Équilibre dans les Systèmes Quantiques Intégrables : Une Approche par la Thermodynamique de Bethe": {"page": 29, "pages": "", "nb_pages": ""},
#     "3. Dynamique hors-équilibre et hydrodynamique généralisée": {"page": 45, "pages": "", "nb_pages": 14},
#     "4. Fluctuations de la distribution de rapidités dans les états stationnaires du modèle de Lieb–Liniger homogène": {"page": "", "pages": "", "nb_pages": 18},
#     "5. Dispositif expérimental": {"page": "", "pages": "", "nb_pages": 22},
#     "6. Étude du protocole de bi-partition : Mesure de distribution de rapidités locales rho(x,θ) pour des systèmes hors équilibre": {"page": "", "pages": "", "nb_pages": 16},
#     "7. Mise en place d'un confinement longitudinal dipolaire": {"page": "", "pages": "", "nb_pages": 22},
#     "Conclusion": {"page": "", "pages": "", "nb_pages": 2},
#     "Annex A - Action de P et H sur l'état de Bethe": {"page": "", "pages": "", "nb_pages": 4},
#     "Annex B - Réduction GHD vers transport d’Euler": {"page": "", "pages": "", "nb_pages": 4},
#     "Annex C - Dérivation alternative des fluctuations de rho": {"page": "", "pages": "", "nb_pages": 2},
#     "Annex D - Propriétés des facteurs d'homothétie": {"page": "", "pages": "", "nb_pages": 4},
#     "Annex E - Polarisabilité dynamique et potentiel dipolaire optique": {"page": "", "pages": "", "nb_pages": 4},
#     "Annex F - Moment tensoriel J=1/2": {"page": "", "pages": "", "nb_pages": 2},
#     "Bibliographie": {"page": "", "pages": "", "nb_pages": 6},
#     "Résumé": {"page": "", "pages": "", "nb_pages": 1},
#     "Blanc_final": {"page" : "" , "pages" : "" , "nb_pages" : 1},
# }

# # ========== Correction automatique des clés erronées ==========
# for title, entry in parts.items():
#     if "page " in entry:
#         entry["page"] = entry["page "]
#         del entry["page "]

# # ========== Output folder ==========
# output_dir = "pdf_decoupes"
# os.makedirs(output_dir, exist_ok=True)

# # ========== Load PDF ==========
# reader = PdfReader(input_pdf)
# total_pages = len(reader.pages)

# # ========== List for summary ==========
# summary_rows = []

# # ========== Infer missing ranges ==========
# titles = list(parts.keys())

# for i, title in enumerate(titles):
#     entry = parts[title]

#     page = entry["page"]
#     pages = entry["pages"]
#     nb = entry["nb_pages"]

#     # Validation : page must be int
#     if not isinstance(page, int) and not isinstance(pages, str) and not isinstance(nb, int) :
#         raise ValueError(f"Erreur : section « {title} » a un 'page' invalide : {page} , 'pages' invalide : {pages} , 'nb_pages' invalide : {nb} ")

#     # --- Case 1 : pages="x-y" ---
#     if isinstance(pages, str) and re.match(r"^\d+-\d+$", pages):
#         start, end = map(int, pages.split("-"))
#         entry["page"] = start
#         entry["nb_pages"] = end - start + 1

#     # --- Case 2 : pages empty but nb_pages known ---
#     elif pages == "" and isinstance(nb, int) and nb > 0:
#         if not isinstance(page, int) :
#             entry["page"] = parts[titles[i-1]]["page"] + parts[titles[i-1]]["nb_pages"] 
#             page = entry["page"]
#         start = page
#         end = page + nb - 1
#         entry["pages"] = f"{start}-{end}"

#     # --- Case 3 : both empty → infer from next section ---
#     elif pages == "" and nb == "":
#         start = page
#         if i < len(titles) - 1:
#             next_page = parts[titles[i + 1]]["page"]
#             end = next_page - 1
#         else:
#             end = total_pages

#         entry["pages"] = f"{start}-{end}"
#         entry["nb_pages"] = end - start + 1

#     else:
#         raise ValueError(f"Format inconnu dans la section : {title}")

# # ========== EXTRACTION ==========
# for title, entry in parts.items():
#     start, end = map(int, entry["pages"].split("-"))

#     # Validation : page range
#     if end < start:
#         raise ValueError(f"Erreur : plage invalide pour « {title} » : {start}-{end}")

#     if start < 1 or end > total_pages:
#         raise ValueError(f"Erreur : plage hors PDF pour « {title} » ({start}-{end})")

#     writer = PdfWriter()
#     for i in range(start - 1, end):
#         writer.add_page(reader.pages[i])

#     safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
#     output_path = os.path.join(output_dir, f"{safe_name}.pdf")

#     with open(output_path, "wb") as f:
#         writer.write(f)

#     print(f"✔ {title} → pages {start}-{end} → {output_path}")

#     summary_rows.append([title, start, end, entry["nb_pages"], output_path])

# # ========== TABLEAU RÉCAPITULATIF ==========
# print("\n====== RÉCAPITULATIF ==========\n")
# print(tabulate(summary_rows, headers=["Titre", "Début", "Fin", "Pages", "Fichier"], tablefmt="github"))

# # ========== EXPORT JSON ==========
# with open("sections.json", "w") as f:
#     json.dump(parts, f, indent=4, ensure_ascii=False)

# print("\n📁 JSON exporté → sections.json")
# print("🎉 Tout est découpé automatiquement et validé !")



from pypdf import PdfReader, PdfWriter
import os
import json
import re
from tabulate import tabulate  # pip install tabulate

# ============
# 📄 PDF source
# ============
input_pdf = "main.pdf"

# ============
# 🧩 Sections
# ============
parts = {
    "Titre_saclay": {"page": 1, "pages": "1-1", "nb_pages": 1},
    "Résumé_saclay": {"page": "", "pages": "", "nb_pages": 1},
    "Blanc_1": {"page": "", "pages": "", "nb_pages": 2},
    "Titre": {"page": "", "pages": "", "nb_pages": 1},
    "Blanc_2": {"page": "", "pages": "", "nb_pages": 1},
    "Acronymes": {"page": "", "pages": "", "nb_pages": 2},
    "Pourquoi 1D ?": {"page": "", "pages": "", "nb_pages": 4},
    "Introduction": {"page": "", "pages": "", "nb_pages": 4},
    "Sommaire": {"page": "", "pages": "", "nb_pages": 6},
    "1. Modèle de Lieb-Liniger et approche Bethe Ansatz": {"page": "", "pages": "", "nb_pages": 22},
    "2. Relaxation et Équilibre dans les Systèmes Quantiques Intégrables : Une Approche par la Thermodynamique de Bethe": {"page": "", "pages": "", "nb_pages": 18},
    "3. Dynamique hors-équilibre et hydrodynamique généralisée": {"page": "", "pages": "", "nb_pages": 18},
    "4. Fluctuations de la distribution de rapidités dans les états stationnaires du modèle de Lieb–Liniger homogène": {"page": "", "pages": "", "nb_pages": 24},
    "5. Dispositif expérimental": {"page": "", "pages": "", "nb_pages": 24},
    "6. Étude du protocole de bi-partition : Mesure de distribution de rapidités locales rho(x,θ) pour des systèmes hors équilibre": {"page": "", "pages": "", "nb_pages": 18},
    "7. Mise en place d'un confinement longitudinal dipolaire": {"page": "", "pages": "", "nb_pages": 24},
    "Conclusion": {"page": "", "pages": "", "nb_pages": 2},
    "Annex A - De la transformation de Fourier aux etats de Bethe ": {"page": "", "pages": "", "nb_pages": 44},
    "Annex B - Action de P et H sur l'état de Bethe": {"page": "", "pages": "", "nb_pages": 4},
    "Annex C - Réduction GHD vers transport d’Euler": {"page": "", "pages": "", "nb_pages": 4},
    "Annex D - Dérivation alternative des fluctuations de rho": {"page": "", "pages": "", "nb_pages": 4},
    "Annex E - Propriétés des facteurs d'homothétie": {"page": "", "pages": "", "nb_pages": 2},
    "Annex F - Polarisabilité dynamique et potentiel dipolaire optique": {"page": "", "pages": "", "nb_pages": 4},
    "Annex G - Moment tensoriel J=1/2": {"page": "", "pages": "", "nb_pages": 2},
    "Bibliographie": {"page": "", "pages": "", "nb_pages": 8},
    #"Résumé": {"page": "", "pages": "", "nb_pages": 1},
   #"Blanc_final": {"page" : "" , "pages" : "" , "nb_pages" : 1},
}

# ========= Correction automatique des clés erronées ==========
for title, entry in parts.items():
    if "page " in entry:
        entry["page"] = entry["page "]
        del entry["page "]

# ========= Output folder ==========
output_dir = "pdf_decoupes"
os.makedirs(output_dir, exist_ok=True)

# ========= Load PDF ==========
reader = PdfReader(input_pdf)
total_pages = len(reader.pages)

# ========= List for summary ==========
summary_rows = []

# ========= Infer missing ranges ==========
titles = list(parts.keys())

for i, title in enumerate(titles):
    entry = parts[title]
    page = entry["page"]
    pages = entry["pages"]
    nb = entry["nb_pages"]

    # Validation
    if not isinstance(page, int) and pages == "" and nb == "":
        raise ValueError(f"Section « {title} » a des informations de pages manquantes.")

    # --- Case 1 : pages="x-y" ---
    if isinstance(pages, str) and re.match(r"^\d+-\d+$", pages):
        start, end = map(int, pages.split("-"))
        entry["page"] = start
        entry["nb_pages"] = end - start + 1

    # --- Case 0b : pages="{1,3,10}" ---
    elif isinstance(pages, str) and re.match(r"^\{[\d,]+\}$", pages):
        page_list = [int(p) for p in pages.strip("{}").split(",")]
        entry["page"] = page_list[0]
        entry["nb_pages"] = len(page_list)
        entry["page_list"] = page_list

    # --- Case 2 : pages empty but nb_pages known ---
    elif pages == "" and isinstance(nb, int) and nb > 0:
        if not isinstance(page, int):
            entry["page"] = parts[titles[i-1]]["page"] + parts[titles[i-1]]["nb_pages"]
            page = entry["page"]
        start = page
        end = page + nb - 1
        entry["pages"] = f"{start}-{end}"

    # --- Case 3 : both empty → infer from next section ---
    elif pages == "" and nb == "":
        start = page
        if i < len(titles) - 1:
            next_page = parts[titles[i + 1]]["page"]
            if not isinstance(next_page, int):
                next_page = total_pages
            end = next_page - 1
        else:
            end = total_pages
        entry["pages"] = f"{start}-{end}"
        entry["nb_pages"] = end - start + 1

    else:
        pass  # autres cas déjà traités

# ========= EXTRACTION ==========
for title, entry in parts.items():
    writer = PdfWriter()
    
    if "page_list" in entry:
        # Extraction des pages individuelles
        for p in entry["page_list"]:
            if p < 1 or p > total_pages:
                raise ValueError(f"Page {p} hors PDF pour « {title} »")
            writer.add_page(reader.pages[p - 1])
        start, end = entry["page_list"][0], entry["page_list"][-1]
    else:
        start, end = map(int, entry["pages"].split("-"))
        if end < start:
            raise ValueError(f"Plage invalide pour « {title} » : {start}-{end}")
        for i in range(start - 1, end):
            writer.add_page(reader.pages[i])

    safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
    output_path = os.path.join(output_dir, f"{safe_name}.pdf")

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✔ {title} → pages {start}-{end} → {output_path}")
    summary_rows.append([title, start, end, entry["nb_pages"], output_path])

# ========= TABLEAU RÉCAPITULATIF ==========
print("\n====== RÉCAPITULATIF ==========\n")
print(tabulate(summary_rows, headers=["Titre", "Début", "Fin", "Pages", "Fichier"], tablefmt="github"))

# ========= EXPORT JSON ==========
with open("sections.json", "w") as f:
    json.dump(parts, f, indent=4, ensure_ascii=False)

print("\n📁 JSON exporté → sections.json")
print("🎉 Découpage terminé et validé !")

