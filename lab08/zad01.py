import nltk
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Załaduj dane z pliku
with open("artykul.txt", "r", encoding="utf-8") as f:
    text = f.read()

# a) Wyświetl długość tekstu
print("Oryginalny tekst:")
print(text[:500])  # wyświetl tylko kawałek
print("")

# b) Tokenizacja
nltk.download('punkt')
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)
print(f"Liczba słów po tokenizacji: {len(tokens)}")

# c) Usuwanie stopwords
nltk.download('stopwords')
tokens = [word.lower() for word in tokens if word.isalpha()]  # usuwanie znaków interpunkcyjnych
filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
print(f"Liczba słów po usunięciu stopwords: {len(filtered_tokens)}")

# d) Usunięcie dodatkowych niepotrzebnych słów (przykład)
extra_stopwords = ['said', 'would']
filtered_tokens = [word for word in filtered_tokens if word not in extra_stopwords]
print(f"Liczba słów po usunięciu dodatkowych stopwords: {len(filtered_tokens)}")

# e) Lematyzacja
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print(f"Liczba słów po lematyzacji: {len(lemmatized)}")

# f) Tworzenie wektora zliczającego słowa
word_freq = Counter(lemmatized)
common_words = word_freq.most_common(10)

# Wykres słupkowy
words, counts = zip(*common_words)
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color="skyblue")
plt.title("Top 10 najczęściej występujących słów")
plt.xlabel("Słowo")
plt.ylabel("Liczba wystąpień")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# g) Chmura tagów
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Chmura tagów")
plt.show()
