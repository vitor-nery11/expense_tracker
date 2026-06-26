def main():
    print('running expense tracker!')

    # get user input for expense.
    get_user_expense()
    
    # Write their expense to a file 
    save_expense_to_file()

    # Read file and summarize expenses.
    summarize_expenses()



def get_user_expense():
    print('Running expense tracker')
    expense_name = input('Enter expense name:')
    expense_amount = float(input('Enter the expense amount '))
    print(f"You've entered {expense_name}, {expense_amount}")

    
    expense_categories = ['Food', 'Home ', 'Work', 'fun', 'misc']


    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f'{i + 1}. {category_name}')

        value_range = f' 1 - {len(expense_categories)}'
        select_index = int(input(f'Enter a category number {value_range}:s'))
        break



def save_expense_to_file():
    print(f'Saving user expense')


def summarize_expenses():
    print(f'Summarize user expense')





if __name__ == '__main__':
    main()
    