import pytest


@pytest.mark.regression
def test_title_name(open_home_page):
    assert open_home_page.is_title() is True


@pytest.mark.regression
def test_search_in_page(open_home_page):
    assert open_home_page.is_search_visible() is True


@pytest.mark.regression
def test_login_button(open_home_page):
    assert open_home_page.is_login_button_clickable() is True


@pytest.mark.regression
def test_not_logged_in_title(open_home_page):
    assert open_home_page.is_visible_not_logged_in() is True


@pytest.mark.regression
def test_topics_in_page(open_home_page):
    assert open_home_page.is_visible_topics() is True
