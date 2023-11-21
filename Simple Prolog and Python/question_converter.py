# question_converter.py


def question_to_prolog(query):
    query = query.lower().replace('?', '')


    #Are X and Y the parents of Z?
    if all(word in query for word in ["are", "and", "the", "parents", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "the", "parents", "of"]]
        return f'parent(X, {list_of_names[2]})'

    #Who are the parents of X?
    elif 'who are the parents of ' in query:
        name = query.replace("who are the parents of ", "")
        return f'parent(X, {name.lower()})' 
    
    #Who is the father of X?
    elif 'who is the father of ' in query:
        name = query.replace("who is the father of ", "")
        return f'father(X, {name.lower()})' 
    
    #Who is the mother of X?
    elif 'who is the mother of ' in query:
        name = query.replace("who is the mother of ", "")
        return f'mother(X, {name.lower()})' 

    else:
        return False



def question_answer_converter(question_result, query):
    query = query.lower().replace('?', '')
    
    #Who are the parents of X?
    if 'who are the parents of' in query:
        if len(question_result) == 1:
            return f"The Parent is {question_result[0]['X']}"
        elif len(question_result) == 2:
            return f"The Parents are {question_result[0]['X']} and {question_result[1]['X']}"
        else:
            return "Name/s is not yet in the knowledge base"
    

    #Who is the father of X?
    elif 'who is the father of ' in query:
        if len(question_result) == 1:
            return f"The father is {question_result[0]['X']}"
        else:
            return "Name/s is not yet in the knowledge base"
        
    
    #Who is the mother of X?
    elif 'who is the mother of ' in query:
        if len(question_result) == 1:
            return f"The mother is {question_result[0]['X']}"
        else:
            return "Name/s is not yet in the knowledge base"



    #Are X and Y the parents of Z?
    elif all(word in query for word in ["are", "and", "the", "parents", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "the", "parents", "of"]]
        list_of_parents = [question_result[0]['X'], question_result[1]['X']]
        if all(item in list_of_names for item in list_of_parents):
            return f"Answer: Yes" 
        else:
            return f"Answer: No"