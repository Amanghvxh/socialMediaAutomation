import json

def convert_to_object(quotes_list):
    return [{"quote": item[0], "author": item[1], "key": False} for item in quotes_list]

def update_pending_json(new_quotes):
    # Read the existing JSON
    try:
        with open('utils/pending.json', 'r') as file:
            data = json.load(file)
            if "pending_quotes" in data:
                data["pending_quotes"].extend(new_quotes)
            else:
                data["pending_quotes"] = new_quotes
    except FileNotFoundError:
        data = {"pending_quotes": new_quotes}

    # Write the updated JSON back to the file
    with open('utils/pending.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Read the array from the file
    with open('quotes.txt', 'r') as file:
        quotes_array = eval(file.read())
    
    new_quotes = convert_to_object(quotes_array)
    update_pending_json(new_quotes)
