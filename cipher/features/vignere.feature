Feature: Encoding and decoding Vignere
As someone who enjoys ciphers
  I want a website that can encrypt and decrypt vignere
  to function properly.

  Background:
    Given I open the vignere cipher page
  Scenario: Encrypting valid text with Vignere
    When I vignere encrypt the text "Visioneer" with key "PUN"
    Then I expect the vignere result to be "Kcfxiatye"

  Scenario: Decrypting valid text with Vignere
    When I vignere decrypt the text "Ymern ylxsapffk" with key "WORDS"
    Then I expect the vignere result to be "Cynov cxgpitroh"
    When I vignere decrypt the text "Cynov cxgpitroh" with key "KEY"
    Then I expect the vignere result to be "Super encrypted"

  Scenario: Decrypting empty text with Vignere
    When I vignere decrypt the text " " with key "UNLOCK"
    Then I expect the vignere result to be " "

  Scenario: Decrypting text with an empty key with Vignere
    When I vignere decrypt the text "Wabx robr" with key " "
    Then I expect an error
  
  Scenario: Decrypting text with a symbols only key with Vignere
    When I vignere decrypt the text "kwyccwk" with key "1337"
    Then I expect an error

  Scenario: Encrypting empty text with Vignere
    When I vignere encrypt the text " " with key "TOSUCCESS"
    Then I expect the vignere result to be " "

  Scenario: Encrypting text with an empty key with Vignere
    When I vignere encrypt the text "Filler text" with key " "
    Then I expect an error
  
  Scenario: Encrypting text with a symbols only key with Vignere
    When I vignere encrypt the text "1337 $P34K" with key "1337"
    Then I expect an error