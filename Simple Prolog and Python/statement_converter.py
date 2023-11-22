from pyswip import *


prolog_file = Prolog()
prolog_file.consult('family.pl')








########################################################################################################################
#This section detects User Input and Converts it to Prolog Facts#
########################################################################################################################



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
        new_child_name = [list_of_names[1]]
        child_list = get_children_of_parents(list_of_names, new_child_name)
        parents_list = get_parents_of_siblings(list_of_names)
        return [f'mother({list_of_names[0]}, {new_child_name[0]})', 
                f'parent({list_of_names[0]}, {new_child_name[0]})',
                f'child({new_child_name[0]}, {list_of_names[0]})'] + child_list + parents_list
    
    #X is a child of Y.
    elif "is a child of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "child", "of"]]
        return [f'child({list_of_names[0]}, {list_of_names[1]})', f'parent({list_of_names[1]}, {list_of_names[0]})']
    
    #X and Y are siblings.
    elif "are siblings" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["and", "are", "siblings"]]
        parents_list = get_parents_of_siblings(list_of_names)
        return [f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list
    
    #X is a sister of Y.
    elif "is a sister of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "sister", "of"]]
        parents_list = get_parents_of_siblings(list_of_names)
        return [f'sister({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list
    
    #X is a brother of Y.
    elif "is a brother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "brother", "of"]]
        parents_list = get_parents_of_siblings(list_of_names)
        return [f'brother({list_of_names[0]}, {list_of_names[1]})', f'sibling({list_of_names[0]}, {list_of_names[1]})'] + parents_list

    #X is a grandmother of Y.
    elif "is a grandmother of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandmother", "of"]]
        return [f'grandmother({list_of_names[0]}, {list_of_names[1]})', 
                f'grandchild({list_of_names[1]}, {list_of_names[0]})']

    #X is a grandfather of Y.
    elif "is a grandfather of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "grandfather", "of"]]
        return [f'grandfather({list_of_names[0]}, {list_of_names[1]})', f'grandchild({list_of_names[1]}, {list_of_names[0]})']

    #X is a daughter of Y.s
    elif "is a daughter of" in query:
        query = query.split()
        list_of_names = [word for word in query if word not in ["is", "a", "daughter", "of"]]
        return [f'child({list_of_names[0]}, {list_of_names[1]})', 
                f'parent({list_of_names[1]}, {list_of_names[0]})', 
                f'daughter({list_of_names[0]}, {list_of_names[1]})']

    else:
        return False
    


########################################################################################################################
#This section provides logic to find the relationship between siblings and parents#
########################################################################################################################

def find_siblings():
    return


###########################  CODE TO FIND Children ###################################

def find_children(list_of_names):
    # List to store query results
    children_list =  []

    # Query for each name
    for name in list_of_names:
        parent_query = list(prolog_file.query(f"parent({name}, Y)"))
        father_query = list(prolog_file.query(f"father({name}, Y)"))
        mother_query = list(prolog_file.query(f"mother({name}, Y)"))

        for parent in parent_query:
            children_list.append(parent['Y']) 
        
        for father in father_query:
            children_list.append(father['Y'])
        
        for mother in mother_query:
            children_list.append(mother['Y'])

    children_list = list(set(children_list))

    return children_list

def get_parent_child_pairs(parents_list, children_list):

    list_of_parent_child_pairs = []

    for i in range(len(parents_list)):
        for name in children_list:
            for name2 in children_list:
                if name == name2:
                    continue
                elif name and name2 not in parents_list[i]:
                    continue
                elif name and name2 and "parent" in parents_list[i]:
                    fact = parents_list[i].replace('parent(', '').replace(')', '').replace(' ', '')
                    parent_child = fact.split(",")
                    list_of_parent_child_pairs.append(parent_child)
                elif name and name2 and "child" in parents_list[i]:
                    fact = parents_list[i].replace('child(', '').replace(')', '').replace(' ', '')
                    parent_child = fact.split(",")
                    list_of_parent_child_pairs.append(parent_child)

    return list_of_parent_child_pairs


def process_children(parents_list, children_list):

    list_of_parent_child_pairs = get_parent_child_pairs(parents_list, children_list)

    updated_parents_list = []

    for child in children_list:
        for parent in parents_list:
            if child in parent:
                for name in children_list:
                    if name in parent:
                        continue
                    else:
                        pair_detection  = []
                        for pair in list_of_parent_child_pairs:
                            if child in pair and name in pair:
                                pair_detection.append(True)
                                print(child)
                                print(name)
                                print(pair)
                                print(True)
                            else:
                                pair_detection.append(False)

                        if True in pair_detection:
                            continue
                        else:
                            updated_parents_list.append(parent.replace(child, name))
            else:
                continue
    
    updated_parents_list = list(set(updated_parents_list) - set(parents_list))
    
    return updated_parents_list

def get_children_of_parents(list_of_names, child_name):
    print("get_children_of_parents")
    children_list = find_children(list_of_names)
    children_list = children_list + child_name
    print("children_list")
    print(children_list)
    parents_list = find_parents(children_list)
    print("parents_list")
    print(parents_list)
    updated_parents = process_children(parents_list, children_list)
    print("updated_parents")
    print(updated_parents)

    list_of_parent_child_pairs = get_parent_child_pairs(parents_list, children_list)

    sibling_list = []

    for child in children_list:
        for name in children_list:
            if child == name:
                continue
            else:
                pair_detection  = []
                for pair in list_of_parent_child_pairs:
                    if child in pair and name in pair:
                        pair_detection.append(True)
                        print(child)
                        print(name)
                        print(pair)
                        print(True)
                    else:
                        pair_detection.append(False)
                if True in pair_detection:
                    continue
                else:
                    sibling_list.append(f"sibling({child}, {name})")

    print("sibling_list")
    print(sibling_list)

    return updated_parents + sibling_list
    

###########################  CODE TO FIND PARENTS ###################################

def get_parents_of_siblings(list_of_names):
    parents_list = find_parents(list_of_names)
    final_parents = process_parents(parents_list, list_of_names)
    print("Final Parents")
    print(final_parents)
    return final_parents

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
        parents_list.extend([
            f"child({name}, {parent['X']})" for parent in parent_query
        ])
        parents_list.extend([
            f"child({name}, {father_query[0]['X']})" if father_query else None,
            f"child({name}, {mother_query[0]['X']})" if mother_query else None,
        ])

    # Remove None values and empty strings from the list
    parents_list = [result for result in parents_list if result is not None and result != '']

    print("Parents_List")
    print(parents_list)
       
    return parents_list

def process_parents(parents_list, list_of_names):
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

###########################  CODE TO FIND PARENTS ###################################