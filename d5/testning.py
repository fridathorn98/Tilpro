import unittest

from bintreeFile import Bintree

class BintreeTest(unittest.TestCase):

    def testInsert(self):
         """ Testar Subj och Pred """
         b = Bintree()
         b.store("adam", 123)
         self.assertEqual(b.root.key, "adam")
         self.assertEqual(b.root.value, 123)


    def testInsertMore(self): #tre insättningar
         b = Bintree()
         b.store("adam", 123)
         self.assertEqual(b.root.key, "adam")
         self.assertEqual(b.root.value, 123)
         b.store("bianca", 456)
         self.assertEqual(b.root.right.key, "bianca")
         self.assertEqual(b.root.right.value, 456)
         b.store("clara", 789)
         self.assertEqual(b.root.right.right.key, "clara")
         self.assertEqual(b.root.right.right.value, 789)

    def testSearch(self):
         b = Bintree()
         with self.assertRaises(KeyError):
             b.search("eva")

    def testSearchMore(self): #tre search
         b = Bintree()
         b.store("bianca", 456)
         b.store("adam", 123)
         b.store("clara", 789)
         self.assertEqual(b.search("bianca"), 456)
         self.assertEqual(b.search("clara"), 789)
         self.assertEqual(b.search("adam"), 123)

if __name__ == '__main__':
    unittest.main()
