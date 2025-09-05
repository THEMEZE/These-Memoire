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

