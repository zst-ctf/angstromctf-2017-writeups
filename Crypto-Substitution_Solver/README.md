# Substitution Cipher
**Category: Crypto**
**Points: 60**

### Challenge
> We have discovered some [ciphertext](https://angstromctf.com/static/crypto/substitution_cipher/ciphertext.txt). We need you to find the plaintext. The flag is in the {flag} format, not the actf{flag} format. There are no spaces in flag.

### Hint
> The letters seem to be the only thing that was encrypted...how unfortunate.

### Solution
Unfortunately, [quipqiup](http://quipqiup.com/) did not solve it for me, so let's try [another substitution solver tool](https://www.guballa.de/substitution-solver). This time the latter worked, the result is in *output.txt*


From the hint, we can see that the flag is the last portion of the ciphertext because of the braces `{ }`
Hence, the flag is `{fewgoodmenjessep}`