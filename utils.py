import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from langdetect import detect
import nltk

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')


class clean_text:
    """
    Class for preprocessing and cleaning raw text input.
    Includes punctuation removal, lowercasing, number removal,
    stopword removal, lemmatization, and language detection.
    """

    def __init__(self):
        """
        Initialize the cleaner with a text input.
        
        Parameters:
        text (str): Raw input text to be cleaned.
        """
        pass

    def __call__(self):
        """Print the current text stored in the object."""
        print(f"this is your text input : {self.__text}")

    def remove_punctuation(self, text):
        """Remove punctuation characters from text."""
        return ''.join(char for char in text if char not in string.punctuation)

    def lowering(self, text):
        """Convert text to lowercase."""
        return text.lower()

    def review_language(self):
        """Detect the language of the text."""
        return detect(self.__text)

    def replace_number_with_space(self, text):
        """Replace digits with a space and collapse multiple spaces."""
        tmptext = re.sub(r'\d+', ' ', text)
        tmptext = re.sub(r'\s+', ' ', tmptext)
        return tmptext.strip()

    def lemmatizing(self, text):
        """Lemmatize each word in the text."""
        lemma = WordNetLemmatizer()
        return " ".join(lemma.lemmatize(word) for word in text.split())

    def remove_stopwords(self, text):
        """Remove common English stopwords from text."""
        lst_stopwords = set(stopwords.words('english'))
        return " ".join(word for word in text.split() if word not in lst_stopwords)

    def cleaning(self, text):
        """
        Apply all cleaning steps in sequence and return cleaned text.
        Steps:
        1. Lowercase
        2. Remove punctuation
        3. Replace numbers
        4. Remove stopwords
        5. Lemmatize
        """
        text = self.lowering(text)
        text = self.remove_punctuation(text)
        text = self.replace_number_with_space(text)
        text = self.remove_stopwords(text)
        text = self.lemmatizing(text)
        return text


    
if __name__ == '__main__':
    text = (" he is my brothers  hello! 123My name 123 1 is 12G4h Bang. How13 are231 you? There are a lot of horses")
    cleaner = clean_text()
    print(cleaner.cleaning(text))
