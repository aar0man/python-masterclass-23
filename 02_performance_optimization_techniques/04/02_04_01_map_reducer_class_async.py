import re
import asyncio
import time

from utils import timeit, read_data_from_file, write_data_to_file


class MapReduce:
    def __init__(self, text):
        self.text = self.prepare_text(text)
    
    def prepare_text(self, text):
        """ pregatire si cleanup """
        # TODO - improve re
        pattern = r"[^a-zA-Z0-9.\-“ ]"
        text = re.sub(pattern, "", text)
        return text.lower()

    def get_text_chunks(self):
        """ imparte textul in bucati mai mici """
        return self.text.split('.')

    def get_text_chunks(self):
        """ imparte textul in bucati mai mici """
        return self.text.split('.')

    async def map_function(self, chunk):
        """ imparte textul in cuvinte """
        return [(word, 1) for word in chunk.split()]

    async def get_mapped_data(self, text_chunks):
        """ faza de mapare """
        mapped_data = [await self.map_function(chunk) for chunk in text_chunks]
        return [item for sublist in mapped_data for item in sublist]

    def sort_shuffled_data(self, shuffled_data):
        """ sortare set date """
        return {i[0]: i[1] for i in sorted(shuffled_data.items())}

    def get_shuffled_data(self, mapped_data):
        """ faza de shuffle si sortare """
        shuffled_data = {}
        for word, count in mapped_data:
            shuffled_data.setdefault(word, []).append(count)
        return self.sort_shuffled_data(shuffled_data)

    async def reduce_function(self, word_counts):
        """ adunam toate valorile pentru fiecare cheie """
        return sum(word_counts)

    async def get_reduced_data(self, shuffled_data):
        """ faza de reductie """
        return [(word, await self.reduce_function(word_counts)) for word, word_counts in shuffled_data.items()]

    def print_results(self, temp_file_name):
        """ Printare date """
        results = read_data_from_file(temp_file_name)
        print(results)

    async def get_results(self, print_results=True):

        text_chunks = self.get_text_chunks()
        mapped_data = await self.get_mapped_data(text_chunks)
        shuffled_data = self.get_shuffled_data(mapped_data)
        reduced_data = await self.get_reduced_data(shuffled_data)

        temp_file_name = write_data_to_file(reduced_data)
        if print_results:
            self.print_results(temp_file_name)


@timeit
async def main():
    data = read_data_from_file("/home/andrei/workspace/masterclass/masterclass/python-masterclass-23/random_text.txt")
    map_reduce = MapReduce(data*10)
    await map_reduce.get_results(print_results=False)


if __name__ == '__main__':
    start_time = time.perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.20f} seconds')