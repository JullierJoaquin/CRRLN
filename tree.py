import os

def print_tree(startpath, prefix=""):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
        dirs[:] = [d for d in dirs if not d.startswith(".")]  # Ignora carpetas ocultas
        break  # Solo muestra el primer nivel

print_tree(".")
