from . import des
import requests

def initial(initUrl):
    s = requests.Session()
    response = s.get(initUrl)
    al = 'LT{}cas'.format(response.text.split('LT')[1].split('cas')[0])
    be = response.text.split('action="')[1].split('"')[0]
    return s, al, be

def constructPara(id, passwd, lt):
    al = {
        'none': 'on',
        'rsa': des.strEnc(id+passwd+lt, '1', '2', '3'),
        'ul': str(len(id)),
        'pl': str(len(passwd)),
        'lt': lt,
        'execution': 'e1s1',
        '_eventId': 'submit',
    }
    return '&'.join([i+'='+j for i, j in al.items()])

def login(id, passwd):
    baseUrl = 'https://webvpn.dlut.edu.cn'
    # baseUrl = 'https://sso.dlut.edu.cn'
    s, lt, buttonLink = initial('https://webvpn.dlut.edu.cn/login?cas_login=true')
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    }
    res = s.post(baseUrl + buttonLink, constructPara(id, passwd, lt), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return s

if __name__ == '__main__':
    s = login('19260817', '123456')
    s.get('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/login.php?redirect=index.php')
    print(s.post('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/orderRoomAction.php?action=checkSession').text)