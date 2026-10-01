products = {
    101: "Laptop",
    102: "Mobile Phone",
    103: "Headphones",
    104: "Keyboard"
}

# Display all product codes using keys()
print("Product Codes:")
for code in products.keys():
    print(code)

# Display all product names using values()
print("\nProduct Names:")
for name in products.values():
    print(name)
