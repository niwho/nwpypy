import requests

r = requests.get("http://epub.cnki.net/KNS/request/SearchHandler.ashx?action=&NaviCode=*&ua=1.11&PageName=ASP.brief_default_result_aspx&DbPrefix=SCDB&DbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=SCDBINDEX.xml&db_opt=CJFQ%2CCJFN%2CCDFD%2CCMFD%2CCPFD%2CIPFD%2CCCND%2CCCJD%2CHBRD&txt_1_sel=TI%24%25%3D%7C&txt_1_value1=%E8%AE%A1%E7%AE%97%E6%9C%BA&txt_1_special1=%25&his=0&parentdb=SCDB&__=Wed%20Mar%2005%202014%2022%3A58%3A37%20GMT%2B0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)")
print r.headers['set-cookie']
print requests.utils.dict_from_cookiejar(r.cookies)
r1 = requests.get("http://epub.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&dbPrefix=SCDB&dbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=SCDBINDEX.xml&research=off&t=1394031517472&keyValue=%E8%AE%A1%E7%AE%97%E6%9C%BA&S=1",
                  cookies=requests.utils.dict_from_cookiejar(r.cookies))
print r1.status_code
print r1.text

