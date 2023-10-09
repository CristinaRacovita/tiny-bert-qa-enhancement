from datasets import load_dataset


class DataLoader:
    def __init__(self, directory="../data/"):
        self.directory = directory

    def store_data(self):
        # download and chache data
        squad_data = load_dataset("squad")
        squad_data.cache_files

        # store a json for train and validation data
        for split, dataset in squad_data.items():
            dataset.to_json(f"{self.directory}squad_data_{split}.json")
        print(f"The dataset is stored at {self.directory}")

    def load_data(self):
        # load the train and validation datasets
        data_files = {
            "train": f"{self.directory}squad_data_train.json",
            "validation": f"{self.directory}squad_data_validation.json",
        }

        data = load_dataset("json", data_files=data_files)

        return data


if __name__ == "__main__":
    data_loader = DataLoader()
    data_loader.store_data()
