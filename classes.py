class BudgetCategory:
    def __init__(self, category):
        self.__budget_categories = {}
        self.__expense_categories = {}
        self.__category = category

    def set_budget(self, category, budget):
        self.__budget_categories[category] = budget
        

    def add_expense(self, category, expense):
        if category not in self.__expense_categories:
            self.__expense_categories[category] = []
        self.__expense_categories[category].append(expense)

    def display_category_summary(self, category):
        if category not in self.__budget_categories:
            print(f"{category} does not exist.")
        if category not in self.__expense_categories:
            print(f"{category} does not exist.")
        return self.__budget_categories[category] - sum(self.__expense_categories[category])

def main():
    budget_manager = BudgetCategory("Main Budget")

    while True:
        try:
            print("\n1. Add category and budget\n2. Add expense to category\n3. Display Category Summary\n4. Exit Program")
            choice = input("\nFrom the above menu, please type your selection:\n")

            if choice == '1':
                category = input("What category would you like to add?\n")
                amount = float(input("What is your budget for this category?\n$ "))
                budget_manager.set_budget(category, amount)
                print(f"You have set a category of {category}, with a total budget of {amount}")
            
            elif choice == '2':
                category = input("What category would you like to add an expense to?\n")
                amount = float(input("How much is the expense?\n$"))
                budget_manager.add_expense(category, amount)
                print(f"You have added an expense of ${amount} to category {category}>")

            elif choice == '3':
                category = input("Which category would you like the summary for?")
                print(f"Here is how much you have left of your budget:  ${budget_manager.display_category_summary(category)} from category {category}.")

            elif choice == '4':
                print("Closing program.......")
                break

        except Exception as e:
            print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()
