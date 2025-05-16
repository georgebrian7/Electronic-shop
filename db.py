obj ={
     "id": 1,
      "name": "Smartphone",
      "brand": "Samsung",
      "model": "Galaxy S24",
      "price": 999.99,
      "category": "Mobile Devices"
}

def readDB(filename="db.json"):
    """
    for reading dB
    """
    with open(filename, mode='r') as jsonfile:
        data = json.load(jsonfile)
