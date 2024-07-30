def get_initial_quote(customer_info, loan_purpose, loan_amount):
    # This is a simplified pricing model. In a real application, this would be more complex.
    base_apr = 10.0
    apr_adjustments = {
        'car': -0.5,
        'debtConsolidation': 1.0,
        'houseRenovation': 0.0,
        'personalLoan': 0.5
    }
    
    apr = base_apr + apr_adjustments.get(loan_purpose, 0)
    monthly_payment = (loan_amount * (apr / 100 / 12)) / (1 - (1 + apr / 100 / 12) ** -60)
    
    return {
        'loan_amount': loan_amount,
        'apr': round(apr, 2),
        'monthly_payment': round(monthly_payment, 2),
        'tenure': 60
    }

def get_counter_offer(customer_info, loan_purpose, loan_amount, initial_quote):
    # This is a simplified counter offer. In a real application, this would be more complex.
    counter_apr = initial_quote['apr'] - 0.5
    counter_monthly_payment = (loan_amount * (counter_apr / 100 / 12)) / (1 - (1 + counter_apr / 100 / 12) ** -60)
    
    return {
        'loan_amount': loan_amount,
        'apr': round(counter_apr, 2),
        'monthly_payment': round(counter_monthly_payment, 2),
        'tenure': 60
    }