# VeroSkills

Note:

```
class Account:
    
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
checking = Account('checking', 5000)

checking.deposit(3000)

print(checking.account_type)
print(checking.balance)
```