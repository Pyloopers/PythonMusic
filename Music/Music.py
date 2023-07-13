import os
import pygame

# Function to search for music files in a directory
def search_music(directory):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav'):
                music_files.append(os.path.join(root, file))
    return music_files

# Function to play music
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        # Allow seeking through the song
        command = input("Enter 'seek' to seek or 'stop' to stop the music: ")

        if command == "seek":
            seek_pos = input("Enter the position to seek to (in seconds): ")
            seek_pos = float(seek_pos)
            pygame.mixer.music.set_pos(seek_pos)

        if command == "stop":
            pygame.mixer.music.stop()
            break

# Directory to search for music files
music_directory = 'D:\Amit\python'

# Search for music files in the directory
music_files = search_music(music_directory)

# Play the selected music file
for i, file in enumerate(music_files):
    print(f"{i+1}. {file}")

selection = input("Enter the number of the song you want to play: ")
selection = int(selection) - 1

if 0 <= selection < len(music_files):
    chosen_file = music_files[selection]
    play_music(chosen_file)
else:
    print("Invalid selection.")
