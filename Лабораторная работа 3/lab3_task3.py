# TODO  Напишите функцию count_letters
def count_letters(text_):
    text1_ = text_.lower()
    letterslist = []
    dict_ = {}
    for char_ in text1_:
        if char_.isalpha():
            letterslist.append(char_)
    for letter in set(letterslist):
        dict_[letter] = letterslist.count(letter)
    return dict_

# TODO Напишите функцию calculate_frequency
def calculate_frequency(lettersdict_):
    freqdict = {}
    totalcount_ = sum(lettersdict_.values())
    for key in lettersdict_.keys():
        freqdict[key] = round((lettersdict_[key])/totalcount_, 2)
    return freqdict
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
#В МОЕМ СЛОВАРЕ БУКВЫ В ДРУГОМ ПОРЯДКЕ ПОЭТОМУ ТАКОЙ ДУРАЦКИЙ ВЫВОД ДЕЛАТЬ ПРИШЛОСЬ
A = calculate_frequency(count_letters(main_str))
print('у:', A['у'])
print('л:', A['л'])
print('к:', A['к'])
print('о:', A['о'])
print('м:', A['м'])
print('р:', A['р'])
print('ь:', A['ь'])
print('я:', A['я'])
print('д:', A['д'])
print('б:', A['б'])
print('з:', A['з'])
print('е:', A['е'])
print('ё:', A['ё'])
print('н:', A['н'])
print('ы:', A['ы'])
print('й:', A['й'])
print('а:', A['а'])
print('т:', A['т'])
print('ц:', A['ц'])
print('п:', A['п'])
print('и:', A['и'])
print('ч:', A['ч'])
print(f"ю: {A['ю']:.2f}")
print('в:', A['в'])
print('с:', A['с'])
print('х:', A['х'])
print('г:', A['г'])
print(f"ш: {A['ш']:.2f}")
print('ж:', A['ж'])
print(f"щ: {A['щ']:.2f}")
