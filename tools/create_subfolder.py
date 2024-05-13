from pathlib import Path


def create_directory(folder: str, user_folder="Documents") -> str:
    home = Path.home() / user_folder
    folder_path = home / folder

    # Использование метода `mkdir` с параметром `parents=True`,
    # чтобы создать все необходимые родительские папки автоматически.
    folder_path.mkdir(parents=True, exist_ok=True)

    return str(folder_path)

if __name__ == '__main__':
    print(create_directory('Kommersant/LentaRU'))
