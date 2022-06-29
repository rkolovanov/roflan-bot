from roflan_bot.actions.Action import Action
from roflan_bot.actions.ActionType import ActionType
from roflan_bot.common.InterClassStorage import InterClassStorage


class ActionRecognizer:
    @staticmethod
    def recognize(message: str):
        recognized_actions = []
        actions = InterClassStorage.get("actions")
        split_message = message.split()

        for name, action in actions.items():
            for phrase in action["phrases"]:
                split_phrase = phrase.split()
                matching_word_count = 0

                for phrase_word in split_phrase:
                    if phrase_word in split_message:
                        matching_word_count += 1

                if matching_word_count == len(split_phrase):
                    action_type = ActionType(action["uid"], name, action["description"], action["access_level"])
                    recognized_actions.append(Action(action_type, message))

        return recognized_actions
