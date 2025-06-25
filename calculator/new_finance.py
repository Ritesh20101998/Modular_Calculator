import math
import os
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd
import sqlite3
import logging

logging.basicConfig(
    filename='financial.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def simple_interest(p, r, t):
    """Calculate simple interest given principal, rate, and time."""
    try:
        result = p * r * t / 100
        logging.info(f"simple_interest | p={p}, r={r}, t={t} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"simple_interest | p={p}, r={r}, t={t} | error={e}")
        raise

def compound_interest(p, r, t, n):
    """Calculate compound interest given principal, rate, time, and compounding frequency."""
    try:
        if n == 0:
            raise ValueError("Compounding frequency 'n' cannot be zero.")
        result = p * (math.pow((1 + r/(100*n)), n*t)) - p
        logging.info(f"compound_interest | p={p}, r={r}, t={t}, n={n} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"compound_interest | p={p}, r={r}, t={t}, n={n} | error={e}")
        raise

def risk_return_analysis(returns):
    """Calculate mean return and standard deviation for a list of returns."""
    try:
        if not returns:
            raise ValueError("Returns list cannot be empty.")
        mean_return = float(sum(returns)) / len(returns)
        variance = float(sum((r - mean_return) ** 2 for r in returns)) / len(returns)
        stddev = variance ** 0.5
        result = {'mean_return': round(mean_return, 4), 'stddev': round(stddev, 4)}
        logging.info(f"risk_return_analysis | returns={returns} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"risk_return_analysis | returns={returns} | error={e}")
        raise

def format_currency(value, currency='USD'):
    """Format a value as currency with two decimal places."""
    try:
        formatted = f"{currency} {Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):,.2f}"
        logging.info(f"format_currency | value={value}, currency={currency} | result={formatted}")
        return formatted
    except Exception as e:
        logging.exception(f"format_currency | value={value}, currency={currency} | error={e}")
        raise

def read_financial_data_csv(filepath):
    """Read financial data from a CSV file and return as a list of records."""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        df = pd.read_csv(filepath)
        records = df.to_dict(orient='records')
        logging.info(f"read_financial_data_csv | filepath={filepath} | records_count={len(records)}")
        return records
    except Exception as e:
        logging.exception(f"read_financial_data_csv | filepath={filepath} | error={e}")
        raise

def read_financial_data_excel(filepath):
    """Read financial data from an Excel file and return as a list of records."""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        df = pd.read_excel(filepath, engine='openpyxl')  # engine explicitly set
        records = df.to_dict(orient='records')
        logging.info(f"read_financial_data_excel | filepath={filepath} | records_count={len(records)}")
        return records
    except Exception as e:
        logging.exception(f"read_financial_data_excel | filepath={filepath} | error={e}")
        raise

def save_financial_record(db_path, table, record):
    """Save a financial record to a SQLite database table."""
    try:
        conn = sqlite3.connect(db_path)
        columns = ', '.join(record.keys())
        placeholders = ', '.join(['?'] * len(record))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        conn.execute(sql, tuple(record.values()))
        conn.commit()
        conn.close()
        logging.info(f"save_financial_record | db_path={db_path}, table={table}, record={record}")
    except Exception as e:
        logging.exception(f"save_financial_record | db_path={db_path}, table={table}, record={record} | error={e}")
        raise
