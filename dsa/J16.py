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



#  find first non repeating character in "leetcode"
def check(s):
    c = {}

    for l in s:
        c[l] = c.get(l,0)+1

    for i,l in enumerate(s):
        if c[l] ==1:
            return i
    return -1

print(check("leetcodelots"))
