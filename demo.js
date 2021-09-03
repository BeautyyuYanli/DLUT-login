// this demo shows how to login the webvpn system using the code in py_ver/
// and then login the liberary seats revervation system through webvpn
// and then check the session status

const got = require('got');
const login = require('./js_ver');
baseUrl = 'https://webvpn.dlut.edu.cn/';
main = async() => {
    // login webvpn system
    // login(username, passwd)
    const cookieJar = await login('19260817', '123456')
    // show the cookieJar
    console.log(cookieJar.getCookies(baseUrl))
    // login liberary seats reservation system
    let res = await got({
        method: 'get', 
        url: 'https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/login.php?redirect=index.php',
        cookieJar,
    });
    for (let i in res.headers['set-cookie'])
        await cookieJar.setCookie(res.headers['set-cookie'][i], baseUrl);
    // check session status
    res = await got({
        method: 'post', 
        url: 'https://webvpn.dlut.edu.cn/http/77726476706e69737468656265737421e3f24088693c6152300c85b98c1b26312567d1d0/yanxiujian/client/orderRoomAction.php?action=checkSession',
        cookieJar,
    });
    console.log(res.body)
}
main()