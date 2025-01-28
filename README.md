# Thai Date Extractor

**Thai Date Extractor** is a Python library that helps extract dates and date ranges from Thai text queries. It supports various formats, including natural language (e.g., "วันนี้", "สัปดาห์นี้"), Thai numerals (e.g., "นั้น/เมษา/พ.ศ."), and common date formats.

---

## Features
- **Natural language support**:
  - "วันนี้" → Current date
  - "สัปดาห์นี้" → Start and end dates of the current week
  - "เดือนนี้" → Start and end dates of the current month
  - "เดือนหน้า" → Start and end dates of the next month
  - "เดือนที่แล้ว" → Start and end dates of the previous month
- **Thai numerals support**:
  - Automatically converts Thai numerals (e.g., "นั้น-เก้า") into Arabic numerals (e.g., "1-9").
- **Custom date range parsing**:
  - Handles formats like `dd/mm/yyyy ถึง dd/mm/yyyy`.
- **Year range support**:
  - Extracts specific years (e.g., "ปี 2567").

---

## Installation

Install via pip:

```bash
pip install thai_date_extractor
```

---

## Usage

### Example 1: Extracting Dates from Thai Natural Language
```python
from thai_date_extractor import extract_date_range_from_query

query = "รายงานความเคลื่อนไหวอสัปดาห์นี้"
result = extract_date_range_from_query(query)
print(result)
# Output: {'start_date': '2025-01-22', 'end_date': '2025-01-28'}
```

### Example 2: Extracting Dates from Thai Numerals
```python
query = "รายงานตั้งแต่ ๑๕/๐๑/๒๕๖๗ ถึง ๒๐/๐๑/๒๕๖๗"
result = extract_date_range_from_query(query)
print(result)
# Output: {'start_date': '2024-01-15', 'end_date': '2024-01-20'}
```

### Example 3: Extracting a Year Range
```python
query = "รายงานปี 2567"
result = extract_date_range_from_query(query)
print(result)
# Output: {'start_date': '2567-01-01', 'end_date': '2567-12-31'}
```

---

## API Reference

### `extract_date_range_from_query(query: str) -> dict`
Extracts a date range or a specific date from a Thai query string.

#### Parameters:
- `query` (str): The input string containing the date-related query.

#### Returns:
- `dict`: A dictionary containing:
  - `start_date` (str): The start date in the format `YYYY-MM-DD`.
  - `end_date` (str): The end date in the format `YYYY-MM-DD`.

#### Example:
```python
query = "รายงานตั้งแต่ 01/01/2025 ถึง 31/12/2025"
result = extract_date_range_from_query(query)
print(result)
# Output: {'start_date': '2025-01-01', 'end_date': '2025-12-31'}
```

---

## Supported Patterns

1. **Today**: `"วันนี้"`  
   - Extracts the current date as both start and end.

2. **This Week**: `"สัปดาห์นี้"`  
   - Extracts the start (Monday) and end (Sunday) dates of the current week.

3. **This Month**: `"เดือนนี้"`  
   - Extracts the start and end dates of the current month.

4. **Next Month**: `"เดือนหน้า"`  
   - Extracts the start and end dates of the next month.

5. **Last Month**: `"เดือนที่แล้ว"`  
   - Extracts the start and end dates of the previous month.

6. **Date Ranges**: `"dd/mm/yyyy ถึง dd/mm/yyyy"`  
   - Parses date ranges in Thai or Arabic numerals.

7. **Years**: `"ปี xxxx"`  
   - Extracts the full year range (e.g., `"ปี 2567"` → `start_date: 2567-01-01`, `end_date: 2567-12-31`).

---

## Running Tests

You can run unit tests to verify the functionality:

```bash
python -m unittest discover tests
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Feedback and Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/yourusername/thai_date_extractor).

---

Happy coding! 🎉
