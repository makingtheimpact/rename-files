# rename-files
Python script that renames files within a directory.

## Description
This script is designed to rename optimized png files, to trim unnecessary characters from the file name after being optimized. 

### Features:
* Works with png files
* Loops to make it easy to run for each subdirectory

#### Planned Changes and Features:
* Support any file type
* Provide templates for common file name conventions for automatic renaming
* Option to rename files in all subdirectories

### How It Works: 
1. Download a copy of the script to your computer.
2. Open a command prompt or terminal with admin privileges and navigate to where the script file is located using `cd` to change directories. 
3. Run the command: `python rename-files.py` to start the script. 
4. When prompted, enter the root directory that contains the subdirectories that contain the files.
5. When prompted, name of the subdirectory containing the files you want renamed.
6. Once the renaming is complete, you can enter `y` to put in the name of another subdirectory, or enter `n` to end the program.

## Changelog

### 1.0.0
- Initial release of the plugin.

## Upgrade Notice

### 1.0.0
- First release of the script, no upgrade notices.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This plugin is open-sourced software licensed under the [GPLv2](https://www.gnu.org/licenses/gpl-2.0.html) license.