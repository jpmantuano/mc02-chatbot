import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))


def parse_sentence(sentence) -> bool:
    question_words = ["who", "are", "name", "is", "are", "whom", "whose"]

    word_tokens = word_tokenize(sentence.lower())
    word_tokens = [w for w in word_tokens if not w in stop_words]

    SentenceDetector.tagged_tokens = nltk.pos_tag(word_tokens)

    SentenceDetector.is_question = True if any(x in word_tokens[0] for x in question_words) else False
    return SentenceDetector.is_question


class SentenceDetector:
    tagged_tokens = {}
    is_question = False
