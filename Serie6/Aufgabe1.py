# 1. Definieren der Liste der zu sortierenden Wörter
words = ["Programming", "Python", "algorithm", "sort", "data", "a", "aeiou"]


def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for vowel in vowels:
        vowel_count += word.count(vowel)
    return vowel_count


sorted_words = sorted(words, key=count_vowels)


print(sorted_words)