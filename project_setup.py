import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQ_FILE = ROOT / "requirements.txt"

STANDARD_PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "jupyter",
    "notebook",
]

def create_day_folders(start=1, end=31):
    for day in range(start, end + 1):
        folder = ROOT / f"day{day:02d}"
        folder.mkdir(exist_ok=True)

def setup_virtualenv():
    if not VENV_DIR.exists():
        subprocess.run(["python", "-m", "venv", str(VENV_DIR)], check=True)

def write_requirements():
    if not REQ_FILE.exists():
        REQ_FILE.write_text("\n".join(STANDARD_PACKAGES) + "\n")

def install_requirements():
    pip = VENV_DIR / "Scripts" / "pip.exe"
    if pip.exists():
        subprocess.run([str(pip), "install", "--upgrade", "pip"], check=True)
        subprocess.run([str(pip), "install", "-r", str(REQ_FILE)], check=True)
    else:
        print("pip not found inside .venv")

def main():
    create_day_folders()
    setup_virtualenv()
    write_requirements()
    install_requirements()

if __name__ == "__main__":
    main()
