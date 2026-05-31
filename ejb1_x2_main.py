"""El objetivo general del ejercicio es simular que existe información sobre las compras y ventas de productos, 
en las que intervienen clientes y vendedores; a continuación, deberemos implementar funciones que nos permitan
 extraer información estadística.
Se debe crear en el paquete llamado “bills” con la siguiente estructura:
bills/
        __init__.py
        entity.py
        item.py
        stats.py
En el módulo denominado "entity.py", se deben establecer las clases siguientes: "Person", "Buyer" y "Seller", 
las cuales representan a clientes y vendedores.

La clase "Person" es una clase abstracta que contiene el método abstracto "print()" y contiene los atributos 
comunes de las clases "Buyer" y "Seller". El alumno debe identificar estos atributos y crear un constructor 
con estos atributos.

La clase "Buyer" representa a un comprador, cuyos atributos son el dni(dni: str), el nombre completo 
(full_name: str), la edad (age: int), el correo electrónico (email: str), el teléfono móvil  (mobile: str) y 
su domicilio  (address: str). El alumno debe crear un constructor con estos atributos.
La clase "Seller" representa a un comprador, cuyos atributos son el dni (dni: str), correo (email: str),
teléfono móvil (mobile: str), domicilio fiscal (bussines_name: str), razón social (bussines_address: str). 
El alumno debe crear un constructor con estos atributos.

En el módulo denominado "Item", se deben establecer las clases siguientes: "Product", "Tax", las cuales 
representan las facturas, los productos e impuestos.

La clase denominada "Tax" se refiere a los impuestos que se derivan de cada producto. Los tipos de impuestos
que se presentan son los siguientes: el impuesto al valor agregado (IVA) y el impuesto a la salida de divisas 
(ISD). Los dos impuestos representan un porcentaje de gravamen en función del precio por la cantidad. 
Sus atributos son el identificador del impuesto (tax_id: str), tipo impuesto (tax_type: TaxType) y 
porcentaje de retención (percentage: float). Nótese existe un parámetro tipo enumeración TaxType, cuya 
función es identificar el tipo de impuesto.  El alumno debe crear un constructor con los atributos señalados.

La clase "Product" representa a un producto, cuyos atributos son el identificador (product_id: str), 
el nombre (name: str), la fecha de caducidad (expiration_date: datetime), el código de barras (bar_code: str), 
la cantidad (quantity: int), el precio (price: float) y una lista de impuestos (taxes: list[Tax]). 
El alumno debe crear un constructor para estos atributos.

Esta debe incluir los siguientes métodos:

calculate_tax(tax:Tax): Se trata de una función que permite calcular el valor total del impuesto se calcula 
mediante la multiplicación de la cantidad por el precio y posteriormente multiplicar por el porcentaje 
de ese impuesto. El parámetro "tax" permite la filtración de la lista en función del tipo de impuesto, 
sea IVA o ISD. Para el cálculo del ISD se debe multiplicar por un valor factor constante (ISD_FACTOR) 
igual a 0.25. El valor a retornar es un número de tipo “float”.

calculate_total_taxes(): Se trata de una función que posibilita la determinación de la suma total de los 
impuestos depositados en una factura, es decir, todos aquellos que se encuentran incluidos en la lista de 
impuestos, para esto se debe hacer uso de la función “calculate_tax(tax)”. El valor a retornar es un número 
de tipo “float”.

calculate_total(): Permite calcular el total de un producto de la siguiente manera: se debe multiplicar el 
valor total por la cantidad y luego se deberá sumar con el total de impuestos “calculate_total_taxes”.
El valor a retornar es un número de tipo “float”.

La clase “Bill” se refiere a una factura y representa una transacción realizada entre un comerciante y un 
comprador; además, contiene los productos que se vendieron en una transacción. Los atributos son 
el id factura(bill_id:str), fecha de emisión(sale_date: datetime), un vendedor (seller: Seller), 
un comprador (buyer: Buyer), y una lista de productos(products: list[Product]). Esta debe incluir el siguiente 
método:
calculate_total(): Es una función que sirve para calcular el total de la factura de la siguiente manera: se debe
 sumar el total individual de cada factura. El valor a retornar es un número de tipo “float”.

En el módulo denominado "Stats", en este módulo se deben crear la clase "Statistics", este sirve para realizar 
un análisis estadístico con la información de las facturas.

La clase Statistics tiene como atributo una lista de facturas, cuyo propósito es obtener información estadística 
del comercio de los productos.

Los métodos de esta clase son:

find_top_sell_product(): Se trata de una función que permite buscar el producto más vendido, es decir, 
el producto que aparece con mayor frecuencia en las facturas. El valor devolver es una tupla donde el primer 
valor es tipo “Product” y el segundo es la cantidad de apariciones del producto. Por ejemplo:
(<bills.item.Product object at 0x000002D8F6DE2DD0>, 6)

find_top_two_sellers(): Es una función que permite obtener hasta los 2 vendedores con el mayor importe total 
de ventas, pertenecientes a la clase "Seller". La función debe devolver una lista ordenada de mayor a menor 
importe, con un máximo de 2 elementos. Si solo existe un vendedor con ventas registradas, la lista contendrá 
únicamente ese vendedor. Por ejemplo:
[<bills.entity.Seller object at 0x000002D8F6983BD0>, <bills.entity.Seller object at 0x000002D8F6DE2F50>]

find_buyer_lowest_total_purchases(): Se trata de una función que permite buscar al comprador con el menor 
importe total de compras. El valor a devolver es una tupla en donde el primer valor es una entidad de tipo 
“Buyer” y el segundo el total de ventas.  Por ejemplo:
(<bills.entity.Buyer object at 0x0000020A8789F190>, 53.5)

order_products_by_tax(order_type:orderType): Se trata de una función que permite devolver una lista ordenada 
de todos productos. El parámetro order_type, es un tipo de enumeración OrderType, nos permite identificar 
si el orden es ascendente o descendente, y debe ordenar por la suma total de impuestos para un producto. 
El valor a devolver es una lista de tuplas en donde cada tupla se compone de entidad tipo “Product” y la 
suma total de impuestos. Por ejemplo:
[(<bills.item.Product object at 0x000001A5B79D2A50>, 180.0), (<bills.item.Product object at 0x000001A5B79D2910>, 37.08)]

"""

from bills import *
from util_package.bill_manager import BillManager



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
bill_manager = BillManager()
bills = bill_manager.create_bills_example()
statistics = Statistics(bills)
statistics.show()
print(statistics.find_top_sell_product())
print(statistics.find_buyer_lowest_total_purchases())
print(statistics.find_top_two_sellers())
print(statistics.order_products_by_tax(OrderType.DES))
