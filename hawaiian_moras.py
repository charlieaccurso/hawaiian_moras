MORA_COUNTS = {
    'h': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'p': 0,
    'w': 0,
    'ʻ': 0,
    'a': 1,
    'e': 1,
    'i': 1,
    'o': 1,
    'u': 1,
    'ā': 2,
    'ē': 2,
    'ī': 2,
    'ō': 2,
    'ū': 2
}

CONSONANTS= ['h', 'k', 'l', 'm', 'n', 'p', 'w', 'ʻ']


def get_mora_count(hawaiian_word):
    total_mora_count = 0

    for letter in hawaiian_word:
        total_mora_count += MORA_COUNTS.get(letter, 0)

    return "{hawaiian_word}: {total_mora_count}".format(hawaiian_word=hawaiian_word, total_mora_count=total_mora_count)

def get_syllables(hawaiian_word):
    syllables= []
    current_syllable= ''
    for letter in hawaiian_word:
        current_syllable+= letter
        if letter not in CONSONANTS:
            syllables.append(current_syllable)
            current_syllable= ''
    
    return "{hawaiian_word}: {syllables}".format(hawaiian_word=hawaiian_word, syllables=syllables)
        


print(get_mora_count('ʻīlio'))
print(get_syllables('ʻīlio'))

some_text= "makemake ʻoe e hoʻokaika kino i ka hola ʻumikūmamālua o ke awakea"
some_words= some_text.split()
for word in some_words:
    print(get_mora_count(word))
    print(get_syllables(word))



