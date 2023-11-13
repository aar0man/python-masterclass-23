import re
import concurrent.futures
from utils import timeit, read_data_from_file


class MapReduce:
    def __init__(self, text):
        self.text = self.prepare_text(text)
    
    def prepare_text(self, text):
        pattern = r"[^a-zA-Z0-9.\-“ ]"
        text = re.sub(pattern, "", text)
        return text.lower()

    def get_text_chunks(self):
        return self.text.split('.')

    def map_function(self, chunk):
        return [(word, 1) for word in chunk.split()]

    def get_mapped_data(self, text_chunks):
        mapped_data = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            mapped_data = [item for sublist in executor.map(self.map_function, text_chunks) for item in sublist]
        return mapped_data

    def sort_shuffled_data(self, shuffled_data):
        return {i[0]: i[1] for i in sorted(shuffled_data.items())}

    def get_shuffled_data(self, mapped_data):
        shuffled_data = {}
        for word, count in mapped_data:
            shuffled_data.setdefault(word, []).append(count)
        return self.sort_shuffled_data(shuffled_data)

    def reduce_function(self, word_counts):
        return sum(word_counts)

    def get_reduced_data(self, shuffled_data):
        reduced_data = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            reduced_data = list(executor.map(lambda item: (item[0], self.reduce_function(item[1])), shuffled_data.items()))
        return reduced_data

    def print_results(self, reduced_data):
        for word, count in reduced_data:
            print(f'{word}: {count}')

    def get_results(self, print_results=True):
        text_chunks = self.get_text_chunks()
        mapped_data = self.get_mapped_data(text_chunks)
        shuffled_data = self.get_shuffled_data(mapped_data)
        reduced_data = self.get_reduced_data(shuffled_data)

        # if print_results:
        #     self.print_results(reduced_data)


@timeit
def main():
    data = read_data_from_file("/home/andrei/workspace/masterclass/masterclass/python-masterclass-23/random_text.txt")
    map_reduce = MapReduce(data*10)
    map_reduce.get_results(print_results=True)


if __name__ == '__main__':
    main()
