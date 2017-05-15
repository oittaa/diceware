# Diceware password generator

Diceware password generator in Python. Uses "EFF's New Wordlists for Random Passphrases" dictionary.

```bash
git clone https://github.com/oittaa/diceware.git
cd diceware
./diceware.py
```

For example:

```
$ ./diceware.py
recapture animosity jawline fanciness marshland clear
```

## Is it secure?

The security level provided by Diceware depends heavily on your source of
random.

This Python implementation uses the `random.SystemRandom` source provided by
Python. On Linux, `getrandom()` syscall is used if available. On a Unix-like
system, random bytes are read from the `/dev/urandom` device. On Windows, it
will use `CryptGenRandom()`.

### Links

* [EFF's New Wordlists for Random Passphrases](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)
* [eff_large_wordlist.txt](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt)
* [random.SystemRandom](https://docs.python.org/3/library/random.html#random.SystemRandom)
