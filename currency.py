# Currency conversion rates (relative to USD)
EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'PKR': 278.50,  # Pakistani Rupee
    'INR': 83.12,   # Indian Rupee
    'CAD': 1.36,
    'AUD': 1.53,
    'JPY': 149.50,
    'CNY': 7.24,
    'AED': 3.67,
    'SAR': 3.75
}

def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another
    
    Args:
        amount: The amount to convert
        from_currency: Source currency code (e.g., 'USD')
        to_currency: Target currency code (e.g., 'EUR')
    
    Returns:
        Converted amount
    """
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported currency. Supported: {list(EXCHANGE_RATES.keys())}")
    
    # Convert to USD first, then to target currency
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_currency]
    
    return converted_amount

def get_supported_currencies():
    """Return list of supported currencies"""
    return list(EXCHANGE_RATES.keys())

def get_exchange_rate(currency):
    """Get exchange rate for a specific currency"""
    if currency in EXCHANGE_RATES:
        return EXCHANGE_RATES[currency]
    return None
