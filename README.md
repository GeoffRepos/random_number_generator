# Random Number Generator

A simple, well-commented Python random number generator. Generates integers or floats within a range, with a small CLI and importable functions.

## Features
- Generate a single integer or float
- Generate multiple numbers at once
- Minimal CLI with `--kind`, `--min`, `--max`, `--count`, and `--examples`

## Quick Start

### Prerequisites
- Python 3.9+ installed and available in PATH

### Run examples
```powershell
# From the project root
python .\src\number_generator.py --examples
```

### Generate numbers via CLI
```powershell
# 3 random integers between 10 and 20
python .\src\number_generator.py --kind int --min 10 --max 20 --count 3

# 5 random floats between 1.5 and 2.5
python .\src\number_generator.py --kind float --min 1.5 --max 2.5 --count 5
```

## Use as a library
```python
from number_generator import random_int, random_float, generate_many

n = random_int(1, 10)
x = random_float(0.0, 1.0)
values = generate_many("int", 5, 10, 20)
```

## Notes
- For integer generation, bounds are inclusive.
- For float generation, values are uniformly distributed across `[min, max]`.
