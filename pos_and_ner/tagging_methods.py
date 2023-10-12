from flair.models import SequenceTagger
from flair.data import Sentence


class TaggingMethod:
    def __init__(self, method_type) -> None:
        self.tagger = SequenceTagger.load(method_type)

    @property
    def tagger(self) -> SequenceTagger:
        return self.tagger


class NERTaggingMethod(TaggingMethod):
    def __init__(self) -> None:
        super().__init__("ner")

    def get_ner_over_percent(self, sentence_text, percent):
        # Create a Flair Sentence object
        sentence = Sentence(sentence_text)

        # Run NER tagging on the sentence
        super().tagger.predict(sentence, return_probabilities_for_all_classes=True)

        tags = []

        for index, entity in enumerate(sentence):
            entity_tags = [
                (entity.text, x.value, x.score)
                for x in entity.tags_proba_dist["ner"]
                if x.score > percent and x.value != "O"
            ]
            entity_tags.sort(key=lambda x: x[2], reverse=True)
            if len(entity_tags) > 0:
                tags.append({index: entity_tags})

        return tags


class POSTaggingMethod(TaggingMethod):
    def __init__(self) -> None:
        super().__init__("pos")

    def get_pos(self, sentence_text):
        # Create a Flair Sentence object
        sentence = Sentence(sentence_text)

        # Run POS tagging on the sentence
        super().tagger.predict(sentence)

        tags = []

        for index, entity in enumerate(sentence):
            tags.append({index: (entity.text, entity.tag)})

        return tags
