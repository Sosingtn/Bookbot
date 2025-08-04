def get_num_words(content):
    counted_words = len(content.split())
    return counted_words

def get_num_chars(content):
    letters = {}

    for letter in content:
        if not letter.isalpha():
            continue
        lower_letter = letter.lower()
        if lower_letter not in letters:
            letters[lower_letter] = 1
        else:
            letters[lower_letter] += 1
    return letters

def turn_dict_into_list(dicts):
    list_of_dict = []
    for char in dicts:
        count = dicts[char]
        new_dict = {"char":char,"num":count}
        # append dict to list
        list_of_dict.append(new_dict)
    # sort list of dict
    list_of_dict.sort(reverse=True,key=sort_on)
    # return sorted
    return list_of_dict



# helper
def sort_on(list_dicts):
    return list_dicts["num"]
