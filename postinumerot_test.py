# Kirjoita postinumerot-moduulin testit tähän tiedostoon
# from postinumerot import get_postalcode_by_post_name
from postinumerot import get_postalcode_by_post_name


def test_finding_kainasto():
    assert get_postalcode_by_post_name("KAINASTO") == "61820"

def test_finding_nothing():
    assert get_postalcode_by_post_name("KIATO") == ""

def test_finding_teuva():
    assert get_postalcode_by_post_name("teuva") == "64700, 64701"
