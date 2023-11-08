from utils import timeit, get_random_list
import multiprocessing
import concurrent.futures


data = ["Astazi suntem la masterclass",
        "Avem topic-uri interesante la masterclass",
        "Python masterclass este ceva wow",
        "La masterclass am vazut lucruri noi",
        "Da",
        "Explorând Python la masterclass",
        "Explorand Python la masterclass",
        "Tehnici de optimizare a codului la masterclass",
        "Data Science si Machine Learning la masterclass",
        "Dezvoltarea web cu Python la masterclass",
        "Imbunatatirea abilitatilor de programare la masterclass",
        "Cum sa deveniti un expert Python la masterclass",
        "Securitate cibernetica si etica in IT la masterclass",
        "Introducere in programarea cu Python la masterclass",
        "Masterclass-ul Python si viitorul dezvoltarii software",
        "Proiecte practice si studii de caz la masterclass",
        "Utilizarea eficienta a bibliotecilor Python la masterclass",
        "Lucrul in echipa si colaborarea la masterclass",
        "Dezvoltarea competentelor de analiza de date la masterclass",
        "Intelegerea algoritmilor si structurilor de date la masterclass",
        "Python si aplicatii de invatare automata la masterclass",
        "Crearea de aplicatii web Python de inalta performanta la masterclass"]

words_to_match = ["masterclass", "aplicatii", "Python"]
max_loop = 1000


@timeit
def without_index(_data):
    for i in range(1000):
        for word in words_to_match:
            matches = [s for s in _data if word in s]


class InvertedIndex():
    index = None
    def __init__(self, _data):
        self._data = _data
        self.index = {}
        self.create_index()
        self.create_index_batch()
        self.create_index_multi()
        self.create_index_futures()

    # ============================================================================================

    @timeit
    def create_index(self):
        self.index = {}
        for i, doc in enumerate(self._data):
            for word in doc.split():
                self.index.setdefault(word, []).append(i)

    # ============================================================================================

    @timeit
    def create_index_batch(self):
        self.index = {}
        temp_index = {}
        for i, doc in enumerate(self._data):
            for word in doc.split():
                temp_index.setdefault(word, []).append(i)

        # Update the main index in a batch
        for word, indices in temp_index.items():
            self.index[word] = self.index.get(word, []) + indices

    # ============================================================================================

    @timeit
    def with_index(self):
        for i in range(1000):
            for word in words_to_match:
                results = self.index[word]
                matches = [self._data[i] for i in results]

    # ============================================================================================

    @timeit
    def create_index_multi(self):
        self.index = {}
        num_processes = multiprocessing.cpu_count()

        chunks = [self._data[i:i + len(self._data) // num_processes] for i in range(0, len(self._data), len(self._data) // num_processes)]

        pool = multiprocessing.Pool(processes=num_processes)
        result = pool.map(self.process_chunk, chunks)

        self.index = {}
        for partial_index in result:
            for word, doc_indices in partial_index.items():
                self.index.setdefault(word, []).extend(doc_indices)

    def process_chunk(self, chunk):
        partial_index = {}
        for i, doc in enumerate(chunk):
            for word in doc.split():
                partial_index.setdefault(word, []).append(i)
        return partial_index

    # ============================================================================================

    @timeit
    def create_index_futures(self):
        num_threads = 8  # You can adjust the number of threads based on your system's capacity

        self.index = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            future_to_chunk = {executor.submit(self.process_chunk, chunk): chunk for chunk in self.split_data(num_threads)}
            for future in concurrent.futures.as_completed(future_to_chunk):
                chunk = future_to_chunk[future]
                partial_index = future.result()
                for word, doc_indices in partial_index.items():
                    self.index.setdefault(word, []).extend(doc_indices)

    def split_data(self, num_threads):
        chunk_size = len(self._data) // num_threads
        return [self._data[i:i + chunk_size] for i in range(0, len(self._data), chunk_size)]


if __name__ == '__main__':
    print(f"{len(data)} items")
    without_index(data.copy())
    inverted_index_class = InvertedIndex(data.copy())
    inverted_index_class.with_index()
    
    print()

    data += get_random_list()
    print(f"{len(data)} items")
    without_index(data.copy())
    inverted_index_class = InvertedIndex(data.copy())
    inverted_index_class.with_index()