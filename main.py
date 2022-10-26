# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os

from bs4 import BeautifulSoup

import requests


def get_title_html(html_1):
    soup = BeautifulSoup(html_1, "html.parser")
    title_url_date = soup.find('div', class_='clearfix dirconone').find_all('li')
    for i in title_url_date:
        # print(i)
        url = i.find('a')['href']
        print(url)


def generate_git_url():
    entries = os.listdir('C:\\Users\\admin\\Desktop\\Gitee\\android')
    for entry in entries:
        print(entry)
        with open('data.txt', 'a') as f:
            data = 'ssh://git@xx.xx.xx.xx:1022/android/' + entry.__str__() + '\n'
            f.write(data)


def generate_git_url1():
    with open('url/android.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            l = line.replace('http://xx.xx.com/gitlab/android/', '').replace('.git', '')
            print(l)
            with open('handle/android.txt', 'a') as f1:
                f1.write(l)


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
            elif line.__contains__('ntyytech-java'):
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
    with open('handle/java/taoke.txt', 'r') as f:
        readlines = f.readlines()
        print(readlines)
        for line in readlines:
            new_project_name = line.replace('\n', '')
            print(new_project_name)
            api_create_project(new_project_name, java_taoke)


if __name__ == '__main__':
    create_android_projects()
    # handle_url('data1.txt')
    # generate_git_url1()
