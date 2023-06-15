class Id:
  def __init__(self, surname, name, company, job, e_mail):
    self.surname = surname
    self.name = name
    self.company = company
    self.job = job
    self.e_mail = e_mail

name_1 = Id(surname="Michał", name="Plebański", company="Widoczni", job="Expert", e_mail="mp@gmail.com")
name_2 = Id(surname="Monika", name="Grabowska", company="Plus", job="Leader", e_mail="mg@gmail.com")
name_3 = Id(surname="Mikołaj", name="Kuś", company="Icea", job="Senior", e_mail="mk@gmail.com")
name_4 = Id(surname="Jula", name="Tychońska", company="Verseo", job="Mid", e_mail="jt@gmail.com")
name_5 = Id(surname="Nina", name="Ninowska", company="Tense", job="Junior", e_mail="nn@gmail.com")

list_id = [name_1, name_2, name_3, name_4, name_5]

for item in list_id:
  print(f"{item.surname} {item.name} {item.e_mail}")