class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.word_dict = {}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dict = dict
        for d in dict:
            d = list(d)
            for i in range(len(d)):
                word = d[:i] + ['*'] + d[i+1:]
                word = ''.join(word)
                self.word_dict[word] = self.word_dict.get(word, 0) + 1
        print(self.word_dict)
        print(self.dict)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        list_word = list(word)
        for i in range(len(list_word)):
            w = list_word[:i] + ['*'] + list_word[i+1:]
            w = ''.join(w)
            print(w)
            if w in self.word_dict and (word not in self.dict or self.word_dict[w] != 1):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
