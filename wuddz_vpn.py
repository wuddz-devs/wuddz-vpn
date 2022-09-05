"""
░░░░░░░░░░░██╗░░░░░░░██╗██╗░░░██╗██████╗░██████╗░███████╗░░░░░░██╗░░░██╗██████╗░███╗░░██╗░░░░░░░░░░░
░░░░░░░░░░░██║░░██╗░░██║██║░░░██║██╔══██╗██╔══██╗╚════██║░░░░░░██║░░░██║██╔══██╗████╗░██║░░░░░░░░░░░
░░░░░░░░░░░╚██╗████╗██╔╝██║░░░██║██║░░██║██║░░██║░░███╔═╝█████╗╚██╗░██╔╝██████╔╝██╔██╗██║░░░░░░░░░░░
░░░░░░░░░░░░████╔═████║░██║░░░██║██║░░██║██║░░██║██╔══╝░░╚════╝░╚████╔╝░██╔═══╝░██║╚████║░░░░░░░░░░░
░░░░░░░░░░░░╚██╔╝░╚██╔╝░╚██████╔╝██████╔╝██████╔╝███████╗░░░░░░░░╚██╔╝░░██║░░░░░██║░╚███║░░░░░░░░░░░
░░░░░░░░░░░░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═════╝░╚══════╝░░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚══╝░░░░░░░░░░░

 [*]Descr:     CONNECT TO RANDOM NORDVPN SERVER OR AN ALTERNATE PROVIDER SERVER WITH A VALID ACCOUNT
 [*]Coder:     Wuddz_Devs                                                                           
 [*]Email:     wuddz_devs@protonmail.com                                                            
 [*]Github:    https://github.com/wuddz-devs                                                        
 [*]Telegram:  https://t.me/wuddz_devs                                                              
 [*]Videos:    https://mega.nz/folder/IWVAXTqS#FoZAje2NukIcIrEXXKTo0w                               
 [*]Reddit:    https://reddit.com/user/wuddz-devs                                                   
 [*]Youtube:   wuddz-devs                                                                           

 [*]Menu:
    1    =>    Connect To NordVPN Servers                          
    2    =>    Connect To Alternate Servers                        
    p    =>    Specify Openvpn Executable File Path Or Default Used
    e    =>    Exit Program                                        
"""

import sys, re, random
from subprocess import Popen, PIPE
from pathlib import Path
from os import name, path, remove, system
system('')


def clear_screen():
    if name=='nt':system('cls')
    else:system('clear')

def get_menu(em):
    a=input(em+'\n\n\033[1;32;40m...Hit Enter|Return Key To Continue....\033[0m\n') or None
    if a:return

def get_config(cdr,pc,vpnc=None):
    ptc=f'{cdr}udp'
    if pc=='t':ptc=f'{cdr}tcp'
    try:
        clear_screen()
        vpnl=Path.joinpath(Path.cwd(),ptc)
        if vpnc!=None:
            if '-' in str(vpnc):cnf=list(Path(vpnl).rglob(vpnc+'*.ovpn'))
            else:cnf=[str(v) for v in list(Path(vpnl).rglob(vpnc+'*.ovpn')) if not '-' in str(Path(v).stem)]
        else:cnf=[str(x) for x in list(Path(vpnl).rglob('*.ovpn'))]
        ove=random.choice(cnf)
        o,p=path.split(ove)
        ovp=Path.joinpath(Path.cwd(),p)
        with open(ove, 'r', encoding='utf-8') as ovr:
            with open(ovp, 'w', encoding='utf-8') as ovw:
                for line in ovr:
                    ovw.write(str(line).replace('cipher AES-256-CBC', 'data-ciphers-fallback AES-256-CBC'))
        return ovp
    except:pass
    get_menu('\n\033[1;31;40m*No Configs Found*\033[0m')

