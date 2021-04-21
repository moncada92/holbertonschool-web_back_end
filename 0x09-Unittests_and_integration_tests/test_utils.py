#!/usr/bin/env python3
"""
Unittest utils.py
Run: python3 -m unittest test_utils | tail -1
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test the access_nested_map function
        """
        self.assertEquals(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        test the access_nested_map function (exception)
        """
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    """
    Test cases
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_class):
        """
        test the get_json function
        """
        mock_class.return_value = test_payload
        self.assertEquals(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases
    """

    def test_memoize(self):
        """
        test the memoize function
        """
        class TestClass:
            """
            Test Class
            """

            def a_method(self):
                """
                a_method
                """
                return 42

            @memoize
            def a_property(self):
                """
                a_property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
