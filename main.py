import os
import shutil
import getpass

s_folder = os.getcwd()
uname = getpass.getuser()

destination = f"C:/Users/{uname}/Zomboid/mods"

for folder in os.listdir(s_folder):
    s_path = os.path.join(s_folder, folder)
    d_path = os.path.join(destination, folder)

    if os.path.isdir(s_path):
        try:
            shutil.copytree(s_path, d_path)

        except FileExistsError:
            continue

print("Done!")
