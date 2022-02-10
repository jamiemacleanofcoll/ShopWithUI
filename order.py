class CreditCard:
    valid_month: int
    valid_year: int
    owner: str
    number: str
    cvv: int

    def __init__(self, valid_month, valid_year, owner, number, cvv):
        self.valid_month = valid_month
        self.valid_year = valid_year
        self.owner = owner
        self.number = number
        self.cvv = cvv


class Address:
    first_name: str
    last_name: str
    street: str
    number: int
    zip_code: int
    city: str

    def __init__(self, first_name, last_name, street, number, zip_code, city):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.number = number
        self.zip_code = zip_code
        self.city = city


class Order:
    address: Address
    credit_card: CreditCard
    card: dict[int, int]

    def __init__(self, address, credit_card, card):
        self.address = address
        self.credit_card = credit_card
        self.card = card
