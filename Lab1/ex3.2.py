import json
import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

try:
    with open('internetdata.json', 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} records from internetdata.json")
except FileNotFoundError:
    print("ERROR: internetdata.json not found!")
    exit(1)

def process_records(records_to_process):
    processed_data = []
    for record in records_to_process:
        processed_record = {}

        if 'internetuserate' in record and record['internetuserate'] is not None:
            processed_record['internet_usage_normalized'] = record['internetuserate'] / 100.0

        if 'incomeperperson' in record and record['incomeperperson'] is not None:
            processed_record['income_category'] = (
                'high' if record['incomeperperson'] >= 10000 else 'low'
            )
            processed_record['income_log'] = (
                np.log(record['incomeperperson']) if record['incomeperperson'] > 0 else 0
            )

        for key, value in record.items():
            if key not in processed_record:
                processed_record[key] = value

        processed_data.append(processed_record)

    return processed_data

def time_processing_n_records(n_records, repetitions=100):
    subset = data[:n_records]

    def process_wrapper():
        return process_records(subset)

    execution_time = timeit.timeit(
        'process_wrapper()',
        setup='from __main__ import process_wrapper',
        number=repetitions
    )

    average_time = execution_time / repetitions
    return average_time, execution_time

record_counts = [1000, 2000, 5000, 10000]
repetitions = 100

average_times = []
total_times = []

for n in record_counts:
    if n > len(data):
        continue
    avg, total = time_processing_n_records(n, repetitions)
    average_times.append(avg)
    total_times.append(total)

x = np.array(record_counts)
y = np.array(average_times)

slope, intercept, r_value, _, std_err = stats.linregress(x, y)
regression_line = intercept + slope * x

plt.figure(figsize=(12, 8))
plt.scatter(x, y, s=100, label='Actual Measurements')
plt.plot(x, regression_line, linewidth=2.5,
         label=f'y = {intercept:.6f} + {slope:.6e}x')
plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time (seconds)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output.3.2.png', dpi=300)
plt.show()
