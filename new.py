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


print(winning_streak(['L', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'W']))