from flask import Flask, request

import SentenceDetector

app = Flask(__name__)


@app.route('/sentence', methods=["POST"])
def detect_sentence():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        # create prolog query or statement, then return answer
        is_question = SentenceDetector.parse_sentence(json['sentence'])
        if is_question:
            return {"response": "sentence is a question"}
        else:
            return {"response": "added to knowledge base"}
    else:
        return {"response": "Content-Type not supported!"}

    # with PrologMQI() as mqi:
    #     with mqi.create_thread() as prolog_thread:
    #         result = prolog_thread.query("atom(a)")
    #         return str(result)


if __name__ == '__main__':
    app.run()
