# count the number of characters in a string, with a number beside each character indicating how many times it appears in the string

def count_characters(s):
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

