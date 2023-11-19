# main_script.py
from pyswip import *
from question_converter import *
from statement_converter import  *

def load_prolog_file(file_path):
    prolog = Prolog()
    prolog.consult(file_path)
    return prolog

def query_prolog_file(prolog, query):
    solutions = list(prolog.query(query))
    return solutions

if __name__ == "__main__":
    # Assuming 'family.pl' is in the same directory
    prolog_file_path = 'family.pl'

    # Load the Prolog file
    prolog_file = load_prolog_file(prolog_file_path)
    

    while True:
        # User input for the question
        user_input = input("Enter your question (or type 'exit' to end): ")

        # Exit the loop if the user enters 'exit'
        if user_input.lower() == 'exit':
            break

        #This code block detects if a user_input is a question or a statement through a question mark
        if '?' in user_input:
            
            prolog_query = question_to_prolog(user_input) # Convert the user's question to a Prolog query
            
            #Validate if this is a valid question
            if prolog_query == False:
                print("Invaid Format")
            else:
                # Perform the user's query
                question_result = query_prolog_file(prolog_file, prolog_query)
                if question_result == []:
                    print("Name/s is not yet in the knowledge base")
                    continue
                question_answer = question_answer_converter(question_result,user_input)
                
                # Display user's query result
                print("\nUser's Query Results:")
                for solution in question_result:
                    print(solution)
                print(question_answer)

        else:
            prolog_fact = statement_to_prolog(user_input) # Convert the user's statement to a Prolog Fact

            #Validate if this is a valid statement
            if prolog_fact == False:
                print("Invaid Format")
            else:
                # Add the fact into the knowledge base
                for fact in prolog_fact:
                    if query_prolog_file(prolog_file, fact):
                        continue
                    else:
                        prolog_file.assertz(fact)
                print('''"''' + user_input + '''"''' + " is in the knowledge base.")


        





        

        
