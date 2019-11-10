#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      L
#
# Created:     09/11/2019
# Copyright:   (c) L 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib
import time
import win32com.client as w
from bs4 import BeautifulSoup

def main():
    page_link = r'https://swapi.co/api/people'
    api = ApiHelper()
    api.star_wars_characters(page_link)
    print(api.star_wars_details)


class ApiHelper:
    def __init__(self):
        self.star_wars_details = dict({0 : {'name' : 'Star War character name',
                                            'age' : 'Star War character age',
                                            'height' : 'Star War character height',
                                            'gender' : 'Star War character gender'}})

    def star_wars_characters(self, page_nr):
        ie = w.Dispatch('InternetExplorer.Application')
        ie.visible = True

        html_text = self.get_html_data_from_url(ie, page_nr)

        self.extract_data(html_text)

        # check if more results on next page exists
        link_for_next = self.check_next_exist(html_text)

        while (link_for_next):

            next_html_text = self.get_html_data_from_url(ie, link_for_next)

            self.extract_data(next_html_text)

            link_for_next = None;

            link_for_next = self.check_next_exist(next_html_text)



    def get_html_data_from_url(self, ie_object, url):

        ie_object.navigate(url)

        while ie_object.ReadyState !=4:
            time.sleep(2)

        doc = ie_object.Document

        while doc.ReadyState !='complete':
            time.sleep(2)

        text = ie_object.Document.body.InnerHTML

        return text


    def extract_data(self, html_data):
        soup = BeautifulSoup(html_data, r"html.parser")
        data_text = soup.get_text()
        data_list = data_text.split('{')

##        if 'HTTP 404 NOT FOUND' in data_text:
##            return

        for each_data in data_list:
            if 'name' in each_data:

                # determine next index of start wars details dictionalry
                star_wars_index = len(self.star_wars_details)
                self.star_wars_details[star_wars_index] = dict()

                data = each_data.split('\n')

                for each in data:
                    if 'name' in each or 'birth_year' in each or 'gender' in each or 'height' in each:
                        data = each.strip().replace(',', '').split(':')
                        self.star_wars_details[star_wars_index][data[0]] = data[1]


    def check_next_exist(self, html_data):
        soup = BeautifulSoup(html_data, r"html.parser")
        data_text = soup.get_text()
        data_list = data_text.split('{')

        for each_data in data_list:
            if 'count' in each_data and 'next' in each_data:
                data = each_data.split('\n')

                for each in data:
                    if 'next' in each:
                        data = each.split(': ')
                        if data[1].strip().replace(',', '') == 'null':
                            return None
                        else:
                            return data[1].replace("\"", '').replace(',', '')


if __name__ == '__main__':
    main()
