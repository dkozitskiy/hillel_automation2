import pytest


@pytest.mark.regression
def test_clickable_name_in_login_page(open_login_page, env):
    login_page = open_login_page
    python_page = login_page.login(env.login, env.password)
    assert python_page.is_clickable_name() is True


@pytest.mark.regression
def test_title_name(open_login_page, env):
    login_page = open_login_page
    python_page = login_page.login(env.login, env.password)
    assert python_page.is_title() is True


@pytest.mark.regression
def test_left_menu_in_login_page(open_login_page, env):
    login_page = open_login_page
    python_page = login_page.login(env.login, env.password)
    assert python_page.is_content_menu_visible() is True


@pytest.mark.regression
def test_article_title(open_login_page, env):
    login_page = open_login_page
    python_page = login_page.login(env.login, env.password)
    assert python_page.is_article_title('Python') is True


@pytest.mark.regression
def is_test_page_url(open_login_page, env):
    login_page = open_login_page
    python_page = login_page.login(env.login, env.password)
    assert python_page.is_check_url() is True
