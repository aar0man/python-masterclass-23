import re
from utils.utils import timeit, read_data_from_file, write_data_to_file


class MapReduce:
    def __init__(self, text):
        self.text = self.prepare_text(text)
    
    def prepare_text(self, text):
        """ Pregătire și cleanup """
        # TODO - improve re
        pattern = r"[^a-zA-Z0-9.\-“ ]"
        text = re.sub(pattern, "", text)
        return text.lower()

    def get_text_chunks(self):
        """ Împarte textul în bucăți mai mici """
        return self.text.split('.')

    def map_function(self, chunk):
        """ Împarte textul în cuvinte """
        return [(word, 1) for word in chunk.split()]

    def get_mapped_data(self, text_chunks):
        """ Faza de mapare """
        mapped_data = [self.map_function(chunk) for chunk in text_chunks]
        return [item for sublist in mapped_data for item in sublist]

    def sort_shuffled_data(self, shuffled_data):
        """ Sortare set date """
        return {i[0]: i[1] for i in sorted(shuffled_data.items())}

    def get_shuffled_data(self, mapped_data):
        """ Faza de shuffle și sortare """
        shuffled_data = {}
        for word, count in mapped_data:
            shuffled_data.setdefault(word, []).append(count)
        return self.sort_shuffled_data(shuffled_data)

    def reduce_function(self, word_counts):
        """ Adunăm toate valorile pentru fiecare cheie """
        return sum(word_counts)

    def get_reduced_data(self, shuffled_data):
        """ Faza de reductie """
        return [(word, self.reduce_function(word_counts)) for word, word_counts in shuffled_data.items()]

    def print_results(self, temp_file_name):
        """ Printare date """
        results = read_data_from_file(temp_file_name)
        print(results)

    def get_results(self, print_results=True):
        text_chunks = self.get_text_chunks()
        mapped_data = self.get_mapped_data(text_chunks)
        shuffled_data = self.get_shuffled_data(mapped_data)
        reduced_data = self.get_reduced_data(shuffled_data)

        temp_file_name = write_data_to_file(reduced_data)
        if print_results:
            self.print_results(temp_file_name)


@timeit
def main():
    data = read_data_from_file("/utils/random_text.txt")
    map_reduce = MapReduce(data*10)
    map_reduce.get_results(print_results=False)


if __name__ == '__main__':
    main()
