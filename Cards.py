"""
with open("./red_cards.txt", encoding='utf-8') as RCards_txt:
    RCards_list = RCards_txt.read()
"""
with open(r"C:\Users\Михаил\Documents\GitHub\500EnilCards\white_cards.txt", encoding='utf-8-sig') as WCards_txt:
    WCards_list = WCards_txt.read()
print(WCards_list)
class WhiteCards:
    # создаем атрибуты класса
    WC_count = WCards_list.count(";") +  1  #  определяем количество карт
    WC_list = WCards_list.split(" ; ")  #  Формируем список из карт

