from unittest import TestCase
import pytest
from joke_bot import JokeBot


class TestJokeBot(TestCase):

    def test_generate_joke(self):
        bot = JokeBot()
        joke_types = ['programming', 'rjokes', 'christmas']
        for joke_type in joke_types:
            bot.joke_type = joke_type
            joke = bot.generate_joke()
            assert isinstance(joke, str), "Joke is not a string."
            assert len(joke) > 5, "Joke is too short"

    def test_rate_the_joke(self):
        bot = JokeBot()
        joke_types = ['programming', 'rjokes', 'christmas']
        for joke_type in joke_types:
            bot.joke_type = joke_type
            joke = bot.generate_joke()
            rating = bot.rate_the_joke(joke)
            assert isinstance(rating, (int, float)), "Rating is not a number."
            assert 0 <= rating <= 10, "Rating is not within the correct range."

