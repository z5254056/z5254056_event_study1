with open('data/iso.txt', 'r') as f:
    words = [word for line in f for word in line.split()]

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f'{word}: {count}')