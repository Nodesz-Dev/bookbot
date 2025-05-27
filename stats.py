def count_words(text_to_count):
    list_of_words = text_to_count.split()
    return len(list_of_words);

def count_characters(text_to_count):
    Text_after_lowercase = text_to_count.lower()
    Character_dictionary = {}

    for char in Text_after_lowercase:
        # check to see if the key exists in the dictionary already
        if char in Character_dictionary:
        # if it does exist, then increment the value of the key by 1
            Character_dictionary[char] += 1
        # if it doesnt exists, we add the key and set its value to 1
        else:
            Character_dictionary[char] = 1
        
    return Character_dictionary;

def sort_on(dict):
    return dict["num"]

def sort_character_list(character_dictionary):
    list_of_dict = []

    for key in character_dictionary:
        if key.isalpha():
            #print(f"char : {key}, num : {character_dictionary[key]}")
            list_of_dict.append({"char" : key, "num" : character_dictionary[key]})

    #print(list_of_dict)
    #return list_of_dict.sort(reverse=True, key=sort_on(list_of_dict))
    return sorted(list_of_dict, key=lambda i: i['num'], reverse=True)

    
