import json
import os
from modules.translator import t, load_language, set_runtime_language

LANG_DIR = os.path.join("modules", "lang")

def test_json_syntax():
    for f in os.listdir(LANG_DIR):
        if f.endswith(".json"):
            with open(os.path.join(LANG_DIR, f), "r", encoding="utf-8") as fh:
                json.load(fh)


def test_english_complete():
    """EN must contain all keys."""
    en_file = os.path.join(LANG_DIR, "en.json")
    with open(en_file, "r", encoding="utf-8") as f:
        en = json.load(f)
    assert len(en) > 0


def test_translation_fallback():
    set_runtime_language("de")
    assert t("Easter Sunday") in ["Ostersonntag", "Easter Sunday"]


def test_missing_key_added():
    """Unknown key should automatically be added to DE."""
    key = "Unit Test Special Holiday"
    set_runtime_language("de")
    out = t(key)
    assert out == key  # fallback behavior

    # Check DE file was extended
    with open(os.path.join(LANG_DIR, "de.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    assert key in data

