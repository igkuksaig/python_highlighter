"""Test module
file: test_highlighter.py
date: 12.12.2012
author smith@example.com
license: MIT"""

import unittest
from highlighter import create_app


class HighlightTest(unittest.TestCase):
    """Test class for flask app."""

    def setUp(self):
        """This method is called each time the test routine run"""
        self.app = create_app().test_client()

        self.search_text = 'text'
        self.text = 'Sample text to be highlighted text'
        self.highlighted_text = b'Sample <mark>text</mark> to be highlighted <mark>text</mark>'

    def tearDown(self):
        """This method is called after the test routine is finished
        to clear out the data created in setUp method."""
        self.search_text = ""
        self.text = ""
        self.highlighted_text = ""

    def test_markup_text(self):
        """Test markup process"""
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text})
        self.assertIn(self.highlighted_text, response.data)
