import unittest
import validators
from ..src.config import(
    URL_LIST,
    CONTENT_REQUIRED,
)

# Test Functions
def is_valid_list(items):
    """Check if urls is a list."""
    if isinstance(items, list):
        return True
    return False

def is_valid_url(url):
    return validators.url(url)

# Unit tests
class TestIsList(unittest.TestCase):
    def test_valid_list(self):
        self.assertTrue(is_valid_list(URL_LIST)) # Test if url list is valid
        self.assertTrue(is_valid_list(CONTENT_REQUIRED)) # Test if required content list is valid
        
class TestURLValidation(unittest.TestCase): # Test if URL is valid
    def test_valid_url(self):
        for url in URL_LIST:
           self.assertTrue(is_valid_url(url))
           

if __name__ == "__main__":
    unittest.main()