import re, subprocess, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
version = sys.argv[1]
if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]{0,80}", version):
    raise ValueError("Version no valida")
image = "calculadora:" + version
name = "calculadora-" + version[:20]
def run(*args):
    subprocess.run(args, cwd=root, check=True)
run("docker", "build", "-t", image, ".")
run("docker", "run", "-d", "--name", name,
    "-p", "127.0.0.1:8080:8080", image)
try:
    run(sys.executable, "scripts/smoke_release.py", "http://127.0.0.1:8080")
except Exception:
    run("docker", "logs", name)
    run("docker", "stop", name)
    raise
print("Despliegue verificado:", name, image)
