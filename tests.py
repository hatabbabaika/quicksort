import unittest
import quicksort


class SortingTests(unittest.TestCase):
    def test_sorting(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        input_data = [6, 5, 7, 4, 8, 9, 0, 2, 3, 1]
        quicksort.sort(input_data)

        self.assertEqual(expected, input_data)

    def test_sorting_with_pivot_item(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        input_data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        quicksort.sort(input_data, 3)

        self.assertEqual(expected, input_data)

    def test_range_sorting(self):
        expected = [4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

        input_data = [6, 5, 7, 4, 8, 9, 0, 0, 0, 0]
        quicksort.sort(input_data, start=0, end=5)

        self.assertEqual(expected, input_data)

    def test_range_sorting_with_pivot_item(self):
        expected = [4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

        input_data = [6, 5, 7, 4, 8, 9, 0, 0, 0, 0]
        quicksort.sort(input_data, 6, 0, 5)

        self.assertEqual(expected, input_data)


class SubFunctionTests(unittest.TestCase):
    def test_swap_items(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        input_data = [1, 2, 7, 4, 5, 6, 3, 8, 9]
        i = 2
        j = 6
        quicksort.__swap_items__(input_data, i, j)

        self.assertEqual(expected, input_data)

    def test_partition(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        input_data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        pivot = 4
        start = 0
        end = len(input_data) - 1
        result = quicksort.__partition__(input_data, pivot, start, end)

        self.assertEqual(expected, input_data)
        self.assertEqual(result, expected.index(pivot))

    def test_find_pivot_0(self):
        expected_list = [1, 2, 3, 4, 5]
        expected_pivot = 3

        input_data = [1, 2, 3, 4, 5]
        result = quicksort.__find_pivot__(input_data, 0, 4)

        self.assertEqual(expected_list, input_data)
        self.assertEqual(expected_pivot, result)

    def test_find_pivot_1(self):
        expected_list = [1, 2, 3, 4, 5]
        expected_pivot = 3

        input_data = [3, 2, 5, 4, 1]
        result = quicksort.__find_pivot__(input_data, 0, 4)

        self.assertEqual(expected_list, input_data)
        self.assertEqual(expected_pivot, result)

    def test_find_pivot_2(self):
        expected_list = [1, 3, 2, 5, 4]
        expected_pivot = 2

        input_data = [2, 3, 4, 5, 1]
        result = quicksort.__find_pivot__(input_data, 0, 4)

        self.assertEqual(expected_list, input_data)
        self.assertEqual(expected_pivot, result)
