#!/usr/bin/python3
"""Defines unittests for models/user.py."""
def test_email_is_public_str(self):
    us = User()
    self.assertEqual(str, type(us.email))

def test_password_is_public_str(self):
    us = User()
    self.assertEqual(str, type(us.password))

def test_first_name_is_public_str(self):
    us = User()
    self.assertEqual(str, type(us.first_name))

def test_last_name_is_public_str(self):
    us = User()
    self.assertEqual(str, type(us.last_name))
