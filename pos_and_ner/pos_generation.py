from flair.models import SequenceTagger
from flair.data import Sentence

# Load a pretrained POS tagging model from Flair (e.g., English POS)
tagger = SequenceTagger.load("pos")
TEST_SENTENCE = "The United States of America, also known as the USA, is a country in North America."


def get_pos(sentence_text):
    # Create a Flair Sentence object
    sentence = Sentence(sentence_text)

    # Run POS tagging on the sentence
    tagger.predict(sentence)

    tags = []

    for index, entity in enumerate(sentence):
        tags.append({index: (entity.text, entity.tag)})

    return tags


print(get_pos(TEST_SENTENCE))
