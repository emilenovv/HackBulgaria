def unique_words_count(arr):
    words = {}
    for word in arr:
        words[word] = 1
    return len(words)

print(unique_words_count(["python", "python", "python", "ruby"]))
