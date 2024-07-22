import json
import os

# In-memory storage for songs
songs = {}
next_id = 1

# File to persist songs
songs_file = 'songs.json'

def load_songs():
    global songs, next_id
    if os.path.exists(songs_file):
        with open(songs_file, 'r') as file:
            data = json.load(file)
            songs = data['songs']
            next_id = data['next_id']

def save_songs():
    with open(songs_file, 'w') as file:
        data = {'songs': songs, 'next_id': next_id}
        json.dump(data, file)

load_songs()
def create_song():
    global next_id
    title = input("Enter the song title: ")
    lyrics = input("Enter the song lyrics: ")
    songs[next_id] = {"id": next_id, "title": title, "lyrics": lyrics}
    next_id += 1
    save_songs()
    print("Song created successfully!\n")

def edit_song():
    song_id = int(input("Enter the song ID to edit: "))
    if song_id in songs:
        title = input("Enter the new song title: ")
        lyrics = input("Enter the new song lyrics: ")
        songs[song_id] = {"id": song_id, "title": title, "lyrics": lyrics}
        save_songs()
        print("Song updated successfully!\n")
    else:
        print("Song ID not found.\n")

def view_song():
    song_id = int(input("Enter the song ID to view: "))
    if song_id in songs:
        song = songs[song_id]
        print(f"\nTitle: {song['title']}\nLyrics:\n{song['lyrics']}\n")
    else:
        print("Song ID not found.\n")

def list_songs():
    if songs:
        print("\nList of Songs:")
        for song in songs.values():
            print(f"ID: {song['id']}, Title: {song['title']}")
        print()
    else:
        print("No songs available.\n")
def delete_song():
    song_id = input("Enter the song ID to delete: ")
    if song_id in songs:
        del songs[song_id]
        save_songs()
        print("Song deleted successfully!\n")
    else:
        print("Song ID not found.\n")
def main_menu():
    while True:
        print("Songwriting App")
        print("1. Create a New Song")
        print("2. Edit an Existing Song")
        print("3. View a Song")
        print("4. List All Songs")
        print("5. Delete a Song")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_song()
        elif choice == '2':
            edit_song()
        elif choice == '3':
            view_song()
        elif choice == '4':
            list_songs()
        elif choice == '5':
            delete_song()
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main_menu()
