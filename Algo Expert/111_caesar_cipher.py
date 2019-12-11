"""
Caesar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
Sample input: "xyz", 2 Sample output: "zab"
"""

def caesarCipherEncryptor(string,key):
    answer=""
    for i in range(len(string)):
        dig = ord(string[i])
        new = dig + key%26
        if new > 122:
            new = dig + key%26 - 122 + 96

        answer += chr(new)

    return answer


print(caesarCipherEncryptor('xyz',2))
print(caesarCipherEncryptor('abc',26))