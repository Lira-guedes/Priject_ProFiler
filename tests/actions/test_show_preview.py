import pytest
from pro_filer.actions.main_actions import show_preview


@pytest.mark.parametrize(
    "context, expected",
    [
        ({'all_files': [], 'all_dirs': []},
         "Found 0 files and 0 directories\n"),
        ({'all_files':
          ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt'],
          'all_dirs': []},
         "Found 6 files and 0 directories\n"
         "First 5 files: ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']\n"
         "First 5 directories: []\n"),
        ({'all_files': [], 'all_dirs': ['ddd', 'eee', 'fff']},
         "Found 0 files and 3 directories\n"
         "First 5 files: []\n"
         "First 5 directories: ['ddd', 'eee', 'fff']\n"),
        ({'all_files': ['a.txt', 'b.txt', 'c.txt'],
          'all_dirs': ['ddd', 'eee', 'fff']},
         "Found 3 files and 3 directories\n"
         "First 5 files: ['a.txt', 'b.txt', 'c.txt']\n"
         "First 5 directories: ['ddd', 'eee', 'fff']\n"),
    ],
)
def test_show_preview(context, expected, capsys):
    show_preview(context)
    result = capsys.readouterr()
    assert result.out == expected
