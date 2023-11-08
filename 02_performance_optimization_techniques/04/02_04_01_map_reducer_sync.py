from random_text import RANDOM_TEXT
from utils import timeit


def map_function(text):
    words = text.split()
    word_count = [(word, 1) for word in words]
    return word_count


def reduce_function(word_counts):
    word_count = sum(word_counts)
    return word_count


def get_text_chunks(text):
    return text.split('.')


def get_shuffled_data(mapped_data):
    shuffled_data = {}
    for word, count in mapped_data:
        shuffled_data.setdefault(word, []).append(count)
    return shuffled_data


@timeit
def main():
    text = RANDOM_TEXT * 10
    text_chunks = get_text_chunks(text)

    mapped_data = []
    for chunk in text_chunks:
        mapped_data.extend(map_function(chunk))
    
    shuffled_data = get_shuffled_data(mapped_data)

    reduced_data = [(word, reduce_function(word_counts)) for word, word_counts in shuffled_data.items()]
    
    for word, count in reduced_data:
        print(f'{word}: {count}')
        # pass


if __name__ == '__main__':
    main()
