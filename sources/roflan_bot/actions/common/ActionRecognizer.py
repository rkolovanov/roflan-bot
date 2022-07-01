from roflan_bot.common.Storage import Storage


class ActionRecognizer:
    def __init__(self, actions_data: Storage):
        self.actions_data = actions_data

    def recognize_actions(self, text: str) -> list:
        recognized_actions = []
        split_text = text.split()

        for name, action in self.actions_data.items():
            for phrase in action["phrases"]:
                split_phrase = phrase.split()
                matching_word_count = 0

                for phrase_word in split_phrase:
                    if phrase_word in split_text:
                        matching_word_count += 1

                if matching_word_count == len(split_phrase):
                    recognized_actions.append(name)

        return recognized_actions
