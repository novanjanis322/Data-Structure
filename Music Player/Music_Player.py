import os

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, newdata):
        new_node = Node(newdata)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def playsong(self):
        if self.head is None:
            print("No song to play.")
        else:
            song = self.head
            play_song = song.data
            print(f'Playing song: {play_song}')

    def nextsong(self):
        if self.head is None:
            print("No next song to play.")
        else:
            if self.head.next is None:
                print('No next song to play.')
            else:
                song_next = self.head = self.head.next
                play_song_next = song_next.data        
                print(f'Playing next song: {play_song_next}')

    def prevsong(self):
        if self.head is None:
            print('No previous song to play.')
        else:
            if self.head.prev is None:
                print('Already at the first song, no previous song to play.')
            else:
                song_prev = self.head = self.head.prev
                play_song_prev = song_prev.data
                print(f'Playing previous song: {play_song_prev}')

    def display(self):
        if self.head is None:
            print('No songs (empty ._.).')
            return   
        else:
            n = self.head
            global song_number
            song_number = 1
            while n is not None:
                print(f'{song_number}. {n.data}')
                song_number += 1
                n = n.next

playlist = DoublyLinkedList()

# =====================================================================================================

def main_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~cloudtify music player~~~~~~~~~~~~~~~~~~~~~~~~")
    print('''
    1. Add songs
    2. Play song
    3. Skip to next song
    4. Go back to previous song
    5. View current playlist
    6. Close music player\n''')
    try:
        menu_choice = int(input('Choose a menu option: '))

        if menu_choice == 1:
            try:
                number_of_songs = int(input('Enter the number of songs: '))
                for i in range(1, number_of_songs + 1):
                    group, title = input(f'Enter song {i} (group, title): ').split(", ")
                    song_entry = (f'{title} by {group}\n')
                    playlist.append(song_entry)
                os.system('cls')
                print('Song input completed.')
                main_menu()
            except:
                os.system('cls')
                print('***Failed to input***')
                print('   Try again')
                main_menu()

        elif menu_choice == 2:
            os.system('cls')
            playlist.playsong()
            main_menu()

        elif menu_choice == 3:
            os.system('cls')
            playlist.nextsong()
            main_menu()

        elif menu_choice == 4:
            os.system('cls')
            playlist.prevsong()
            main_menu()

        elif menu_choice == 5:
            os.system('cls')
            print('Current playlist: \n')
            playlist.display()
            main_menu()

        elif menu_choice == 6:
            print('Music player closed. Don\'t forget to listen to music anytime, anywhere.')
            
        else:
            os.system('cls')
            print('Only numbers 1-6 are allowed. Try again.')
            main_menu()

    except:
        os.system('cls')
        print('Only integer numbers are allowed. Try again.')  
        main_menu()

main_menu()
