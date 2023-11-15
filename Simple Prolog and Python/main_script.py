# main_script.py
from pyswip import Prolog
from question_converter import question_to_prolog, question_answer_converter

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
            # Convert the user's question to a Prolog query
            prolog_query = question_to_prolog(user_input)
            
            #Validate if this is a valid question
            if prolog_query == False:
                print("Invaid Format")
            else:
                # Perform the user's query
                question_result = query_prolog_file(prolog_file, prolog_query)
                question_answer = question_answer_converter(question_result,user_input)
                # Display user's query resultAre Amy and Jack the parents of Alex?
                print("\nUser's Query Results:")
                for solution in question_result:
                    print(solution)
                print(f"Prolog Query: {prolog_query}")
                print(question_answer)
        else:
            print('this is a statement')
            #code that converts the statement into a Prolog Fact
            #code that writes the Prolog Fact into the prolog database
        





        

        
