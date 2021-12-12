import re
import matplotlib.pyplot as plt


def find_and_write_ftps_to_file():
    with open('references') as input_file, open('ftps', 'w') as output_file:
        pattern = r'\bftp\.[^\s,;]+'
        text = input_file.read()
        result = '\n'.join(re.findall(pattern, text))
        output_file.write(result)


def find_all_numbers():
    with open('2430AD') as input_file, open('numbers', 'w') as output_file:
        pattern = r'[-+]?\d*\.\d+|\d+'
        text = input_file.read()
        result = '\n'.join(re.findall(pattern, text))
        output_file.write(result)


def find_all_words_with_a():
    with open('2430AD') as input_file, open('words_with_a', 'w') as output_file:
        pattern = r'\b\w*[Aa]+\w*\b'
        text = input_file.read()
        result = '\n'.join(re.findall(pattern, text))
        output_file.write(result)


def find_all_exclamation_sentences():
    with open('2430AD') as input_file, open('exclamations', 'w') as output_file:
        pattern = r'[A-Z0-9][\w ,;:]+!'
        text = input_file.read()
        result = '\n'.join(re.findall(pattern, text))
        output_file.write(result)


def make_unique_word_length_distribution_plot():
    with open('2430AD') as input_file:
        pattern = r'\b[A-z\']+\b'
        text = input_file.read()
        result = list(sorted(map(len, set(map(str.lower, re.findall(pattern, text))))))
        plt.hist(result, density=True)
        plt.title('Unique words length histogram plot')
        plt.xlabel('Word length')
        plt.ylabel('Proportion count')
        plt.show()


def execute_regexp_finctions():
    find_and_write_ftps_to_file()
    find_all_numbers()
    find_all_words_with_a()
    find_all_exclamation_sentences()
    make_unique_word_length_distribution_plot()


if __name__ == '__main__':
    execute_regexp_finctions()
