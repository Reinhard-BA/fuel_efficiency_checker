import unittest
from fuel_efficiency_checker import Vehicle

# Dataset for testing
test_data = [
    {"year": 2020, "brand": "toyota", "model": "camry le", "combined_mpg": "30"},
    {"year": 2020, "brand": "toyota", "model": "camry se", "combined_mpg": "28"},
    {"year": 2021, "brand": "honda", "model": "civic lx", "combined_mpg": "32"},]

class TestVehicle(unittest.TestCase):
    
    def test_get_mpg_exact_match(self):
        car = Vehicle("toyota", "camry le", 2020, dataset=test_data)
        result = car.get_mpg()
        # result should be a list of matches, take the first match's mpg
        self.assertIsNotNone(result)  
        self.assertEqual(result[0]["mpg"], 30.0)

    def test_conversion_to_kmpl_uk(self):
        mpg = 30
        kmpl_uk = Vehicle.mpg_to_kmpl_UK(mpg)
        self.assertAlmostEqual(kmpl_uk, 10.62, places=2)  # expected approx

    def test_conversion_to_kmpl_us(self):
        mpg = 30
        kmpl_us = Vehicle.mpg_to_kmpl_US(mpg)
        self.assertAlmostEqual(kmpl_us, 12.75, places=2)

    def test_conversion_to_l_per_100km(self):
        mpg = 30
        l_per_100km = Vehicle.mpg_to_l_per_100km(mpg)
        self.assertAlmostEqual(l_per_100km, 7.84, places=2)

if __name__ == "__main__":
    unittest.main()