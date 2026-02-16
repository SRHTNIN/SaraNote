import os, json

DEFAULT_CONFIG = {
    "Editor": None,
    "ClearScreen": True,
    "CaseSensitiveSearch": False,
    "ListSeparator": ", ",
    "TagPrefix": "",
    "CategoriesFolder": "Categories"
}

def LoadConfig():
    BaseDir = os.path.dirname(os.path.abspath(__file__))
    ConfigPath = os.path.join(BaseDir, "Config.json")

    if not os.path.isfile(ConfigPath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(ConfigPath, "r", encoding="utf-8") as F:
            UserConfig = json.load(F)
    except:
        return DEFAULT_CONFIG.copy()

    Config = DEFAULT_CONFIG.copy()
    Config.update(UserConfig)

    return Config