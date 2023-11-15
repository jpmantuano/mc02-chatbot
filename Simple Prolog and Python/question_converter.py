# question_converter.py


def question_to_prolog(query):
    query = query.lower().replace('?', '')


    #Are Jack and Amy the parents of Alex?
    if all(word in query for word in ["are", "and", "the", "parents", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "the", "parents", "of"]]
        print(list_of_names)
        return f'parent(X, {list_of_names[2]})'

    #Who are the parents of Alex?
    elif 'who are the parents of ' in query:
        name = query.replace("who are the parents of ", "")
        return f'parent(X, {name.lower()})' 
    else:
        return False



def question_answer_converter(question_result, query):
    query = query.lower().replace('?', '')
    
    if 'who are the parents of' in query:
        return f"The Parents are {question_result[0]['X']} and {question_result[1]['X']}"
    
    elif all(word in query for word in ["are", "and", "the", "parents", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "the", "parents", "of"]]
        list_of_parents = [question_result[0]['X'], question_result[1]['X']]
        if all(item in list_of_names for item in list_of_parents):
            return f"Answer: Yes" 
        else:
            return f"Answer: No"