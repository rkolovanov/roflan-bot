from roflan_bot.actions.ActionType import ActionType


class Action:
    def __init__(self, action_type: ActionType, message: str = ""):
        self.action_type = action_type
        self.message = message
