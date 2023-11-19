


def statement_to_prolog(query):
    query = query.lower().replace('.', '')


    #X and Y are the parents of Z.
    if all(word in query for word in ["and", "are", "the", "parents", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["and", "are", "the", "parents", "of"]]
        return [f'parent({list_of_names[0]}, {list_of_names[2]})', f'parent({list_of_names[1]}, {list_of_names[2]})']

    #X is the father of Y.
    elif "is the father of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "father", "of"]]
        return [f'father({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[0]}, {list_of_names[1]})']

    #X is the Mother of Y.
    elif "is the mother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "mother", "of"]]
        return [f'mother({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[0]}, {list_of_names[1]})']
    
    #X is a child of Y.
    elif "is a child of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "child", "of"]]
        return [f'child({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[1]}, {list_of_names[0]})']
    
    #X and Y are siblings.
    elif all(word in query for word in ["and", "are", "siblings"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["and", "are", "siblings"]]
        return [f'sibling({list_of_names[0]}, {list_of_names[1]})']
    
    #X is a sister of Y.
    elif "is a sister of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "sister", "of"]]
        return [f'sister({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})']
    
    #X is a brother of Y.
    elif "is a brother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "brother", "of"]]
        return [f'brother({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})']

    #X is a grandmother of Y.
    elif "is a grandmother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandmother", "of"]]
        return [f'grandmother({list_of_names[0]}, {list_of_names[1]})', f'grandchild({list_of_names[1]}, {list_of_names[0]})']

    #X is a grandfather of Y.
    elif "is a grandfather of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandfather", "of"]]
        return [f'grandfather({list_of_names[0]}, {list_of_names[1]})', f'grandchild({list_of_names[1]}, {list_of_names[0]})']

    #X, Y, and Z are children of W
    elif all(word in query for word in ["and", "are", "children", "of"]):
        query = query.replace(',', '').split()
        list_of_names = [word for word in query if word not in ["and", "are", "children", "of"]]
        print(list_of_names)
        return [
                f'child({list_of_names[0]}, {list_of_names[3]})', 
                f'child({list_of_names[1]}, {list_of_names[3]})',
                f'child({list_of_names[2]}, {list_of_names[3]})',
                f'parent({list_of_names[3]}, {list_of_names[0]})',
                f'parent({list_of_names[3]}, {list_of_names[1]})',
                f'parent({list_of_names[3]}, {list_of_names[2]})'
                ]

    #X is a daughter of Y.
    elif "is a daughter of" or "is the daughter of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "the", "daughter", "of"]]
        return [f'child({list_of_names[0]}, {list_of_names[1]})', 
                f'parent({list_of_names[1]}, {list_of_names[0]})', 
                f'daughter({list_of_names[0]}, {list_of_names[1]})']

    else:
        return False