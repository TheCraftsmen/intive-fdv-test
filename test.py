import unittest
from app import (
    RentalPrice, RentalPricePerHour,
    RentalPricePerDay, RentalPricePerWeek,
    CompanyInvoice
)


class RentalTestCase(unittest.TestCase):
    def setUp(self):
        self.rental_per_hour = RentalPricePerHour(5)
        self.rental_per_day = RentalPricePerDay(2)
        self.rental_per_week = RentalPricePerWeek(3)
        self.rental_price = RentalPrice(10)
        self.invoice = CompanyInvoice()

    def test_rental_price_get_amount_implemented(self):
        self.assertRaises(NotImplementedError, self.rental_price.get_amount)

    def test_rental_per_day_days_assing(self):
        rental_per_day = RentalPricePerDay(4)
        self.assertEqual(rental_per_day.unit, 4)

    def test_company_invoice_add_row(self):
        self.assertTrue(self.invoice.add_invoice_row(0, 5))

    def test_company_invoice_add_row_invalid_type(self):
        self.assertFalse(self.invoice.add_invoice_row(20, 5))

    def test_company_invoice_get_total(self):
        self.assertEqual(self.invoice.get_total(), 25)

    def test_company_invoice_get_total_discount(self):
        self.invoice.add_invoice_row(0, 5)
        self.invoice.add_invoice_row(0, 5)
        self.assertEqual(self.invoice.get_total(), 52.5)        

    def test_rental_per_hour_price(self):
        self.assertEqual(self.rental_per_hour.price, 5, "incorrect default price")

    def test_rental_per_day_price(self):
        self.assertEqual(self.rental_per_day.price, 20, "incorrect default price")

    def test_rental_per_week_price(self):
        self.assertEqual(self.rental_per_week.price, 60, "incorrect default price")

    def test_rental_per_hour_amount(self):
        self.assertEqual(self.rental_per_hour.get_amount(), 25, 'incorrect amount')

    def test_rental_per_day_amount(self):
        self.assertEqual(self.rental_per_day.get_amount(), 40, 'incorrect amount')

    def test_rental_per_week_amount(self):
        self.assertEqual(self.rental_per_week.get_amount(), 180, 'incorrect amount')


if __name__ == '__main__':
    unittest.main()
