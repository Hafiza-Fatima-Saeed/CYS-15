# Phase 1

Correct_Marks = 4
Wrong_Marks = -1
Skip_Marks = 0 
Max_Attempts = 3

Admin_User = "ecat_admin"
Admin_Password = "ecat@2024"

Student_User = "student"
Student_Password = "student123"


questions = [
    {
        'id':'1',
        'Subject':'Physics',
        'question':'Reverse process of vector addition?',
        'choices':{'A':'Subtraction','B':'Division','C':'Multiplication','D':'None'},
        'Answer':'A'
    }, 
    {
        'id':'2',
        'Subject':'Physics',
        'question':'Rocket propulsion is according to?',
        'choices':{'A':'3rd law of motion','B':'1st','C':'2nd','D':'None'},
        'Answer':'A'
    },
    {
        'id':'3',
        'Subject':'Physics',
        'question':'1Cal= j? ',
        'choices':{'A':'418','B':'400','C':'10','D':'4.18'},
        'Answer':'D' 
    },
    {
        'id':'4',
        'Subject':'Physics',
        'question':'Least distance of distinct vision for human eye is?',
        'choices':{'A':'50','B':'25','C':'30','D':'20'},
        'Answer':'B' 
    },
    {
        'id':'5',
        'Subject':'Chemistry',
        'question':'Which gives +3 charge?',
        'choices':{'A':'Al','B':'Ca','C':'Na','D':'all'},
        'Answer':'A' 
    },
    {
        'id':'6',
        'Subject':'Chemistry',
        'question':'Which is not calcerous material?',
        'choices':{'A':'Clay','B':'Marble','C':'Lime','D':'Marine shell'},
        'Answer':'A'  
    },
    {
         'id':'7',
        'Subject':'Chemistry',
        'question':'Which is universal solvent?',
        'choices':{'A':'water','B':'ether','C':'HCL','D':'none'},
        'Answer':'A'
    },
    {
         'id':'8',
        'Subject':'Chemistry',
        'question':'Which of following is not alkali?',
        'choices':{'A':'Ra','B':'Na','C':'K','D':'all'},
        'Answer':'A'
    },
     {
        'id':'9',
        'Subject':'Math',
        'question':'Anon negative number is group under:',
        'choices':{'A':'adddition','B':'multiplication','C':'subtraction','D':'both A and C'},
        'Answer':'A'  
    },
    {
        'id':'10',
        'Subject':'Math',
        'question':'A set no element is called:',
        'choices':{'A':'empty set','B':'unit set','C':'identity set','D':'none'},
        'Answer':'A'  
    },
    {
        'id':'11',
        'Subject':'Math',
        'question':'The A.M between 1000 and 4 is:',
        'choices':{'A':'502','B':'504','C':'500','D':'602'},
        'Answer':'A'  
    },
    {
        'id':'12',
        'Subject':'Math',
        'question':'A matrix with all entry 0 is called:',
        'choices':{'A':'null matrix','B':'unit matrix','C':'identity matrix','D':'none'},
        'Answer':'A'  
    }

]
all_results = []
#Phase 2
def admin_login():
    print("ADMIN LOGIN")
    tries = 0
    while tries < Max_Attempts:
        username = input("Username:")
        password = input("Password:")
        if username == Admin_User and password == Admin_Password:
            print("Login Successful")
            return True
            
        else:
            tries = tries + 1
            print("Incorrect username or password")
            print("Tries Left:", Max_Attempts - tries)
    print("Account Locked")
    return False

def student_login():
    print("STUDENT LOGIN")
    tries = 0
    while tries < Max_Attempts:
        username = input("Username:")
        password = input("Password:")
        
        if username == Student_User and password == Student_Password:
            name = input("Enter full name:")
            roll_no = int(input("Enter Roll Number:"))
            return name,roll_no
        else:
            tries = tries + 1
            print("Incorrect password or username")
            print("Tries left:", Max_Attempts - tries)
    print("Account Locked")
    return None,None


#Phase 3
import time

