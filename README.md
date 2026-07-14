# Bloom Filter Implementation

## Overview
This project implements a **Bloom Filter**, a space-efficient probabilistic data structure used to test whether an element is a member of a set.

Bloom filters are highly efficient but allow for **false positives** (reporting an element is in the set when it is not), while guaranteeing **no false negatives**.

This implementation uses:
- Multiple hash functions via `BitHash`
- A compact bit array using `BitVector`
- Configurable parameters for size and false positive rate

---

## Features
- Space-efficient set membership testing
- Configurable number of hash functions
- Tunable false positive rate
- Fast insert and lookup operations
- Empirical testing of false positive rate

---

## How It Works
A Bloom Filter:
1. Hashes each key multiple times
2. Maps each hash to a position in a bit vector
3. Sets those positions to 1 on insert

To check membership:
- If **any bit is 0 → definitely not in set**
- If **all bits are 1 → possibly in set (false positive possible)**

---

## Project Structure
```
.
├── BloomFilter.py       # Main implementation
├── BitHash.py          # Hash function(s)
├── BitVector.py        # Bit array implementation
├── wordlist.txt        # Input dataset
└── README.md
```

---

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/bloom-filter.git
cd bloom-filter
```

Make sure dependencies (`BitHash`, `BitVector`) are available in the project directory.

---

## Usage

### Basic Example
```python
from BloomFilter import BloomFilter

bf = BloomFilter(numKeys=100000, numHashes=4, maxFalsePositive=0.05)

bf.insert("hello")
bf.insert("world")

print(bf.find("hello"))  # True
print(bf.find("test"))   # Possibly False (or True if false positive)
```

---

## API

### `BloomFilter(numKeys, numHashes, maxFalsePositive)`
Initializes the Bloom Filter.

- `numKeys`: Expected number of elements
- `numHashes`: Number of hash functions
- `maxFalsePositive`: Desired false positive rate

---

### `insert(key)`
Inserts a key into the Bloom Filter.

---

### `find(key)`
Checks if a key is in the Bloom Filter.

- Returns `False` → definitely not present  
- Returns `True` → possibly present  

---

### `falsePositiveRate()`
Returns the **theoretical false positive rate** based on current parameters.

---

### `numBitsSet()`
Returns the number of bits set to 1 in the bit vector.

---

## Example Script

The `__main__` function demonstrates:
1. Creating a Bloom Filter
2. Inserting words from a file (`wordlist.txt`)
3. Measuring:
   - Theoretical false positive rate
   - Actual false positive rate

### Run the Script
```bash
python BloomFilter.py
```

---

## Output Example
```
False Positive rate: 0.048
Missing: 0
Actual False Positive Rate: 0.051
```

---



## Notes
- Bloom Filters **do not store actual data**, only hash signatures.
- False positives increase as the filter fills up.
- Choosing optimal parameters is critical for performance.

---


## AI Usage
- AI was not used to construct the bloom filter, however AI was used for the creation of this read-me file.
