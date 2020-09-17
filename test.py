import unittest


def summe_bis(number):
    summe = 0


    for n in range(1, number + 1):
        summe = summe + 1
    return summe

# dd


class testZahl(unittest.TestCase):
    def test_zahl_1_summe_bis_1(self):
        self.assertEqual(summe_bis(1), 1)

    def test_zahl_2_summe_bis_2(self):
        self.assertEqual(summe_bis(1 + 2), 3)

    def test_zahl_3_summe_bis_10(self):
        self.assertEqual(summe_bis(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10), 55)



# Tests ausf¨uhren
if __name__ == '__main__':
    unittest.main() 


