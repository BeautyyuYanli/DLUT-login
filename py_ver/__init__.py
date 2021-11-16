from . import des
import requests

def initial(initUrl, id):
    s = requests.Session()
    response = s.get(initUrl)
    al = 'LT{}cas'.format(response.text.split('LT')[1].split('cas')[0])
    s.cookies.set('dlut_cas_un', id)
    s.cookies.set('cas_hash', "")
    return s, al

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
    targetUrl = 'https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php'
    s, lt = initial(targetUrl, id)
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
    res = s.post(targetUrl, constructPara(id, passwd, lt), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return s

if __name__ == '__main__':
    s = login('19260817', '123456')
    s.get('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/login.php?redirect=index.php')
    print(s.post('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/orderRoomAction.php?action=checkSession').text)