from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# === GIVEN ===

@given("I open the caesar cipher page")
def step_open_simple_page(context):
    context.behave_driver.get("https://www.simonsingh.net/The_Black_Chamber/caesar.html")

@given("I open the caesar cipher bruteforce page")
def step_open_bruteforce_page(context):
    context.behave_driver.get("https://www.nayuki.io/page/automatic-caesar-cipher-breaker-javascript")

@given("I open the vignere cipher page")
def step_open_vignere_page(context):
    context.behave_driver.get("https://www.nayuki.io/page/vigenere-cipher-javascript")

# === WHEN ===

@when(u'I caesar cipher encrypt the text "{text}" with key "{key}"')
def step_encrypt_with_key(context, text, key):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.presence_of_element_located((By.NAME, "actual")))
    text_area.clear()
    text_area.send_keys(text)
    
    key_input = wait.until(EC.presence_of_element_located((By.NAME, "num")))
    key_input.clear()
    key_input.send_keys(key)

    encrypt_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Encipher Plaintext"))
    )
    encrypt_button.click()

@when(u'I caesar cipher decrypt the text "{text}" with key "{key}"')
def step_decrypt_with_key(context, text, key):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.presence_of_element_located((By.NAME, "encpt")))
    text_area.clear()
    text_area.send_keys(text)
    
    key_input = wait.until(EC.presence_of_element_located((By.NAME, "num")))
    key_input.clear()
    key_input.send_keys(key)

    decrypt_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Decipher Plaintext"))
    )
    decrypt_button.click()

@when(u'I caesar cipher bruteforce the text "{text}"')
def step_bruteforce(context, text):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.presence_of_element_located((By.ID, "text")))
    text_area.clear()
    text_area.send_keys(text)

    break_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='app.doBreak();']"))
    )
    break_button.click()
    
    wait.until(EC.presence_of_element_located((By.ID, "text")))

@when(u'I shift it 16 to the right {key} times')
def step_shift_bruteforce(context, key):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    for i in range(int(key)):
        break_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='app.doShift(+1);']"))
        )
        break_button.click()

    
@when(u'I vignere encrypt the text "{text}" with key "{key}"')
def step_encrypt_vignere(context, text, key):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.presence_of_element_located((By.ID, "text")))
    text_area.clear()
    text_area.send_keys(text)

    key_area = wait.until(EC.presence_of_element_located((By.ID, "key")))
    key_area.clear()
    key_area.send_keys(key)
    
    encrypt_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='app.doCrypt(false);']"))
    )
    encrypt_button.click()

@when(u'I vignere decrypt the text "{text}" with key "{key}"')
def step_decrypt_vignere(context, text, key):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.presence_of_element_located((By.ID, "text")))
    text_area.clear()
    text_area.send_keys(text)

    key_area = wait.until(EC.presence_of_element_located((By.ID, "key")))
    key_area.clear()
    key_area.send_keys(key)

    decrypt_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='app.doCrypt(true);']"))
    )
    decrypt_button.click()


# === THEN ===

@then(u'I expect the encrypted result to be "{text}"')
def step_check_encrypt_result(context, text):
    driver = context.behave_driver
    actual_text = driver.find_element(By.NAME, "encpt").get_attribute("value")
    assert actual_text == text, f"Expected '{text}', but got '{actual_text}'"

@then(u'I expect the decrypted result to be "{text}"')
def step_check_decrypt_result(context, text):
    driver = context.behave_driver
    actual_text = driver.find_element(By.NAME, "actual").get_attribute("value")
    assert actual_text == text, f"Expected '{text}', but got '{actual_text}'"

@then(u'I expect the bruteforce result to be "{text}"')
def step_check_best_bruteforce_result(context, text):
    driver = context.behave_driver
    
    result_textarea = driver.find_element(By.ID, "text")
    actual_text = result_textarea.get_attribute("value")
    
    assert actual_text.lower() == text.lower(), f"Expected '{text.lower()}', but got '{actual_text}'"

@then(u'I expect the 2nd best bruteforce result to be "{text}"')
def step_check_second_best_bruteforce_result(context, text):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    result_textarea = driver.find_element(By.ID, "text")
    old_text = result_textarea.get_attribute("value")
    
    second_result = driver.find_element(By.CSS_SELECTOR, "tbody#guesses tr:nth-of-type(2)")
    second_result.click()

    try:
        wait.until(
            lambda d: d.find_element(By.ID, "text").get_attribute("value") != old_text
        )
    except TimeoutException:
        pass 
    
    actual_text = result_textarea.get_attribute("value")
    
    assert actual_text.lower() == text.lower(), f"Expected '{text.lower()}', but got '{actual_text}'"

@then(u'I expect the vignere result to be "{text}"')
def step_check_vignere_result(context, text):
    driver = context.behave_driver
    
    result_textarea = driver.find_element(By.ID, "text")
    actual_text = result_textarea.get_attribute("value")
    
    assert actual_text.lower() == text.lower(), f"Expected '{text.lower()}', but got '{actual_text}'"

@then(u'I expect an error')
def step_check_alert(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
    except TimeoutException:
        assert False, "Expected alert box to appear; it didn't."