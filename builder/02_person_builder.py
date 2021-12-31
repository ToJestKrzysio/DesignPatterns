class Person:
    name: str
    surname: str
    id: str
    street_address: str
    postal_code: str
    city: str

    def __init__(self):
        self.name = ""
        self.surname = ""
        self.id = ""

        self.street_address = ""
        self.postal_code = ""
        self.city = ""

    def __str__(self) -> str:
        return (f"{self.name} {self.surname} using personal id {self.id}\n"
                f"Living at {self.street_address}, {self.postal_code}, {self.city}")
