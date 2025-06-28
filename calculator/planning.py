"""
Financial Planning Tools
- SIP, Lumpsum, and TVM calculators
- All functions type-checked and documented
"""
import math

def sip_calculator(monthly_investment: float, annual_rate: float, tenure_months: int) -> dict:
    """
    Calculate SIP maturity value, total invested, and total gain.
    
    :param monthly_investment: Amount invested monthly
    :param annual_rate: Annual interest rate (in %)
    :param tenure_months: Investment duration in months
    :return: Dictionary with maturity value, total invested, and total gain
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

def lumpsum_calculator(principal: float, annual_rate: float, tenure_years: int) -> dict:
    """
    Calculate future value and gain for a lumpsum investment.
    
    :param principal: Initial amount invested
    :param annual_rate: Annual interest rate (in %)
    :param tenure_years: Investment duration in years
    :return: Dictionary with maturity value and total gain
    """
    r = annual_rate / 100
    n = tenure_years
    maturity = principal * math.pow(1 + r, n)
    gain = maturity - principal
    return {
        'Maturity Value': round(maturity, 2),
        'Total Gain': round(gain, 2)
    }

def fv(pv: float, rate: float, n: int) -> float:
    """Calculate Future Value (FV) given Present Value (PV), rate, and periods."""
    return round(pv * math.pow(1 + rate, n), 2)

def pv(fv: float, rate: float, n: int) -> float:
    """Calculate Present Value (PV) given Future Value (FV), rate, and periods."""
    return round(fv / math.pow(1 + rate, n), 2)

def pmt(pv: float, rate: float, n: int) -> float:
    """Calculate Payment (PMT) for an annuity."""
    if rate == 0:
        return round(pv / n, 2)
    return round(pv * rate / (1 - math.pow(1 + rate, -n)), 2)

def nper(pv: float, pmt: float, rate: float) -> float:
    """Calculate Number of Periods (NPER) for an annuity."""
    if rate == 0:
        return round(pv / pmt, 2)
    return round(math.log(pmt / (pmt - pv * rate)) / math.log(1 + rate), 2)

def rate(pv: float, pmt: float, n: int) -> float:
    """Calculate Rate for an annuity (approximate)."""
    if n == 0:
        raise ValueError("Number of periods cannot be zero.")
    try:
        # Newton-Raphson or similar could be used for more accuracy
        return 0.0 if abs(pv - pmt * n) < 1e-6 else (pmt / pv) / n
    except Exception:
        return 0.0
