# Tests for schemas

import pytest
from src.ingestion.s3_ingestor import Person

# Test cases for the Person class
def test_person_initialization():
    P = Person(name="John Doe", age=30, super=10000, income=50000) # Constructing a Person object
    assert P.name == "John Doe"
    assert P.age == 30
    assert P.super == 10000
    assert P.income == 50000

def test_super_after_5_years_with_income():
    P = Person(name="Jane Doe", age=28, super=12000, income=60000)
    expected_super = 12000 + (60000 * 0.11 * 5)
    assert P.super_after_5_years() == expected_super 

def test_negative_age_raises_value_error():
    with pytest.raises(ValueError, match="Age cannot be negative."):
        Person(name="Invalid Age", age=-5, super=10000, income=50000)

def test_none_super_raises_value_error():
    with pytest.raises(ValueError, match="Super cannot be None."):
        Person(name="Invalid Age", age=25, super=None, income=50000)

def test_super_after_5_years_without_income():
    P = Person(name="Test", age=30, super=10000, income=None)
    with pytest.raises(ValueError, match="Income cannot be None."):
        P.super_after_5_years()
