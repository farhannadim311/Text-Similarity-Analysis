import string
import math
from collections import Counter, defaultdict
import os
import matplotlib.pyplot as plt

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

def load_files_from_directory(directory):
    """
    Args:
        directory: string, path to the directory containing text files
    Returns:
        list of strings, each containing the content of a file in the directory
    """
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            texts.append(load_file(file_path))
    return texts

def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()

def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    """
    return dict(Counter(input_iterable))

def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return dict(Counter(word))

def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    all_keys = set(freq_dict1.keys()).union(set(freq_dict2.keys()))
    freq_diff = 0
    total_freq = 0
    for key in all_keys:
        freq1 = freq_dict1.get(key, 0)
        freq2 = freq_dict2.get(key, 0)
        freq_diff += abs(freq1 - freq2)
        total_freq += freq1 + freq2
    if total_freq == 0:  # to handle the case where both dictionaries are empty
        return 1.0
    similarity_score = 1 - (freq_diff / total_freq)
    return round(similarity_score, 2)

def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          frequencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    combined_freq = defaultdict(int)
    for word, freq in freq_dict1.items():
        combined_freq[word] += freq
    for word, freq in freq_dict2.items():
        combined_freq[word] += freq
    max_freq = max(combined_freq.values())
    most_frequent_words = [word for word, freq in combined_freq.items() if freq == max_freq]
    return sorted(most_frequent_words)

def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculated as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    file = load_file(file_path)
    text = text_to_list(file)
    my_dict = get_frequencies(text)
    total_words = sum(my_dict.values())
    my_dict = {word: freq / total_words for word, freq in my_dict.items()}
    return my_dict

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    word_document_count = defaultdict(int)
    document_num = len(file_paths)
    for file_path in file_paths:
        text = text_to_list(load_file(file_path))
        unique_words_in_doc = set(text)
        for word in unique_words_in_doc:
            word_document_count[word] += 1
    idf_dict = {word: math.log10(document_num / count) for word, count in word_document_count.items()}
    return idf_dict

def get_tfidf(tf_file_path, idf_file_paths):
    """
    Args:
        tf_file_path: name of file in the form of a string (used to calculate TF)
        idf_file_paths: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    tfidf = [(word, tf[word] * idf[word]) for word in tf if word in idf]
    tfidf.sort(key=lambda x: (x[1], x[0]))
    return tfidf

def plot_word_frequencies(freq_dict, title):
    """
    Args:
        freq_dict: dictionary mapping words to their frequencies
        title: string, title of the plot
    """
    words = list(freq_dict.keys())
    frequencies = list(freq_dict.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()

def plot_tfidf(tfidf_list, title):
    """
    Args:
        tfidf_list: list of tuples (word, TF-IDF score)
        title: string, title of the plot
    """
    words, scores = zip(*tfidf_list)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, scores, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('TF-IDF Scores')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    # Example usage:
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']

    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)

    print("TF:", tf)
    print("IDF:", idf)
    print("TF-IDF:", tf_idf)

    # Plot word frequencies
    plot_word_frequencies(tf, "Term Frequencies")

    # Plot TF-IDF scores
    plot_tfidf(tf_idf, "TF-IDF Scores")
