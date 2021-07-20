import pytest
from ChangePassword import ChangePassword

def test_chg_pwd_valid():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyContinental1234!@#$")
    assert result == True

def test_chg_pwd_opw_invalid():
    result=ChangePassword("password3","BentleyContinental1234!@#$")
    assert result == False

def test_chg_pwd_npw_invalid():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyContinental1234%^")
    assert result == False

def test_chg_pwd_inv_len():
    result=ChangePassword("VolkswagenBeetle2021!","Bentley")
    assert result == False

def test_chg_pwd_inv_noupper():
    result=ChangePassword("VolkswagenBeetle2021!","bentleycontinental")
    assert result == False

def test_chg_pwd_inv_nolower():
    result=ChangePassword("VolkswagenBeetle2021!","BENTLEYCONTINENTAL")
    assert result == False

def test_chg_pwd_inv_nonumber():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyContinental")
    assert result == False

def test_chg_pwd_inv_nospchar():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyContinental12")
    assert result == False

def test_chg_pwd_inv_spchar():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyContinental12%*")
    assert result == False

def test_chg_pwd_inv_50num():
    result=ChangePassword("VolkswagenBeetle2021!","Bentley12345678901!@#$")
    assert result == False

def test_chg_pwd_inv_repchar():
    result=ChangePassword("VolkswagenBeetle2021!","BentleyConteenental!@#$")
    assert result == False

def test_chg_pwd_inv_repnum():
    result=ChangePassword("VolkswagenBeetle2021!","111BentleyContenental!@#$11")
    assert result == False

def test_chg_pwd_valid_boundary():
    result=ChangePassword("VolkswagenBeetle2021!","11BentleyContenental!@#$11")
    assert result == True    

def test_chg_pwd_inv_similar():
    result=ChangePassword("VolkswagenBeetle2021!","VolkswagenBeetle2019$")
    assert result == False  

def test_chg_pwd_valid_similar():
    result=ChangePassword("VolkswagenBeetle2021!","vOlKsWaGenbeetle2021!")
    assert result == True   

def test_chg_pwd_inv_sim100():
    result=ChangePassword("VolkswagenBeetle2021!","VolkswagenBeetle2021!")
    assert result == False

def test_chg_pwd_valid_sim76():
    result=ChangePassword("VolkswagenBeetle2021!","Volkswagenabc2021!")
    assert result == True

def test_chg_pwd_inv_sim81():
    result=ChangePassword("VolkswagenBeetle2021!","VolkswagenBeabcd2021!")
    assert result == False

def test_chg_pwd_valid_spstart():
    result=ChangePassword("VolkswagenBeetle2021!","!@BentleyContinental12!!")
    assert result == True