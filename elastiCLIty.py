import json
import random

"""""
########################
    START OF 
    MENU SYSTEM
#########""##############
"""
## Clear screen by printing 100 blank newlines
def cls():
    print('\n'*100)

## Load data from file
def load_json():
    f = open('modules.json')
    data = json.load(f)
    f.close()
    return data


## List the categories from the cardbank.json file
def list_categories():
    categories = []
    for i in load_json().keys():
        categories.append(i)
    return categories

## List the modules from the chosenCategory listed in cardbank.json file
def list_modules(chosenCategory):
    if chosenCategory is None:
        return None
    else: 
        modulesList = []
        for i in chosenCategory.keys():
            modulesList.append(i)
        return modulesList

## return a dictonary of a specific category key
def category_exist_check(arg):
    data = load_json()
    try:
        data[arg]
    except KeyError:
        cls()
        # print("load_chosen_category: KeyError:")
        return None
    else:
        return data[arg]

## return the data of a chosen category & module 
def load_chosen_module(chosenCatDict, ChosenModule):

    try:
        chosenCatDict[ChosenModule]
    except KeyError:
        cls()
        # print("load_chosen_module: KeyError:")
        return None
    else:
        return chosenCatDict[ChosenModule]


## Handle key errors: input
def pick_category_by_input():
    print(list_categories())
    chosenCategory = category_exist_check(input("Pick a category: "))
    ## CHECK FOR KEY ERRORSS
    if chosenCategory is None:
        print("No category found with that name please try again. (case sensitive)")
        main_menu("Error")
        
    else:
        return(chosenCategory)

## Handle key errors: input
def module_input_checker(chosenCategory):
    print(list_modules(chosenCategory))
    chosenModule = load_chosen_module(chosenCategory, input("Pick a module: "))

    if chosenModule is None:
        print("No module found with that name please try again. (case sensitive)")
        module_menu(chosenCategory, "Error")
    else:
        return chosenModule


## main menu
def main_menu(arg=""):
    if arg != "Error":
        cls()
    ## pick a category and check to see if category exists.
    chosenCategory = pick_category_by_input()
    ## load the modules from the chosen category
    module_menu(chosenCategory)


## seccondary module menu
def module_menu(chosenCategory, arg = ""):
    if arg != "Error":
        cls()
    ## pick a module, check to see if module exists
    chosenModule = module_input_checker(chosenCategory)
    ## load the modules into the databank of questions:answers
    QA_BANK = get_questions_and_answers(chosenModule)
       
    game(QA_BANK)


#load the question and answer banks from chosen Module
def get_questions_and_answers(chosenModule):
    question_bank = []
    answer_bank = []
    for question, answer in chosenModule.items():
        question_bank.append(question)
        answer_bank.append(answer)

    class Questions_and_Answer_Bank:
        def __init__(self):
            self.question = question_bank
            self.answer = answer_bank
            
    QA_BANK = Questions_and_Answer_Bank()
    return QA_BANK




"""
########################
    START OF 
    GAME SYSTEM
#######################
"""


## main game logic
def game(arg):

    ### a sudo clear screen to print 100 new lines
    QA_BANK = arg
    
    ## Return a random index from the QUESTION_BANK
    def random_question_index():
        QUESTION_BANK_indexLength = len(QA_BANK.question) - 1
        return random.randint(0, QUESTION_BANK_indexLength)
    
    ## return a answer key from a designated index
    def get_answer_from_index(index):
        answerAtIndex = QA_BANK.answer[index]
        return answerAtIndex
    ## return a question from a designated index
    def get_question_from_index(index):
        questionAtIndex = QA_BANK.question[index]
        return questionAtIndex

    def get_random_index_and_question():
        index = random_question_index()
        question = (QA_BANK.question[index])
        return index, question
    
    ## prompt the player for a answer and return the input
    def prompt_input():
        return input(": $ ")
    
    ## Return true if answer at index is a List
    def is_answer_at_index_type_list(index):
        answer = get_answer_from_index(index)
        if isinstance(answer, list):
            return True
        else:
            return False

    ## check if answer is correct using the player input and and 
    ## the answer key from an index
    def is_answer_correct(player_input, index):

        ## First check for multiple answers in list form
        if is_answer_at_index_type_list(index) is True:
            ## Itterate over the list of answers to check to see if 
            ## player input matches one of them
            answer_list = get_answer_from_index(index)
            for i in answer_list:
                if player_input == i:
                    return True
                else:
                    continue
            ## if player input does not match any of them  
            ## return check_answer_is_correct == False
            return False
        
        elif player_input == get_answer_from_index(index):
            return True
        else:
            return False

    """
    ########################
    MAIN QUESTION
    LOOP LOGIC
    #######################
    """

    def should_next_or_same_question(index, answer):

        if is_answer_correct(answer, index) is True:
            # print(f"CORRECT!")
            display = "CORRECT: Next Question..."
            init_question(display)
        else:
            display = f"WRONG: The correct answer is: {get_answer_from_index(index)}"
            # print(f"WRONG: \n The correct answer is:", load_answer_from_index(index))
            init_same_question(index, display)
    

    def init_question(display):
        cls()
        ## Print a display message
        print(display)

        ## get random index and the index's question
        index, question = get_random_index_and_question()
        ## print and prompt question
        print(question, end= "")
        answer = prompt_input()
        ## check answer and control if next question or same question is displayed
        should_next_or_same_question(index, answer)


  
    def init_same_question(index, display):
        cls()
        ## print a display message
        print(display)

        ## print a question from a specific index
        print(get_question_from_index(index), end = "")
        ## prompt for answer
        answer = prompt_input()
        ## check answer and control if next question or same question is displayed
        should_next_or_same_question(index,answer)


    """
    #########################################
        INIT FIRST QUESTION
    #########################################
    """

    init_question(display = "")

"""
#########################################
    INIT START OF PROGRAM AND MAIN MENU
#########################################
"""

main_menu()