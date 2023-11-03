import unittest
from src.min_depth import min_depth


class TestMinDepth(unittest.TestCase):
    def test_with_provided_data_1(self):
        root = 1
        edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
        expected_depth = 3
        result = min_depth(root, edges)
        self.assertEqual(result, expected_depth)

    def test_with_provided_data_2(self):
        root = 1
        edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (5, 6)]
        expected_depth = 4
        result = min_depth(root, edges)
        self.assertEqual(result, expected_depth)

    def test_read_write(self):
        with open('C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/input.txt', 'w') as file:
            file.write("1\n1,2\n1,3\n2,4\n3,5\n")
        with open('C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/input.txt', 'r') as file:
            root = int(file.readline())
            edges = [tuple(map(int, line.split(','))) for line in file]
        self.assertEqual(root, 1)
        self.assertEqual(edges, [(1, 2), (1, 3), (2, 4), (3, 5)])

if __name__ == '__main__':
    unittest.main()
