import unittest
from src import pigLatin

class TestPigLatinMethods(unittest.TestCase):


    # Tests for piglatin.split_words()

    def test_split_words_empty_string_returns_list_with_empty_string(self):
        self.assertEqual(
            [''],
            pigLatin.split_words(''),
            'Warning: Calling split_words() on an empty string should return a list with an empty string.'
        )

    def test_split_words_without_space_returns_list_with_word(self):
        sentence_without_spaces = 'aiaiaiaiaiaiaiaiai'
        self.assertEqual(
            [sentence_without_spaces],
            pigLatin.split_words(sentence_without_spaces),
            'Warning: Calling split_words() on a string with no spaces should return a list with one member: the original string.'
        )



    # Tests for piglatin.trim_punctuation()

    def test_trim_punctuation(self):
        test_words = [
            ('Hello!', 'Hello'),
            ("'Test", 'Test')
        ]

        for (word, trimmed_word) in test_words:
            test_trimmed_word = pigLatin.trim_punctuation(word)
            self.assertEqual(
                trimmed_word,
                test_trimmed_word,
                """
                Warning: Calling trim_punctuation() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, trimmed_word, test_trimmed_word)
            )

    def test_trim_punctuation_preserves_contractions(self):
        test_contractions = [
            "ain't",
            "shouldn't"
        ]

        for contraction in test_contractions:
            test_trimmed_word = pigLatin.trim_punctuation(contraction)
            self.assertEqual(
                contraction,
                test_trimmed_word,
                """
                Warning: Calling trim_punctuation() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (contraction, contraction, test_trimmed_word)
            )


    # Tests for piglatin.fix_title_case()

    def test_fix_title_case_matches_title_case(self):
        test_words = [
            ('icariousVay', 'Vicarious', 'Icariousvay'),
            ("ou'reYay", "You're", "Ou'reyay")
        ]
        for (word, match_word, capitalization) in test_words:
            test_capitalization = pigLatin.fix_title_case(word, match_word)
            self.assertEqual(
                capitalization,
                test_capitalization,
                """
                Warning: Calling fix_title_case() on (%s, %s) returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, match_word, capitalization, test_capitalization)
            )


    # Tests for piglatin.convert_word()

    def test_convert_word_works_with_default_examples(self):
        default_examples = [
            ('pig', 'igpay'),
            ('banana', 'ananabay'),
            ('trash', 'ashtray'),
            ('happy', 'appyhay'),
            ('duck', 'uckday'),
            ('glove', 'oveglay'),
            ('eat', 'eatyay'),
            ('omelet', 'omeletyay'),
            ('are', 'areyay')
        ]

        for (word, translation) in default_examples:
            test_translation = pigLatin.convert_word(word)
            self.assertEqual(
                translation,
                test_translation,
                """
                Warning: Calling convert_word() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, translation, test_translation)
            )

    def test_convert_word_works_with_contractions(self):
        contractions = [
            ("ain't", "ain'tyay"),
            ("shouldn't", "ouldn'tshay")
        ]

        for (word, translation) in contractions:
            test_translation = pigLatin.convert_word(word)
            self.assertEqual(
                translation,
                test_translation,
                """
                Warning: Calling convert_word() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, translation, test_translation)
            )


    # Tests for piglatin.to_pig_latin()

    def test_to_pig_latin(self):
        sentences = [
            ("We are building a unified algorithmic architecture to achieve human-level intelligence in vision, language, and motor control.", "Eway areyay uildingbay ayay unifiedyay algorithmicyay architectureyay otay achieveyay uman-levelhay intelligenceyay inyay isionvay, anguagelay, andyay otormay ontrolcay."),
            ("A.I. - you mean Artificial Intelligence?", "A.Iyay. - ouyay eanmay Artificialyay Intelligenceyay?")
        ]

        for (text, translation) in sentences:
            test_translation = pigLatin.to_pig_latin(text)
            self.assertEqual(
                translation,
                test_translation,
                """
                Warning: Calling to_pig_latin() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (text, translation, test_translation)
            )

if __name__ == '__main__':
    unittest.main()