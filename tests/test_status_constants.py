# tests/test_status_constants.py

from helpers.status_constants import status_color, status_label


def test_status_label():
    assert status_label(True) == "ROCKED"
    assert status_label(False) == "PENDING"


def test_status_color():
    assert status_color(True) == "green"
    assert status_color(False) == "orange"
