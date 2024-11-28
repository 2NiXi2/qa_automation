import base64
import os
import random

from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from generator.generator import generated_file
from pages.base_page import BasePage


class UploadAndDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/upload-download')
        self.upload_file_btn = Button(driver, (By.XPATH, '//*[@id="uploadFile"]'))
        self.download_file_btn = Button(driver, (By.XPATH, '//*[@id="downloadButton"]'))
        self.download_result = TextField(driver, (By.XPATH, '//*[@id="uploadedFilePath"]'))

    def upload_file(self):
        file_name, path = generated_file()
        self.upload_file_btn.is_present()
        self.upload_file_btn.send_keys(path)
        os.remove(path)
        self.download_result.is_present()
        text = self.download_result.text()
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        self.download_file_btn.is_present()
        link = self.download_file_btn.get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'D:\PYcharm\qa_automation\testfile{random.randint(0, 888)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file