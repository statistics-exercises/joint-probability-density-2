import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_kval(self) :
          self.assertTrue( np.abs( k-8/411 )<1e-7, "your value for k is incorrect" )
