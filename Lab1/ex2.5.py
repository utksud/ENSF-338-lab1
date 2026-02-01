import json
import timeit

# 1. Define the input path
input_path = r'C:\Users\Utkarsh Sudhir\Downloads\large-file.json'

# 2. Load the file (NOT timed)
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 3. Define normal function
def change_size():
    for record in data:
        if 'size' in record:
            record['size'] = 42

# 4. Time using lambda (10 runs)
total_time = timeit.timeit(
    lambda: change_size(),
    number=10
)

# 5. Average time
avg_time = total_time / 10

# 6. Output
print(f"Total time for 10 runs: {total_time} seconds")
print(f"Average time per run: {avg_time} seconds")
