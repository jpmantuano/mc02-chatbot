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

    #Is X a grandfather of Y?
    elif all(word in query for word in ["is", "a", "grandfather", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandfather", "of"]]
        return f'grandfather(X, {list_of_names[1]})'

    #Is X a grandmother of Y?
    elif all(word in query for word in ["is", "a", "grandmother", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandmother", "of"]]
        return f'grandmother(X, {list_of_names[1]})'

    #Is X a sister of Y?
    elif all(word in query for word in ["is", "a", "sister", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "sister", "of"]]
        return f'sister(X, {list_of_names[1]})'

    #Is X a brother of Y?
    elif all(word in query for word in ["is", "a", "brother", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "brother", "of"]]
        return f'brother(X, {list_of_names[1]})'

    #Is X the mother of Y?
    elif all(word in query for word in ["is", "the", "mother", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "mother", "of"]]
        return f'mother(X, {list_of_names[1]})'

    #Is X the father of Y?
    elif all(word in query for word in ["is", "the", "father", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "father", "of"]]
        return f'father(X, {list_of_names[1]})'

    #Is X a daughter of Y?
    elif all(word in query for word in ["is", "a", "daughter", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "daughter", "of"]]
        return f'daughter(X, {list_of_names[1]})'

    #Is X a son of Y?
    elif all(word in query for word in ["is", "a", "son", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "son", "of"]]
        return f'son(X, {list_of_names[1]})'

    #Is X a child of Y?
    elif all(word in query for word in ["is", "a", "child", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "child", "of"]]
        return f'child(X, {list_of_names[1]})'

    #Is X an uncle of Y?
    elif all(word in query for word in ["is", "an", "uncle", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "an", "uncle", "of"]]
        return f'uncle(X, {list_of_names[1]})'

    #Is X an aunt of Y?
    elif all(word in query for word in ["is", "an", "aunt", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "an", "aunt", "of"]]
        return f'aunt(X, {list_of_names[1]})'

    #Are X and Y siblings?
    elif all(word in query for word in ["are", "and", "siblings"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "siblings"]]
        return f'sibling(X, {list_of_names[1]})'

    #Are X and Y relatives?
    elif all(word in query for word in ["are", "and", "relatives"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "relatives"]]
        return f'relative(X, {list_of_names[1]})'

    #WIP
    #Are W, X and Y children of Z?
    elif all(word in query for word in ["are", ",", "and", "children", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", ",", "and", "children", "of"]]
        return f'child(X, {list_of_names[3]})' #edit index to adapt with number of children

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

    #Is X a grandfather of Y?
    elif 'is' and 'a grandfather of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandfather", "of"]]
        list_of_grandfathers = [question_result[0]['X'], question_result[1]['X']]
        if any(item in list_of_names for item in list_of_grandfathers):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a grandmother of Y?
    elif 'is' and 'a grandmother of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandmother", "of"]]
        list_of_grandmothers = [question_result[0]['X'], question_result[1]['X']]
        if any(item in list_of_names for item in list_of_grandmothers):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a sister of Y?
    elif 'is' and 'a sister of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "sister", "of"]]
        list_of_sisters = [question_result[0]['X'], question_result[1]['X']]
        if any(item in list_of_names for item in list_of_sisters):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a brother of Y?
    elif 'is' and 'a brother of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "brother", "of"]]
        list_of_brothers = [question_result[0]['X'], question_result[1]['X']]
        if any(item in list_of_names for item in list_of_brothers):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X the mother of Y?
    elif 'is' and 'the mother of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "mother", "of"]]
        list_of_mothers = [question_result[0]['X']]
        if all(item in list_of_names for item in list_of_mothers):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X the father of Y?
    elif 'is' and 'the father of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "father", "of"]]
        list_of_fathers = [question_result[0]['X']]
        if all(item in list_of_names for item in list_of_fathers):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a daughter of Y?
    elif 'is' and 'a daughter of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "daughter", "of"]]
        list_of_daughters = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_daughters):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a son of Y?
    elif 'is' and 'a son of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "son", "of"]]
        list_of_sons = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_sons):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X a child of Y?
    elif 'is' and 'a child of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "child", "of"]]
        list_of_children = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_children):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X an uncle of Y?
    elif 'is' and 'an uncle of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "an", "uncle", "of"]]
        list_of_uncles = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_uncles):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Is X an aunt of Y?
    elif 'is' and 'an aunt of ' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "an", "aunt", "of"]]
        list_of_aunts = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_aunts):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Are X and Y siblings?
    elif 'are' and 'and' and 'siblings' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "siblings"]]
        list_of_siblings = [question_result[0]['X']]
        if all(item in list_of_names for item in list_of_siblings):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #Are X and Y relatives?
    elif 'are' and 'and' and 'relatives' in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", "and", "relatives"]]
        list_of_relatives = [question_result[0]['X']]
        if any(item in list_of_names for item in list_of_relatives):
            return f"Answer: Yes"
        else:
            return f"Answer: No"

    #WIP
    #Are W, X and Y children of Z?
    elif all(word in query for word in ["are", ",", "and", "children", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["are", ",", "and", "children", "of"]]
        list_of_children = [question_result[0]['X']]
        if all(item in list_of_names for item in list_of_children):
            return f"Answer: Yes"
        else:
            return f"Answer: No"
