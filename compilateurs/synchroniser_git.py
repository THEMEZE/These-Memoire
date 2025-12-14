import os
import subprocess
from datetime import datetime
from pathlib import Path

MAX_SIZE_MB = 100
MAX_SIZE = MAX_SIZE_MB * 1024 * 1024

repo = Path("./").resolve()


def get_tracked_files():
    """Retourne la liste des fichiers suivis par git"""
    result = subprocess.run(
        ["git", "ls-files"],
        capture_output=True,
        text=True,
        check=True
    )
    return [Path(f) for f in result.stdout.splitlines()]


def remove_large_files(files):
    """Supprime de l’index les fichiers trop gros"""
    large_files = []

    for f in files:
        if f.exists() and f.stat().st_size > MAX_SIZE:
            large_files.append(f)

    if not large_files:
        return False

    print("🛑 Fichiers trop volumineux détectés (>100 MB) :")
    for f in large_files:
        size_mb = f.stat().st_size / 1024 / 1024
        print(f"   - {f} ({size_mb:.1f} MB)")

        # Retirer du suivi git
        subprocess.run(["git", "rm", "--cached", str(f)], check=False)

        # Ajouter au .gitignore
        with open(".gitignore", "a+") as gi:
            gi.seek(0)
            if str(f) not in gi.read():
                gi.write(f"\n{f}\n")

    print("⚠️ Ces fichiers ont été exclus du dépôt.")
    return True

def get_default_remote():
    result = subprocess.run(
        ["git", "remote"],
        capture_output=True,
        text=True,
        check=True
    )
    remotes = result.stdout.splitlines()
    if not remotes:
        raise RuntimeError("Aucun remote configuré.")
    return remotes[0]



def git_sync(repo_path):
    try:
        os.chdir(repo_path)

        # Vérifier le remote
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True, check=True)
        remote = get_default_remote()
        print(f"🔄 Pushing to remote '{remote}'...")
        if remote not in remotes.stdout:
            raise RuntimeError(f"Aucun remote '{remote}' trouvé dans '{remotes}' .")

        # Vérifier fichiers trop lourds AVANT add
        tracked_files = get_tracked_files()
        if remove_large_files(tracked_files):
            print("❌ Push annulé. Recommence après vérification.")
            return

        # Ajouter uniquement les fichiers déjà suivis
        subprocess.run(["git", "add", "-u"], check=True)

        # Vérifier s’il y a quelque chose à committer
        diff_cached = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if diff_cached.returncode == 0:
            print("🟢 Aucun changement git.")
            return

        # Commit
        commit_message = f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push

        subprocess.run(["git", "push", remote, "main"], check=True)
        print("✅ Git push réussi")

    except Exception as e:
        print(f"🛑 Erreur Git : {e}")


print(f"\n🔄 Début synchronisation à {datetime.now().strftime('%H:%M:%S')}")
print(f"🚀 Dépôt : {repo}")
git_sync(repo)
