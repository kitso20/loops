
import re



def inventory_audit(stock_totals):
    return sum(stock_totals)



def black_friday(prices_list):    
    return list(map(lambda n:f'R {str(int(n/2))}',prices_list))


def retry_pin(pin):    
    
    while True:
        trying = input("Enter your PIN:")
        if trying != pin:
            print("Incorrect PIN. Try again.")
        else:
            print('Acces Granted!')
            return
            




def winning_streak(streak):
    # for n in range(len(streak)):

    joined = "".join(streak)
    splited = joined.split('L')

    if "W" not in streak:
        return 0
    
    elif 'L' not in streak:
        return len(streak)
    
    else:
        nums = []
        for item in splited:
            nums.append(len(item))

        return max(nums)

def peak_finder(temperatures):
    first = temperatures[0]
    
    high = []
    for num in temperatures:
        aftr = 0
        if temperatures.index(num) < len(temperatures)-1:
            aftr = temperatures[temperatures.index(num)+1] 
        else:
            break
        if first < num:
            if num > aftr:
                first = aftr
                high.append(num)
    return high


def uuid_validator(list_of_uuids):
    result = {
        'valid_uuids': [],
        'invalid_uuids': []
    }

    return result
    

def inventory_depletion(inventory, daily_sales_projections):
    return ""