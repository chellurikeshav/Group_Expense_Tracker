import time
import math
from turtle import pos
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class GroupExpenseTracker():

    def __init__(self):
        #Initialization
        self.group = {}
        self.balance = {}
        self.expenses = []
        self.other_hold = False
        self.position = 0
        self.waiting_list = [math.inf]

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
    
    #Prechecking the order
    def PreCheckOrder(self,index):
        self.waiting_list.append(index)
        #Busy Waiting Loop
        while self.other_hold or min(self.waiting_list) != index :
            pass
        self.other_hold = True

    #Postchecking the order
    def PostCheckOrder(self,index):
        self.waiting_list.remove(index)
        self.other_hold = False

    #----------------------------------------------------------#
    #Features
    #Create Group
    def CreateGroup(self,new_group):
        self.group = new_group
        #Define balances   
        self.balance["balances"] = {}
        self.balance["name"] = self.group["name"]
        for member in self.group["members"]:
            self.DefineBalances(member)
        return 'Group Created Successfully'
    
    #Add Expenses
    def AddExpenses(self,expense):
        #Checking Parameters
        self.position += 1
        index = self.position
        self.PreCheckOrder(index)

        self.expenses.append(expense)
        self.CheckNewMembers(expense)
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()

        self.PostCheckOrder(index)
        return 'Expense Added Successfully!'
    
    #Update Expenses
    def UpdateExpenses(self,new_expense):
        #Checking Parameters
        self.position += 1
        index = self.position
        self.PreCheckOrder(index)

        for expense in self.expenses:
            if expense["name"] == new_expense["name"]:
                expense["items"] = new_expense["items"]
        self.CheckNewMembers(new_expense)
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()

        self.PostCheckOrder(index)
        return 'Expense Modified Sucessfully!'
    
    #Delete Expenses
    def DeleteExpenses(self,del_expense):
        #Checking Parameters
        self.position += 1
        index = self.position
        self.PreCheckOrder(index)

        for i in range(len(self.expenses)):
            if self.expenses[i] == del_expense:
                self.expenses.pop(i)
                break
        
        #ReDefine balances
        self.balance["balances"] = {}
        for member in self.group["members"]:
            self.DefineBalances(member)
        self.ModifyBalances()
        
        self.PostCheckOrder(index)
        return 'Expense Deleted Sucessfully!'
    
    #Get Balance
    def GetBalance(self):
        return self.balance

expense_tracker = GroupExpenseTracker()

@csrf_exempt
def CreateNewGroup(request):
    if request.method == 'POST':
        jsonData = JSONParser().parse(request)
        return JsonResponse(expense_tracker.CreateGroup(jsonData),safe = False)
    return JsonResponse('To Create Group, Select POST request.',safe = False)

@csrf_exempt
def AddExpenseToGroup(request):
    if request.method == 'POST':
        if expense_tracker.group == {}:
            return JsonResponse('No Group Created ! Create a group to ADD expenses',safe = False)
        jsonData = JSONParser().parse(request)
        return JsonResponse(expense_tracker.AddExpenses(jsonData),safe = False)
    return JsonResponse('To Add Expense, Select POST request.',safe = False)

@csrf_exempt
def UpdateExpenseInGroup(request):
    if request.method == 'PUT':
        if expense_tracker.group == {}:
            return JsonResponse('No Group Created !',safe = False)
        jsonData = JSONParser().parse(request)
        if not expense_tracker.CheckExpense(jsonData['name']):
            return JsonResponse('Expense not found ! Please Try Again.',safe = False)
        return JsonResponse(expense_tracker.UpdateExpenses(jsonData),safe = False)
    return JsonResponse('To Update Expense, Select PUT request.',safe = False)

@csrf_exempt
def DeleteExpenseInGroup(request):
    if request.method == 'DELETE':
        if expense_tracker.group == {}:
            return JsonResponse('No Group Created !',safe = False)
        jsonData = JSONParser().parse(request)
        if not expense_tracker.CheckExpense(jsonData):
                print('Expense not found ! Please Try Again.')
        return JsonResponse(expense_tracker.DeleteExpenses(jsonData),safe = False)
    return JsonResponse('To Update Expense, Select DELETE request.',safe = False)

@csrf_exempt
def GetBalanceExpense(request):
    if request.method == 'GET':
        if expense_tracker.group == {}:
            return JsonResponse('No Group Created !',safe = False)
        return JsonResponse(expense_tracker.GetBalance(),safe = False)
    return JsonResponse('To Get Balance, Select GET request.',safe = False)

