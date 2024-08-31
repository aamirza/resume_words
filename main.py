"""
This script will receive a folder name or a single text file. This folder/file will contain job postings in .txt format.
The script will go through the text and grab a word count to determine the most common words used in the postings.
"""

from rake_nltk import Rake
import nltk

nltk.download("stopwords")
nltk.download("punkt_tab")

POSTING_TEXT_FILE = "job_postings.txt"


def get_text_from_file(file_path: str) -> str:
    """
    This function will read the text from a file and return it as a string.

    :param file_path (str): The path to the file to read.

    :return (str): The text from the file.
    """
    with open(file_path, "r") as file:
        return file.read()


def main() -> None:
    """
    This serves as the main entry point for the script.
    """
    r = Rake()
    # You'll import the text here
    text = get_text_from_file(POSTING_TEXT_FILE)
    r.extract_keywords_from_text(text)
    print(r.get_ranked_phrases_with_scores())


if __name__ == "__main__":
    main()
