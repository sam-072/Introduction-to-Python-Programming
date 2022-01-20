# Code by : Sam._.072

def import_and_create_bank(filename):
    
    bank = {}

    # your code here
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split(":")
        if len(lst)<=1:
            continue
        key = lst[0].strip()
        value = lst[1].strip()
        try:
            value = float(value)
            bank[key] = bank.get(key,0)+value
        except:
            continue
    f.close()

    return bank


def signup(user_accounts, log_in, username, password):
    
    # your code here
    if username in user_accounts or len(password)<8 or username == password:
        return False
    lc, uc, no = False, False, False
    for i in password:
        if 'a'<= i <='z':
            lc = True
        if 'A' <= i <= 'Z':
            uc = True
        if '0' <= i <= '9':
            no = True
    if lc and uc and no:
        user_accounts[username] = password
        log_in[username] = False
        return True
    return False
        
def import_and_create_accounts(filename):

    user_accounts = {}
    log_in = {}

    # your code here
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split('-')
        if len(lst)<=1:
            continue
        username = lst[0].strip()
        password = lst[1].strip()
        if len(password)<8 or username == password or username in user_accounts:
            continue
        lc, uc, no = False, False, False
        for i in password:
            if 'a'<= i <='z':
                lc = True
            if 'A' <= i <= 'Z':
                uc = True
            if '0' <= i <= '9':
                no = True
        if lc and uc and no:
            user_accounts[username] = password
            log_in[username] = False
        else:
            continue
    f.close()
        
    return user_accounts,log_in

def login(user_accounts, log_in, username, password):
    

    # your code here
    if username not in user_accounts or user_accounts[username] != password:
        return False
    log_in[username] = True
    return True
    
def update(bank, log_in, username, amount):
    

    # your code here
    if username in log_in and log_in[username]:
        if username not in bank:
            bank[username] = 0
        if bank[username] + amount < 0:
            return False
        bank[username] += amount
        return True
    return False

def transfer(bank, log_in, userA, userB, amount):
    
    # your code here
    if userA in bank and log_in[userA] and userB in log_in and bank[userA]>=amount:
        bank[userA] -= amount
        bank[userB] = bank.get(userB,0) + amount
        return True
    return False
    
def change_password(user_accounts, log_in, username, old_password, new_password):

    # your code here
    if username in user_accounts and log_in[username] and user_accounts[username]==old_password and old_password != new_password:
        lc, uc, no = False, False, False
        for i in new_password:
            if 'a'<= i <='z':
                lc = True
            if 'A' <= i <= 'Z':
                uc = True
            if '0' <= i <= '9':
                no = True
        if len(new_password)>=8 and lc and uc and no:
            user_accounts[username]=new_password
            return True
        return False
    return False
            
def delete_account(user_accounts, log_in, bank, username, password):
    if username in user_accounts and user_accounts[username]==password and log_in[username]:
        del user_accounts[username]
        del bank[username]
        del log_in[username]
        return True
    return False
    