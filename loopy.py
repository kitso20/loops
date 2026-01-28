
import re



def inventory_audit(stock_totals):
    return sum(stock_totals)



def black_friday(prices_list):    
    return list(map(lambda n:f'R {str(int(n/2))}',prices_list))


def retry_pin(pin):    
    # trying = int(input("Enter your PIN\n"))
    # while :
    #     if trying != pin:
    #         print("Incorrect PIN. Try again.")
    #     else:
            return 'Acces Granted!'




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
    lett = ['g','h','i','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    split_list = []
    for st in list_of_uuids:

        first = st.split()
        for st2 in first:
            second = st2.split('-')
            split_list.append(second)
    
    for string in split_list:
        if len(string[0]) == 8 and len(string[1]) == 4 and len(string[2]) == 4 and len(string[3]) == 4 and len(string[4]) == 12:
            for l in lett:
                if l in string:
                    joined = '-'.join(string)
                    result['invalid_uuids'].append(joined)
                else:
                    joined = '-'.join(string)
                    result['valid_uuids'].append(joined)
        else:
            joined = '-'.join(string)
            result['invalid_uuids'].append(joined)

    
    

    return result
    

def inventory_depletion(inventory, daily_sales_projections):
    return ""