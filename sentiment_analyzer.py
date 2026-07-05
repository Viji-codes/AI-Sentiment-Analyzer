# AI Sentiment Analyzer
# By Vijaya Lakshmi

from textblob import TextBlob

def analyze_sentiment(text):
    # Create TextBlob object
    blob = TextBlob(text)
    
    # Get polarity score
    polarity = blob.sentiment.polarity
    
    # Determine sentiment
    if polarity > 0:
        sentiment = "POSITIVE 😊"
    elif polarity < 0:
        sentiment = "NEGATIVE 😞"
    else:
        sentiment = "NEUTRAL 😐"
    
    return polarity, sentiment

def main():
    print("=" * 50)
    print("   AI SENTIMENT ANALYZER")
    print("   By Vijaya Lakshmi")
    print("=" * 50)
    print()
    
    # Sample texts to analyze
    texts = [
        "I love studying Data Science and AI!",
        "This is terrible and very disappointing.",
        "Today is an ordinary day.",
        "Python programming is amazing and fun!",
        "I hate when things go wrong.",
        "The weather is okay today."
    ]
    
    print("Analyzing Sample Texts:")
    print("-" * 50)
    
    for text in texts:
        polarity, sentiment = analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
        print(f"Score: {polarity:.2f}")
        print("-" * 50)
    
    # Interactive mode
    print("\nNow try your own text!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_text = input("Enter text to analyze: ")
        if user_text.lower() == 'quit':
            print("Thank you for using AI Sentiment Analyzer!")
            break
        polarity, sentiment = analyze_sentiment(user_text)
        print(f"Sentiment: {sentiment}")
        print(f"Score: {polarity:.2f}")
        print("-" * 50)

if __name__ == "__main__":
    main()