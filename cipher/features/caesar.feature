Feature: Encrypting and decrypting caesar cipher
  As someone who enjoys ciphers
  I want websites that can encrypt and decrypt caesar cipher
  to function properly.

  Scenario: Encrypting valid text with caesar cipher
    Given I open the caesar cipher page
    When I caesar cipher encrypt the text "hello there" with key "3"
    Then I expect the encrypted result to be "KHOOR WKHUH"
  
  Scenario: Decrypting valid text with caesar cipher (manual decryption)
    Given I open the caesar cipher page
    When I caesar cipher decrypt the text "Krz duh brx grlqj" with key "3"
    Then I expect the decrypted result to be "how are you doing"
  
  Scenario: Bruteforcing valid text with caesar cipher
    Given I open the caesar cipher bruteforce page
    When I caesar cipher bruteforce the text "krz duh brx grlqj"
    Then I expect the bruteforce result to be "how are you doing"
  
  Scenario: Bruteforcing valid French text with caesar cipher
    Given I open the caesar cipher bruteforce page
    When I caesar cipher bruteforce the text "Uhgchnk, jnxe xlm ohmkx ghf?"
    Then I expect the bruteforce result to be "Bonjour, quel est votre nom?"

  Scenario: The bruteforcer got it wrong. Check other results.
    Given I open the caesar cipher bruteforce page
    When I caesar cipher bruteforce the text "MEHTEFEBYI"
    Then I expect the bruteforce result to be "MEHTEFEBYI"
    And I expect the 2nd best bruteforce result to be "WORDOPOLIS"

  Scenario: Bruteforcing empty text with caesar cipher
    Given I open the caesar cipher bruteforce page
    When I caesar cipher bruteforce the text " "
    Then I expect the bruteforce result to be " "

  Scenario: Using the - and + buttons to manually shift
    Given I open the caesar cipher bruteforce page
    When I caesar cipher bruteforce the text "MEHTEFEBYI"
    Then I expect the bruteforce result to be "MEHTEFEBYI"
    When I shift it 16 to the right 16 times
    Then I expect the bruteforce result to be "WORDOPOLIS"