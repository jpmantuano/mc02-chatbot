


def statement_to_prolog(query):
    query = query.lower().replace('.', '')


    #X is the father of Y.
    if all(word in query for word in ["is", "the", "father", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "father", "of"]]
        return f'father({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[0]}, {list_of_names[1]})'

    #X is the Mother of Y.
    if all(word in query for word in ["is", "the", "mother", "of"]):
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "the", "mother", "of"]]
        return f'mother({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[0]}, {list_of_names[1]})'


    else:
        return False