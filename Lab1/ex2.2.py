import re

VOWELS = set("aeiouy")

def count_vowels_in_word(word: str) -> int:
    return sum(1 for ch in word.lower() if ch in VOWELS)

def main():
    filename = "lab_data/pg2701.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Robust match for: CHAPTER 1. Loomings.
    start_re = re.compile(r"^\s*CHAPTER\s+1\.\s+Loomings\.\s*$", re.IGNORECASE)

    start_index = None
    for i, line in enumerate(lines):
        if start_re.match(line):
            start_index = i
            break

    if start_index is None:
        print('ERROR: Could not find the start line "CHAPTER 1. Loomings."')
        return

    total_words = 0
    total_vowels = 0

    for line in lines[start_index:]:
        words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", line)
        total_words += len(words)
        total_vowels += sum(count_vowels_in_word(w) for w in words)

    if total_words == 0:
        print("ERROR: Counted 0 words. You are likely reading the wrong file/path or parsing failed.")
        return

    print(total_vowels / total_words)

if __name__ == "__main__":
    main()
