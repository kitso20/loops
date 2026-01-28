
from io import StringIO
import loopy as lp
import sys

class TestFunctions():

    def test_inventory_stock_no_items(self):
        assert lp.inventory_audit([]) == 0

    def test_inventory_stock_single_item(self):
        assert lp.inventory_audit([15]) == 15

    def test_inventory_stock_multiple_single_items(self):
        items = [7, 3, 12]

        for item in items:
            assert lp.inventory_audit([item]) == item

    def test_inventory_stock_multiple_items(self):
        assert lp.inventory_audit([5, 10, 3, 8]) == 26

    def test_inventory_stock_multiple_items_2(self):
        assert lp.inventory_audit([0, 20, 30, 50, 10]) == 110

    def test_inventory_stock_multiple_items_stress(self):
        lists_of_items = [
            [3, 5, 7, 8],
            [10, 20, 30, 40, 50],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]

        expected_totals = [23, 150, 55]

        for items, expected in zip(lists_of_items, expected_totals):
            assert lp.inventory_audit(items) == expected

    def test_black_friday_no_items(self):
        assert lp.black_friday([]) == []

    def test_black_friday_single_item(self):
        assert lp.black_friday([100]) == ["R 50"]

    def test_black_friday_multiple_single_items(self):
        prices = [80, 150, 60]

        expected_discounts = ["R 40", "R 75", "R 30"]

        for price, expected in zip(prices, expected_discounts):
            assert lp.black_friday([price]) == [expected]

    def test_black_friday_multiple_items(self):
        assert lp.black_friday([100, 200, 50]) == ["R 50", "R 100", "R 25"]
    
    def test_black_friday_multiple_items_2(self):
        assert lp.black_friday([135, 90, 650]) == ["R 67", "R 45", "R 325"]

    def test_black_friday_multiple_items_stress(self):
        lists_of_prices = [
            [120, 240, 360],
            [75, 150, 225, 300],
            [10, 20, 30, 40, 50]
        ]

        expected_discounts = [
            ["R 60", "R 120", "R 180"],
            ["R 37", "R 75", "R 112", "R 150"],
            ["R 5", "R 10", "R 15", "R 20", "R 25"]
        ]

        for prices, expected in zip(lists_of_prices, expected_discounts):
            assert lp.black_friday(prices) == expected
    
    def test_retry_pin_correct_first_try(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('1234\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.retry_pin('1234')
        sys.stdout = sys.__stdout__
        assert 'Acces Granted!' in captured_output.getvalue()

    def test_retry_pin_incorrect_then_correct(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('0000\n1234\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.retry_pin('1234')
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert output.count('Enter your PIN:') == 2
        assert 'Acces Granted!' in output

    def test_retry_pin_multiple_incorrect_then_correct(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('0000\n1111\n2222\n1234\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.retry_pin('1234')
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert output.count('Enter your PIN:') == 4
        assert 'Acces Granted!' in output

    def test_winning_streak_no_games(self):
        assert lp.winning_streak([]) == 0

    def test_winning_streak_all_losses(self):
        assert lp.winning_streak(['L', 'L', 'L']) == 0

    def test_winning_streak_all_wins(self):
        assert lp.winning_streak(['W', 'W', 'W', 'W']) == 4

    def test_winning_streak_mixed_results(self):
        assert lp.winning_streak(['W', 'L', 'W', 'W', 'L', 'W', 'W', 'W']) == 3

    def test_winning_streak_mixed_results_2(self):
        assert lp.winning_streak(['L', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'W']) == 6  

    def test_winning_streak_variations(self):
        test_cases = [
            (['W', 'L', 'W', 'W', 'L', 'W'], 2),
            (['L', 'L', 'W', 'W', 'W', 'L', 'W', 'W'], 3),
            (['W', 'W', 'L', 'L', 'W', 'W', 'W', 'W'], 4),
            (['L', 'W', 'L', 'W', 'L', 'W'], 1),
            (['W', 'W', 'W', 'L', 'L', 'L'], 3),
            (['L', 'W', 'L', 'W', 'W', 'L', 'W', 'W', 'W', 'L', 'L', 'W', 'W', 'W', 'L', 'W', 'W'], 3)
        ]

        for results, expected_streak in test_cases:
            assert lp.winning_streak(results) == expected_streak  

    def test_peak_finder(self):
        assert lp.peak_finder([1, 3, 7, 1, 2, 6, 3, 2, 1]) == [7, 6]

    def test_peak_finder_no_peaks(self):
        assert lp.peak_finder([1, 2, 3, 4, 5]) == []

    def test_peak_finder_multiple_peaks(self):
        assert lp.peak_finder([5, 10, 5, 10, 5, 10, 5]) == [10, 10, 10]
    
    def test_peak_finder_single_peak(self):
        assert lp.peak_finder([2, 4, 6, 4, 2]) == [6]

    def test_peak_finder_plateau_peak(self):
        assert lp.peak_finder([1, 3, 5, 5, 3, 1]) == []

    def test_peak_finder_edge_peaks(self):
        assert lp.peak_finder([10, 5, 1, 5, 10]) == []

    def test_peak_finder_variations(self):
        test_cases = [
            ([2, 5, 3, 6, 4, 7, 1], [5, 6, 7]),
            ([1, 2, 1, 2, 1, 2, 1], [2, 2, 2]),
            ([9, 7, 5, 3, 1], []),
            ([3, 8, 3, 8, 3], [8, 8]),
            ([6, 4, 6, 4, 6, 4, 6], [6, 6])
        ]

        for data, expected_peaks in test_cases:
            assert lp.peak_finder(data) == expected_peaks

    def test_uuid_validator_valid_uuid(self):
        assert lp.uuid_validator(['123e4567-e89b-12d3-a456-426614174000']) == {'valid_uuids': ['123e4567-e89b-12d3-a456-426614174000'], 'invalid_uuids': []}

    def test_uuid_validator_invalid_uuid(self):
        assert lp.uuid_validator(['123e4567-e89b-12d3-a456-42661417400Z']) == {'valid_uuids': [], 'invalid_uuids': ['123e4567-e89b-12d3-a456-42661417400Z']}
    
    def test_uuid_validator_mixed_uuids(self):
        uuids = [
            '123e4567-e89b-12d3-a456-426614174000',
            '123e4567-e89b-12d3-a456-42661417400Z',
            '550e8400-e29b-41d4-a716-446655440000',
            '550e8400-e29b-41d4-a716-44665544000G'
        ]
        result = lp.uuid_validator(uuids)
        assert result == {
            'valid_uuids': [
                '123e4567-e89b-12d3-a456-426614174000',
                '550e8400-e29b-41d4-a716-446655440000'
            ],
            'invalid_uuids': [
                '123e4567-e89b-12d3-a456-42661417400Z',
                '550e8400-e29b-41d4-a716-44665544000G'
            ]
        }

    def test_uuid_validator_empty_list(self):
        assert lp.uuid_validator([]) == {'valid_uuids': [], 'invalid_uuids': []}

    def test_uuid_validator_varying_test_cases(self):
        test_cases = [
            (['123e4567-e89b-12d3-a456-426614174000'], {'valid_uuids': ['123e4567-e89b-12d3-a456-426614174000'], 'invalid_uuids': []}),
            (['invalid-uuid-string'], {'valid_uuids': [], 'invalid_uuids': ['invalid-uuid-string']}),
            (['550e8400-e29b-41d4-a716-446655440000', 'not-a-uuid'], {'valid_uuids': ['550e8400-e29b-41d4-a716-446655440000'], 'invalid_uuids': ['not-a-uuid']}),
            ([], {'valid_uuids': [], 'invalid_uuids': []}),
            (['123e4567-e89b-12d3-a456-426614174000', '123e4567-e89b-12d3-a456-42661417400Z', '550e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-44665544000G'], {'valid_uuids': ['123e4567-e89b-12d3-a456-426614174000', '550e8400-e29b-41d4-a716-446655440000'], 'invalid_uuids': ['123e4567-e89b-12d3-a456-42661417400Z', '550e8400-e29b-41d4-a716-44665544000G']})
        ]

        for uuids, expected in test_cases:
            assert lp.uuid_validator(uuids) == expected

    def test_inventory_depletion_no_items(self):
        assert lp.inventory_depletion(0, []) == "Inventory depleted."

    def test_inventory_depletion_exact_depletion(self):
        assert lp.inventory_depletion(100, [30, 20, 50]) == "Inventory will last through the entire projection period. Remaining stock: 0"

    def test_inventory_depletion_surplus_stock(self):
        assert lp.inventory_depletion(50, [10, 15, 5]) == "Inventory will last through the entire projection period. Remaining stock: 20"

    def test_inventory_depletion_depletes_early(self):
        assert lp.inventory_depletion(40, [15, 10, 20, 5]) == "Inventory will run out on day 3."
    
    def test_inventory_depletion_depletes_first_day(self):
        assert lp.inventory_depletion(10, [15, 5, 5]) == "Inventory will run out on day 1."

    def test_inventory_depletion_depletes_last_day(self):
        assert lp.inventory_depletion(30, [5, 10, 15]) == "Inventory will last through the entire projection period. Remaining stock: 0"

    def test_inventory_depletion_no_sales(self):
        assert lp.inventory_depletion(25, [0, 0, 0]) == "Inventory will last through the entire projection period. Remaining stock: 25" 

    def test_inventory_depletion_variations(self):
        test_cases = [
            (60, [20, 15, 10], "Inventory will last through the entire projection period. Remaining stock: 15"),
            (25, [10, 10, 10], "Inventory will run out on day 3."),
            (0, [5, 5, 5], "Inventory depleted."),
            (100, [30, 30, 50], "Inventory will run out on day 3."),
            (45, [15, 15, 15], "Inventory will last through the entire projection period. Remaining stock: 0")
        ]

        for initial_stock, daily_sales, expected in test_cases:
            assert lp.inventory_depletion(initial_stock, daily_sales) == expected