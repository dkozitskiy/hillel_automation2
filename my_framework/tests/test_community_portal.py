import pytest


@pytest.mark.regression
def test_title_name(open_community_portal):
    assert open_community_portal.is_title() is True


@pytest.mark.regression
def test_menu_container_in_page(open_community_portal):
    assert open_community_portal.is_visible_menu_container() is True


@pytest.mark.regression
def test_lock_in_page(open_community_portal):
    assert open_community_portal.is_lock_visible() is True


@pytest.mark.regression
def test_how_to_help_in_page(open_community_portal):
    assert open_community_portal.is_how_to_help_visible() is True


# @pytest.mark.regression
# def test_assist_and_social_lifein_page(open_community_portal):
#     assert open_community_portal.is_assist_and_social_life_visible() is True


@pytest.mark.regression
def test_page_url(open_community_portal, env):
    assert open_community_portal.is_check_url(env.community_portal_url) is True
