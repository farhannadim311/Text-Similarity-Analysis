# Text Similarity Analysis

## Project Overview
This project aims to compare the similarity between two texts by analyzing different kinds of word statistics, including term frequency (TF), inverse document frequency (IDF), and TF-IDF scores. It demonstrates various text processing and statistical analysis techniques in Python.

## Key Features
- **Text Preprocessing**:
  - `load_file`: Reads and cleans text data from files, removing punctuation and converting text to lowercase.
  - `text_to_list`: Splits text into a list of words.
  - `load_files_from_directory`: Loads and cleans text data from all files in a specified directory.
- **Frequency Analysis**:
  - `get_frequencies`: Calculates the frequency of words or letters in a given text.
  - `get_letter_frequencies`: Determines the frequency of each letter in a word.
- **Similarity Calculation**:
  - `calculate_similarity_score`: Computes the similarity between two texts based on word frequencies.
  - `get_most_frequent_words`: Identifies the most frequent words across two texts.
- **TF-IDF Calculation**:
  - `get_tf`: Computes the term frequency (TF) of words in a document.
  - `get_idf`: Calculates the inverse document frequency (IDF) of words across multiple documents.
  - `get_tfidf`: Computes the TF-IDF score for words in a document, combining both TF and IDF values.
- **Data Visualization**:
  - `plot_word_frequencies`: Visualizes word frequencies using a bar chart.
  - `plot_tfidf`: Visualizes TF-IDF scores using a bar chart.

## How to Use
1. **Preprocess Text**: Load and clean text files using `load_file` and `load_files_from_directory`.
2. **Frequency Analysis**: Use `get_frequencies` and `get_letter_frequencies` to analyze word and letter frequencies.
3. **Calculate Similarity**: Employ `calculate_similarity_score` to determine how similar two texts are.
4. **TF-IDF Scores**: Calculate term frequency using `get_tf`, inverse document frequency using `get_idf`, and combine them using `get_tfidf` to get TF-IDF scores for words in a document.
5. **Visualize Data**: Use `plot_word_frequencies` and `plot_tfidf` to visualize word frequencies and TF-IDF scores.
6. **Add your own File**: Add your own file under the tests folder to find document distances between your own documents!
