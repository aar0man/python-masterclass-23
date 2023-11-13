import re
import threading
from utils.utils import timeit, read_data_from_file


class MapReduce:
    def __init__(self, text):
        self.text = self.prepare_text(text)
    
    def prepare_text(self, text):
        pattern = r"[^a-zA-Z0-9.\-“ ]"
        text = re.sub(pattern, "", text)
        return text.lower()

    def get_text_chunks(self):
        return self.text.split('.')

    def map_function(self, chunk, result_dict):
        mapped_data = [(word, 1) for word in chunk.split()]
        for word, count in mapped_data:
            result_dict[word] = result_dict.get(word, 0) + count

    def run_map_phase(self, text_chunks, result_dict):
        for chunk in text_chunks:
            self.map_function(chunk, result_dict)

    def reduce_function(self, word_counts):
        return len(word_counts)

    def run_reduce_phase(self, mapped_data, result_dict):
        for word in mapped_data:
            reduced_count = self.reduce_function(word)
            result_dict[word] = reduced_count

    def print_results(self, result_dict):
        for word, count in sorted(result_dict.items()):
            print(f'{word}: {count}')

    def run_map_reduce(self):
        text_chunks = self.get_text_chunks()

        # Map phase
        map_result = {}
        map_threads = []
        for _ in range(4):
            thread = threading.Thread(target=self.run_map_phase, args=(text_chunks, map_result))
            map_threads.append(thread)
            thread.start()
        for thread in map_threads:
            thread.join()

        # Reduce phase
        reduce_result = {}
        reduce_threads = []
        for _ in range(4): 
            thread = threading.Thread(target=self.run_reduce_phase, args=(map_result.keys(), reduce_result))
            reduce_threads.append(thread)
            thread.start()
        for thread in reduce_threads:
            thread.join()

        # self.print_results(reduce_result)

@timeit
def main():
    data = read_data_from_file("/utils/random_text.txt")
    map_reduce = MapReduce(data*10)
    map_reduce.run_map_reduce()

if __name__ == '__main__':
    main()
