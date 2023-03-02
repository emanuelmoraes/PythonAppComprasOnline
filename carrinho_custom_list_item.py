from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout

class CustomCarrinhoListItem(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")
    internal_key = ""

class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True