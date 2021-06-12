dict_words = open("E:\\Py_projects\\assignment\\dict.txt", "r")
x = dict_words.read()
words = x.split()
a = len(words)
input_word = input("Enter the word : ")
word_list = input_word.split()
count = 0
for i in range(a):
    for j in range(len(word_list)):
        if word_list[j] in words[i]:
            count = count + 1
            if count > 2:
                print(words[i])