def calculate_grade(percentage):
    if percentage >= 80:
        return 'Excellent'
    elif percentage >= 65:
        return 'Good'
    elif percentage >= 50:
        return 'Average'
    else:
        return 'Below Average'

def save_result(name,roll_no,answers):
    correct = 0
    wrong = 0
    skipped = 0
    question_number = 1
    for q in questions:
        correct_answer = q['Answer']
        if question_number-1 < len(answers):
            my_answer = answers[question_number-1]
        else:
            my_answer = 'S'
        if my_answer == 'S':
            skipped = skipped + 1
        elif my_answer == correct_answer:
            correct = correct + 1
        else:
            wrong = wrong + 1
        question_number = question_number + 1
    total_questions = len(questions)
    total_score = (correct*4) + (wrong*-1)
    Max_score = total_questions*4
    if Max_score > 0:
        percentage = (total_score/Max_score) * 100
    else:
        percentage = 0
    percentage = round(percentage,2)
    grade = calculate_grade(percentage)
    result= {
        'name':name,
        'roll_no':roll_no,
        'correct answers':correct,
        'wrong answers':wrong,
        'skipped questions':skipped,
        'percentage':percentage,
        'grade':grade,
        'score':total_score,
        'max_score':Max_score
    
    }
    all_results.append(result)
    print("Result saved!")


def run_exam(name,roll_no):
    answers = []
    question_number = 1
    start_time = time.time()
    for q in questions:
        print("\nQuestion:",question_number)
        print("Subject:",q['Subject'])
        print("Question:",q['question'])
        print("A.",q['choices']['A'])
        print("B.",q['choices']['B'])
        print("C.",q['choices']['C'])
        print("D.",q['choices']['D'])
        answer = input("Type A,B,C,D or S to skip:")
        answer = answer.upper()
        if answer == "Submit":
                 break
        answers.append(answer)
        question_number = question_number + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print("Exam Done!")
    print("Your Answers:",answers)
    print("Total Time:",int(time_taken),"seconds")
    save_result(name,roll_no,answers)
    


#Phase 4

def admin_view_all_questions():
    if len(questions) == 0:
        print("No questions yet.")
        return
    num = 1
    for q in questions:
        print("")
        print(num,".Subject:",q['Subject'])
        print("Question:",q['question'])
        print("A.",q['choices']['A'])
        print("B.",q['choices']['B'])
        print("C.",q['choices']['C'])
        print("D.",q['choices']['D'])
        print("Correct Answer:",q['Answer'])
        print('---')
        num = num + 1

def admin_add_question():
    subject = input("Enter subject:")
    question = input("Enter question:")
    a = input("Option A:")
    b = input("Option B:")
    c = input("Option C:")
    d = input("Option D:")
    answer = input("Type correct option A/B/C/D:")
    new_question= {
        'Subject':subject,
        'question':question,
        'choices':{'A':a,'B':b,'C':c,'D':d},
        'Answer':answer.upper()
    }
    questions.append(new_question)
    print("Question added successfully.")

def admin_delete_question():
    if len(questions) == 0:
        print("No questions to be deleted.")
        return
    num = int(input("Enter question number to be deleted:"))
    questions.pop(num - 1)
    print("Deleted!")

def admin_question_stats():

    if len(questions) == 0:
        print("No questions yet.")
        return
    print("Total Questions:",len(questions))
    Math = 0
    Chemistry = 0
    Physics = 0
    for q in questions:
        if q['Subject'] =='Math':
            Math = Math + 1
        elif q['Subject'] == 'Chemistry':
            Chemistry = Chemistry + 1
        elif q['Subject'] == 'Physics':
            Physics = Physics + 1
    print("Physics:",Physics)
    print("Chemistry:",Chemistry)
    print("Maths:",Math)
def admin_view_all_result():
    if len(all_results) == 0:
        print("No results yet.")
        return
    num = 1
    print("Name|Roll|Score|%|Grade")
    for r in all_results:
        print(num,".",r['name'],"|",r['roll_no'],"|",r['score'],"|",r['percentage'],"%|",r['grade'])
        num = num + 1

