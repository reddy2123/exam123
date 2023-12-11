import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
f = open("C:\\Users\\reddy\\Desktop\\da.txt")
text = f.read()

# Convert text to lowercase
text = text.lower()

# Remove non-alphanumeric characters and extra whitespaces
text = re.sub('[^A-Za-z0-9]+', ' ', text)
text = re.sub("\S*\d\S*", "", text).strip()

print(text)
w = word_tokenize(text, preserve_line=True)
ps = PorterStemmer()
ps_st = [ps.stem(a) for a in w]
print("\nStemming:\n\n", ps_st)

# Apply lemmatization using WordNetLemmatizer
wnl = WordNetLemmatizer()
lema = [wnl.lemmatize(i) for i in w]
print("\nLemmatization:\n\n", lema