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