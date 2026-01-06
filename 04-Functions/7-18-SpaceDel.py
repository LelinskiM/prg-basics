def f(sentence):
    for i in sentence:
        if i == " ":
            sentence = sentence.replace(" ", "")
    return sentence

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))