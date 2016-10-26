#!/usr/bin/python
#  -*- coding:utf-8 -*-
#Author DOUMEKI

from selenium import  webdriver
import unittest,time
from selenium.webdriver.common.keys import  Keys


#第一步，用Django创建一个项目， 命令 django-admin startproject <projectName>
#第二步，使用manage.py，创建一个本地web服务器，命令manage.py runserver
#第三步，类继承于testcase类，运行main方法后,可以自动运行test 方法。
#第四步，查看创建的服务器地址，根据需要运行脚本
class TestOne(unittest.TestCase):

    def setUp(self):
        self.startwith()

    def tearDown(self):
        print('closed')

    def startwith(self):
        print ('startwith')
        self.chrome= webdriver.Chrome()
        # self.chrome= webdriver.Ie()
        self.chrome.get('http://127.0.0.1:8000')


    def test_can_start_a_list_and_retrivew_it_later(self):
        self.assertIn('To-Do',self.chrome.title)
        header_text = self.chrome.find_element_by_tag_name('h1').text
        self.assertIn("To-Do",header_text)

        inputbox = self.chrome.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.chrome.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make fly')
        self.fail("Finish the test !")

    def check_for_row_in_list_table(self,rowtext):
        table = self.chrome.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),'New to-do item did not appear in table')
        self.assertIn(rowtext, [row.text for row in rows])



if __name__ == '__main__':
    unittest.main(warnings='ignore')

