import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))


class InputSentence:
    def __init__(self, input_sentence):
        self.question_words = ["who", "are", "name", "is", "are", "whom", "whose"]
        self.word_tokens = word_tokenize(input_sentence.lower())
        # word_tokens = [w for w in word_tokens if not w in stop_words]
        # self.tagged_tokens = nltk.pos_tag(word_tokens)

    def is_question(self):
        return True if any(x in self.word_tokens[0] for x in self.question_words) else False
        # return self.is_question

    def get_tokens(self):
        tokens = [w for w in self.word_tokens if not w in stop_words]
        return nltk.pos_tag(tokens)
        # return self.tagged_tokens
