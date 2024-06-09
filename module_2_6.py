def _single_root_words(root_word, *other_word):
    same_word = []
    for i in other_word:
        if i.lower().count(root_word.lower()) or root_word.lower().count(i.lower()):
            same_word.append(i)
    return same_word

print(_single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))