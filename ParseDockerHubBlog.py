import requests
import re
import json
from pprint import pprint


def read_data_from_site():
    result = {}
    for item in range(1, 97):
        page_dict = {}
        url = 'https://www.docker.com/blog/page/{}/'.format(str(item))
        print(url)
        response = requests.get(url)
        response = response.text.splitlines()
        for line in response:
            match = re.search('<h\d class="post-title"><a href="(.+)">(.+)</a></h\d>', line)
            if match:
                page_dict.update({match.group(2) : match.group(1)})
        result.update({str(item) : page_dict})
    with open('result_dict.json', 'w') as file:
        file.write(json.dumps(result))


if __name__ == '__main__':

    while True:

        choice = input('Press:\n1 - read headers from file\n2 - read headers from site\n')
        if choice == '1':
            with open('result_dict.json') as file:
                result = json.loads(file.read())
            break
        elif choice == '2':
            read_data_from_site()
            with open('result_dict.json') as file:
                result = json.loads(file.read())
            break
        else:
            print('Wrong choise')

    while True:
        selector = input('Enter page number: ')
        pprint(result.get(selector))