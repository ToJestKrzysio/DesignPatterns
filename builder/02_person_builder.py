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

    def __init__(self, person):
        super().__init__(person)

    def name(self, name: str) -> PersonNameBuilder:
        self.person.name = name
        return self

    def surname(self, surname: str) -> PersonNameBuilder:
        self.person.surname = surname
        return self


class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address: str) -> PersonAddressBuilder:
        self.person.street_address = street_address
        return self

    def postal_code(self, postal_code: str) -> PersonAddressBuilder:
        self.person.postal_code = postal_code
        return self

    def city(self, city: str) -> PersonAddressBuilder:
        self.person.city = city
        return self


if __name__ == '__main__':
    person_builder = PersonBuilder()
    person = (person_builder
              .named.name("John").surname("Smith")
              .lives.at("London Street 42").city("London").postal_code("42531")
              .build())
    print(person)

    person_2 = (person_builder
                .named.name("Some").surname("Dude")
                .lives.at("Sunset Boulevard 4/2").city("Los Angeles").postal_code("6432")
                .build())
    print(person_2)
