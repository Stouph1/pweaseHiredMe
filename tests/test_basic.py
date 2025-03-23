
"""
Basic tests for the Discord bot. This ensures that fundamental components work.
"""

import unittest
from unittest.mock import patch
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestBasicFunctionality(unittest.TestCase):
    """Basic tests for the bot functionality"""
    
    def test_version(self):
        """Test that the version is accessible"""
        from bot import __version__
        self.assertIsNotNone(__version__)
    
    @patch('os.getenv')
    def test_environment_variables(self, mock_getenv):
        """Test environment variable handling"""
        mock_getenv.side_effect = lambda key: {
            'BOT_TOKEN': 'test_token',
            'CHANNEL_ID': '123456789'
        }.get(key)
        
        # This import needs to happen after mocking os.getenv
        from bot.core import BOT_TOKEN, CHANNEL_ID
        self.assertEqual(BOT_TOKEN, 'test_token')
        self.assertEqual(CHANNEL_ID, 123456789)