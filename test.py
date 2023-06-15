from faker import Faker
faker = Faker()

class Id:
  def __init__(self, name, company, job, e_mail):
    self.name = name
    self.company = company
    self.job = job
    self.e_mail = e_mail

name_1 = Id(name=faker.name(), company="Widoczni", job="Expert", e_mail="mp@gmail.com")
name_2 = Id(name=faker.name(), company="Plus", job="Leader", e_mail="mg@gmail.com")
name_3 = Id(name=faker.name(), company="Icea", job="Senior", e_mail="mk@gmail.com")
name_4 = Id(name=faker.name(), company="Verseo", job="Mid", e_mail="jt@gmail.com")
name_5 = Id(name=faker.name(), company="Tense", job="Junior", e_mail="nn@gmail.com")

list_id = [name_1, name_2, name_3, name_4, name_5]

for item in list_id:
  print(f"{item.name} {item.e_mail}")