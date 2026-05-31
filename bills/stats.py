from .item import Bill, Product
from .entity import Buyer, Seller

class OrderType:
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        self.bills = bills

    def find_top_sell_product(self) -> tuple[Product, int]:
        product_counts = {}
        # Contamos en cuántas facturas (apariciones) está el producto, no las unidades físicas
        for bill in self.bills:
            for product in bill.products:
                if product in product_counts:
                    product_counts[product] += 1
                else:
                    product_counts[product] = 1
        
        top_product = None
        max_count = -1
        for product, count in product_counts.items():
            if count > max_count:
                max_count = count
                top_product = product
                
        return (top_product, max_count)

    def find_top_two_sellers(self) -> list:
        seller_sales = {}
        for bill in self.bills:
            seller = bill.seller
            total_bill = bill.calculate_total()
            if seller in seller_sales:
                seller_sales[seller] += total_bill
            else:
                seller_sales[seller] = total_bill
                
        sorted_sellers = sorted(seller_sales.items(), key=lambda item: item[1], reverse=True)
        return [seller for seller, total in sorted_sellers[:2]]

    def find_buyer_lowest_total_purchases(self) -> tuple[Buyer, float]:
        buyer_purchases = {}
        for bill in self.bills:
            buyer = bill.buyer
            total_bill = bill.calculate_total()
            if buyer in buyer_purchases:
                buyer_purchases[buyer] += total_bill
            else:
                buyer_purchases[buyer] = total_bill
                
        lowest_buyer = None
        min_purchases = float('inf')
        for buyer, total in buyer_purchases.items():
            if total < min_purchases:
                min_purchases = total
                lowest_buyer = buyer
                
        return (lowest_buyer, min_purchases)

    def order_products_by_tax(self, order_type: OrderType) -> list[tuple[Product, float]]:
        product_taxes = {}
        for bill in self.bills:
            for product in bill.products:
                taxes = product.calculate_total_taxes()
                if product in product_taxes:
                    product_taxes[product] += taxes
                else:
                    product_taxes[product] = taxes
                    
        is_reverse = True if order_type == OrderType.DES else False
        sorted_products = sorted(product_taxes.items(), key=lambda item: item[1], reverse=is_reverse)
        return sorted_products

    def show(self):
        print("Bills")
        for bill in self.bills:
            bill.print()