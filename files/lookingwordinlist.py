some_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

sentence_list = ["i'm going this friday", "i'm not going", "i plan to go saturday"]

new_list = []

for day in some_list:
    for sentence in sentence_list:
        if day in sentence:
            new_list.append(sentence)

print(new_list)