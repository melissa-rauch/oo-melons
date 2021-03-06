"""Classes for melon orders."""
class AbstractMelonOrder():
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty >= 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Set melon_type and tax for domestic orders"""
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Get international country code"""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Governmental order, free of tax and required inspection"""
    def __init__(self, species, qty):
        """Set melon_type and tax for government orders"""
        super().__init__(species, qty, "government", 0.00)
        self.passed_inspection = False

    def mark_inspection(self):
        """Record the fact that the melon(s) passed inspection"""

        self.passed_inspection = True 




