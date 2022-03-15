from statistics import median

def average_count(text_in):
    sentence_count = 0
    total_words = 0

    for key in text_in:
        sentence_count += 1
        total_words += len(text_in[key])

    return (total_words / (sentence_count -1))


def median_count(text_in):
    median_arr = []

    for key in text_in:
        median_arr.append(len(text_in[key]))

    return (median(median_arr))


def repeats(text_in):
    list_words = dict()

    for value in text_in.values():
        for word in value:
            if word in list_words:
                list_words[word] += 1
            else:
                list_words[word] = 1
    return list_words


def top_ngrams(text_in, K, N):
    keys = []

    for value in text_in.values():
        for element in value:
            for letter in element:
                keys.append(letter)
            letters_sequences = [keys[i:] for i in range(N)]

    ngrams_list = list(zip(*letters_sequences))
    ngrams_dictionary = {}

    for ngram in ngrams_list:
        if ngram in ngrams_dictionary:
            ngrams_dictionary[ngram] += 1
        else:
            ngrams_dictionary[ngram] = 1

    print(f"Top-{K} {N}-grams:")

    return (dict(sorted(ngrams_dictionary.items(), key=lambda item: item[1], reverse=True)))


def replace_all(text, dictionary):
    for i, j in dictionary.items():
        text = text.replace(i,j)
    return text


def main():

    text = input().lower()
    correct_text = replace_all(text, {",": "", ":" : "", ";" : "", "?": ".", "!": "." }).split(".")
    text_in = dict()

    for sentence in correct_text:
        text_in[correct_text.index(sentence)+1] = sentence.split()

    list_words = repeats(text_in)
    print("Word repetition list:")

    for key in list_words:
        print(f"{key}:{list_words[key]}")
    average_count(text_in)
    print(f"Average amount of words in sentences:{average_count(text_in)}")
    median_count(text_in)
    print(f"Median amount of words in sentences:{median_count(text_in)}")


    K = 10
    sort_ngram = top_ngrams(text_in, 10, 4)

    for hey in sort_ngram:
        K -= 1
        if K == -1:
            return
        for meow in hey:
            print(f"{meow}", end="")

        print(f":{sort_ngram[hey]}")


        
if __name__ == "__main__":
    main()