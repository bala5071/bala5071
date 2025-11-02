"""Tests for calculator"""
import pytest
from calculator import *


class TestCalculator:
    """Test suite for calculator"""
    
    @pytest.fixture
    def sample_data(self):
        """Provide sample test data"""
        return {"key": "value", "number": 42}
    
    def test_example_valid_input(self, sample_data):
        """Test with valid input"""
        # Arrange
        expected = "expected_result"
        
        # Act
        result = function_to_test(sample_data)
        
        # Assert
        assert result == expected
    
    def test_example_invalid_input(self):
        """Test with invalid input"""
        with pytest.raises(ValueError):
            function_to_test(None)
    
    @pytest.mark.parametrize("input_val,expected", [
        ("test1", "result1"),
        ("test2", "result2"),
    ])
    def test_example_parameterized(self, input_val, expected):
        """Test with multiple inputs"""
        assert function_to_test(input_val) == expected
