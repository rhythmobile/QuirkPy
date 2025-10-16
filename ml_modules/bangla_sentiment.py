class BanglaSentimentAnalyzer:
    """
    Analyze sentiment in Bangla chaotic text

    Example:
    >>> analyzer = BanglaSentimentAnalyzer()
    >>> analyzer.predict("আমি খুব খুশি!")
    'positive'
    """

    def __init__(self):
        self.positive_words = ["ভালো", "খুশি", "আনন্দ"]
        self.negative_words = ["খারাপ", "দুঃখ", "ব্যথা"]

    def predict(self, text):
        """
        Predicts the sentiment of a given Bangla text.

        This is a simple rule-based approach that counts positive and
        negative words to determine the overall sentiment.
        """

        positive_score = 0
        negative_score = 0

        words = text.split()

        for word in words:
            if word in self.positive_words:
                positive_score += 1
            elif word in self.negative_words:
                negative_score += 1

        if positive_score > negative_score:
            sentiment = "positive"

        elif positive_score < negative_score:
            sentiment = "negative"

        else:
            sentiment = "neutral"

        return sentiment