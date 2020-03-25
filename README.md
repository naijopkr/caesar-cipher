# CAESAR CIPHER

## USAGE INSTRUCTION

1. Clone the repository:
```
$ git clone https://github.com/naijopkr/caesar-cipher.git
$ cd caesar-cipher
```

2. Create and activate the virtual environment:
```
$ python -m venv venv
$ source venv/bin/activate
```

3. Install requirements:
```
$ pip install -r requirements.txt
```

4. Test encryption:
```
$ python . -i test.txt -o test_output.txt -k <key_number> // eg: 3
```

5. Test decryption:
```
$ python . -d -i test_output.txt -o test_decrypt.txt -k <key_number> // same used on encryption
```

Check out if the test.txt and the test_decrypt.txt are equal. Check out if the test_output.txt is encrypted. If you find something wrong, let me know. Have fun!
