# test_nftmetadataindexertoolkit.py
"""
Tests for NftMetadataIndexerToolkit module.
"""

import unittest
from nftmetadataindexertoolkit import NftMetadataIndexerToolkit

class TestNftMetadataIndexerToolkit(unittest.TestCase):
    """Test cases for NftMetadataIndexerToolkit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerToolkit()
        self.assertIsInstance(instance, NftMetadataIndexerToolkit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerToolkit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
