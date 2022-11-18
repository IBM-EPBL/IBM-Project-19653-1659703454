import http.client

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "dbe56f5a1cmsh4f89bf562e2d75dp13e937jsna811cd541dd4",
    'X-RapidAPI-Host': "calorieninjas.p.rapidapi.com"
    }

conn.request("GET", "/v1/nutrition?query=rice", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
Footer