import math


import math
def clean_tokenize_corpus(texts: list) -> list:
    if not texts or type(texts) != list:
        return []
    corpus = []
    for text in texts:
        if text and type(text) == str:
            while '<br />' in text:
                text = text.replace('<br />', " ")
            final = []
            words = text.split(" ")
            for w_1 in words:
                new_w = ""
                if not w_1.isalpha():
                    for i in w_1.lower():
                        if i.isalpha():
                            new_w += i
                    if new_w:
                        final.append(new_w.lower())
                else:
                    final.append(w_1.lower())
            corpus += [final]
    return corpus

class TfIdfCalculator:
    def __init__(self, corpus):
        pass
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if type(self.corpus) != list:
            return []
        else:
            for txt in self.corpus:
                tf_values = {}
                if txt:
                    len_txt = len(txt)
                    for w in txt:
                        if not isinstance(w, str):
                            len_txt = len_txt - 1
                    for w in txt:
                        if type(w) == str and w not in tf_values:
                            count_w = txt.count(w)
                            tf_values[w] = count_w / len_txt
                    self.tf_values += [tf_values]
        return self.tf_values

    def calculate_idf(self):
        clean_words = []
        if type(self.corpus) != list:
            return {}
        new_corpus = []
        for txt in self.corpus:
            if type(txt) != list:
                continue
            for element in txt:
                if element not in clean_words and type(element) == str:
                    clean_words += [element]
            new_corpus.append(clean_words)

        len_corpus = len(new_corpus)
        for word in clean_words:
            freq = 0
            for text in self.corpus:
                if text and word in text:
                    freq += 1
            self.idf_values[word] = math.log(len_corpus / freq)


    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return []
        for txt in self.tf_values:
            tf_idf_new = {}
            for word, val in txt.items():
                if word not in tf_idf_new.keys():
                    tf_idf_new[word] = val * self.idf_values.get(word)
            self.tf_idf_values.append(tf_idf_new)

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.corpus):
            return ()
        if self.tf_idf_values is None:
            return ()
        dict_tf_idf = self.tf_idf_values[document_index]
        if not word in dict_tf_idf:
            return ()
        lst_tf_idf = sorted(dict_tf_idf, key=dict_tf_idf.__getitem__, reverse=True)
        return dict_tf_idf.get(word.lower()), lst_tf_idf.index(word.lower())
REFERENCE_TEXTS= []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
