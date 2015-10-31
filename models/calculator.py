import re

class Calculator(object):
    buy_words = set(('buy', 'long', 'kaufen', 'kauf', 'comprar', 'compra', 'bull', 'bullish'))
    sell_words = set(('sell', 'short', 'verkaufen', 'verkauf', 'vender', 'venta', 'bear', 'bearish'))
    close_words = set(('close', 'closed', 'closing', 'geschlossen', 'cerrado', 'cerrada', 'cerrando'))

    def __init__(self):
        self.buys = 0
        self.sells = 0
        self.volume = 0
        self.score = 0.0

    def add_tweet(self, tweet):
        buy_or_sell = False
        closed = False
        words = set(word.lower() for word in re.findall(r"\w+", tweet.text))
        if words.intersection(self.close_words):
            closed = True
        if words.intersection(self.buy_words):
            if closed:
                self.sells += 1
            else:
                self.buys += 1
            buy_or_sell = True
        if words.intersection(self.sell_words):
            if closed:
                self.buys += 1
            else:
                self.sells += 1
            buy_or_sell = True
        if buy_or_sell:
            self.volume += 1

    def calculate_score(self):
        """ Calculate the score after all tweets have been added """
        if self.buys or self.sells:
            self.score = (self.buys - self.sells) / float(self.buys + self.sells)
