# multiplication_quiz.py - Recreation of multiplication_quiz.py without pyinputplus.
import random
import time

def multiplication_quiz():
    """Creates and runs multiplication quiz at run time."""
    num_questions = 10  # Number of questions; can be changed
    correct = 0  # Correct number of questions
    # Loop through each question.
    for question_number in range(1, num_questions+1):
        a = random.randint(0, 9)  # Number 1
        b = random.randint(0, 9)  # Number 2
        # Multiplication question to solve
        prompt = '#%s: %s X %s = ' % (question_number, a, b)
        # retry limit
        retry_limit = 3
        # boolean to detect correct answer
        correct_answer = False
        # start timer
        start_time = time.perf_counter()
        # variable for run time of question
        run_time = 0
        # Loops over question until out of retries.
        while retry_limit != 0:
            # Prompts user for valid answer
            while True:
                print(prompt)
                try:
                    user_answer = int(input('> '))
                    break
                except ValueError:
                    print('Please input a number.')
            # If user answers correctly
            if user_answer == (a * b):
                correct_answer = True
                # Checks run time
                end_time = time.perf_counter()
                run_time = end_time - start_time
                break
            # Checks run time
            end_time = time.perf_counter()
            run_time = end_time - start_time
            # If time exceeded
            if run_time >= 8:
                break
            # If answer is incorrect
            retry_limit -= 1
            print('Incorrect!')
        # If answer is correct but time exceeded
        if run_time >= 8:
            print('Out of time!')
        # If answer is correct and time is not exceeded
        elif correct_answer:
            print('Correct!')
            correct += 1
        # Waits to print next question
        time.sleep(1)
    # Prints out number correct out of total questions.
    print('Score: %s/%s correct!' % (correct, num_questions))


def main():
    """Main method to check if multiplication_quiz() method works."""
    multiplication_quiz()

# If program is run (and not imported), calls main() method.
if __name__ == '__main__':
    main()
