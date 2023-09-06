from marshmallow import Schema, fields, post_load
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'{ self.name } is {self.age} years old.'


class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)
        

# input_data = {}
# input_data['name'] = input('what is your name?')
# input_data['age'] = input('what is your age?')

# person = Person(name = input_data['name'], age = input_data['age'])

# schema = PersonSchema()
# result = schema.dump(person)
# print (result)

# #---

# person_data = {"name": 'amardip', "age": 24}
# pp = PersonSchema()
# print (pp.load(person_data))

#--------

personSchema = Schema.from_dict( {"name" : fields.Str(), "age" : fields.Int()})

person = Person(name = "vicky", age = 30)
schema = personSchema()
result = schema.dump(person)
print (result)

personData = {"name" : 30, "age": 'amard'}
ss = PersonSchema()
result = ss.load(personData)
print (result)