const des = require('./des.js');
const got = require('got');
const tough = require('tough-cookie');
var baseUrl
initial = async (initUrl) => {
    const cookieJar = new tough.CookieJar();
    const res = await got({
        method: 'get',
        url: initUrl,
        cookieJar
    });
    const lt = 'LT' + res.body.split('LT')[1].split('cas')[0] + 'cas';
    const buttonLink = res.body.split('action="')[1].split('"')[0]
    for (let i in res.headers['set-cookie'])
        await cookieJar.setCookie(res.headers['set-cookie'][i], baseUrl);
    return { lt, buttonLink, cookieJar }
}
constructPara = async (id, passwd, lt) => {
    const al = {
        'none': 'on',
        'rsa': des.strEnc(id + passwd + lt, '1', '2', '3'),
        'ul': id.length,
        'pl': passwd.length,
        'lt': lt,
        'execution': 'e1s1',
        '_eventId': 'submit',
    };
    let be = '';
    for (i in al) {
        be += i + '=' + al[i] + '&';
    }
    return be;
}
login = async (id, passwd) => {
    baseUrl = 'https://webvpn.dlut.edu.cn'
    const { lt, buttonLink, cookieJar } = await initial('https://webvpn.dlut.edu.cn/login?cas_login=true')
    let res = await got({
        method: 'post',
        url: baseUrl + buttonLink,
        cookieJar,
        body: await constructPara(id, passwd, lt),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        followRedirect: false,
    });
    for (let i in res.headers['set-cookie'])
        await cookieJar.setCookie(res.headers['set-cookie'][i], baseUrl);
    res = await got({
        method: 'get',
        url: res.headers['location'],
        cookieJar,
    });
    return cookieJar;
}
module.exports = login;