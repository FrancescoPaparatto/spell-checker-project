import json
from utils import load_file, create_dictionary


def main():
    # TODO: evaluate to create an helper function also for getting config files in order to handle JsonDecodeError 
    with open("config.json", "r") as file:
        config = json.load(file)

    try:
        english_dictionary = create_dictionary(
            load_file(config["dictionary"]["english_path"])
        )

        business_dictionary = create_dictionary(
            load_file(config["dictionary"]["business_path"])
        )
    except FileNotFoundError as e:
        print(e)

    else:
        dictionary = english_dictionary | business_dictionary


if __name__ == "__main__":
    main()
