from fwf_Mapper import FwfMapper
width_mapping = {
    "arId": (3,5),
    "arName": (5, 15),
    "arDate": (15, 22),
    "arAmount": (25, 35),
}
trailing = "0"

field_mapping = {
    "arId": "id",
    "arName": "name",
    "arDate": "date",
    "arAmount": "amount",
}

data = [{
    "id": 1,
    "name": "alfajor",
    "date": "20200101",
    "amount": "10000"
},
{
    "id": 2,
    "name": "chocolate",
    "date": "20200102",
    "amount": "20000"
},
{
    "id": 3,
    "name": "galleta",
    "date": "20200103",
    "amount": "30000"
},
{
    "id": 4,
    "name": "dulce de leche",
    "date": "20200104",
    "amount": "40000"
}]

mapper = FwfMapper(width_mapping, trailing, field_mapping, data)
print(mapper.is_all_mapped())
print(mapper.get_result())