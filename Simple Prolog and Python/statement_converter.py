from pyswip import *


prolog_file = Prolog()
prolog_file.consult('family.pl')



def find_children():
    return

def find_siblings():
    return


def statement_to_prolog(query):
    query = query.lower().replace('.', '')


    #X and Y are the parents of Z.
    if "are the parents of" in query:
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
    elif "are siblings" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["and", "are", "siblings"]]
        parents_list = find_parents(list_of_names)
        return [f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list
    
    #X is a sister of Y.
    elif "is a sister of" or "is the sister of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "the", "sister", "of"]]
        parents_list = find_parents(list_of_names)
        return [f'sister({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list
    
    #X is a brother of Y.
    elif "is a brother of" or "is the brother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "the", "brother", "of"]]
        parents_list = find_parents(list_of_names)
        return [f'brother({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list

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
    elif "are children of" in query:
        query = query.replace(',', '').split()
        list_of_names = [word for word in query if word not in ["and", "are", "children", "of"]]
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
    




def find_parents(list_of_names):
    # List to store query results
    parents_list = []

    # Query for each name
    for name in list_of_names:
        parent_query = list(prolog_file.query(f"parent(X, {name})"))
        father_query = list(prolog_file.query(f"father(X, {name})"))
        mother_query = list(prolog_file.query(f"mother(X, {name})"))

        # Add results to the list
        parents_list.extend([
            f"parent({parent['X']}, {name})" for parent in parent_query
        ])
        parents_list.extend([
            f"father({father_query[0]['X']}, {name})" if father_query else None,
            f"mother({mother_query[0]['X']}, {name})" if mother_query else None
        ])

    # Remove None values and empty strings from the list
    parents_list = [result for result in parents_list if result is not None and result != '']
    
    def replace_name(parents_list, list_of_names):
        new_name = []
        for name in list_of_names:
            found = any(name in item for item in parents_list)
            if found:
                old_name = name
            else:
                new_name.append(name)

        facts_list = []

        for name in new_name:
            facts_list.append([fact.replace(old_name, name) for fact in parents_list])

        facts_list = [item for sublist in facts_list for item in sublist]
        facts_list = [f'{fact}' for fact in facts_list]

        return facts_list
    
    final_parents = replace_name(parents_list, list_of_names)
    print(final_parents)

    return final_parents