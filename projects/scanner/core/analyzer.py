import difflib


class ResponseAnalyzer:

    @staticmethod
    def similarity(a, b):
        return difflib.SequenceMatcher(None, a, b).ratio()

    @staticmethod
    def is_different(baseline, attack):
        ratio = ResponseAnalyzer.similarity(baseline, attack)
        return ratio < 0.95  # якщо сильно відрізняється

    @staticmethod
    def contains_keywords(text, keywords):
        return any(k.lower() in text.lower() for k in keywords)