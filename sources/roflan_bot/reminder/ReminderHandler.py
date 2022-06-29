from datetime import datetime
from roflan_bot.reminder.Reminder import Reminder


class ReminderHandler:
    def __init__(self):
        self._reminders = []

    def add(self, reminder: Reminder):
        self._reminders.append(reminder)

    def remove(self, reminder: Reminder):
        self._reminders.remove(reminder)

    def remove_and_get_expired_reminders(self):
        timestamp = datetime.now()
        expired_reminders = []

        for reminder in self._reminders:
            if timestamp > reminder.timestamp:
                expired_reminders.append(reminder)
                self.remove(reminder)

        return expired_reminders
