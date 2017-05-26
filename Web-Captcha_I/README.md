# Captcha I
**Category: Web**
**Points: 70**

### Challenge
> As an avid fan of computer generated postmodernism, you have come across a [website](http://web.angstromctf.com:1342/) that uses computer art as a captcha. Enter the correct pin number to get the flag.

### Hint
> Good thing the pin is so short.

### Solution
I'm not sure if it is the correct method of doing so, but I bruteforced both the captcha and the pin using a Python script.

At pin 612, the page returns the flag `actf{comp_abstract_art_2F239B}`