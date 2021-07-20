import pytest
from ChangePassword import ChangePassword

def test_chg_pwd_valid():
    result=ChangePassword("password1","BentleyContinental1234!@#$")
    assert result == True

def test_chg_pwd_opw_invalid():
    result=ChangePassword("password3","BentleyContinental1234!@#$")
    assert result == False

def test_chg_pwd_npw_invalid():
    result=ChangePassword("password3","BentleyContinental1234%^")
    assert result == False