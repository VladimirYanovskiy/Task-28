from api import Passport
from settings import valid_telephone_7, valid_email, valid_login, valid_personal_account, valid_password, invalid_password, \
    valid_telephone_8, invalid_telephone_1, invalid_telephone_2, invalid_telephone_3, \
    valid_email_1, invalid_email_2, invalid_email_3, invalid_email_4, invalid_personal_account_4, \
    invalid_personal_account_6, invalid_personal_account_8, invalid_personal_account_11, invalid_personal_account_13
import os

pf = Passport()


# Test EXP-010
def test_get_api_key_with_correct_telephone_7_and_correct_password(telephone_7=valid_telephone_7, password=valid_password):
    """Проверка авторизации существующего клиента по номеру мобильного телефона и паролю,
    с использованием корректных данных и кода абонента "7"."""
    status, result = pf.get_api_key_tel7(telephone_7, password)

    assert status == 200
    assert 'key' in result

# Test EXP-011
def test_get_api_key_with_correct_email_and_correct_password(email=valid_email, password=valid_password):
    """Проверка авторизации существующего клиента по почте и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_mail(email, password)

    assert status == 200
    assert 'key' in result

# Test EXP-012
def test_get_api_key_with_correct_login_and_correct_password(login=valid_login, password=valid_password):
    """Проверка авторизации существующего клиента по логину и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_log(login, password)

    assert status == 200
    assert 'key' in result

# Test EXP-013
def test_get_api_key_with_correct_personal_account_and_correct_password(personal_account=valid_personal_account, password=valid_password):
    """Проверка авторизации существующего клиента по лицевому счёту и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_account(personal_account, password)

    assert status == 200
    assert 'key' in result

# Test EXP-014
def test_get_api_key_with_correct_telephone_8_and_correct_password(telephone_8=valid_telephone_8, password=valid_password):
    """Проверка авторизации существующего клиента по номеру мобильного телефона и паролю,
    с использованием корректных данных и кода абонента "8"."""
    status, result = pf.get_api_key_tel8(telephone_8, password)

    assert status == 200
    assert 'key' in result

# Test EXP-015
def test_get_api_key_with_wrong_telephone_1_and_correct_password(telephone_1=invalid_telephone_1, password=valid_password):
    """Проверка авторизации с использованием некорректного телефону 12 цифр и корректного пароля."""
    status, result = pf.get_api_key_tel1(telephone_1, password)

    assert status == 403
    assert 'key' in result

# Test EXP-016
def test_get_api_key_with_wrong_telephone_2_and_correct_password(telephone_2=invalid_telephone_2, password=valid_password):
    """Проверка авторизации с использованием некорректного телефона 10 цифр и корректного пароля."""
    status, result = pf.get_api_key_tel2(telephone_2, password)

    assert status == 403
    assert 'key' in result

# Test EXP-017
def test_get_api_key_with_wrong_telephone_3_and_correct_password(telephone_3=invalid_telephone_3, password=valid_password):
    """Проверка авторизации с использованием некорректного телефона 10 цифр, 1 буква и корректного пароля."""
    status, result = pf.get_api_key_tel3(telephone_3, password)

    assert status == 403
    assert 'key' in result

# Test EXP-018
def test_get_api_key_with_incorrect_valid_email_1_and_correct_password(email_1=valid_email_1, password=valid_password):
    """Проверка авторизации с использованием некорректной валидной электронной почты и корректного пароля."""
    status, result = pf.get_api_key_mail1(email_1, password)

    assert status == 403
    assert 'key' in result

# Test EXP-019
def test_get_api_key_with_correct_invalid_email_2_and_correct_password(email_2=invalid_email_2, password=valid_password):
    """Проверка авторизации с использованием корректной электронной почты без символа "@" и корректного пароля."""
    status, result = pf.get_api_key_mail2(email_2, password)

    assert status == 403
    assert 'key' in result

# Test EXP-020
def test_get_api_key_with_correct_invalid_email_3_and_correct_password(email_3=invalid_email_3, password=valid_password):
    """Проверка авторизации с использованием корректной электронной почты без символа "." и корректного пароля."""
    status, result = pf.get_api_key_mail3(email_3, password)

    assert status == 403
    assert 'key' in result

# Test EXP-021
def test_get_api_key_with_correct_invalid_email_4_and_correct_password(email_4=invalid_email_4, password=valid_password):
    """Проверка авторизации с использованием корректной электронной почтой без символа "@", "." и корректного пароля."""
    status, result = pf.get_api_key_mail4(email_4, password)

    assert status == 403
    assert 'key' in result

# Test EXP-022
def test_get_api_key_with_invalid_personal_account_4_and_correct_password(personal_account_4=invalid_personal_account_4, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (4 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account4(personal_account_4, password)

    assert status == 403
    assert 'key' in result

# Test EXP-023
def test_get_api_key_with_invalid_personal_account_6_and_correct_password(personal_account_6=invalid_personal_account_6, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (6 цифр) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account6(personal_account_6, password)

    assert status == 403
    assert 'key' in result

# Test EXP-024
def test_get_api_key_with_invalid_personal_account_8_and_correct_password(personal_account_8=invalid_personal_account_8, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (8 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account8(personal_account_8, password)

    assert status == 403
    assert 'key' in result

# Test EXP-025
def test_get_api_key_with_invalid_personal_account_11_and_correct_password(personal_account_11=invalid_personal_account_11, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (11 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account11(personal_account_11, password)

    assert status == 403
    assert 'key' in result

# Test EXP-026
def test_get_api_key_with_invalid_personal_account_13_and_correct_password(personal_account_13=invalid_personal_account_13, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (13 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account13(personal_account_13, password)

    assert status == 403
    assert 'key' in result

# Test EXP-027
def test_get_api_key_with_correct_telephone_7_and_wrong_password(telephone_7=valid_telephone_7, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного мобильного телефона и неверного пароля."""
    status, result = pf.get_api_key_tel7(telephone_7, password)

    assert status == 403
    assert 'key' in result

# Test EXP-028
def test_get_api_key_with_correct_email_and_wrong_password(email=valid_email, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректной почты и неверного пароля."""
    status, result = pf.get_api_key_mail(email, password)

    assert status == 403
    assert 'key' in result

# Test EXP-029
def test_get_api_key_with_correct_login_and_wrong_password(login=valid_login, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного логина и неверного пароля."""
    status, result = pf.get_api_key_log(login, password)

    assert status == 403
    assert 'key' in result

# Test EXP-030
def test_get_api_key_with_correct_personal_account_and_wrong_password(personal_account=valid_personal_account, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного лицевого счёта и неверного пароля."""
    status, result = pf.get_api_key_account(personal_account, password)

    assert status == 403
    assert 'key' in result