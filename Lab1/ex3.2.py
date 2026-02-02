import json
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# --------------------------------------------------
# Load data
# --------------------------------------------------
with open(
    r'C:\Users\Utkarsh Sudhir\Desktop\sem4\338\Lab1\internetdata.json',
    'r',
    encoding='utf-8'
) as f:
    data = json.load(f)

print("Total records loaded:", len(data))

# --------------------------------------------------
# Processing function
# --------------------------------------------------
def process_records(records):
    processed = []
    for record in records:
        new_record = record.copy()

        if 'internetuserate' in record and record['internetuserate'] is not None:
            new_record['internet_usage_normalized'] = record['internetuserate'] / 100

        if 'incomeperperson' in record and record['incomeperperson'] is not None:
            new_record['income_log'] = (
                np.log(record['incomeperperson'])
                if record['incomeperperson'] > 0 else 0
            )

        processed.append(new_record)

    return processed

# --------------------------------------------------
# Helper: expand data to N records
# --------------------------------------------------
def get_n_records(n):
    repeats = (n // len(data)) + 1
    expanded = (data * repeats)[:n]
    return expanded

# --------------------------------------------------
# Timing function
# --------------------------------------------------
def average_time_for_n_records(n, repetitions=100):
    records = get_n_records(n)

    start = time.perf_counter()
    for _ in range(repetitions):
        process_records(records)
    end = time.perf_counter()

    return (end - start) / repetitions

# --------------------------------------------------
# Run experiments
# --------------------------------------------------
record_counts = [1000, 2000, 5000, 10000]
average_times = []

for n in record_counts:
    avg = average_time_for_n_records(n, repetitions=100)
    average_times.append(avg)

x = np.array(record_counts)
y = np.array(average_times)

print("x values:", x)
print("y values:", y)

# --------------------------------------------------
# Linear regression
# --------------------------------------------------
slope, intercept, r_value, _, _ = stats.linregress(x, y)
regression_line = intercept + slope * x

# --------------------------------------------------
# Plot
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=80, label="Average processing time")
plt.plot(x, regression_line, label="Linear regression")

plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.title("Linear Regression of Processing Time vs Number of Records")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("output.3.2.png", dpi=300)
plt.show()
