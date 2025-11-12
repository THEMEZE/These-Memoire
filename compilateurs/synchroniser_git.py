import os
import time
import subprocess
import zipfile
from datetime import datetime
from pathlib import Path

repo = os.path.expanduser("./")

def git_sync(repo_path):
    try:
        os.chdir(repo_path)

        # Vérifier que le dépôt a bien un remote
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True, check=True)
        if "origin" not in remotes.stdout:
            raise RuntimeError("Aucun remote 'origin' trouvé.")

        # Ajouter les fichiers modifiés uniquement (sans les non suivis)
        subprocess.run(["git", "add", "-u"], check=True)

        # Vérifier s’il y a des changements dans l’index (staging)
        diff_cached = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if diff_cached.returncode == 0:
            print("🟢 Aucun changement git.")
            return

        # Commit + Push
        commit_message = f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"✅ Git push : {repo_path}")

    except Exception as e:
        msg = f"Erreur Git : {repo_path} → {e}"
        print(f"🛑 {msg}")
        
print(f"\n🔄 Début synchronisation à {datetime.now().strftime('%H:%M:%S')}")
#print(f"🚀 Traitement : {repo.name}")
print(f"🚀 Traitement : {repo}")
git_sync(repo)
