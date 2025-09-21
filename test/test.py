delivery_partner="swiggy"

def hotel():
    item="dosa"

    def order():
        quantity=2
        print(f"your {item}  quantity of {quantity} is ready to deliver from {delivery_partner}")
    order()
hotel()