# Group_Expense_Tracker
An Appllication created using Python3
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is Group Expense Tracker where we can create a group and after adding all the expenses, It shows the simplified way of paying debts among group members. 
Along with this, you can add, modify or delete expenses as an when needed.
	
## Technologies
Project is created with:
* Python 3.9
	
## Setup
1. To run this project, make sure you installed python3 in your computer.If not installed, install from [Python](https://www.python.org/downloads/)
2. Run the group_expense_tracker.py file
3. You will see the option
```
  Select:
            1. Create Group
            2. Add Expenses to Group
            3. Update Expenses
            4. Delete Expenses
            5. Get Balance
            6. Exit
```  
  Note : After selecting and entering every required field, you  will be shown the above options.

4. To create new group, Select 1. You will be asked to enter Name and Members of group. Enter these similar to given example format.
```
  Enter Name of Group: Home
  Enter Members of Group (Give Space for Every New Member): A B 
```

5. To add expenses to group, Select 2. You will be asked to enter Name of Expense, Item Name, Value, Paid_by and Owed_by. Enter these similar to given example format.
```
  Enter Name of expense: Fruits and Milk
  Items
  Name: milk
  Value: 50
  Paid_by: [{"A": 40, "B": 10}]
  Owed_by: [{"A": 20,"B": 20, "C": 10}]
  
```
6. After that, you will be asked whether to add more items.
```
  Want to Add More:
                        1. Yes
                        2. NO
```
7. If YES, Enter 1. You will be asked to enter the items. Enter these similar to given example format.
```
  Name: milk
  Value: 50
  Paid_by: [{"A": 40, "B": 10}]
  Owed_by: [{"A": 20,"B": 20, "C": 10}]
```
  Else, Enter 2.
8.To update expenses to group, Select 3. You will be asked to enter Name of Expense, Item Name, Value, Paid_by and Owed_by. Enter these similar to given example format.
```
  Enter Name of expense: Fruits and Milk
  Items
  Name: sweet milk
  Value: 50
  Paid_by: [{"A": 10,"B": 30, "C": 10}]
  Owed_by: [{"A": 40, "B": 10}]
```
9. Again, You will be asked whether to add more items. (Follow Step 6 and 7)
10. To delete expenses to group, Select 4. You will be asked to enter Name of Expense. Enter these similar to given example format.
```
   Enter Name of expense: Fruits and Milk
```
11. To get balance, Select 5. You will be displayed the balances in simplified form.
```
Current Balance :
{'name': 'Home', 'balances': {'A': {'total_balance': -50, 'owes_to': [{'C': 50}], 'owed_by': []}, 'B': {'total_balance': 0, 'owes_to': [], 'owed_by': []}, 'C': {'total_balance': 50, 'owes_to': [], 'owed_by': [{'A': 50}]}}}
```
12. To quit the application, Select 6.

  
