# English to Arabic Translators

This is a python 3 web scraping script to translate English text to Arabic,
and back,
using the web browser automation tool Selenium.

The translation is done using the service provided by freetranslations.org


### How to Use?

Instantiate a Translator object, then call `translate(text)` on it like so:

```python
from Translator import Translator

tr = Translator()

text = input("Type Something: ")
arab_translation = tr.translate(text)
print(arab_translation)
back_to_english = tr.reverse(arab_translation)
print(back_to_english)
```

Note: you could pass `True` to Translator to make it headless.


### Installation

Install Selenium and click using:

```
pip install selenium click
```

Then download Chrome WebDriver from
[here](https://chromedriver.storage.googleapis.com/index.html?path=2.46/),
then extract and place it in the same folder.
or if you choose to use Firefox, install geckodriver

```
sudo apt install firefox-geckodriver
```


### Contents

- Translator.py: A class which opens the browser and provide a function to translate text.
- Sample.py: A simple script that demonstrates the use of Translator on a text file.
- echoscript.py: A personal script that echoes back personal poems written by me, Karen.

### References

- [Translation Service](https://www.freetranslations.org/english-to-arabic-translation.html)
- [Selenium WebDriver](https://selenium-python.readthedocs.io)
