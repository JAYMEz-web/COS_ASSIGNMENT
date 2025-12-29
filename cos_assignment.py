# Personal Income Tax Calculator for 2009 tax year
# COS 201 Assignment

def calculate_personal_tax(filing_status, taxable_income):
    # Tax rates 
    tax_rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
    
    # Income brackets for each filing status
    # Note: using a dict here because it's easier to read than nested lists
    income_brackets = {
        0: [8350, 33950, 82250, 171550, 372950, float('inf')],     # single filers
        1: [16700, 67900, 137050, 208850, 372950, float('inf')],   # married jointly/widow
        2: [8350, 33950, 68525, 104425, 186475, float('inf')],     # married separately  
        3: [11950, 45500, 117450, 190200, 372950, float('inf')]    # head of household
    }
    
    # Basic validation
    if filing_status not in income_brackets:
        raise ValueError("Invalid filing status - must be 0, 1, 2, or 3")
    
    # No tax on zero or negative income
    if taxable_income <= 0:
        return 0.0
    
    bracket_limits = income_brackets[filing_status]
    total_tax = 0.0
    previous_bracket = 0.0
    
    # Calculate tax for each bracket
    for i, (rate, bracket_limit) in enumerate(zip(tax_rates, bracket_limits)):
        # Figure out how much income falls in this bracket
        income_in_bracket = min(taxable_income, bracket_limit) - previous_bracket
        
        if income_in_bracket > 0:
            tax_for_bracket = income_in_bracket * rate
            total_tax += tax_for_bracket
            previous_bracket = bracket_limit  # Move to next bracket
            
        # Stop if we've calculated all the income
        if taxable_income <= bracket_limit:
            break
            
    return total_tax

# Main program execution
def main():
    try:
        print("=== US Federal Income Tax Calculator (2009) ===")
        print("Filing Status Options:")
        print("0 - Single")
        print("1 - Married Filing Jointly or Qualifying Widow(er)")  
        print("2 - Married Filing Separately")
        print("3 - Head of Household")
        print()
        
        # Get user input
        status_input = input("Enter your filing status (0-3): ").strip()
        status = int(status_input)
        
        income_input = input("Enter your taxable income: $").strip()
        income = float(income_input)
        
        # Calculate the tax
        calculated_tax = calculate_personal_tax(status, income)
        
        # Display result
        print(f"\nYour federal income tax is: ${calculated_tax:.2f}")
        
    except ValueError as error:
        print(f"Error: {error}")
        print("Please enter valid numbers only.")
    except KeyboardInterrupt:
        print("\nProgram cancelled by user.")

# Run the program
if __name__ == "__main__":
    main()