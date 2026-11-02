#Exercise 1
print("---Exercise 1---")

customer = {
    "name": "Alice",
    "Name": "Not Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": "12400"

}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("---Exercise 2---")
customer['phone'] = "555-5555"
print(customer)
customer["tier"] = "Platinum"
print(customer)
del customer["Name"]
print(customer)


print(customer.get("Name", "Not Found"))
print(customer.get("ytd_spend", "NaN")) #Not a Number

print("---Exercise 3---")
print(customer.get("email", "no email on file"))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught:", error)
