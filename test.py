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

  def contact(self):
    return f"Wybieram numer {self.contact_phone} i dzwonię do {self.name}"

  @property
  def name_length(self):
    return len(self.name)

class BaseContact(Id):
    def __init__(self, private_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone = private_phone

    @property
    def contact_phone(self):
        return self.private_phone

class BusinessContact(Id):
    def __init__(self, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_phone = company_phone

    @property
    def contact_phone(self):
        return self.company_phone

def create_contacts(type, number):
    contacts = []
    number = int(number)

    if type == "private":
        for single_id in range(number):
            contacts.append(BaseContact(name=faker.name(), company=faker.word(), job=faker.job(), e_mail=faker.email(), private_phone=faker.phone_number()))

    elif type == "company":
        for single_id in range(number):
            contacts.append(BusinessContact(name=faker.name(), company=faker.word(), job=faker.job(), e_mail=faker.email(), company_phone=faker.phone_number()))
        
    return contacts

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
    contacts = create_contacts(type_of_id, number_of_id)
    if type_of_id == "private":
        for item in contacts:
            print(f"Imię i nazwisko: {item.name}, Firma: {item.company}, Stanowisko: {item.job}, E-mail:{item.e_mail}, Telefon prywatny: {item.private_phone} \n")
    elif type_of_id == "company":
        for item in contacts:
            print(f"Imię i nazwisko: {item.name}, Firma: {item.company}, Stanowisko: {item.job}, E-mail:{item.e_mail}, Telefon słubowy: {item.company_phone} \n")