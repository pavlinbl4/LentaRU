import shutil
import unittest
from pathlib import Path

from tools.create_subfolder import create_directory


class TestCreateDirectory(unittest.TestCase):
    def test_create_directory(self):
        # �������� ����� � ����������� ���������� Documents
        folder_name = "test_folder"
        folder_path = create_directory(folder_name)
        self.assertTrue(Path(folder_path).exists())
        self.assertEqual(Path(folder_path).parent, Path.home() / "Documents")
        shutil.rmtree(folder_path)

        # �������� ����� � ���������������� ����������
        custom_user_folder = "CustomDocuments"
        folder_path = create_directory(folder_name, custom_user_folder)
        self.assertTrue(Path(folder_path).exists())
        self.assertEqual(Path(folder_path).parent, Path.home() / custom_user_folder)
        shutil.rmtree(Path(folder_path).parent)

    def test_create_directory_with_nonexistent_user_folder(self):
        # �������� ����� � ���������������� ����������, ������� �� ����������
        custom_user_folder = "NonexistentDocuments"
        folder_name = "test_folder"
        folder_path = create_directory(folder_name, custom_user_folder)
        self.assertTrue(Path(folder_path).exists())
        self.assertEqual(Path(folder_path).parent, Path.home() / custom_user_folder)
        shutil.rmtree(Path(folder_path).parent)

if __name__ == '__main__':
    unittest.main()
