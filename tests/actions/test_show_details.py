import pytest
from pro_filer.actions.main_actions import show_details  # NOQA


@pytest.fixture(scope="function")
def directory(tmp_path):
    dir = tmp_path / "dir"
    dir.mkdir()
    path = dir / "test_file.txt"
    path.write_text("A, B, C, D, E, F, G")
    other_file = dir / "test_file"
    other_file.touch()
    return dir


@pytest.mark.parametrize(
    "file, expected",
    [
        (
            "test_file.txt",
            (
                "File name: test_file.txt\n"
                "File size in bytes: 19\n"
                "File type: file\n"
                "File extension: .txt\n"
                "Last modified date: 2024-01-22\n"
            ),
        ),
        (
            "test_file",
            (
                "File name: test_file\n"
                "File size in bytes: 0\n"
                "File type: file\n"
                "File extension: [no extension]\n"
                "Last modified date: 2024-01-22\n"
            ),
        ),
        (
            "1234.txt",
            "File '1234.txt' does not exist\n",
        ),
    ],
)
def test_show_details(file, directory, expected, capsys):
    show_details({"base_path": f"{directory}/{file}"})
    result = capsys.readouterr()
    assert result.out == expected