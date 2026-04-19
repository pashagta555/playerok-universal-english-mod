The text is already in English. It appears to be a Python code snippet that defines several classes and functions related to configuration files and settings management.

Here's the breakdown:

1. The `SettingsFile` class is defined using the `@dataclass` decorator from the `dataclasses` module. This class represents a settings file with attributes such as `name`, `path`, `need_restore`, and `default`.
2. Three instances of the `SettingsFile` class are created: `CONFIG`, `MESSAGES`, and `CUSTOM_COMMANDS`. Each instance has its own set of default values.
3. The `DATA` list is created to store all the settings files.
4. Two functions are defined:
	* `validate_config(config, default)`: checks if a given configuration dictionary matches the expected structure (i.e., it conforms to the standard template).
	* `restore_config(config, default)`: restores missing parameters in a configuration dictionary by filling them with values from the standard template.
5. The `get_json(path, default, need_restore=True)` function is defined to read and write JSON files:
	+ It creates the file if it doesn't exist
	+ Updates the file if new data is provided
	+ Restores the file to its original state if needed (i.e., if `need_restore` is True)
6. The `set_json(path, new)` function is defined to update a JSON file:
	+ It writes the new data to a temporary file
	+ Atomically replaces the existing file with the new one

The `Settings` class has two static methods:

1. `get(name, data=DATA)`: retrieves the settings for a given name from the specified list of settings files.
2. `set(name, new, data=DATA)`: updates the settings for a given name in the specified list of settings files.

Note that this code does not contain any specific business logic or functionality related to the bot or its features. It appears to be a generic framework for managing configuration files and settings.

