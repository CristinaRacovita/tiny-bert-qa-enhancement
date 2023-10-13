import json
from tagging_methods import NERTaggingMethod, POSTaggingMethod


def store_taggings():
    # Open the input JSON file for reading
    input_file_path = "./data/squad_data_train.json"
    data = []

    with open(input_file_path) as f:
        for line in f:
            data.append(json.loads(line))

    # POS and NER Tagging Methods
    pos_method = POSTaggingMethod()
    ner_method = NERTaggingMethod()

    # Iterate through each object in the JSON data and add the 'Test' property
    for obj in data:
        obj["POS_question"] = pos_method.get_pos(obj["question"])
        obj["POS_context"] = pos_method.get_pos(obj["context"])

        obj["NER_question"] = ner_method.get_ner_over_percent(obj["question"], 0.0)
        obj["NER_context"] = ner_method.get_ner_over_percent(obj["context"], 0.0)

    # Open a new JSON file for writing
    output_file_path = "data/output.json"
    with open(output_file_path, "w") as output_file:
        for data_line in data:
            output_file.write(json.dumps(data_line) + "\n")

    print(f"Data with 'Test' property added has been saved to {output_file_path}")


if __name__ == "__main__":
    store_taggings()
