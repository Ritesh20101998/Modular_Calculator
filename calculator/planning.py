"""
General Financial Planning Tools
- SIP Calculator
- Lumpsum Calculator
- Time Value of Money (PV, FV, I/Y, N, PMT)
"""
import math

def sip_calculator(monthly_investment, annual_rate, tenure_months):
    """
    Calculate SIP maturity value, total invested, and total gain.
    """
    r = annual_rate / (12 * 100)
    n = tenure_months
    maturity = monthly_investment * ((math.pow(1 + r, n) - 1) / r) * (1 + r)
    total_invested = monthly_investment * n
    gain = maturity - total_invested
    return {
        'Maturity Value': round(maturity, 2),
        'Total Invested': round(total_invested, 2),
        'Total Gain': round(gain, 2)
    }

def lumpsum_calculator(principal, annual_rate, tenure_years):
    """
    Calculate future value and gain for a lumpsum investment.
    """
    r = annual_rate / 100
    n = tenure_years
    maturity = principal * math.pow(1 + r, n)
    gain = maturity - principal
    return {
        'Maturity Value': round(maturity, 2),
        'Total Gain': round(gain, 2)
    }

def fv(pv, rate, n):
    """
    Calculate Future Value (FV) given Present Value (PV), rate, and periods.
    """
    return pv * math.pow(1 + rate, n)

def pv(fv, rate, n):
    """
    Calculate Present Value (PV) given Future Value (FV), rate, and periods.
    """
    return fv / math.pow(1 + rate, n)

def pmt(pv, rate, n):
    """
    Calculate Payment per period (PMT) for a loan/investment.
    """
    if rate == 0:
        return pv / n
    return pv * rate * math.pow(1 + rate, n) / (math.pow(1 + rate, n) - 1)

def nper(pv, pmt, rate):
    """
    Calculate Number of Periods (N) given PV, PMT, and rate.
    """
    if rate == 0:
        return pv / pmt
    return math.log(pmt / (pmt - pv * rate)) / math.log(1 + rate)

def rate(pv, pmt, n):
    """
    Approximate Interest Rate (I/Y) given PV, PMT, and N (using Newton's method).
    """
    guess = 0.05
    for _ in range(100):
        f = pv * math.pow(1 + guess, n) + pmt * (math.pow(1 + guess, n) - 1) / guess
        df = pv * n * math.pow(1 + guess, n - 1) - pmt * (math.pow(1 + guess, n) - 1) / (guess ** 2) + pmt * n * math.pow(1 + guess, n - 1) / guess
        new_guess = guess - f / df
        if abs(new_guess - guess) < 1e-6:
            return new_guess
        guess = new_guess
    return guess
