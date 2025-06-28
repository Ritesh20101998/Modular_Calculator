"""
Financial Calculator Module
- Simple and compound interest, risk/return, currency formatting, data I/O
- All functions type-checked, logged, and robust
"""
import os
import math
from typing import List, Dict, Any
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd
import sqlite3
import logging

logging.basicConfig(
    filename='financial.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def simple_interest(p: float, r: float, t: float) -> float:
    """Calculate simple interest given principal, rate, and time."""
    try:
        result = p * r * t / 100
        logging.info(f"simple_interest | p={p}, r={r}, t={t} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"simple_interest | p={p}, r={r}, t={t} | error={e}")
        raise

def compound_interest(p: float, r: float, t: float, n: int) -> float:
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

def risk_return_analysis(returns: List[float]) -> Dict[str, float]:
    """Calculate mean return and standard deviation for a list of returns."""
    try:
        if not isinstance(returns, list) or not all(isinstance(x, (int, float)) for x in returns):
            raise TypeError("Returns must be a list of numbers.")
        mean_return = sum(returns) / len(returns)
        stddev = (sum((x - mean_return) ** 2 for x in returns) / len(returns)) ** 0.5
        logging.info(f"risk_return_analysis | returns={returns} | mean={mean_return}, stddev={stddev}")
        return {'mean_return': mean_return, 'stddev': stddev}
    except Exception as e:
        logging.exception(f"risk_return_analysis | returns={returns} | error={e}")
        raise

def format_currency(value: float, currency: str = 'USD') -> str:
    """Format a value as currency with two decimal places."""
    try:
        formatted = f"{currency} {Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):,.2f}"
        logging.info(f"format_currency | value={value}, currency={currency} | result={formatted}")
        return formatted
    except Exception as e:
        logging.exception(f"format_currency | value={value}, currency={currency} | error={e}")
        raise

def read_financial_data_csv(filepath: str) -> List[Dict[str, Any]]:
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

def read_financial_data_excel(filepath: str) -> List[Dict[str, Any]]:
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

def save_financial_record(db_path: str, table: str, record: Dict[str, Any]):
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

def emi_calculator(principal: float, annual_rate: float, tenure_months: int) -> Dict[str, float]:
    """
    Calculate EMI, total payment, and total interest for a loan.
    Args:
        principal: Loan amount (P)
        annual_rate: Annual interest rate in percent (R)
        tenure_months: Tenure in months (N)
    Returns:
        dict with EMI, total_payment, total_interest
    """
    try:
        if principal <= 0 or annual_rate < 0 or tenure_months <= 0:
            raise ValueError("Principal, rate, and tenure must be positive.")
        monthly_rate = annual_rate / (12 * 100)
        n = tenure_months
        if monthly_rate == 0:
            emi = principal / n
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
        total_payment = emi * n
        total_interest = total_payment - principal
        result = {
            'EMI': round(emi, 2),
            'Total Payment': round(total_payment, 2),
            'Total Interest': round(total_interest, 2)
        }
        logging.info(f"emi_calculator | principal={principal}, annual_rate={annual_rate}, tenure_months={tenure_months} | result={result}")
        return result
    except Exception as e:
        logging.exception(f"emi_calculator | principal={principal}, annual_rate={annual_rate}, tenure_months={tenure_months} | error={e}")
        raise

def emi_amortization_schedule(principal: float, annual_rate: float, tenure_months: int) -> List[Dict[str, float]]:
    """
    Generate an EMI amortization schedule as a list of dicts.
    Each entry contains: month, EMI, principal_paid, interest_paid, remaining_principal
    """
    try:
        schedule = []
        monthly_rate = annual_rate / (12 * 100)
        n = tenure_months
        if monthly_rate == 0:
            emi = principal / n
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
        remaining = principal
        for month in range(1, n + 1):
            interest = remaining * monthly_rate
            principal_paid = emi - interest
            remaining -= principal_paid
            if remaining < 0:  # Avoid negative due to float rounding
                principal_paid += remaining
                remaining = 0
            schedule.append({
                'Month': month,
                'EMI': round(emi, 2),
                'Principal Paid': round(principal_paid, 2),
                'Interest Paid': round(interest, 2),
                'Remaining Principal': round(remaining, 2)
            })
        logging.info(f"emi_amortization_schedule | principal={principal}, annual_rate={annual_rate}, tenure_months={tenure_months} | schedule_generated")
        return schedule
    except Exception as e:
        logging.exception(f"emi_amortization_schedule | principal={principal}, annual_rate={annual_rate}, tenure_months={tenure_months} | error={e}")
        raise

def emi_amortization_to_excel(principal: float, annual_rate: float, tenure_months: int, filepath: str) -> str:
    """
    Generate EMI amortization schedule and save as an Excel file.
    Args:
        principal: Loan amount
        annual_rate: Annual interest rate in percent
        tenure_months: Tenure in months
        filepath: Path to save the Excel file
    """
    try:
        schedule = emi_amortization_schedule(principal, annual_rate, tenure_months)
        df = pd.DataFrame(schedule)
        df.to_excel(filepath, index=False)
        logging.info(f"emi_amortization_to_excel | file saved: {filepath}")
        return filepath
    except Exception as e:
        logging.exception(f"emi_amortization_to_excel | error: {e}")
        raise

# Alias for compatibility with tests and API
finance = __import__(__name__)
