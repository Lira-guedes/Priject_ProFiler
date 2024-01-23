from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
from tempfile import mkdtemp
import pytest
import os


# Contém arquivos duplicados
@pytest.fixture
def create_duplicate_files(tmp_path):
    temp_dir = mkdtemp(dir=tmp_path)
    file1 = os.path.join(temp_dir, "example_file1.txt")
    file2 = os.path.join(temp_dir, "example_file2.txt")
    file3 = os.path.join(temp_dir, "example_file3.txt")

    with open(file1, "w") as file:
        file.write("AAA")
    with open(file2, "w") as file:
        file.write("BBB")
    with open(file3, "w") as file:
        file.write("AAA")

    return [file1, file2, file3]


def test_find_duplicate_files(create_duplicate_files):
    result = find_duplicate_files({"all_files": create_duplicate_files})
    expected = [(create_duplicate_files[0], create_duplicate_files[2])]
    assert result == expected


# Não contém arquivos duplicados
@pytest.fixture
def create_temp_files(tmp_path):
    temp_dir = mkdtemp(dir=tmp_path)
    file1 = os.path.join(temp_dir, "example_file1.txt")
    file2 = os.path.join(temp_dir, "example_file2.txt")
    file3 = os.path.join(temp_dir, "example_file3.txt")

    with open(file1, "w") as file:
        file.write("AAA")
    with open(file2, "w") as file:
        file.write("BBB")
    with open(file3, "w") as file:
        file.write("CCC")

    return [file1, file2, file3]


def test_no_find_duplicate_files(create_temp_files):
    result = find_duplicate_files({"all_files": create_temp_files})
    assert result == []


# Não contém nada
def test_no_find_file(tmp_path):
    file1 = tmp_path / "example_file1.txt"
    file1.write_text("AAA")
    file2 = tmp_path / "example_file2.txt"
    file2.write_text("BBB")

    result = {"all_files": [str(file1), "example_file1.txt", str(file2),
              "example_file2.txt", "example_file3.txt"]}

    with pytest.raises(ValueError):
        find_duplicate_files(result)
