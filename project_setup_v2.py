import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
ACTIVATE_PATH = VENV_DIR / "Scripts" / "activate"
PIP_PATH = VENV_DIR / "Scripts" / "pip.exe"
REQ_FILE = ROOT / "requirements.txt"
NUM_DAYS = 31

STANDARD_PACKAGES = [
    "numpy", "pandas", "matplotlib", "seaborn",
    "scikit-learn", "jupyter", "notebook",
]

def setup_virtualenv():
    if not VENV_DIR.exists():
        subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    if not ACTIVATE_PATH.exists():
        print("❌ Could not find .venv/Scripts/activate — aborting.")
        sys.exit(1)

def create_day_folders():
    for day in range(1, NUM_DAYS + 1):
        (ROOT / f"day{day:02d}").mkdir(exist_ok=True)

def write_requirements():
    REQ_FILE.write_text("\n".join(STANDARD_PACKAGES) + "\n")

def install_packages():
    if not PIP_PATH.exists():
        print("❌ pip.exe not found in .venv — aborting.")
        sys.exit(1)
    subprocess.run([str(PIP_PATH), "install", "--upgrade", "pip"], check=True)
    subprocess.run([str(PIP_PATH), "install", "-r", str(REQ_FILE)], check=True)

def main():
    print("🔧 Setting up .venv...")
    setup_virtualenv()

    print("📁 Creating folders day01 to day31...")
    create_day_folders()

    print("📝 Writing requirements.txt...")
    write_requirements()

    print("📦 Installing packages...")
    install_packages()

    print("\n✅ All done!")
    print("👉 To activate: .venv\\Scripts\\activate")

if __name__ == "__main__":
    main()
