# mad_libs.py - A program to read in a Mad Libs template file and output a Mad Libs result file.
"""A program to play with Mad Libs and just have fun!"""
from pathlib import Path

def main():
    """Program to play with Mad Libs."""
    # Checks if the Mad Libs template exists in the same folder as this program.
    # If file does not exist, user is asked to enter another file name.
    while True:
        file_name = input('Enter file name for Mad Libs template: ')
        file_path = Path(Path.cwd(), file_name + '.txt')
        if file_path.is_file():
            print('Opening file...')
            madlib_template = open(file_path, 'r')
            break
        else:
            print('File not located. Please try again.')

    # Checks if a file with this name already exists in this folder.
    # If it exists, user is asked to enter a different file name.
    while True:
        output_file_name = input('Enter file name for Mad Libs results: ')
        output_file_path = Path(Path.cwd(), output_file_name + '.txt')
        if not output_file_path.is_file():
            madlib_output = open(output_file_path, 'w')
            break
        else:
            print('File name already exists. Please try again.')

    print('Reading file...')  # updates user visually
    # Read contents of template file.
    madlib_content = madlib_template.readlines()
    # List to store mad lib[sentence][word]
    madlib_sentences = []
    for string in madlib_content:
        madlib_sentences.append(string.split(' '))

    # Loops through list to find keywords (ADJECTIVE, NOUN, VERB, ADVERB) and replace them with user input.
    for i in range(len(madlib_sentences)):  # Loops through sentences.
        for word in madlib_sentences[i]:  # Loops through words in each sentence.
            if word == 'ADJECTIVE' or word == 'NOUN' or word == 'VERB' or word == 'ADVERB':
                if word == 'NOUN' or word == 'VERB':
                    prompt = 'Enter a {}:\n'
                else:
                    prompt = 'Enter an {}:\n'
                user_input = input(prompt.format(word.lower()))
                word_index = madlib_sentences[i].index(word)
                madlib_sentences[i][word_index] = user_input.upper()

    # List to store madlib results
    madlib_results = []
    # Loops through each sentence string and joins them back together
    for i in range(len(madlib_sentences)):
        madlib_results.append(' '.join(madlib_sentences[i]))
    # Outputs each sentence to terminal and writes them to the output file.
    for sentence in madlib_results:
        print(sentence)
        madlib_output.write(sentence)

    # Closes files.
    madlib_template.close()
    madlib_output.close()


if __name__ == "__main__":
    main()
