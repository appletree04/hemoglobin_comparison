import json

with open("../data/processed_data/data.json", "r") as f:
    data = json.load(f)

    folders = ["alpha1", "alpha2"] + list(
        set(
            data[x]["organism"] for x in data
        )
    )

    print(folders)