import re
import os
cwd = os.getcwd()  # Get the current working directory (cwd)

with open(r"C:\Users\Михаил\Documents\GitHub\500EnilCards\src\red_cards.txt", encoding='utf-8-sig') as RCards_txt:
    RCards_list = RCards_txt.read()

with open(r"C:\Users\Михаил\Documents\GitHub\500EnilCards\src\white_cards.txt", encoding='utf-8-sig') as WCards_txt:
    WCards_list = WCards_txt.read()

class WhiteCards:
    # создаем атрибуты класса
    WC_count = WCards_list.count(";") +  1  #  определяем количество карт
    WC_list = WCards_list.split("; ")  #  Формируем список из карт

class RedCards:
    # создаем атрибуты класса
    RC_count = RCards_list.count(";") +  1  #  определяем количество карт
    RC_list = re.sub("[_]+", "*****", RCards_list).split("; ")  #  Формируем список из карт