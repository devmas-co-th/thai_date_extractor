import re
from datetime import datetime, timedelta

def convert_thai_numbers_to_arabic(text):
    """Convert Thai numerals (๐-๙) to Arabic numerals (0-9)."""
    thai_to_arabic_map = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
    return text.translate(thai_to_arabic_map)

def extract_date_range_from_query(query):
    """
    Extract date ranges or specific dates from a query string.
    Supports Thai numerals, natural language, and common date formats.
    """
    # Convert Thai numerals to Arabic numerals
    query = convert_thai_numbers_to_arabic(query)
    today = datetime.today()

    # Define patterns and their processing logic
    patterns = [
        {
            "pattern": r"วันนี้",
            "logic": lambda: {"start_date": today.strftime('%Y-%m-%d'), "end_date": today.strftime('%Y-%m-%d')}
        },
        {
            "pattern": r"สัปดาห์นี้",
            "logic": lambda: {
                "start_date": (today - timedelta(days=today.weekday())).strftime('%Y-%m-%d'),
                "end_date": (today + timedelta(days=6 - today.weekday())).strftime('%Y-%m-%d')
            }
        },
        {
            "pattern": r"เดือนนี้",
            "logic": lambda: {
                "start_date": today.replace(day=1).strftime('%Y-%m-%d'),
                "end_date": (today.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)
            }
        },
        {
            "pattern": r"เดือนหน้า",
            "logic": lambda: {
                "start_date": (today.replace(day=1) + timedelta(days=31)).replace(day=1).strftime('%Y-%m-%d'),
                "end_date": ((today.replace(day=1) + timedelta(days=31)).replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)
            }
        },
        {
            "pattern": r"เดือนที่แล้ว",
            "logic": lambda: {
                "start_date": ((today.replace(day=1) - timedelta(days=1)).replace(day=1)).strftime('%Y-%m-%d'),
                "end_date": (today.replace(day=1) - timedelta(days=1)).strftime('%Y-%m-%d')
            }
        },
        {
            "pattern": r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\s*ถึง\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
            "logic": lambda match: {
                "start_date": datetime.strptime(match.group(1), '%d/%m/%Y').strftime('%Y-%m-%d'),
                "end_date": datetime.strptime(match.group(2), '%d/%m/%Y').strftime('%Y-%m-%d')
            }
        },
        {
            "pattern": r"ปี\s?(\d{4})",
            "logic": lambda match: {
                "start_date": datetime(int(match.group(1)), 1, 1).strftime('%Y-%m-%d'),
                "end_date": datetime(int(match.group(1)), 12, 31).strftime('%Y-%m-%d')
            }
        }
    ]

    # Process the query based on patterns
    for pattern in patterns:
        match = re.search(pattern["pattern"], query)
        if match:
            return pattern["logic"](match) if "match" in pattern["logic"].__code__.co_varnames else pattern["logic"]()

    # If no pattern matches
    return None
