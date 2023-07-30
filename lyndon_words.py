# For a quiz to find all Lyndon words of length 10 from a set of 2 letters (a, b).

def is_special(word):
    """Returns True if word is special, False otherwise."""
    for i in range(1, len(word)):
        if word[i:] < word:
            return False
    return True

from itertools import product
# def words(length):
#     """Generates all words of given length."""
#     all = product(('a', 'b'), repeat=length)
#     print(len(all))
#     return all

def test_words(length):
    """Tests all words of given length."""
    all = 0
    count = 1
    for word in product(('a', 'b'), repeat=length):
        all += 1
        if is_special(word):
            print(f"{count:2}: {' '.join(word)}")
            count += 1
    return count, all

print(test_words(10))