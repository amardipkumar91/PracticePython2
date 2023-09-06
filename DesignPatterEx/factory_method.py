import json
class Vehicle(object):
    def __init__(self, id, name, company):
        self.id = id
        self.name = name
        self.company = company

class VechicleInfo(object):
    def info(self, vechile, type):
        infor = get_info(type)
        return infor(vechile)

def get_info(type):
    if type == '2':
        return _bike_info
    elif type == '4':
        return _car_info
    elif type == '8':
        return _truck_info
    else:
        raise ValueError(type)

def _bike_info(vehicle):
    payload = {'id' : vehicle.id, 'name' : vehicle.name, 'company' : vehicle.company, 'cost' : 50000}
    return json.dumps(payload)

def _car_info(vehicle):
    payload = {'id' : vehicle.id, 'name' : vehicle.name, 'company' : vehicle.company, 'cost' : 800000}
    return json.dumps(payload)

def _truck_info(vehicle):
    payload = {'id' : vehicle.id, 'name' : vehicle.name, 'company' : vehicle.company, 'cost' : 9000000}
    return json.dumps(payload)

obj = Vehicle(1, 'passion', 'hero')
information = VechicleInfo()
data = information.info(obj,'2')
print(data)

information = VechicleInfo()
data = information.info(obj,'4')
print(data)

information = VechicleInfo()
data = information.info(obj,'8')
print(data)


