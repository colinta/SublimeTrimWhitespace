import sublime
import sublime_plugin


class TrimWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        value = kwargs.get("value")
        if value is not None:
            s = sublime.load_settings("Preferences.sublime-settings")
            s.set("trim_trailing_white_space_on_save", value)
            sublime.save_settings("Preferences.sublime-settings")
