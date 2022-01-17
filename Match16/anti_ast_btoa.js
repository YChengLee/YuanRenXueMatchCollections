f = "U9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi+9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi";
var md5 = require('./md5');

function d(e) {
  var n = {};
  n.fYWEX = function (e, t) {
    return e || t;
  }, n.bWcgB = function (e, t) {
    return e * t;
  }, n.SlFsj = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678";

  for (var r = n, o = "1|3|0|4|2|5".split("|"), a = 0;;) {
    switch (o[a++]) {
      case "0":
        var s = l.length;
        continue;

      case "1":
        e = r.fYWEX(e, 32);
        continue;

      case "2":
        for (i = 0; i < e; i++) c += l.charAt(Math.floor(r.bWcgB(Math.random(), s)));
        continue;

      case "3":
        var l = r.SlFsj;
        continue;

      case "4":
        var c = "";
        continue;

      case "5":
        return c;
    }

    break;
  }
}



function btoa(e) {
  var r = {};
  r.TGmSp = "INVALID_CHARACTER_ERR", r.SkkHG = "return /\" + this + \"/", r.TKgNw = "^([^ ]+( +[^ ]+)+)+[^ ]}", r.aYkvo = function (e) {
    return e();
  }, r.kukBH = function (e, t) {
    return e % t;
  }, r.evetF = function (e, t) {
    return e >> t;
  }, r.GfTek = "iwnNJ",
  r.pHtmC = function (e, t) {
    return e << t;
  }, r.LCaAn = function (e, t) {
    return e | t;
  }, r.cVCcp = function (e, t) {
    return e << t;
  }, r.OWUOc = function (e, t) {
    return e & t;
  }, r.thjIz = function (e, t) {
    return e << t;
  }, r.jLRMs = function (e, t) {
    return e & t;
  }, r.jdwcO = function (e, t) {
    return e === t;
  }, r.kPdGe = "FAVYf", r.Bgrij = "LVZVH", r.QIoXW = function (e, t) {
    return e & t;
  }, r.eMnqD = function (e, t) {
    return e == t;
  }, r.aQCDK = function (e, t) {
    return e + t;
  }, r.lGBLj = function (e, t) {
    return e(t);
  };
  var i = r;
  for (var o, a, s, l = 0, c = []; l < e.length;) {
    switch (a = e.charCodeAt(l), s = i.kukBH(l, 6)) {
      case 0:
        c.push(f.charAt(i.evetF(a, 2))); // a>>2
        break;

      case 1:
        try {
          "WhHMm" === i['GfTek'] || true && c['push'](f['charAt'](i.pHtmC(2 & o, 3) | i.evetF(a, 4))) //pHtmC a<<b evetF: a>>b
      } catch (e) {
          c['push'](f['charAt'](i['LCaAn'](i.cVCcp(3 & o, 4), a >> 4))) //cVCcp  a<<b
      }
      break;

      case 2:
        c.push(f.charAt(i.LCaAn(i.cVCcp(15 & o, 2), i.evetF(a, 6)))),
        c.push(f.charAt(i.OWUOc(a, 63)));
        break;

      case 3:
        c.push(f.charAt(i.evetF(a, 3)));
        break;

      case 4:
        c.push(f.charAt(i.LCaAn(i.thjIz(i.OWUOc(o, 4), 6), i.evetF(a, 6))));
        break;

      case 5:
        c.push(f.charAt(i.LCaAn(i.thjIz(i.jLRMs(o, 15), 4), a >> 8))), c.push(f.charAt(i.jLRMs(a, 63)));
    }

    o = a, l++;
  }
  return (0 == s ?
    false || (c.push(f.charAt(i.QIoXW(o, 3) << 4)), c.push("FM")) :
    i.eMnqD(s, 1) && (c.push(f.charAt((15 & o) << 2)), c.push("K")),
    // c = ['y', 'n', 'B', '4', '', '', 'A', 'x', '2', 'Q', '4', 'U', 'U', 'O', 'y', 'U', 'FM'],
    i.aQCDK(i.aQCDK(d(15), md5(c.join(""))), i.lGBLj(d, 10)))
}

var get_m = function(){
    p_s = Date['parse'](new Date)['toString']();
    m = btoa(p_s);
    return ([m, p_s])
};
//
// console.log(btoa("1635929868000"));
//
// //d7QFTsKkfQbz54We6398ab9a28af6fb147f477c3762db2deMBQpC3SnB
// //Fchm5Y785ihNBMBe6398ab9a28af6fb147f477c3762db2dnJcTwNibbK