import pytest
from apts.secrets import mask_text
from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
import os

def test_mask_text_url_encoded():
    secret = "key with spaces"
    # length of "key with spaces" is 15 (> 8)
    text = "Error: https://api.example.com?key=key%20with%20spaces failed"

    masked = mask_text(text, secret)

    assert "key%20with%20spaces" not in masked
    assert "key ...aces" in masked

def test_mask_text_multiple_secrets():
    secrets = ["longer_secret1", "longer_secret2"]
    # lengths are 14 (> 8)
    text = "Found longer_secret1 and also longer_secret2"

    masked = mask_text(text, secrets)

    assert "longer_secret1" not in masked
    assert "longer_secret2" not in masked
    assert "long...ret1" in masked
    assert "long...ret2" in masked

def test_to_html_path_traversal_prevention():
    place = Place(52.2297, 21.0122, name="Warsaw")
    equipment = Equipment()
    obs = Observation(place, equipment)

    # Try to read a file with an invalid extension
    with pytest.raises(ValueError, match="Only .template, .html, or .htm files are allowed"):
        obs.to_html(custom_template="/etc/passwd")

    with pytest.raises(ValueError, match="Only .template, .html, or .htm files are allowed"):
        obs.to_html(custom_template="config.ini")
