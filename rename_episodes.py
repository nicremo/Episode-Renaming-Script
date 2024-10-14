import os
import re

def get_season_folders(path, ignore_folders=None):
    if ignore_folders is None:
        ignore_folders = []
    # List all subdirectories in the given path
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # Ignore specific folders if provided
    folders = [f for f in folders if f not in ignore_folders]
    return folders

def extract_season_number(folder_name):
    # Try to extract the season number from the folder name
    match = re.search(r'(S(eason)?\s?|Staffel\s?)(\d+)', folder_name, re.IGNORECASE)
    if match:
        return int(match.group(3))
    else:
        # Try to extract the first number found in the folder name
        match = re.search(r'(\d+)', folder_name)
        if match:
            return int(match.group(1))
        else:
            print(f"Could not extract season number from '{folder_name}'.")
        return None

def extract_episode_number(file_name):
    # Try to extract the episode number from the file name
    match = re.search(r'(E(pisode)?\s?| - )(\d+)', file_name, re.IGNORECASE)
    if match:
        return int(match.group(3))
    else:
        # Look for patterns like S01E01
        match = re.search(r'S\d+E(\d+)', file_name, re.IGNORECASE)
        if match:
            return int(match.group(1))
        else:
            print(f"Could not extract episode number from '{file_name}'.")
        return None

def rename_episodes(root_path, ignore_folders=None, extra_text=""):
    season_folders = get_season_folders(root_path, ignore_folders)
    for season_folder in season_folders:
        season_number = extract_season_number(season_folder)
        if season_number is None:
            continue
        season_path = os.path.join(root_path, season_folder)
        episode_files = [f for f in os.listdir(season_path) if os.path.isfile(os.path.join(season_path, f))]
        for episode_file in episode_files:
            episode_number = extract_episode_number(episode_file)
            if episode_number is None:
                continue
            old_file_path = os.path.join(season_path, episode_file)
            file_extension = os.path.splitext(episode_file)[1]
            new_file_name = f"Attack on Titan S{season_number:02d} E{episode_number:02d}{extra_text}{file_extension}"
            new_file_path = os.path.join(season_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{episode_file}' -> '{new_file_name}'")

if __name__ == "__main__":
    # Paths to the folders
    mini_mtbb_path = "/Users/---/Downloads/[EXAMPLE]MiniMTBB"
    trix_path = "/Users/---/Downloads/[EXAMPLE]Shingeki no Kyojin - AV1"
    # Rename the files in the "Mini MTBB" folder
    rename_episodes(mini_mtbb_path)
    # Rename the files in the "Trix" folder, ignoring "OVAs" and adding "English Dub"
    rename_episodes(trix_path, ignore_folders=["OVAs"], extra_text=" English Dub")
