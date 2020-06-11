import os
import json


def get_venvs() -> list:
	user_path = f"C:/Users/{os.getlogin()}/.virtualenvs/"
	directories = [directory for directory in os.listdir(user_path) if os.path.isdir(f"{user_path}/{directory}/")]
	return directories


def get_sublime_text_config():
	anaconda_settings_user = f"C:/Users/{os.getlogin()}/AppData/Roaming/Sublime Text 3/Packages/User/Anaconda.sublime-settings"

	with open(anaconda_settings_user) as jsonFile:
		return json.load(jsonFile)


def set_sublime_text_venv(venv):
	content_file = get_sublime_text_config()
	new_venv = f"C:/Users/{os.getlogin()}/.virtualenvs/{venv}/Scripts/python.exe"
	content_file['python_interpreter'] = new_venv
	anaconda_settings_user = f"C:/Users/{os.getlogin()}/AppData/Roaming/Sublime Text 3/Packages/User/Anaconda.sublime-settings"
	with open(anaconda_settings_user, "w") as f:
		f.write(json.dumps(content_file))


def get_sublime_text_venv():
	content_file = get_sublime_text_config()
	return content_file['python_interpreter']



if __name__ == '__main__':
	pass