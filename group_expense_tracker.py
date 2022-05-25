class GroupExpenseTracker():

    #Initialization
    def __init__(self):
        #Initialize Group
        self.group = {}
        #Initialize Balances    
        self.balance = {}
        #Initialize Expenses
        self.expenses = []

    #Defining default Balance when Adding, Modifying or Deleting Expenses
    def DefineBalances(self,member):
        self.balance["balances"][member] = {
            "total_balance": 0,
            "owes_to": [],
            "owed_by": []
        }

    #Checking if there is new members in group
    def CheckNewMembers(self,expense):
        for item in expense["items"]:
            exp = ["paid_by","owed_by"]
            for term in exp:
                for member in (item[term][0].keys()):
                    if member not in self.balance["balances"].keys():
                        self.DefineBalances(member)
                        self.group["members"].append(member)

    #Checking Whether the Expense is present in Expenses
    def CheckExpense(self,expense_name):
        for expense in self.expenses:
            if expense["name"] == expense_name:
                return True
        return False

    #Modifying Expenses for Adding or Updating
    def ModifyBalances(self):
        #Checking if group is created or not
        if self.group == {}:
            print('No Group Created')
            return 0
        #Recursive Function to Simplify Debts
        def Simplify_Recursion(net):
            index_members = dict(zip([x for x in range(len(net))],self.group["members"]))
            giver = net.index(min(net))
            reciever = net.index(max(net))
            if net[giver]==0 and net[reciever]==0:
                return 0
            min_of_trade = min(-net[giver],net[reciever])
            net[giver]+=min_of_trade
            net[reciever]-=min_of_trade
            self.balance["balances"][index_members[giver]]["owes_to"].append({
                index_members[reciever]:min_of_trade
            })
            self.balance["balances"][index_members[reciever]]["owed_by"].append({
                index_members[giver]:min_of_trade
            })
            Simplify_Recursion(net)
        net_change_cash = {}
        #Initializing Balances
        for mem in self.group["members"]:
            net_change_cash[mem]=0
        #calculating net expenses of each person
        for expense in self.expenses:
            for item in expense["items"]:
                exp = ["paid_by","owed_by"]
                for term in exp:
                    for mem,val in item[term][0].items():
                        if term == "paid_by":
                            net_change_cash[mem]+=val
                        if term == "owed_by":
                            net_change_cash[mem]-=val
        for memb in self.group["members"]:
            self.balance["balances"][memb]["total_balance"] = net_change_cash[memb]
        Simplify_Recursion(list(net_change_cash.values()))

    #Features
    #Create Group
    def CreateGroup(self,name,members):
        #Define group
        self.group = {"name": name,"members": members}
        self.balance["name"] = name
        #Define balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        print('Group Created Successfully!')

    #Add Expenses
    def AddExpenses(self,expense):
        #Checking if group is created or not
        if self.group == {}:
            print('No Group Created')
            return 0
        self.expenses.append(expense)
        self.CheckNewMembers(expense)
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()
        print('Expense Added Successfully!')

    #Update Expenses
    def UpdateExpenses(self,new_expense):
        #Checking if group is created or not
        if self.group == {}:
            print('No Group Created')
            return 0
        for expense in self.expenses:
            if expense["name"] == new_expense["name"]:
                expense["items"] = new_expense["items"]
        self.CheckNewMembers(new_expense)
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()
        print('Expense Modified Sucessfully!')

    #Delete Expenses
    def DeleteExpenses(self,del_expense_name):
        #Checking if group is created or not
        if self.group == {}:
            print('No Group Created')
            return 0
        for i in range(len(self.expenses)):
            if self.expenses[i]["name"] == del_expense_name:
                self.expenses.pop(i)
                break
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()
        print('Expense Deleted Sucessfully!')

    #Get Balance
    def GetBalance(self):
        #Checking if group is created or not
        if self.group == {}:
            print('No Group Created')
            return 0
        print('Current Balance :')
        return self.balance

expense_tracker = GroupExpenseTracker()
while True:
    value = int(input('''
            Select:
            1. Create Group
            2. Add Expenses to Group
            3. Update Expenses
            4. Delete Expenses
            5. Get Balance
            6. Exit
    '''))
    
    if value == 1:
        name = input('Enter Name of Group: ')
        members_of_group = input('Enter Members of Group (Give Space for Every New Member): ').split()
        expense_tracker.CreateGroup(name,members_of_group)
    
    if value == 2:
        print('''
            Enter Expense in to ADD given format
            Ex :{"name": "Fruits and Milk",
                "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                            {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]} 
        ''')
        name_expense = input('Enter Name of expense: ')
        items = []
        while True:
            print('Items')
            name = input('Name: ')
            value = int(input('Value: '))
            paid_by = input('Paid_by: ')
            owed_by = input('Owed_by: ')

            new_dict = {"name":name,"value":value,"paid_by":eval(paid_by),"owed_by":eval(owed_by)}
            items.append(new_dict)

            add_more = int(input('''
                    Want to Add More:
                        1. Yes
                        2. NO
            '''))
            if add_more == 2:
                break
        print('\n')
        add_expense = {"name":name_expense,"items":items}
        expense_tracker.AddExpenses(add_expense)
    
    if value == 3:
        print('''
            Enter Expense in to UPDATE given format
            Ex :{"name": "Fruits and Milk",
                "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
                            {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]} 
        ''')
        name_expense = input('Enter Name of expense: ')
        if not expense_tracker.CheckExpense(name_expense):
            print('Expense not found ! Please Try Again.')
            continue
        items = []
        while True:
            print('Items')
            name = input('Name: ')
            value = int(input('Value: '))
            paid_by = input('Paid_by: ')
            owed_by = input('Owed_by: ')

            new_dict = {"name":name,"value":value,"paid_by":eval(paid_by),"owed_by":eval(owed_by)}
            items.append(new_dict)

            add_more = int(input('''
                    Want to Add More:
                        1. Yes
                        2. NO
            '''))
            if add_more == 2:
                break
        print('\n')
        update_expense = {"name":name_expense,"items":items}
        expense_tracker.UpdateExpenses(update_expense)
    
    if value == 4:
        name_expense = input('Enter Name of expense: ')
        if not expense_tracker.CheckExpense(name_expense):
            print('Expense not found ! Please Try Again.')
            continue
        expense_tracker.DeleteExpenses(name_expense)
    
    if value == 5:
        balance = expense_tracker.GetBalance()
        print(balance)
    
    if value == 6:
        print('Exiting the Application. Thank you!!!')
        break

