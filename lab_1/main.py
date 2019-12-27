import math
REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if type(word)!= str:
            return -1
        if word not in self.storage:
            if not self.storage:
                ident = 1
            else:
                ident = max(self.storage.values()) + 1
            self.storage[word] = ident
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
        return - 1

    def get_original_by(self, id_of: int) -> str:
        if type(id_of) == int and id_of in self.storage.values:
           id_of = list(self.storage.values()).index(id_of)
            return list(self.storage.keys())[id_of]
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if type(corpus) == tuple:
            return {}
        for word in corpus:
            if word not in self.storage:
                self.storage[word] = self.put(word)
        return self.storage


class NGramTrie:
    def __init__(self, n):
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.size = size

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence != tuple(sentence) or sentence == () or sentence is None:
            return "ERROR"
        kol_combinations = []
        for i in range(len(sentence)):
            if i < len(sentence) - self.size:
                kol_combinations.append(sentence[i: i + self.size])
            elif i == len(sentence) - self.size:
                kol_combinations.append(sentence[i:])
        for gram in kol_combinations:
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
        return "OK"

    def calculate_log_probabilities(self):
		kol_variants=[]
        for key in self.gram_frequencies.keys():
            kol_variants.append(key)
        count = 0
        while count != len(kol_variants):
            for gram in variants:
                grams = []
                gram_count = self.gram_frequencies[gram]
                for extra_gram in kol_variants:
                    if gram[:-1] == extra_gram[:-1]:
                        grams.append(self.gram_frequencies[extra_gram])
                count_grams = sum(grams)
                e_log = math.log(gram_count / count_grams)
                self.gram_log_probabilities[gram] = e_log
                count = count + 1

    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.gram_log_probabilities is None or type(prefix)!= tuple or or prefix == () len(prefix) != self.size - 1 :
            return []
        s = []
        s.extend(list(prefix))
        list_n = []
        for gram in self.gram_log_probabilities:
            gram_1 = gram[:len(gram) - 1]
            list_n.append(gram_1)
        while prefix in list_n:
            prob_l = []
            for keys, values in self.gram_log_probabilities.items():
                if prefix == keys[:len(keys) - 1]:
                    prob_l.append((values, keys))
            prob_l.sort(reverse=True)
            s.append(prob_l[0][1][-1])
            prefix = prob_l[0][1][1:]
        return s


def encode(storage_instance, corpus) -> list:
    new_corpus = []
    if corpus is not None:
        for s in corpus:
            encoded_sentence = []
            for word in s:
                encoded_sentence.append(storage_instance.get_id_of(word))
            new_corpus.append(encoded_sentence)
    else:
        return []
    return new_corpus


def split_by_sentence(text: str) -> list:
    sentences = []
    if type(text)!= str or '.' not in text or text == '' :
        return sentences
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace('?', '.')
    text = text.replace('!', '.')
    text = text.split('. ')
    for sentence in text:
        clear = ''
        for symbol in sentence:
            if symbol.isalpha() or sym == ' ':
                clear += sym
        if clear_sentence:
            s = ['<s>']
            s.extend(clear.split())
            s.append('</s>')
            sentences.append(s)
    return sentences
