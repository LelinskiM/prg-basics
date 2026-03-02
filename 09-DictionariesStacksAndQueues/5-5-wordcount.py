paragraph = "cat dog mouse cat rat cat mouse"

words = paragraph.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print results
for word, count in word_count.items():
    print(word, ":", count)