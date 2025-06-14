def count_words(text):
    words = text.split()
    return len(words)   

def count_characters(text: str):
    occurences = {}
    words = text.split()

    for word in words:
        for char in word.lower():
            if char in occurences:
                occurences[char] += 1
            else:
                occurences[char] = 1
            
    return occurences


def sort_dict(word_dict: dict):
    sorted_dict = []
    for char in word_dict:
        entry = {"char": char, "num": word_dict[char]}
        sorted_dict.append(entry)
    sorted_dict.sort(key=lambda x: x["num"], reverse=True)
    return sorted_dict
