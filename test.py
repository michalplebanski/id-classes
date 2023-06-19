import sys
import logging
from faker import Faker

faker = Faker()

private_id = []
company_id = []

class Id:
  def __init__(self, name, company, job, e_mail):
    self.name = name
    self.company = company
    self.job = job
    self.e_mail = e_mail

  def __repr__(self):
    return f'{self.name} {self.company} {self.job} {self.e_mail}'

class BaseContact(Id):
    def __init__(self, private_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone = private_phone

    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.name}"

    def name_length(self):
        name_given = len(self.name)
        return f"Długość imienia i nazwiska to: {name_given}"

class BusinessContact(Id):
    def __init__(self, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_phone = company_phone

    def contact(self):
        return f"Wybieram numer {self.company_phone} i dzwonię do {self.name}"

    def name_length(self):
        name_given = len(self.name)
        return f"Długość imienia i nazwiska to: {name_given}"

def create_contacts(type, number):
    if type == "private":
        for single_id in range(1, int(number)):
            single_id = BaseContact(name=faker.name(), company=faker.word(), job=faker.job(), e_mail=faker.email(), private_phone=faker.phone_number())
            private_id.append(single_id)
            for item in private_id:
                print(f"Imię i nazwisko: {item.name}, Firma: {item.company}, Stanowisko: {item.job}, E-mail:{item.e_mail}, Telefon prywatny: {item.private_phone} \n")

    elif type == "company":
        for single_id in range(1, int(number)):
            single_id = BusinessContact(name=faker.name(), company=faker.word(), job=faker.job(), e_mail=faker.email(), company_phone=faker.phone_number())
            company_id.append(single_id)
            for item in company_id:
                print(f"Imię i nazwisko: {item.name}, Firma: {item.company}, Stanowisko: {item.job}, E-mail:{item.e_mail}, Telefon prywatny: {item.company_phone} \n")

def validation_number(number):
    try:
        int(number)
    except:
        logging.warning("Nie podano cyfry!")
        exit(1)

if __name__ == "__main__":
    type_of_id = input("Jaką wizytówkę chcesz stworzyć? Wpisz: 'private' or 'company: '")
    if type_of_id != "private" and type_of_id != "company":
        logging.warning("Podano zły typ wizytówki!")
        exit(1)
    number_of_id = input("Ile wizytówek chcesz stworzyć? ")
    validation_number(number_of_id)
    create_contacts(type_of_id, number_of_id)