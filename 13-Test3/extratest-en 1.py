# -*- coding: utf-8 -*-
"""
Exam ZICSS1-1112 — unit test script (extended)

How to use:
1) Put this file in the same folder as your solutions: p1.py, p2.py, ..., p10.py.
2) Run:  python check-tests-ZICSS1-1112.py
3) The unittest report will be written to results.txt (as in the provided template).

The tests are based on the examples under each task in the PDF and include TWO
additional assertions per task.
"""
import sys
import unittest


class Test(unittest.TestCase):
    # (p1.py) RPN with + and - operators
    def test_p1(self):
        import p1
        # examples from the PDF
        self.assertEqual(p1.f("2 3 4 5 + - +"), -4)
        self.assertEqual(p1.f("11 7 + 15 - 14 +"), 17)
        # +2 extra
        self.assertEqual(p1.f("5 1 - 2 +"), 6)         # (5-1)+2
        self.assertEqual(p1.f("10 2 3 + -"), 5)       # 10-(2+3)

    # (p2.py) counting people using '+' (enter) and '-' (leave)
    def test_p2(self):
        import p2
        # examples from the PDF
        self.assertEqual(p2.f(""), 0)
        self.assertEqual(p2.f("+-+"), 1)
        self.assertEqual(p2.f("+-++++-+----"), 0)
        self.assertEqual(p2.f("+-+++++-"), 4)
        # +2 extra
        self.assertEqual(p2.f("++++----"), 0)
        self.assertEqual(p2.f("++-+--+"), 1)

    # (p3.py) variable name validation (length 1..6)
    def test_p3(self):
        import p3
        # examples from the PDF
        self.assertTrue(p3.f("aBC"))
        self.assertTrue(p3.f("_ab_c"))
        self.assertTrue(p3.f("abcdef"))
        self.assertFalse(p3.f("8abc"))
        self.assertFalse(p3.f("no_book"))
        # +2 extra
        self.assertTrue(p3.f("A_9"))
        self.assertTrue(p3.f("__"))

    # (p4.py) class C: initial + '-' + age; lowercase <18, uppercase >=18
    def test_p4(self):
        import p4
        # examples from the PDF (check str())
        self.assertEqual(str(p4.C("John", 18)), "J-18")
        self.assertEqual(str(p4.C("Anna", 17)), "a-17")
        # +2 extra
        self.assertEqual(str(p4.C("maria", 18)), "M-18")
        self.assertEqual(str(p4.C("Z", 1)), "z-1")

    # (p5.py) stadium class C with methods m1 (set/add), m2 (mean over listed sectors)
    def test_p5(self):
        import p5
        # base example
        stadium = p5.C({"A": 120, "D": 150, "G": 90, "K": 110})
        stadium.m1("G", 130)
        self.assertEqual(stadium.m2("GD"), 140)   # mean of 130 and 150
        self.assertEqual(stadium.m2("KEJ"), 110)  # only K exists
        # +2 extra with integer means
        self.assertEqual(stadium.m2("AGK"), 120)  # (120+130+110)/3
        stadium.m1("E", 50)                       # add a new sector
        self.assertEqual(stadium.m2("EG"), 90)    # (50+130)/2

    # (p6.py) filter scores and return max+min after filter
    def test_p6(self):
        import p6
        res = [95, 90, 20, 50, 70]
        # examples from the PDF
        fnc1 = lambda x: x > 50
        fnc2 = lambda x: x > 30 and x < 90
        self.assertEqual(p6.f(fnc1, res), 165)
        self.assertEqual(p6.f(fnc2, res), 120)
        # +2 extra
        fnc3 = lambda x: x >= 90
        fnc4 = lambda x: x % 2 == 0
        self.assertEqual(p6.f(fnc3, res), 185)   # 95 + 90
        self.assertEqual(p6.f(fnc4, res), 110)   # 90 + 20

    # (p7.py) sort files by the trailing number (ascending)
    def test_p7(self):
        import p7
        # example from the PDF
        files = ["copy179", "copy15", "copy3", "copy123", "copy9"]
        self.assertEqual(p7.f(files), ["copy3", "copy9", "copy15", "copy123", "copy179"])
        # +2 extra
        files2 = ["img11", "img2", "img10"]
        self.assertEqual(p7.f(files2), ["img2", "img10", "img11"])
        files3 = ["x10", "x2", "x5"]
        self.assertEqual(p7.f(files3), ["x2", "x5", "x10"])

    # (p8.py) counter class: m2 +=10, m3 -=10, m4(n) ±=n
    def test_p8(self):
        import p8
        # example from the PDF
        c = p8.C(5)
        self.assertEqual(c.m1(), 5)
        c.m2(); self.assertEqual(c.m1(), 15)
        c.m4(-8); self.assertEqual(c.m1(), 7)
        c.m3(); self.assertEqual(c.m1(), -3)
        c.m4(25); self.assertEqual(c.m1(), 22)
        self.assertEqual(str(c), "22")
        # +2 extra
        c.m4(8); self.assertEqual(c.m1(), 30)
        c.m3(); self.assertEqual(c.m1(), 20)

    # (p9.py) cars: order=1 alphabetical by reg; order=2 >=200 km descending by km
    def test_p9(self):
        import p9
        # examples from the PDF
        cars = [{"KR333": 138}, {"WL555": 497}, {"DB444": 341}, {"MC222": 412}]
        self.assertEqual(
            p9.f(cars, 1),
            [{"DB444": 341}, {"KR333": 138}, {"MC222": 412}, {"WL555": 497}],
        )
        self.assertEqual(
            p9.f(cars, 2),
            [{"WL555": 497}, {"MC222": 412}, {"DB444": 341}],
        )
        # +2 extra
        cars2 = [{"AA1": 50}, {"CC3": 250}, {"BB2": 200}]
        self.assertEqual(p9.f(cars2, 1), [{"AA1": 50}, {"BB2": 200}, {"CC3": 250}])
        self.assertEqual(p9.f(cars2, 2), [{"CC3": 250}, {"BB2": 200}])

    # (p10.py) keep only British dates DD/MM/YYYY (with leading zeros)
    def test_p10(self):
        import p10
        # example from the PDF
        dates = "2021-1-3;05/12/2024:1998-12-11,9 maj 2007;;31/03/2021,,1/9/2011"
        self.assertEqual(p10.f(dates), ["05/12/2024", "31/03/2021"])
        # +2 extra (format-only check, no semantic calendar validation)
        dates2 = "4/1/2025,04/01/2025,2010-11-30,30/11/2010"
        self.assertEqual(p10.f(dates2), ["04/01/2025", "30/11/2010"])  # only DD/MM/YYYY
        dates3 = "01/01/1999,1999-01-01,1/01/1999,15/09/2011"
        self.assertEqual(p10.f(dates3), ["01/01/1999", "15/09/2011"])  # preserve order


if __name__ == "__main__":
    # as in the template, write the unittest report to results.txt
    sys.stderr = open('results.txt', 'w', encoding='utf-8')
    unittest.main(verbosity=2)
