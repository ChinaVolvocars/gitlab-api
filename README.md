# 使用gitlab api批量创建1000个新的项目






```py
import os

import requests
from bs4 import BeautifulSoup

android = 6
ios = 7
web = 8
tools = 10

java_framework = 11
java_mid = 12
java_obs = 13
java_other = 14
java_public_service = 15
java_social = 16
java_taoke = 17
java_xiyakjx = 18

devops = 19
private_token = 'NZjJatp45hjxMhZRVUGh'
gitlab_host = 'http://192.168.5.59:1080/'
headers = {
    'PRIVATE-TOKEN': private_token
}

api_projects = 'api/v4/projects/'

def api_create_project(new_project_name, namespace_id):
    """
    使用gitlab api批量创建项目
    """
    payload = {
        "name": new_project_name,
        "path": new_project_name,
        "namespace_id": namespace_id,
        "initialize_with_readme": "false"
    }
    res = requests.post(url=('%s%s' % (gitlab_host, api_projects)), params=payload, headers=headers)
    print(res.json())


def handle_url(file):
    """
    分类url
    """
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.__str__()
            if line.__contains__('android'):
                print('android：%s' % line)
                with open('url/android.txt', 'a') as f1:
                    f1.write(line)
            elif line.__contains__('ios'):
                print('ios：%s' % line)
                with open('url/ios.txt', 'a') as f1:
                    f1.write(line)
            elif line.__contains__('h5'):
                print('web：%s' % line)
                with open('url/web.txt', 'a') as f1:
                    f1.write(line)
            elif line.__contains__('java'):
                print('java：%s' % line)
                with open('url/java.txt', 'a') as f1:
                    f1.write(line)
            elif line.__contains__('tools/'):
                print('tools：%s' % line)
                with open('url/tools.txt', 'a') as f1:
                    f1.write(line)
            else:
                print('other：%s' % line)
                with open('url/other.txt', 'a') as f1:
                    f1.write(line)


def create_android_projects():
    """
    取出android.txt中要创建的项目名称，调用api开始批量创建项目
    """
    with open('handle/java/tk.txt', 'r') as f:
        readlines = f.readlines()
        print(readlines)
        for line in readlines:
            new_project_name = line.replace('\n', '')
            print(new_project_name)
            api_create_project(new_project_name, java_taoke)


if __name__ == '__main__':
    create_android_projects()


```
