#the card flip Game
#code base from AugustDanell in learning kivy
from turtle import Screen
from docutils.nodes import image
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import random
import time

from pygments.styles.dracula import background

''' card
    The class card is a memory card class. It has a non-unique id called 'type' and a link as an attribute. The attribute type pertains to the link, so a card with the type 1 will
    have the same link as another card with type 1, both of them will have link to a picture of a duck. By comparing the types we can, as such, discern if we have a match between
    two cards or not.  
'''


#making the full deck of cards

full_deck = {
    1: "memory_asset/2_of_hearts.png", 2: "memory_asset/2_of_spades.png",
    3: "memory_asset/2_of_diamonds.png", 4: "memory_asset/2_of_clubs.png",
    5: "memory_asset/3_of_hearts.png", 6: "memory_asset/3_of_spades.png",
    7: "memory_asset/3_of_diamonds.png", 8: "memory_asset/3_of_clubs.png",
    9: "memory_asset/4_of_hearts.png", 10: "memory_asset/4_of_spades.png",
    11: "memory_asset/4_of_diamonds.png", 12: "memory_asset/4_of_clubs.png",
    13: "memory_asset/5_of_hearts.png", 14: "memory_asset/5_of_spades.png",
    15: "memory_asset/5_of_diamonds.png", 16: "memory_asset/5_of_clubs.png",
    17: "memory_asset/6_of_hearts.png", 18: "memory_asset/6_of_spades.png",
    19: "memory_asset/6_of_diamonds.png", 20: "memory_asset/6_of_clubs.png",
    21: "memory_asset/7_of_hearts.png", 22: "memory_asset/7_of_spades.png",
    23: "memory_asset/7_of_diamonds.png", 24: "memory_asset/7_of_clubs.png",
    25: "memory_asset/8_of_hearts.png", 26: "memory_asset/8_of_spades.png",
    27: "memory_asset/8_of_diamonds.png", 28: "memory_asset/8_of_clubs.png",
    29: "memory_asset/9_of_hearts.png", 30: "memory_asset/9_of_spades.png",
    31: "memory_asset/9_of_diamonds.png", 32: "memory_asset/9_of_clubs.png",
    33: "memory_asset/10_of_hearts.png", 34: "memory_asset/10_of_spades.png",
    35: "memory_asset/10_of_diamonds.png", 36: "memory_asset/10_of_clubs.png",
    37: "memory_asset/jack_of_hearts.png", 38: "memory_asset/jack_of_spades.png",
    39: "memory_asset/jack_of_diamonds.png", 40: "memory_asset/jack_of_clubs.png",
    41: "memory_asset/queen_of_hearts.png", 42: "memory_asset/queen_of_spades.png",
    43: "memory_asset/queen_of_diamonds.png", 44: "memory_asset/queen_of_clubs.png",
    45: "memory_asset/king_of_hearts.png", 46: "memory_asset/king_of_spades.png",
    47: "memory_asset/king_of_diamonds.png", 48: "memory_asset/king_of_clubs.png",
    49: "memory_asset/ace_of_hearts.png", 50: "memory_asset/ace_of_spades.png",
    51: "memory_asset/ace_of_diamonds.png", 52: "memory_asset/ace_of_clubs.png",
    53: "memory_asset/front_card.png"
}

#The Memory Card Class
class card:
    def __init__(self, type):
        self.type = type
        self.link = full_deck.get(type, None)


    #seeing if the cards are equal
    def _eq_(self, other):
        return self.type == other.type

class Memory(App):
    def fisher_yates(self):
        ''' fisher_yates
            The fisher-yates algorithm is a shuffling algorithm to achieve pseudo randomness. We use it to shuffle the memory cards when initiating the game.
        '''

        for i in range(len(self.card_list) - 1, 0, -1):
            rand = random.randint(0, i)
            self.card_list[i], self.card_list[rand] = self.card_list[rand], self.card_list[i]

    #un flip a card
    def un_flip(self, id):
        index = id - 1

        # Unflipping the card:
        self.display_list[index].clear_widgets()
        self.add_button(str(id))

    #flip a card
    def flip_card(self, id):
        # Setting the index and checking if it is a won card already, and if so, we should do nothing:
        index = id - 1
        if (index in self.winning_indices):
            return 0

        # Incrementing the turn counter:
        self.turn_counter += 1

        # Count flips, set as flipped and potentially alternate turn:
        if (self.turn_counter == 3):
            self.turn_counter = 0
            first_card, second_card = self.flipped_cards

            # See if we got two of the same:
            is_pair = False
            print(first_card, second_card)
            if (self.card_list[first_card] == self.card_list[second_card]):
                print("Ok, they are the same")
                is_pair = True
                self.winning_indices.append(first_card)
                self.winning_indices.append(second_card)

            if (not is_pair):
                print("Unflipping")
                self.un_flip(first_card + 1)
                self.un_flip(second_card + 1)
                self.player_turn = (self.player_turn % 2) + 1
                self.flipped_cards = [0, 0]

            return 0

        # Flipping the card:
        self.display_list[index].clear_widgets()
        memory_photo = Image(source=self.card_list[index].link)

        #adding a black border to every card
        with memory_photo.canvas.before:
            Color (0,0,0)
            self.rect = Rectangle (size = memory_photo.size, pos = memory_photo.pos)

        self.display_list[index].add_widget(memory_photo)
        self.flipped_cards[self.turn_counter - 1] = id - 1

    def add_button(self, id):
        ''' add_button
            A helper function to add and bind a button.
        '''

        b = Button(
            border=(10, 10, 10, 10),
            text=id,
            size_hint= (1, 0.5),
            bold=True,
            background_normal = "memory_asset/front_card.png"

        )

        self.display_list[int(id) - 1].add_widget(b)
        b.bind(on_press=lambda x: self.flip_card(int(b.text)))
        self.button_list.append(b)

    def fill_buttons(self):
        ''' fill_buttons
            A helper function that fills the board with buttons ranging from 1 .. to n, where n is the amount of cards the players want to have.
        '''

        for id in range(1, (self.amount_of_cards * 2) + 1):
            self.add_button(str(id))

    def fill_sub_layouts(self):
        ''' fill_sub_layouts
            Fills the sub layouts, that would be, layouts to be used like cards. To achieve the flipping affect we use inner layouts as cards and upon flipping we clear the widget
            and then paint the image on that layout (or the button if unflipping).
        '''

        for layout in self.display_list:
            self.window.add_widget(layout)


#display a random num of cards

    def build(self):
        #null for background
        Window.clearcolor = (227/255, 188/255,152/255 ,1)
        self.amount_of_cards = random.randint(4,7)
        self.flipped_cards = [0, 0]  # Holds the index of the two flipped cards.
        self.winning_indices = []
        self.turn_counter = 0
        self.player_turn = 1

        #creates a display layout for each cards
        self.display_list = [GridLayout(cols=1) for i in range(self.amount_of_cards * 2)]

        #the randomly selected cards
        selected_cards = random.sample(list(full_deck.keys()), self.amount_of_cards)
        self.card_list = [card(i) for i in selected_cards]*2

        # Shuffling the cards around
        self.fisher_yates()

        # Fixing a grid:
        self.window = GridLayout(cols = self.amount_of_cards)
        self.button_list = []

        # Generating subgrids in the window layout:
        self.fill_sub_layouts()

        # Adding buttons:
        self.fill_buttons()

        return self.window

if __name__ == "__main__":
    Memory().run()

