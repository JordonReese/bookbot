def num_words_func(str):
    word_count = str.split()
    return len(word_count)



def char_count(text):
    character_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_dict(dict):
    dict_list = []
    for key in dict:
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["count"] = dict[key]
        dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=lambda x: x["count"])
    return dict_list

