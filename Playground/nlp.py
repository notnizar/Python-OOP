import string
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

nltk.download('stopwords')
nltk.download('wordnet')

text = "This is an example to demonstrate removing stop words."
tokens = word_tokenize(text)
stop_words = stopwords.words('english')

filterd_tokens = [word for word in tokens if word.lower() not in stop_words]

punctuation_tokens = [word for word in filterd_tokens if word not in string.punctuation]
print(punctuation_tokens)

stemmed_tokens = [stemmer.stem(words) for words in punctuation_tokens]

print(stemmed_tokens)

lemmatized_tokens = [lemmatizer.lemmatize(words) for words in punctuation_tokens]

print(lemmatized_tokens)