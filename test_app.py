import unittestfrom app import addclass TestApp(unittest.TestCase): def
test_add(self): self.assertEqual(add(10, 20), 30) def
test_zero(self): self.assertEqual(add(0, 0), 0)if __name__ ==
&quot;__main__&quot;: unittest.main()
