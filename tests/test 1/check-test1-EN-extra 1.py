'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(118,20),"0x12")
        self.assertEqual(p1.f(174,62),"0x32")

    def test_p2(self):
        import p2
        self.assertEqual(p2.f("U",False,True),79)
        self.assertEqual(p2.f("S",True,True),44)
        self.assertEqual(p2.f("J",False,False),40)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("aabbccddee"),False)
        self.assertEqual(p3.f("a2345"),False)
        self.assertEqual(p3.f("zxcvbn"),True)
        self.assertEqual(p3.f("poiuytrewq"),True)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f(6),"*/*/*/*/*/*")
        self.assertEqual(p4.f(1),"*")
        self.assertEqual(p4.f(0),"")

    def test_p5(self):
        import p5
        self.assertEqual(p5.f(8,12),33)
        self.assertEqual(p5.f(97,115),294)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("3,2,2,4,2","3,4,3"),2)
        self.assertEqual(p6.f("3,3,4,5,5","5,5,5,2"),1)
        self.assertEqual(p6.f("3,3","5,2,4"),0)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f(1,5),12)
        self.assertEqual(p7.f(30,90),178)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f(1,60,3600),True)
        self.assertEqual(p8.f(5,300,18000),True)
        self.assertEqual(p8.f(5,300,17000),False)
        self.assertEqual(p8.f(5,200,18000),False)

    def test_p9(self):
        import p9
        self.assertEqual(p9.f("L,L,L,M,M,S,S,S"),"M")
        self.assertEqual(p9.f("S,M,S,S,M"),"L")
        self.assertEqual(p9.f("L,M,S,M,S,L,L"),"S")

    def test_p10(self):
        import p10
        self.assertEqual(p10.f("13:06","13:03"),"13:03")
        self.assertEqual(p10.f("13:06","1:03pm"),"1:03pm")
        self.assertEqual(p10.f("13:06","1:06pm"),"13:06")


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
