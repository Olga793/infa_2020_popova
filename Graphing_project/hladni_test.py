import hladni_model as hm
import numpy as np
import unittest
import random

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_harmonic_force(self):
        a=random.randint(0, 100)
        b=random.randint(0, 100)
        c=random.randint(0, 100)
        self.assertEqual(round(hm.harmonic_force(a, b, c), 1),  round(c*np.cos(np.pi*a* b/3), 1))
    
 
if __name__ == '__main__': 
    unittest.main()
