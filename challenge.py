# 1: PREFIX TO WORD
def add_prefix_un(word):
    return 'un' + word

# 2: PREFIX TO WORD GROUPS
def make_word_groups(g_words):
    prefix = g_words[0]
    words = g_words[1:]
    return prefix + ' --> ' + ' : '.join([prefix + word for word in words])

# 3: REMOVE SUFFIX
def remove_suffix_ness(word):
    if word.endswith('ness'):
        if word[-5] == 'i':
            return word[:-5] + 'y'
        else:
            return word[:-4]
    return word

# 4: EXTRACT AND TRANSFORM
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    if adjective.endswith('.'):
        adjective = adjective[:-1]
    return adjective + 'en'

# TEST
print("TASK 1: PREFIX TO WORD")
print(add_prefix_un("happy"))  # 'unhappy'
print(add_prefix_un("manageable"))  # 'unmanageable'

print("\nTASK2: PREFIX TO WORD GROUPS")
print(make_word_groups(['en', 'close', 'joy', 'lighten']))  # 'en --> enclose : enjoy : enlighten
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))  
print(make_word_groups(['auto', 'didactic', 'graph', 'mate'])) 
print(make_word_groups(['inter', 'twine', 'connected', 'dependent'])) 

print("\nTASK 3: REMOVE SUFFIX")
print(remove_suffix_ness("heaviness"))  # 'heavy'
print(remove_suffix_ness("brightness"))  # 'bright'
print(remove_suffix_ness("sharpness"))  # 'sharp'
print(remove_suffix_ness("happiness"))  # 'happy'
print(remove_suffix_ness("sadness"))  # 'sad'

print("\nTASK 4: EXTRACT AND TRANSFORM")
print(adjective_to_verb('I need to make that bright.', -1))  # 'brighten'
print(adjective_to_verb('It got dark as the sun set.', 2))  # 'dark'