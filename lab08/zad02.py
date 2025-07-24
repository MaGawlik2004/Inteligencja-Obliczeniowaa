import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import text2emotion as te

# Upewnij się, że masz wszystkie zasoby
nltk.download('vader_lexicon')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Dwie przykładowe recenzje (możesz je zmienić na własne z booking/tripadvisor)
positive_review = """
The hotel was absolutely amazing! The staff was friendly, the room was clean and spacious, and the breakfast was delicious. 
I would definitely stay here again. One of the best experiences I've had while traveling!
"""

negative_review = """
This hotel was terrible. The room was dirty, the staff was rude and unhelpful. 
It was the worst experience I've ever had. I would never recommend this place to anyone.
"""

# === VADER Sentiment ===
sia = SentimentIntensityAnalyzer()

def analyze_with_vader(text):
    scores = sia.polarity_scores(text)
    print("Tekst:")
    print(text)
    print("\n📊 VADER Sentiment:")
    print(f"Pozytywne (pos): {scores['pos']}")
    print(f"Neutralne  (neu): {scores['neu']}")
    print(f"Negatywne (neg): {scores['neg']}")
    print(f"Compound score  : {scores['compound']}")
    print("-" * 50)

# === Text2Emotion ===
def analyze_with_text2emotion(text):
    emotions = te.get_emotion(text)
    print("😊 Text2Emotion (emocje):")
    for emotion, score in emotions.items():
        print(f"{emotion}: {score}")
    print("=" * 50)

# === Analiza recenzji ===
print("\n🟢 Recenzja pozytywna:")
analyze_with_vader(positive_review)
analyze_with_text2emotion(positive_review)

print("\n🔴 Recenzja negatywna:")
analyze_with_vader(negative_review)
analyze_with_text2emotion(negative_review)
