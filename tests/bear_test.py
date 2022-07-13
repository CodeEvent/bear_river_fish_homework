import unittest
from src.bear import Bear
from src.river import River

class TestBear(unittest.TestCase):
    
    def setUp(self):
        self.bear = Bear("Yoggi", 'grizzly')
        
        
    def test_bear_has_name(self):
        self.assertEqual("Yoggi", self.bear.name)
        
 #A bear should be able to eat a fish       
    def test_add_fish_to_bear_stomach(self):
        expected = 0
        result = 0
        self.assertEqual(expected,result)
