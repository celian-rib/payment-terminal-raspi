from werkzeug.wrappers import response
import server

# response = server.send_scan("jean", 50)
# transaction = response.json()
# print(transaction)

response = server.get_user_info("michel")
user = response.json()
print(user)