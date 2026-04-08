#count characters

def count_characters2(s):

    new_dict = {}
    for ch in s:
        if ch == " ":
            continue
        if ch in new_dict:
            new_dict[ch] += 1
        else:
            new_dict[ch] = 1
    return new_dict

final_dict = count_characters2("Hello my name is Mustafa")

print(final_dict)

print()

for key, value in final_dict.items():
        print(key, ":", value)