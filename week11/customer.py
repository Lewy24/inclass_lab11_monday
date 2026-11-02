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

