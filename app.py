# -*- coding: utf-8 -*-


class RentalPriceException(Exception):
    pass


class RentalPrice(object):

    def __init__(self, unit):
        self.unit = unit

    def get_amount(self):
        raise NotImplementedError()


class RentalPricePerHour(RentalPrice):

    price = 5

    def get_amount(self):
        return self.price * self.unit


class RentalPricePerDay(RentalPrice):

    price = 20

    def get_amount(self):
        return self.price * self.unit


class RentalPricePerWeek(RentalPrice):

    price = 60

    def get_amount(self):
        return self.price * self.unit


class CompanyInvoice(object):

    OPEN = 0
    CLOSED = 1
    FAMILYRENTALDISCOUNT = 0.3
    RENTALPRICES = {
        0: RentalPricePerHour,
        1: RentalPricePerDay,
        2: RentalPricePerWeek
    }

    invoice_rows = []

    def __init__(self):
        self.status = self.OPEN

    def add_invoice_row(self, type_of_rent, unit):
        if self.status == 1 or type_of_rent not in self.RENTALPRICES.keys():
            return False
        self.invoice_rows.append(
            self.RENTALPRICES[type_of_rent](unit).get_amount()
        )
        return True

    def get_total(self):
        if 3 <= len(self.invoice_rows) <= 5:
            return (1 - self.FAMILYRENTALDISCOUNT) * sum(self.invoice_rows)
        else:
            return sum(self.invoice_rows)

    def closed_invoice(self):
        self.status = self.CLOSED
