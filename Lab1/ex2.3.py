import json

# 1. Define the paths
input_path = r'C:\Users\Utkarsh Sudhir\Downloads\large-file.json'
output_path = 'output.2.3.json'

# 2. Load the file
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

    # Change the 'size' field in every record to 42
    for record in data:
        if 'size' in record:
            record['size'] = 42

    # Reverse the order of the list
    data.reverse()

    # Write back the result to output.2.3.json
    with open(output_path, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out)

print("Done")
