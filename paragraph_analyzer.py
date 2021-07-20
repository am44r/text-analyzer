import string

file = open("paragraph.txt", "rt", encoding='utf-8')
lines = file.readlines()


#number of words
words = [i for item in lines for i in item.split()]

#number of sentences
periods = [p for p in words if '.' in p]
excla = [p for p in words if '!' in p]
question = [p for p in words if '?' in p]
punc = len(periods) + len(excla) + len(question)

#number of characters
characters = 0
for i in range(0, len(words)):
    characters += len(words[i])
    if "" in words[i]:
        characters += 1

#checking the text for the word the user chose
user_word = str(input('What word would you like to find the occurence of?: '))
user_word_count = 0
for j in range(0, len(words)):
    if user_word in words[j]:
        user_word_count += 1

    if user_word.title() in words[j]:
        user_word_count += 1


print(f'There are {len(words)} words in this paragraph\n')
print(f'There are {punc} sentences in this paragraph\n')
print(f'There are {characters} characters in this paragraph\n')
print(f'{user_word} occurs {user_word_count} times in this text')
