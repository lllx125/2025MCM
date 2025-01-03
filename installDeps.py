import subprocess
import sys


def install_requirements():
    """
    Installs Python packages as listed in `requirements.txt`
    by running the shell command: pip install -r requirements.txt
    """
    try:
        # We use the same Python executable to ensure consistency.
        # This is especially helpful if you're using a virtual environment.
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install requirements.")
        print("Error:", e)


if __name__ == "__main__":
    install_requirements()
