# shopping_logic.py
# Simplified version of reassignment and savings logic for multi-store shopping comparison

import pandas as pd

def try_parse_price(price_str):
    try:
        return float(str(price_str).replace("$", "").replace("(2pk)", "").split()[0])
    except:
        return None

def clean_price(value):
    try:
        return float(str(value).replace("$", "").replace("(2pk)", "").strip())
    except:
        return 0.0

def get_second_best(row, skip_store):
    prices = {
        "Walmart": try_parse_price(row["Walmart"]),
        "Kroger": try_parse_price(row["Kroger"]),
        "H-E-B": try_parse_price(row["H-E-B"]),
        "Joe V's": try_parse_price(row["Joe V's"]),
        "Sam's Club": try_parse_price(row["Sam's Club"]),
        "Amazon": try_parse_price(row["Amazon"])
    }
    valid_prices = {k: v for k, v in prices.items() if k != skip_store and v is not None}
    return min(valid_prices.items(), key=lambda x: x[1]) if valid_prices else (None, None)
