def strip_punctuation_ru(data):
    punctuation = [',', '.', '!', '?', ';', ':', '-', '—', '(', ')', '"', "'"]
    for char in punctuation:
        data = data.replace(char, ' ')
    words = data.split()
    return ' '.join(words)
