import marisa_trie
from utils.utils import timeit, random_string


@timeit
def default_tries_matches(_strings, search_key='AA'):
	return [s for s in _strings if s.startswith(search_key)]


class SearchTrie():
	def __init__(self, strings):
		self.trie = marisa_trie.Trie(strings)

	def init_strings_dict(self, strings):
		for string in strings:
			self.trie[string] = string

	@timeit
	def search(self, prefix='AA'):
		return self.trie.prefixes(prefix)


if __name__ == '__main__':
	strings = [random_string(32) for i in range(100000)]

	default_tries_matches(strings)

	search_trie = SearchTrie(strings)
	search_trie.search()