def nord_main(pc,opvpn):
    """ [*]NordVPN Country Codes:
    al = Albania      cy = Cyprus           in = India         nl = Netherlands       es = Spain        
    ar = Argentina    cz = CzechRepublic    id = Indonesia     nz = NewZealand        se = Sweden       
    au = Australia    dk = Denmark          ie = Ireland       mk = NorthMacedonia    ch = Switzerland  
    at = Austria      ee = Estonia          il = Israel        pl = Poland            tw = Taiwan       
    be = Belgium      fi = Finland          it = Italy         pt = Portugal          th = Thailand     
    br = Brazil       fr = France           jp = Japan         ro = Romania           tr = Turkey       
    ba = Bosnia       de = Germany          lv = Latvia        rs = Serbia            uk = UnitedKingdom
    bg = Bulgaria     ge = Georgia          lt = Lithuania     sg = Singapore         ua = Ukraine      
    ca = Canada       gr = Greece           lu = Luxembourg    sk = Slovakia          us = USA          
    cl = Chile        hk = HongKong         md = Moldova       si = Slovenia          vn = Vietnam      
    cr = CostaRica    hu = Hungary          my = Malaysia      za = SouthAfrica                         
    hr = Croatia      is = Iceland          mx = Mexico        kr = SouthKorea                          

    DoubleVPN Country Codes:
    ca-us = Canada-USA                      nl-ch = Netherlands-Switzerland
    ch-nl = Switzerland-Netherlands         uk-fr = UK-France              
    ch-se = Switzerland-Sweden              uk-nl = UK-Netherlands         
    fr-uk = France-UK                       se-ch = Sweden-Switzerland     
    hk-tw = HongKong-Taiwan                 se-nl = Sweden-Netherlands     
    nl-se = Netherlands-Sweden              tw-hk = Taiwan-HongKong        
    nl-uk = Netherlands-UK                  us-ca = USA-Canada             

    Country Code    =>    [e.g us = Connects To Random Nord USA Vpn Server]
    Ctrl+C          =>    Disconnects VPN If Connected                     
    b               =>    Back To Menu                                     
"""
    while True:
        try:
            clear_screen()
            vpna=input('\033[1;32;40m'+nord_main.__doc__+'\033[0m\nInput Country Code or b=> ') or None
            if vpna=='b':break
            elif vpna.lower()+' =' in str(nord_main.__doc__):
                ovp=get_config('nord_',pc,vpnc=vpna.lower())
                vpn_connect(ovp,opvpn)
        except:pass

def vpn_connect(ovp,opvpn):
    try:
        vpna=Path.joinpath(Path.cwd(),'vpncreds.txt')
        cmd=[opvpn, '--config', ovp, '--auth-user-pass', vpna,
            '--connect-timeout', '10', '--connect-retry-max',
            '2', '--remap-usr1', 'SIGTERM']
        with Popen(cmd, stdout=PIPE, universal_newlines=True) as vco:
            for l in vco.stdout:
                if str(l).count('AUTH_FAILED')!=0:print('\n\033[1;34;40mAccount Not Valid\033[0m')
                elif str(l).count('Initialization Sequence Completed')!=0:
                    print('\n\033[1;34;40mConnected To '+str(path.split(ovp)[1])+'\033[0m')
    except:pass
    remove(ovp)
    get_menu('\n\033[1;31;40m*VPN Not Connected*\033[0m')

def sub_main(vp,opvpn):
    """ [*]Choose Server Protocol:
    t    =>    Connect To Tcp Server
    u    =>    Connect To Udp Server
    b    =>    Back To Menu         
"""
    while True:
        try:
            clear_screen()
            pc=input('\033[1;32;40m'+sub_main.__doc__+'\033[0m\nInput Choice=> ') or None
            if pc =='b':break
            elif pc in 'u,t':
                if vp=='1':nord_main(pc,opvpn)
                else:
                    ovp=get_config('alt_',pc)
                    vpn_connect(ovp,opvpn)
        except:pass

def main():
    opvpn=''
    hd='\033[1;32;40m [*]Openvpn Executable Path  e.g  C:\\Program Files (x86)\\OpenVPN\\bin\\openvpn.exe\033[0m\n'
    while True:
        try:
            clear_screen()
            if not opvpn:
                if name=='nt':opvpn='C:\\Program Files\\OpenVPN\\bin\\openvpn.exe'
                else:opvpn='openvpn'
            vp=input('\033[1;32;40m'+__doc__+'\033[0m\nInput Choice=> ') or None
            if vp=='e':break
            elif vp in '1,2':sub_main(vp,opvpn)
            elif vp=='p':
                clear_screen()
                opn=input(hd+'\nInput Path Or Pass=> ')
                if Path(opn).exists():opvpn=opn
        except:pass
    clear_screen()


if __name__=='__main__':
    main()