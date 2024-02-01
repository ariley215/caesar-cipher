# LAB - Class 18

Project: Cryptography - the Caesar Cipher

Author: Andrea Riley(Thiel)

Collaborator: Stephanie Johnson

## Feature Tasks

Create an encrypt function that takes in a plain text phrase and a numeric shift.

- the phrase will then be shifted that many letters. *completed 01-31-2024 3:30PM EST*
  - E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
- shifts that exceed 26 should wrap around. *completed 01-31-2024 3:30PM EST*
  - E.g. encrypt(‘abc’,27) would return ‘bcd’.
- shifts that push a letter out or range should wrap around. *completed 01-31-2024 4:30PM EST*
  - E.g. encrypt(‘zzz’,1) would return ‘aaa’.
- Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.*completed 01-31-2024 4:30PM EST*
- Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.*completed 02-01-2024 5:30PM EST*
- Devise a method for the computer to determine if code was broken with minimal human guidance.*completed 02-01-2024 5:30PM EST*

## Setup

How to initialize/run your application (where applicable)

python caesar_cipher/cipher.py

## Tests

Run tests: pytest tests/test_ceasar.py


Describe any tests that you did not complete, skipped, etc:

The two tests for the crack function are failing
