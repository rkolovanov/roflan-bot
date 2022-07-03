from roflan_bot.actions.common.Action import Action
from roflan_bot.actions.DisableFeatureAction import DisableFeatureAction
from roflan_bot.actions.EnableFeatureAction import EnableFeatureAction
from roflan_bot.actions.FeatureListAction import FeatureListAction
from roflan_bot.actions.GoodbyeAction import GoodbyeAction
from roflan_bot.actions.GreetingAction import GreetingAction
from roflan_bot.actions.NoAnswerAction import NoAnswerAction
from roflan_bot.actions.QuietAction import QuietAction
from roflan_bot.actions.RemindAction import RemindAction
from roflan_bot.actions.ThankAction import ThankAction
from roflan_bot.actions.UpdateDataAction import UpdateDataAction
from roflan_bot.actions.WakeUpAction import WakeUpAction
from roflan_bot.actions.WhoIsAction import WhoIsAction
from roflan_bot.common.Storage import Storage
import logging
import typing


class ActionRegistry:
    _ACTION_CLASSES = {
        "wake_up": WakeUpAction,
        "greeting": GreetingAction,
        "thank": ThankAction,
        "quiet": QuietAction,
        "goodbye": GoodbyeAction,
        "no_answer": NoAnswerAction,
        "feature_list": FeatureListAction,
        "enable_feature": EnableFeatureAction,
        "disable_feature": DisableFeatureAction,
        "update_data": UpdateDataAction,
        "remind": RemindAction,
        "who_is": WhoIsAction
    }

    def __init__(self, actions_data: Storage):
        self._logger = logging.getLogger(__name__)
        self._actions = {}

        for action_name, action_data in actions_data.items():
            if action_name in self._ACTION_CLASSES.keys():
                action_class = self._ACTION_CLASSES[action_name]
                self._actions[action_name] = action_class(action_name,
                                                          action_data["description"],
                                                          action_data["access_level"])
            else:
                self._logger.warning(f"Неизвестное действие: '{action_name}'")

    def get(self, action_name: str) -> typing.Any:
        if action_name in self._actions.keys():
            return self._actions[action_name]

        self._logger.error(f"Неизвестное действие: '{action_name}'")
        return Action()

    def __getitem__(self, action_name: str) -> typing.Any:
        return self.get(action_name)
