from pathlib import Path
import os, subprocess, venv
root = Path(__file__).resolve().parents[1]
env = root / ".venv"
venv.EnvBuilder(with_pip=True).create(env)
python = env / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
subprocess.run([str(python), "-m", "pip", "install", "-r",
                str(root / "requirements-test.txt")], check=True)
