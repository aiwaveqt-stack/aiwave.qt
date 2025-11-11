class CurrencyConverter:
    def __init__(self):
        # Exchange rates stored in a dictionary
        self.exchange_rates = {
            "USD": 1.0,  # Base currency
            "EUR": 0.85,
            "GHS": 16.02,  # Example rate for GHS to USD
            "NGN": 1666.39,  # Example rate for NGN to USD
            "GBP": 0.75,
            "CAD": 1.25
        }

    def convert_to_usd(self, amount, currency):
        """Convert any currency to USD"""
        return amount / self.exchange_rates[currency]

    def convert_from_usd(self, amount, currency):
        """Convert USD to any currency"""
        return amount * self.exchange_rates[currency]

    def get_user_input_string(self, message):
        """Get user input as a string"""
        return input(message)

    def get_user_input_double(self, message):
        """Get user input as a float"""
        return float(input(message))

    def run(self):
        print("Welcome to the Currency Converter!")
        print("-" * 52)

        print("Available currencies: USD, EUR, GHS, NGN, GBP, CAD")
        print("-" * 52)

        from_currency = self.get_user_input_string(
            "Enter the currency you want to convert from (e.g., USD): "
        ).upper()
        amount = self.get_user_input_double(f"Enter amount in {from_currency}: ")
        print("-" * 52)

        to_currency = self.get_user_input_string(
            "Enter the currency you want to convert to (e.g., EUR): "
        ).upper()
        print("-" * 52)

        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            amount_in_usd = self.convert_to_usd(amount, from_currency)
            converted_amount = self.convert_from_usd(amount_in_usd, to_currency)
            print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Invalid currency! Please ensure you enter a valid currency code.")
        print("-" * 52)


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()
