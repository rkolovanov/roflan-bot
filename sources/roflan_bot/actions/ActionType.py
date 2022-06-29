class ActionType:
    NONE = 0

    def __init__(self, uid: int = NONE, name: str = "None", description: str = "", access_level: int = 0):
        self.uid = uid
        self.name = name
        self.description = description
        self.access_level = access_level
