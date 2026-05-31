from enum import Enum
import datetime
from .entity import Buyer, Seller

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    def __init__(self, tax_id: str = None, tax_type: TaxType = None, percentage: float = 0.0):
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage


class Product:
    def __init__(self, product_id: str, name: str, *args, quantity: int = 0, price: float = 0.0, taxes: list[Tax] = None, **kwargs):
        self.product_id = product_id
        self.name = name
        
        # Mapeo flexible de parámetros posicionales provenientes de BillManager
        if len(args) >= 3:
            # Si se pasa: (id, name, date, description, quantity, price)
            self.quantity = args[2]
            self.price = args[3] if len(args) > 3 else price
        else:
            self.quantity = quantity
            self.price = price
            
        self.taxes = taxes if taxes is not None else kwargs.get('taxes', [])

    def calculate_tax(self, tax: Tax) -> float:
        # En la UOC el porcentaje viene como tasa (ej: 0.5 = 50%). No se divide por 100.
        base_tax = self.quantity * self.price * tax.percentage
        if tax.tax_type == TaxType.ISD:
            return base_tax * ISD_FACTOR
        return base_tax

    def calculate_total_taxes(self) -> float:
        total_taxes = 0.0
        for tax in self.taxes:
            total_taxes += self.calculate_tax(tax)
        return total_taxes

    def calculate_total(self) -> float:
        return (self.quantity * self.price) + self.calculate_total_taxes()

    def __eq__(self, another):
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        return hash(self.product_id)

    def print(self):
        print(f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime.date, seller: Seller, buyer: Buyer, products: list[Product]):
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller
        self.buyer = buyer
        self.products = products

    def calculate_total_taxes(self) -> float:
        total_taxes = 0.0
        for product in self.products:
            total_taxes += product.calculate_total_taxes()
        return total_taxes

    def calculate_total(self) -> float:
        total = 0.0
        for product in self.products:
            total += product.calculate_total()
        return total

    def print(self):
        print(f"Bill Id:{self.bill_id} , date:{self.sale_date} ")
        print("Seller:")
        self.seller.print()
        print("Buyer:")
        self.buyer.print()
        print("Products:")
        for product in self.products:
            product.print()