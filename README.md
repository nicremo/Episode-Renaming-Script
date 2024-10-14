# Episode-Renaming-Script

### Overview of the Python Script
The script helps rename video files for a show, organizing them by season and episode. It scans folders, identifies season and episode numbers in the folder and file names, and renames the files using a standard format. The renaming pattern includes the show's name, season number, episode number, and optional extra text.

This Python script is designed to rename video files for TV shows, organizing them by season and episode. The script scans a directory for season folders and episode files, extracts season and episode numbers from folder and file names, and renames the files in a consistent format.

## Features

- Automatically identifies season and episode numbers from folder and file names.
- Ignores specified folders during the renaming process.
- Adds custom text (e.g., language tags) to renamed files.
- Handles common naming conventions such as "S01E01" or "Episode 1".

## Usage

1. **Clone the repository** and navigate to the project directory.
2. Modify the `mini_mtbb_path` and `trix_path` variables to match the directories containing your TV show files.
3. Run the script using Python:

    ```bash
    python rename_episodes.py
    ```

### Example

In this example, the script renames episodes of *Attack on Titan*:

```python
# Renames episodes in the "Mini MTBB" folder
rename_episodes("/path/to/MiniMTBB")

# Renames episodes in the "Trix" folder, ignoring "OVAs" and appending "English Dub" to filenames
rename_episodes("/path/to/Trix", ignore_folders=["OVAs"], extra_text=" English Dub")
```

## Functions

### `get_season_folders(path, ignore_folders=None)`
Retrieves a list of season folders from the specified path, excluding folders listed in `ignore_folders`.

### `extract_season_number(folder_name)`
Extracts the season number from a folder name. It searches for common patterns like `Season 1` or `S01`.

### `extract_episode_number(file_name)`
Extracts the episode number from a file name. Supports patterns like `E01`, `Episode 1`, or `S01E01`.

### `rename_episodes(root_path, ignore_folders=None, extra_text="")`
Renames all episode files in the specified folder, using the detected season and episode numbers. Optionally adds extra text to the file name.

## Notes

- This script is particularly useful for organizing video files downloaded with inconsistent naming conventions.
- Make sure to adjust the folder paths and any additional preferences before running the script.

## License

This project is licensed under the MIT License.
