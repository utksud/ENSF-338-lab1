import re
import timeit

VOWELS = set("aeiouy")

def count_vowels_in_word(word: str) -> int:
    return sum(1 for ch in word.lower() if ch in VOWELS)

def compute_average(lines) -> float:
    # start counting at: CHAPTER 1. Loomings. (included)
    start_re = re.compile(r"^\s*CHAPTER\s+1\.\s+Loomings\.\s*$", re.IGNORECASE)

    start_index = None
    for i, line in enumerate(lines):
        if start_re.match(line):
            start_index = i
            break
    if start_index is None:
        return 0.0

    total_words = 0
    total_vowels = 0

    for line in lines[start_index:]:
        words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", line)
        total_words += len(words)
        total_vowels += sum(count_vowels_in_word(w) for w in words)

    return total_vowels / total_words if total_words else 0.0

def main():
    # NOT TIMED: reading the file
    filename = "lab_data/pg2701.txt"
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # compute once so you can print the actual answer (printing is NOT timed)
    avg_vowels = compute_average(lines)
    print(f"Average vowels per word: {avg_vowels}")

    # TIMED: computation only (no file read, no print inside)
    timer = timeit.Timer(lambda: compute_average(lines))
    total_time = timer.timeit(number=100)      # run 100 times
    avg_time = total_time / 100                # average per run

    print(f"Average time over 100 runs: {avg_time} seconds")

if __name__ == "__main__":
    main()
