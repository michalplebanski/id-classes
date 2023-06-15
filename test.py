from faker import Faker
faker = Faker()

class Id:
  def __init__(self, name, company, job, e_mail):
    self.name = name
    self.company = company
    self.job = job
    self.e_mail = e_mail

  def __str__(self):
    return f'{self.name} {self.company} {self.job} {self.e_mail}'

  def __repr__(self):
    return f'{self.name} {self.company} {self.job} {self.e_mail}'

  def contact(person):
    return f"Kontaktuję się z {person}"


name_1 = Id(name=faker.name(), company="Widoczni", job="Expert", e_mail="mp@gmail.com")
name_2 = Id(name=faker.name(), company="Plus", job="Leader", e_mail="mg@gmail.com")
name_3 = Id(name=faker.name(), company="Icea", job="Senior", e_mail="mk@gmail.com")
name_4 = Id(name=faker.name(), company="Verseo", job="Mid", e_mail="jt@gmail.com")
name_5 = Id(name=faker.name(), company="Tense", job="Junior", e_mail="nn@gmail.com")

list_id = [name_1, name_2, name_3, name_4, name_5]

for person in list_id:
  print(Id.contact(person))

sorted_id_name = sorted(list_id, key=lambda x: x.name)
sorted_id_email = sorted(list_id, key=lambda x: x.e_mail)

