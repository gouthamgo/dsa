#  hashmap/dictionary patterns

def count_letters(word):
    count = {}

    for letter in word:
        if letter in count:
            count[letter] = count[letter] + 1
        else:
            count[letter] = 1
    return count 

print(count_letters('checking'))



# Method 2 :

def count_letter(word):
    count = {}

    for letter in word:
         count[letter] = count.get(letter,0) + 1
    return count
print(count_letter('basic'))