import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

# 1. Load data
with open(r'C:\Users\Utkarsh Sudhir\Desktop\sem4\338\Lab1\internetdata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Processing function (remains the same)
def process_records(records):
    processed = []
    for record in records:
        new_record = record.copy()
        if 'internetuserate' in record and record['internetuserate'] is not None:
            new_record['internet_usage_normalized'] = record['internetuserate'] / 100
        if 'incomeperperson' in record and record['incomeperperson'] is not None:
            new_record['income_log'] = np.log(record['incomeperperson']) if record['incomeperperson'] > 0 else 0
        processed.append(new_record)
    return processed

# 3. Setup for timing
# Get the first 1000 records
records_to_process = data[:1000] if len(data) >= 1000 else (data * (1000 // len(data) + 1))[:1000]

# Use timeit.repeat
# number=1 means we time one execution of the function per 'repeat'
# repeat=1000 means we get 1000 total measurements
measured_times = timeit.repeat(
    stmt='process_records(records_to_process)',
    globals=globals(),
    repeat=1000,
    number=1
)

# 4. Plotting the Histogram
plt.figure(figsize=(10, 6))
plt.hist(measured_times, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.title("Distribution of Processing Times (1000 Records)")
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and Show
plt.tight_layout()
plt.savefig("output.3.3.png", dpi=300)
plt.show()

print(f"Min time: {min(measured_times):.6f}s")
print(f"Max time: {max(measured_times):.6f}s")
