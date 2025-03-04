class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.aux_withdraw = []

    def deposit(self, amount, description=""):
        # Append to ledger
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        # Check funds and append to ledger if possible
        if self.check_funds(amount):
           self.ledger.append({'amount': -amount, 'description': description})
           self.aux_withdraw.append({'amount': amount})
           return True
        else:
            return False 

    def get_balance(self):
        # Calculate and return balance
        self.balance = 0
        self.out_money = 0
        
        for entry in range(0,len(self.ledger)):
            self.balance += self.ledger[entry]['amount']

            
            #self.out_money += self.aux_withdraw[entry]['amount']
        return self.balance

    def transfer(self, amount, category):
        # Check funds and perform transfer if possible
        if self.withdraw(amount,f'Transfer to {category.name}'):
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        # Compare amount with balance
        #print(self.get_balance())
        return self.get_balance() >= amount

    def __str__(self):
        # Title line
        title = f"{self.name:*^30}\n"  # Center the name in 30 characters, surrounded by *

        # Ledger entries
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]  # First 23 characters of the description
            amount = f"{entry['amount']:.2f}"  # Format amount to 2 decimal places
            items += f"{description:<23}{amount:>7}\n"  # Left-align description, right-align amount

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        # Combine everything
        return title + items + total

def create_spend_chart(categories): #I could't make this function right so I freakd out and asked chatGPT to do it for me
    # Step 1: Calculate total withdrawals for each category
    cat_amount = []
    for cat in categories:
        total_withdrawals = sum(entry['amount'] for entry in cat.ledger if entry['amount'] < 0)
        cat_amount.append(abs(total_withdrawals))  # Use absolute value for withdrawals

    # Step 2: Calculate percentages (rounded down to the nearest 10)
    total_withdrawals = sum(cat_amount)
    cat_per100 = [(amount / total_withdrawals * 100) // 10 * 10 for amount in cat_amount]

    # Step 3: Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):  # From 100 to 0 in steps of 10
        chart += f"{i:3}| "  # Add the percentage label
        for percent in cat_per100:
            chart += "o  " if percent >= i else "   "  # Add 'o' or spaces
        chart += "\n"

    # Step 4: Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Step 5: Add category names vertically
    max_name_length = max(len(cat.name) for cat in categories)
    category_names = [cat.name.ljust(max_name_length) for cat in categories]  # Normalize name lengths

    for i in range(max_name_length):
        chart += "     "  # Add padding for alignment
        for name in category_names:
            chart += name[i] + "  "  # Add letter with spacing
        if i < max_name_length - 1:
            chart += "\n"  # New line except for the last line

    return chart
   # return chart.rstrip()  # Remove trailing newline