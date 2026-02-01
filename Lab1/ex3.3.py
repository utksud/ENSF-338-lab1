import json
import timeit
import matplotlib.pyplot as plt

with open('internetdata.json', 'r') as f:
    data = json.load(f)

def process_records(records):
    result = []
    for r in records:
        processed = r.copy()
        if 'incomeperperson' in processed:
            processed['incomeperperson'] = processed.get('incomeperperson', 0) * 1.05
        result.append(processed)
    return result

subset = data[:1000]

def wrapper():
    return process_records(subset)

times = timeit.repeat(
    'wrapper()',
    setup='from __main__ import wrapper',
    repeat=1000,
    number=1
)

times_ms = [t * 1000 for t in times]

plt.figure(figsize=(8, 5))
plt.hist(times_ms, bins=20, edgecolor='black')
plt.title('Processing Time Distribution (1000 records, 1000 repetitions)')
plt.xlabel('Time (ms)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output.3.3.png')
plt.show()
