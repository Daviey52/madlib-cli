with open("madlib.txt", "w") as file:

    word_to_be_filled = [
        "Adjective",
        "A First Name",
        "Plural Noun",
        "Large Animal",
        "Small Animal",
        "Number 1-50",
        "Number",
    ]

    typed_words = []
    for i in word_to_be_filled:
        if i == "Adjective":
            print("type an ", i)
            typed_words.append(input().capitalize())

        else:
            print("type an", i)
            typed_words.append(input().capitalize())

    file.writelines("%s" % line for line in typed_words)
print(file)

newText = open("madlib.txt", "w")
new_name = str(newText)
newText.write(new_name)
newText.close()
newText = open("madlib.txt", "r")
print(newText)
