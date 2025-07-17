# Tests for schemas

import pytest
from src.ingestion.s3_ingestor import Person

# Test cases for the Person class
def test_person_initialization():
    person = Person(name="John Doe", age=30, super=10000, income=50000)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.super == 10000
    assert person.income == 50000

def test_super_after_5_years_with_income():
    person = Person(name="Jane Doe", age=28, super=12000, income=60000)
    expected_super = 12000 + (60000 * 0.11 * 5)
    assert person.super_after_5_years() == expected_super 