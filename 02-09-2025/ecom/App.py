from product_manager import (
    create_product, read_all_products, read_by_product_name, update_product, delete_product, products,
    read_by_id, read_by_product_tags, read_by_product_description
)
from product import Product

def menu():
    message =  \
    "\n1. Add Product" \
    "\n2. View All Products" \
    "\n3. Search Product by Name" \
    "\n4. Update Product" \
    "\n5. Delete Product" \
    "\n6. Search Product by ID" \
    "\n7. Search Product by Tag" \
    "\n8. Search Product by Description" \
    "\n9. Exit\n" \
    "Enter your choice (1-9): "
    
    choice = int(input(message))
    if choice == 1:
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        category = input("Enter product category: ")
        tags = input("Enter product tags (comma separated): ").split(",")
        tags = [t.strip() for t in tags]
        stock = int(input("Enter product stock: "))
        price = float(input("Enter product price: "))
        create_product(product_id, name, description, category, tags, stock, price)
        print("Product added.")
    elif choice == 2:
        all_products = read_all_products()
        print("All Products:")
        for prod in all_products:
            print(prod)
    elif choice == 3:
        name = input("Enter product name to search: ")
        index = read_by_product_name(name)
        if index != -1:
            print(f"Product '{name}' found: {products[index]}")
        else:
            print(f"Product '{name}' not found.")
    elif choice == 4:
        product_id = int(input("Enter product ID to update: "))
        index = read_by_id(product_id)
        if index != -1:
            print("Old product details:")
            print(products[index])
            name = input("Enter new product name: ")
            description = input("Enter new product description: ")
            category = input("Enter new product category: ")
            tags = input("Enter new product tags (comma separated): ").split(",")
            tags = [t.strip() for t in tags]
            stock = int(input("Enter new product stock: "))
            price = float(input("Enter new product price: "))
            update_product(product_id, name, description, category, tags, stock, price)
            print("Product updated.")
        else:
            print(f"Product with ID {product_id} not found.")
    elif choice == 5:
        name = input("Enter product name to delete: ")
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            delete_product(name)
            print("Product deleted (if it existed).")
        else:
            print("Delete operation cancelled.")
    elif choice == 6:
        pid = int(input("Enter product ID to search: "))
        index = read_by_id(pid)
        if index != -1:
            print(f"Product with ID {pid} found: {products[index]}")
        else:
            print(f"Product with ID {pid} not found.")
    elif choice == 7:
        tag = input("Enter tag to search: ")
        results = read_by_product_tags(tag)
        if results:
            print("Products with tag '{}':".format(tag))
            for idx, prod in results:
                print(prod)
        else:
            print(f"No products found with tag '{tag}'.")
    elif choice == 8:
        keyword = input("Enter keyword to search in description: ")
        results = read_by_product_description(keyword)
        if results:
            print("Products with keyword '{}':".format(keyword))
            for idx, prod in results:
                print(prod)
        else:
            print(f"No products found with keyword '{keyword}'.")
    return choice

def menus():
    print("Product Management System")
    choice = menu()
    while choice != 9:
        choice = menu()
    print("Thank you for using the Product Management System.")

menus()