from src.checkout import Cart


def test_cart_init():
    my_cart = Cart()
    my_cart1 = Cart()
    my_cart1.add_item("CH1")
    assert len(my_cart.contents) == 0
    assert my_cart.num_oatmeal == 0
    assert my_cart.num_coffee == 0
    assert my_cart.num_chai == 0
    assert my_cart.num_apples == 0
    assert my_cart.total == 0
    assert my_cart1.num_chai == 1


def test_BOGO():
    my_cart = Cart()
    my_cart.add_item("CF1")
    my_cart.print_receipt()
    assert my_cart.total == 11.23
    assert my_cart.num_coffee == 1
    my_cart.add_item("CF1")
    my_cart.print_receipt()
    assert my_cart.total == 11.23
    assert my_cart.num_coffee == 2
    my_cart.add_item("CF1")
    my_cart.print_receipt()
    assert my_cart.total == 22.46
    assert my_cart.num_coffee == 3


def test_CHMK():
    my_cart = Cart()
    my_cart.add_item("MK1")
    my_cart.print_receipt()
    assert my_cart.total == 4.75
    my_cart.add_item("CH1")
    my_cart.print_receipt()
    assert my_cart.total == 3.11
    my_cart.add_item("CH1")
    my_cart.print_receipt()
    assert my_cart.total == 6.22
    my_cart.add_item("MK1")
    my_cart.print_receipt()
    assert my_cart.total == 10.97


def test_APPL():
    my_cart = Cart()
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 6.00
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 12.00
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 13.5
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 18.00


def test_APOM():
    my_cart = Cart()
    my_cart.add_item("OM1")
    my_cart.print_receipt()
    assert my_cart.total == 3.69
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 6.69
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 12.69
    my_cart.add_item("OM1")
    my_cart.print_receipt()
    assert my_cart.total == 13.38


def test_cart_combo1():
    my_cart = Cart()
    my_cart.add_item("CH1")
    my_cart.add_item("AP1")
    my_cart.add_item("CF1")
    my_cart.add_item("MK1")
    my_cart.print_receipt()
    assert my_cart.total == 20.34


def test_cart_combo2():
    my_cart = Cart()
    my_cart.add_item("MK1")
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 10.75


def test_cart_combo3():
    my_cart = Cart()
    my_cart.add_item("AP1")
    my_cart.add_item("AP1")
    my_cart.add_item("CH1")
    my_cart.add_item("AP1")
    my_cart.print_receipt()
    assert my_cart.total == 16.61











