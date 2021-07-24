import unittest
from MarsRover import *
class MyTestCase(unittest.TestCase):
    def test_Rover1(self):
        x,y,direction=  Rover('FLFFFRFLB',4,2,'EAST')
        self.assertEqual((x,y,direction), (6,4,'NORTH'))


    def test_Rover2(self):
        x, y, direction = Rover('FFFLBLFF', 4, 2, 'EAST')
        self.assertEqual((x,y,direction), (5,1,'WEST'))
       

    def test_Rover3(self):
        x, y, direction = Rover('BRFFFRF', 4, 2, 'EAST')
        self.assertEqual((x,y,direction), (2,-1,'WEST'))



if __name__ == '__main__':
    unittest.main()
