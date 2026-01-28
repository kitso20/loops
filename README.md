# Assessment 002 - Python Repeating Instructions (Loops)

## Learning Outcomes assessed:

- Conditional statements

- Functions

- Basic loops

- Advanced Loops

- Simple algorithms (Problem solving)

- Basic Command line commands

---

## Assessment Structure

The following Assessment has two sections:

- [Form based assessment](https://forms.gle/j2fjmR5eTijKjJZ9A) 

- Coding Assessment (Questions are below)

You can answer them in any order.

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **60%** |
| Form-Based Section (MCQs + written responses) | **40%** |


### Coding section

Your coding score is determined by the number of tests you pass.

Let:

- T = total number of coding tests

- P = number of tests you pass

```bash
Coding Score = (P / T) × 60%
```

### Form-based section

Your form-based score is determined by your correct responses to the assessment form.

Let:

- Q = total number of questions

- C = number of correct answers

```bash
Form Score = (C / Q) × 40%
```

### Final Score & Pass Mark

Your final score is the sum of both components:

```bash
Final Score = Coding Score + Form Score
```


To pass the overall assessment, your Final Score must be **60%(Mininum Pass Mark) or higher** .

---

### How to run your tests

To run all your tests

```bash
python3 -m pytest tests/test_loopy.py -v
```

To run your tests individually

```bash
python3 -m pytest tests/test_loopy.py::TestFunctions::test_inventory_stock_multiple_items -v
```

or

```bash
python3 -m pytest tests/test_loopy.py::TestFunctions::test_inventory_stock_multiple_items -vv
```

---

## Fundamentals Coding Assessment

This assessment consists of five Python functions. Each function has a partially written
implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

### Project Structure

```text
loops/
├── loopy.py          # <-- This is where you write your solutions
├── tests/
│   └── test_loopy.py # <-- These are the tests you must make pass
└── README.md                # <-- Assessment instructions (this file) 
```

---

### Question 1 - `inventory_audit(stock_totals)`

Uncle Sipho runs a busy spaza shop in the heart of Gugulethu. It’s Friday afternoon, and the delivery truck is about to arrive with new supplies. Before he can place his order, Uncle Sipho needs to know exactly how many items are left on his main display shelf so he doesn't over-order.

He’s counted the items in four different categories:

**5** packets of Simba Fruit Chutney chips
**10** cans of Stoney Ginger Beer
**3** loaves of fresh white bread
**8** bars of chocolate

Uncle Sipho is busy helping a customer, so he has asked you to quickly add up these numbers. 
Apply your logic to the `inventory_audit()` function that takes a list of these quantities and returns the total number of items currently in stock.

- **Input:** A list of integers representing item quantities (e.g., [5, 10, 3, 8])
- **Output:** A single integer representing the sum of all items (e.g., 26)

---

### Question 2 - `black_friday(prices_list)`

A local sneaker store, The Kicks Stand, is participating in the nationwide Black Friday craze. The owner, Mo, has decided to keep things simple; everything in the store is 50% off. The shop is packed, and the queue is stretching out the door. Mo needs a quick way to show customers the new, discounted prices on their receipts so there are no arguments at the till. He has a list of the original prices for the items a customer is buying, and he needs you to generate a list of the "Sale Prices".

Apply your logic to the `black_friday()` function that takes a list of original prices. It should calculate *50%* of each price and return a new list of prices.

- **Input:** A list of integers (e.g., [100, 200, 50])
- **Output:** A list of strings formatted with the currency symbol (e.g., ["R 50", "R 100", "R 25"])

---

### Question 3 - `retry_pin(pin)`

It’s the 25th of the month—Payday! Thabo is standing at a busy ATM at Maponya Mall. The queue behind him is getting long, and the "uncles" in line are starting to huff and puff because they want to get their shopping done.

In his excitement, Thabo has forgotten his 4-digit PIN. The ATM is programmed to be patient, but it won't let him see his balance nor withdraw money until he gets the PIN exactly right.

Apply your logic to the `retry_pin()` function which simulates this security check. The function should continuously prompt the user with "Enter your PIN" for as long as the PIN is incorrect.

- *If the user enters the wrong PIN*, the program should print: "Incorrect PIN. Try again." and then ask for the PIN again.
- *If the user enters the correct PIN* (e.g. `2468`), the program should print: "Access Granted!" and then stop asking.

---

### Question 4 - `winning_streak(streak)`

The Springboks are on a world tour, and the whole of South Africa is wearing their green and gold jerseys every Friday. From Loftus Versfeld to Twickenham, the fans are tracking every single match.

The South African Rugby Union (SARU) wants to update their website with a "Longest Winning Streak" stat to show just how dominant the team has been. They have a list of results where "W" stands for a glorious win and "L" stands for a tough loss. They need you to look through the season's history and find the highest number of consecutive wins (wins in a row).

Apply your logic to the `winning_streak()` funciton which analyses a list of game results. The function must count how many times "W" appears in a row and return the highest count found.

- **Input:** A list of strings (e.g., ["W", "L", "W", "W", "L", "W", "W", "W"])
- **Output:** An integer representing the longest streak (e.g., 3)

---

### Question 5 - `peak_finder(temperatures)`

The South African Weather Service (SAWS) is monitoring a massive heatwave moving across the Northern Cape. In towns like Upington, the temperature can climb incredibly high, but it often fluctuates.

A "Local Peak" occurs when one day is hotter than the day before it and the day after it. The weather station has sent you a list of maximum temperatures (in degrees Celsius) recorded over the last few weeks. To help farmers prepare for the hottest spikes, you need to identify every "Peak Temperature" in the sequence.

Apply your logic to the `peak_finder()` function which looks through the list of temperatures. It should identify any temperature that is strictly greater than the one immediately before it and the one immediately after it.

- **Input:** A list of integers (e.g., [30, 32, 31, 35, 33, 36, 34, 38, 37, 39, 35, 40, 38, 37, 36, 35, 34, 33, 32, 31, 30])
- **Output:** A list of the identified peak temperatures (e.g., [32, 35, 36, 38, 39, 40])

---

### Question 6 - `uuid_validator(list_of_uuids)`

Standard Bank is merging its old computer systems into a brand-new "Cloud" database. To make sure every customer’s account is secure and easy to find, the bank uses UUIDs (Universally Unique Identifiers) as digital ID numbers.

During the migration, some of the data got mixed up. Some IDs are perfect, but others are missing characters or have symbols where they don't belong. The Department Lead has tasked you with writing a script to sort through a pile of raw ID strings. You need to separate the good data from the bad data.

Apply your logic to the `uuid_validator()` function which takes a list of strings. Your function must check each string against the official UUID rules and sort them into two separate lists.

#### What makes a UUID valid?

```text
    - It must be exactly 36 characters long
    - It must follow the 8-4-4-4-12 pattern (8 chars, hyphen, 4 chars, hyphen, etc.).
    - The characters must only be hexadecimal (0-9 and a-f) and hyphens in the correct spots.
```

- **Input:** A list of strings (e.g., ["550e8400-e29b-41d4-a716-446655440000", "abc-123-gh-789"]).
- **Output:** A dictionary with two keys: 'valid_uuids' and 'invalid_uuids', each containing a list of strings.

```python
{ 'valid_uuids': ["550e8400-e29b-41d4-a716-446655440000"], 'invalid_uuids': ["abc-123-gh-789"] }
```

---

### Question 7 - `inventory_depletion(inventory, daily_sales_projections)`

Aunty Fatima’s bakery in Bo-Kaap is famous for her Sunday morning koesisters. With the festive season approaching, she has a specific amount of spicy dough (the `inventory_count`) ready to go. Based on previous years, she has a list of `daily_sales_projections` for the upcoming week.

Aunty Fatima is a master of planning. She wants to use these projections to stay ahead of the crowd; if the dough is going to run out, she needs to know exactly which day she should start mixing and proofing a fresh batch to keep the baskets full for the tourists and locals.

Apply your logic to the `inventory_depletion()` function. You need to subtract each day's sales from the total and determine if the stock hits zero or below.

- **If the stock will run out:** Return a string so Aunty Fatima knows when to prepare her fresh batch (e.g., `"Inventory will run out on day 3"`).

- **If the stock lasts the whole week:** Return a string showing the leftover amount so she knows she's covered (e.g., `"Inventory will last through the entire projection period. Remaining stock: 1"`).

---

## Your Goal

Read the instructions above for each question, then complete each function in `loopy.py` while ensuring that:

- The code is valid Python

- Each function behaves according to the instructions

- All unit tests pass successfully

Good luck — and remember to think carefully about your solutions!