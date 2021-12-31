from __future__ import annotations


class Person:
    name: str
    surname: str
    street_address: str
    postal_code: str
    city: str

    def __init__(self):
        self.name = ""
        self.surname = ""

        self.street_address = ""
        self.postal_code = ""
        self.city = ""

    def __str__(self) -> str:
        return (f"{self.name} {self.surname}\n"
                f"Living at {self.street_address}, {self.postal_code}, {self.city}")


class PersonBuilder:

    def __init__(self, person: Person | None = None):
        self.person = person if person else Person()

    @property
    def named(self) -> PersonNameBuilder:
        return PersonNameBuilder(self.person)

    @property
    def lives(self) -> PersonAddressBuilder:
        return PersonAddressBuilder(self.person)

    def build(self) -> Person:
        return self.person


class PersonNameBuilder(PersonBuilder):
    pass


class PersonAddressBuilder(PersonBuilder):
    pass
