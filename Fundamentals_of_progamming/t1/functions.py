def create_product(name,price,quantity):
    """
    :param name: name of the product
    :param price: price of the product
    :param quantity: quantity of the product
    :return: the created product
    """
    return [name,price,quantity]

def get_name(product):
    return product[0]

def get_price(product):
    return product[1]

def get_quantity(product):
    return product[2]

def set_name(product,name):
    product[0] = name

def set_price(product,price):
    product[1] = price

def set_quantity(product,quantity):
    product[2] = quantity

def to_string(product):
    return "name: "+get_name(product)+" price: "+str(get_price(product))+" quantity: "+str(get_quantity(product))

def add_product(product_list, name, price, quantity):
    """
    :param product_list: list of product
    :param name: name of the product
    :param price: price of the product
    :param quantity: quantity of the product
    """
    try:
        price = int(price)
        quantity = int(quantity)
        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive integers.")

        new_product = create_product(name, price, quantity)
        product_list.append(new_product)
    except ValueError:
        raise ValueError("Price and quantity must be valid integers.")

def remove_product(product_list, name):
    """
    :param product_list: list of products
    :param name: the name of the product we want to remov
    """
    for product in product_list:
        if get_name(product) == name:
            product_list.remove(product)
            return
    raise ValueError("Product does not exist.")

def list_sorted(product_list):
    """
    :param product_list: list of products
    :return: the list sorted by name
    """
    return sorted(product_list, key=get_name, reverse=True)

def total_price(list):
    """
    :param list: the list of products
    :return: the total price of the products (price*quantity)
    """
    final_price = 0
    for product in list:
        price = get_price(product)
        quantity = get_quantity(product)
        final_price =final_price+price * quantity

    return final_price

#tests
def test_add_product():
    product_list = []
    add_product(product_list, "Apple", "10", "5")
    assert len(product_list) == 1
    assert product_list[0] == ["Apple", 10, 5]

    product_list = []
    try:
        add_product(product_list, "Banana", "-5", "3")
    except ValueError:
        pass
    assert len(product_list) == 0

test_add_product()

def tests():
    product = create_product("Apple", 10, 5)
    assert product == ["Apple", 10, 5], "create_product failed for valid input"
    assert get_name(product) == "Apple", "get_name failed"
    assert get_price(product) == 10, "get_price failed"
    assert get_quantity(product) == 5, "get_quantity failed"

    product2 = create_product("Banana", 15, 8)
    assert product2 == ["Banana", 15, 8], "create_product failed for the product"
    assert get_name(product2) == "Banana", "get_name failed for second product"
    assert get_price(product2) == 15, "get_price failed for second product"
    assert get_quantity(product2) == 8, "get_quantity failed for second product"

tests()
def test_remove_product():
        product_list = [
            create_product("Apple", 10, 5),
            create_product("Banana", 15, 8),
            create_product("Carrot", 20, 3),
        ]

        # Test 1: Remove an existing product
        remove_product(product_list, "Banana")
        assert len(product_list) == 2, "Product list length is incorrect after removal"
        assert all(get_name(p) != "Banana" for p in product_list), "Banana was not removed"

        # Test 2: Remove another existing product
        remove_product(product_list, "Apple")
        assert len(product_list) == 1, "Product list length is incorrect after second removal"
        assert all(get_name(p) != "Apple" for p in product_list), "Apple was not removed"

test_remove_product()
