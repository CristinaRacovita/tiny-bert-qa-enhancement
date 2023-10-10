from flair.models import SequenceTagger
from flair.data import Sentence

# Load a pretrained POS tagging model from Flair (e.g., English POS)
tagger = SequenceTagger.load("ner")
TEST_SENTENCE = "The United States of America, also known as the USA, is a country in North America."


def get_ner_over_percent(sentence_text, percent):
    # Create a Flair Sentence object
    sentence = Sentence(sentence_text)

    # Run POS tagging on the sentence
    tagger.predict(sentence, return_probabilities_for_all_classes=True)

    tags = []

    for index, entity in enumerate(sentence):
        test = [
            (entity.text, x.value, x.score)
            for x in entity.tags_proba_dist["ner"]
            if x.score > percent
        ]
        test.sort(key=lambda x: x[2], reverse=True)
        tags.append({index: test})

    return tags


print(get_ner_over_percent(TEST_SENTENCE, 0.1))