def admin_view_detailed_result():
    if len(all_results) == 0:
        print("No results yet.")
        return
    
    num = 1
    for r in all_results:
        print(num,".",r['name'],"-",r['roll_no'])
        num = num + 1
    choice = input("Enter student number:")
    choice = int(choice)
    if choice>=1 and choice<=len(all_results):
       student = all_results[choice - 1]
       print("\nDetailed result for:",student['name'])
       print("Roll no:",student['roll_no'])
       print("Score:",student['score'],"/",student['total'])
       print("Percentage:",student['percentage'],"%")
       print("Grade:",student['grade'])
       print("Time taken:",student['time_taken'],"seconds")
    else:
        print("Incorrect number")

def admin_class_stat():
    if len(all_results) == 0:
        print("No results yet.")
        return
    highest = all_results[0]['score']
    lowest = all_results[0]['score']
    passed = 0
    total = 0
    for r in all_results:
        score = r['score']
        if highest > score:
            highest = score
        if lowest < score:
            lowest = score
        total = total + score
        if r['percentage'] >= 50:
            passed = passed + 1
    average = total/len(all_results)
    failed = len(all_results) - passed
    print("Highest Score:",highest)
    print("Lowest Score:",lowest)
    print("Average Score:",average)
    print("Passed:",passed)
    print("Failed:",failed)

def logout():
    while True:
        print("\n ADMIN MENU")
        print("1. Show all questions")
        print("2. Add new question")
        print("3. Delete question")
        print("4. Question stats")
        print("5. Show all result")
        print("6. Show one student")
        print("7. Class stats")
        print("8.Logout")
        choice = input("Enter 1-8:")
        if choice == '1':
            admin_view_all_questions()
        elif choice == '2':
            admin_add_question()
        elif choice == '3':
            admin_delete_question()
        elif choice == '4':
            admin_question_stats()
        elif choice == '5':
            admin_view_all_result()
        elif choice == '6':
            admin_view_detailed_result()
        elif choice == '7':
            admin_class_stat()
        elif choice == '8':
            print("Logged out")
            break
        else:
            print("Type something between 1 to 8 only.")


#Phase 5
def admin_portal():
    admin_login()
    if admin_login == False:
        return
    
    while True:
        print("\nADMIN PORTAL")
        print("\n ADMIN MENU")
        print("1. Show all questions")
        print("2. Add new question")
        print("3. Delete question")
        print("4. Question stats")
        print("5. Show all result")
        print("6. Show one student")
        print("7. Class stats")
        print("8.Logout")
        choice = input("Select Option:")
        if choice == '1':
            admin_view_all_questions()
        elif choice == '2':
            admin_add_question()
        elif choice == '3':
            admin_delete_question()
        elif choice == '4':
            admin_question_stats()
        elif choice == '5':
            admin_view_all_result()
        elif choice == '6':
            admin_view_detailed_result()
        elif choice == '7':
            admin_class_stat()
        elif choice == '8':
            break
        else:
            print("Incorrect Option!")

def student_portal():
    name,roll_no = student_login()
    if name == "":
        return
    while True:
        print("\nSTUDENT PORTAL")
        print("1. View Exam Rules")
        print("2. Start Exam")
        print("3.Logout")

        choice = input("Select Option:")
        if choice == '1':
            print("Correct: +4| Wrong: -1| Skipped: 0")
            print("Computer will shut down when time is completed.")
            print("Student can leave after finishing half of exam. ")
            print("Student must read all options before marking answer.")
            print("Type Submit to end exam.")
        elif choice == '2':
            run_exam(name,roll_no)
        elif choice == '3':
            break
        else:
            print("Invalid Option")

def main_menu():
    print("Welcome to the ECAT Exam")
    print("1.Admin Portal")
    print("2.Student Portal")
    print("3.Exit")
    ch = input("Select Portal:")

    if ch == '1':
        admin_portal()
    elif ch == '2':
        student_portal()
    elif ch == '3':
        print("Exit")
           
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main_menu()

