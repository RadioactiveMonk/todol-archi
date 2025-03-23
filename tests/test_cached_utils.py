from backend.core.cached_utils import get_categories, get_stylesheet
from configuration.constants import DEFAULT_THEME
import pytest


def test_get_categories_returns_list():
    categories = get_categories()
    assert isinstance(categories, list)
    assert all(isinstance(cat, str) for cat in categories)


def test_get_stylesheet_returns_str():
    stylesheet = get_stylesheet(DEFAULT_THEME)
    assert isinstance(stylesheet, str)
    assert len(stylesheet) > 0


def test_get_stylesheet_same_theme_cached():
    s1 = get_stylesheet(DEFAULT_THEME)
    s2 = get_stylesheet(DEFAULT_THEME)
    assert s1 == s2  # 🧠 pas un vrai test de cache, mais on vérifie que c’est stable
