#!/bin/zsh

# === Configuration ===
SRC="/Users/themezeguillaume/Desktop/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These-Memoire"
DEST="/Volumes/NO NAME/interface_web_launcher/sites/Scroll_Web/quantum-mechanics-thesis-main/These_Memoire"
LOGFILE="/Volumes/NO NAME/backup_these.log"

# Créer un dossier de destination horodaté pour garder les anciennes versions
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DEST_TIMESTAMPED="${DEST}_${TIMESTAMP}"

# === Sauvegarde ===
echo "=== Sauvegarde lancée $(date) ===" | tee -a "$LOGFILE"
echo "Source : $SRC" | tee -a "$LOGFILE"
echo "Destination : $DEST_TIMESTAMPED" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

# Lancer rsync avec barre de progression, vitesse et taille
# --info=progress2 affiche une seule barre globale
# --human-readable rend les tailles plus lisibles
# --stats affiche un résumé complet à la fin
rsync -ah --info=progress2 --stats "$SRC/" "$DEST_TIMESTAMPED/" | tee -a "$LOGFILE"

# === Résumé final ===
echo "" | tee -a "$LOGFILE"
echo "=== Sauvegarde terminée $(date) ===" | tee -a "$LOGFILE"
echo "---------------------------------------------" | tee -a "$LOGFILE"

