from string import Template

from flask import Flask, request

from InputSentence import InputSentence
import query_templates

app = Flask(__name__)


@app.route('/sentence', methods=["POST"])
def detect_sentence():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.get_json()
        # create prolog query or statement, then return answer
        input_sentence = InputSentence(json['sentence'])
        # is_question = SentenceDetector.parse_sentence(json['sentence'])
        token_sequence = []
        if input_sentence.is_question():
            query = Template('ffather(x, $x)')
            for token in input_sentence.get_tokens():
                token_sequence.append(token[1])
                # if str(token[1]) == "NNP":
                #     query.substitute(x=token[0])

            # print("-".join(token_sequence))

            return {"response": "sentence is a question",
                    "tokens": input_sentence.get_tokens(),
                    "sentence_pattern": token_sequence,
                    "query": query.__str__()}
        else:
            return {"response": "added to knowledge base",
                    "tokens": input_sentence.get_tokens(),
                    "sentence_pattern": token_sequence,
                    "query": query_templates.father_of}
    else:
        return {"response": "Content-Type not supported!"}

    # with PrologMQI() as mqi:
    #     with mqi.create_thread() as prolog_thread:
    #         result = prolog_thread.query("atom(a)")
    #         return str(result)


if __name__ == '__main__':
    app.run()
