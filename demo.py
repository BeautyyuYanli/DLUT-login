# this demo shows how to login the webvpn system using the code in py_ver/
# and then login the liberary seats revervation system through webvpn
# and then check the session status

import py_ver
# login webvpn system
# s: requests.Session
s = py_ver.login(id='19260817', passwd='123456')
# show the wengine_vpn_ticket
print(s.cookies['wengine_vpn_ticket'])
# login liberary seats reservation system
s.get('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/login.php?redirect=index.php')
# check session status
print(s.post('https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/orderRoomAction.php?action=checkSession').text)