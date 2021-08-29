import server

response = server.send_scan("jean", -50)
transaction = response.json()
print(transaction)