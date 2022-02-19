vowels = "aiueo"
def get_count(sentence):
    return sum(sentence.count(a) for a in vowels)
