"""Contains classes and objects related to settings"""

class Setting:
    def __init__(self, name, val):
        self.val = val
        self.name = name


class Settings:
    """Contains all possible settings"""

    def __init__(self):
        self.settings = []
        self.keywords = ["autosave", "animations", "save_trainers", "load_mods"]

    def from_dict(self, src):
        for i in src:
            self.settings.append(Setting(i, src[i]))
        for i in self.keywords:
            if i not in [i.name for i in self.settings]:
                self.settings.append(Setting(i, True))

    def __call__(self, name):
        return [i for i in self.settings if i.name == name][0]

    def dict(self):
        """Returns a dict of all current settings"""
        return {i.name: i.val for i in self.settings}

settings = Settings()