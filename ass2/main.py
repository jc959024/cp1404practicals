"""
Name:Huayu Zhong
Date Started:20/1/2024
Brief Project Description: songlist
GitHub URL:
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from songcollection import SongCollection
from song import Song

class SongListApp(App):
    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')
        self.root = self.create_layout()
        self.update_song_list()
        return self.root

    def sort_songs(self, *args):
        sort_attribute = self.sort_by_spinner.text.lower()
        if sort_attribute == 'learned':
            sort_attribute = 'is_learned'
        self.song_collection.sort(sort_attribute)
        self.update_song_list()

    def create_layout(self):
        main_layout = BoxLayout(orientation='horizontal')
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.3)

        self.sort_by_spinner = Spinner(
            text='Sort by:',
            values=('Artist', 'Title', 'Year', 'Learned'),
            size_hint_y=None,
            height=50
        )
        self.sort_by_spinner.bind(text=self.sort_songs)
        left_layout.add_widget(self.sort_by_spinner)

        self.title_input = TextInput(multiline=False, hint_text='Title')
        self.artist_input = TextInput(multiline=False, hint_text='Artist')
        self.year_input = TextInput(multiline=False, hint_text='Year')
        left_layout.add_widget(self.title_input)
        left_layout.add_widget(self.artist_input)
        left_layout.add_widget(self.year_input)

        add_song_button = Button(text='Add Song', on_press=self.add_song)
        left_layout.add_widget(add_song_button)

        self.right_layout = GridLayout(cols=1, size_hint_x=0.7)
        self.status_label = Label(size_hint_y=None, height=50)
        self.right_layout.add_widget(self.status_label)

        main_layout.add_widget(left_layout)
        main_layout.add_widget(self.right_layout)

        return main_layout

    def on_stop(self):
        self.song_collection.save_songs('songs.json')

    def add_song(self, instance):
        if not all([self.title_input.text, self.artist_input.text, self.year_input.text]):
            self.status_label.text = "All fields must be completed"
            return
        try:
            year = int(self.year_input.text)
            if year <= 0:
                raise ValueError("Year must be > 0")
        except ValueError:
            self.status_label.text = "Please enter a valid number for year"
            return

        self.song_collection.add_song(Song(
            self.title_input.text,
            self.artist_input.text,
            year,
            False))
        self.title_input.text = ""
        self.artist_input.text = ""
        self.year_input.text = ""
        self.update_song_list()

    def clear_fields(self, instance):
        self.title_input.text = ''
        self.artist_input.text = ''
        self.year_input.text = ''
        self.status_label.text = ''

    def update_song_list(self):
        self.right_layout.clear_widgets()
        self.right_layout.add_widget(self.status_label)
        for song in self.song_collection.songs:
            button_color = (0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1)
            song_button = Button(text=str(song), background_color=button_color)
            self.right_layout.add_widget(song_button)

if __name__ == "__main__":
    SongListApp().run()




