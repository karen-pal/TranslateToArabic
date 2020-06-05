from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import click

LANGUAGES = {
    "turkish": "https://www.freetranslations.org/english-to-turkish-translation.html",
    "arab": "https://www.freetranslations.org/english-to-arabic-translation.html",
    "greek": "https://www.freetranslations.org/english-to-greek-translation.html",
    "hindi": "https://www.freetranslations.org/english-to-hindi-translation.html",
    "spanish": "https://www.freetranslations.org/english-to-spanish-translation.html",
    "german": "https://www.freetranslations.org/english-to-german-translation.html",
}


class Translator:
    def __init__(self, language, browser="Firefox", headless=False):
        options = Options()
        if headless:
            options.headless = True
        if browser == "Firefox":
            from selenium.webdriver import Firefox

            self._br = Firefox()
        self._br.get(LANGUAGES[language])
        # self._br.set_page_load_timeout(25)

    def translate(self, string):
        if not string:
            return "Done"
        for i in range(3):
            try:
                return self._translate(string.replace("\\", ""))
            except Exception as e:
                print(e)
                sleep(2)
        raise ConnectionAbortedError

    def _translate(self, string):
        tag = self._br.find_element_by_id("InputText")
        tag.send_keys(Keys.CONTROL + "a")
        tag.send_keys(Keys.DELETE)
        tag.send_keys(string)
        self._br.find_element_by_class_name("translate-form-control").click()
        WebDriverWait(self._br, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "mttextarea"))
        )
        return self._br.find_element_by_xpath("//*[@id='TranslationOutput']/div").text

    def reverse(self, string):
        tag = self._br.find_element_by_id("LangPair_SwapImg")
        tag.click()
        tag = self._br.find_element_by_id("InputText")
        tag.send_keys(Keys.CONTROL + "a")
        tag.send_keys(Keys.DELETE)
        return self.translate(string)

    def close(self):
        self._br.close()


@click.command
@click.option(
    "--browser",
    default="Firefox",
    help="browser to run the script to. Options: Firefox, Chrome",
)
def translator(browser):
    return Translator()
