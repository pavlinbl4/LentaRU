import os.path
from pathlib import Path
import shutil


def create_directory(folder: str, user_folder="Documents") -> str:
    home = f'{str(Path.home())}/{user_folder}'
    folder_path = os.path.join(home, folder)
    os.makedirs(folder_path, exist_ok=True)

    return folder_path


if __name__ == '__main__':
    assert create_directory("WWWWWWWW/dddd", user_folder='Music') == '/Users/evgeniy/Music/WWWWWWWW/dddd'
    shutil.rmtree('/Users/evgeniy/Music/WWWWWWWW/')

