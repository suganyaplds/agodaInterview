import pytest
from ChangePassword import ChangePassword

def test_chg_pwd_valid():
    result=ChangePassword("password1","BentleyContinental1234!@#$")
    assert result == True

def test_chg_pwd_opw_invalid():
    result=ChangePassword("password3","BentleyContinental1234!@#$")
    assert result == False

def test_chg_pwd_npw_invalid():
    result=ChangePassword("password1","BentleyContinental1234%^")
    assert result == False

def test_chg_pwd_inv_len():
    result=ChangePassword("password1","Bentley")
    assert result == False

def test_chg_pwd_inv_noupper():
    result=ChangePassword("password1","bentleycontinental")
    assert result == False

def test_chg_pwd_inv_nolower():
    result=ChangePassword("password1","BENTLEYCONTINENTAL")
    assert result == False

def test_chg_pwd_inv_nonumber():
    result=ChangePassword("password1","BentleyContinental")
    assert result == False

def test_chg_pwd_inv_nospchar():
    result=ChangePassword("password1","BentleyContinental12")
    assert result == False

def test_chg_pwd_inv_spchar():
    result=ChangePassword("password1","BentleyContinental12%*")
    assert result == False

def test_chg_pwd_inv_50num():
    result=ChangePassword("password1","Bentley12345678901!@#$")
    assert result == False

def test_chg_pwd_inv_repchar():
    result=ChangePassword("password1","BentleyConteenental!@#$")
    assert result == False

def test_chg_pwd_inv_repnum():
    result=ChangePassword("password1","111BentleyContenental!@#$11")
    assert result == False
    