from schema import StudentSchema, PersonSchema

students = StudentSchema().all()
persons = PersonSchema().all()

[print(student) for student in students]
print("\n")
[print(person) for person in persons]
