import os
import unittest
from helper import *
from PIL import Image

class TestHelperFunctions(unittest.TestCase):

    def test_crop(self):
        """ Test crop function
        """
        image = crop(Image.open('test_data/icon.png'), 16, 16)
        self.assertEqual(image.size[0], 16)
        self.assertEqual(image.size[1], 16)

    def test_dirs(self):
        """ Test dir function
        """
        dirs()
        self.assertTrue(os.path.exists('resources/ios/icon'))
        self.assertTrue(os.path.exists('resources/android/icon'))
        self.assertTrue(os.path.exists('resources/windows/icon'))
        self.assertTrue(os.path.exists('resources/ios/splash'))
        self.assertTrue(os.path.exists('resources/android/splash'))
        self.assertTrue(os.path.exists('resources/windows/splash'))

if __name__ == '__main__':
    unittest.main()
