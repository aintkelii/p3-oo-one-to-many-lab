import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
   
def test_pet_init():
    """Test Pet class initialization"""
   

    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
   

    Pet.all = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    

    Pet.all = []

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    
    Pet.all = []

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    

    Pet.all = []

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    