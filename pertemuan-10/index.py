class InvalidOptionError(Exception):
    def __init__(self, option, message=None):
        self.option = option
        self.message = message or f"Invalid option: {option}"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class DuplicateInputError(Exception):
    def __init__(self, product, message=None):
        self.product = product
        self.message = message or f"Product '{product}' already exists."
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ProductNotFoundError(Exception):
    def __init__(self, product, message=None):
        self.product = product
        self.message = message or f"Product '{product}' not found."
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ProductManager:
    def __init__(self):
        self.products = ['apple', 'banana', 'orange']

    def add_product(self, name: str):
        name = name.strip()
        if not name:
            raise ValueError("Product name cannot be empty.")
        if name in self.products:
            raise DuplicateInputError(name)
        self.products.append(name)

    def delete_product(self, name: str):
        name = name.strip()
        if name not in self.products:
            raise ProductNotFoundError(name)
        self.products.remove(name)

    def list_products(self):
        return list(self.products)

def main():
    pm = ProductManager()

    while True:
        print("\n== Product Menu ==")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice not in {"1", "2", "3"}:
                raise InvalidOptionError(choice)

            if choice == "1":
                name = input("\nProduct name to add: ").lower()
                try:
                    pm.add_product(name)
                    print(f"\nAdded: {name.strip()}")
                except DuplicateInputError as e:
                    print(f"\nError: {e}")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "2":
                name = input("\nProduct name to delete: ").lower()
                try:
                    pm.delete_product(name)
                    print(f"\nDeleted: {name.strip()}")
                except ProductNotFoundError as e:
                    print(f"\nError: {e}")

            else:
                print("\nExiting.")
                break

            if pm.list_products():
                print("\nProducts:", ", ".join(pm.list_products()))
            else:
                print("\nNo products.")

        except InvalidOptionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()