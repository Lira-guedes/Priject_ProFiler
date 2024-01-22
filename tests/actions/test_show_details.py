import pytest
from pro_filer.actions.main_actions import show_details  # NOQA


@pytest.mark.parametrize(
    "context, expected",
    [
      
    ],
)
def test_show_details(context, expected, capsys):
    show_details(context)
    captured_output, _ = capsys.readouterr()
    assert captured_output.strip() == expected
