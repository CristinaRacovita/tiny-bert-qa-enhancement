import json
from tagging_methods import NERTaggingMethod, POSTaggingMethod
from tqdm import tqdm


def store_taggings():
    # Open the input JSON file for reading
    input_file_path = "./squad_data_train.json"
    data = []

    with open(input_file_path) as f:
        for line in f:
            data.append(json.loads(line))

    # return data

    pos_method = POSTaggingMethod()
    ner_method = NERTaggingMethod()

    already_read_contexts = dict()

    # Iterate through each object in the JSON data and add the 'Test' property
    for i in tqdm(range(len(data))):
        obj = data[i]
        if obj["context"] not in already_read_contexts.keys():
            obj["NER_context"] = ner_method.get_ner_over_percent(obj["context"], 0.1)
            obj["POS_context"] = pos_method.get_pos(obj["context"])
            already_read_contexts[obj["context"]] = (
                obj["NER_context"],
                obj["POS_context"],
            )
        else:
            obj["NER_context"] = already_read_contexts[obj["context"]][0]
            obj["POS_context"] = already_read_contexts[obj["context"]][1]
            obj["NER_question"] = ner_method.get_ner_over_percent(obj["question"], 0.1)
            obj["POS_question"] = pos_method.get_pos(obj["question"])

    # Open a new JSON file for writing
    output_file_path = "./squad_data_train_pos_ner.json"
    with open(output_file_path, "w") as output_file:
        for data_line in data:
            output_file.write(json.dumps(data_line) + "\n")

    print(f"Data with 'Test' property added has been saved to {output_file_path}")


if __name__ == "__main__":
    store_taggings()
