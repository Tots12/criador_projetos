import platform,sys,os,subprocess


def check_lingua(string):
    linguas = ['rb','c','node','py','nodeelectron','nodediscord','jsp5']
    if string in linguas:    return True

def check():
    if 'W' in platform.system():    return False
    #else:
        #if 'comando não encontrado' in subprocess.check_output('wget --help',shell=True):    return False;os.system('clear')           
     #   else:   return True
    else:    return True
def main(lingua,pasta):
    if check() == True:
        if len('a') == 1:
            lingua =  lingua
            pasta = pasta
            if check_lingua(lingua) == True:
                os.system('mkdir {}'.format(pasta));os.chdir(pasta)
                               
                if lingua == 'rb':
                    os.system('echo require("classe.rb") > index.rb && echo classe.rb')
                elif lingua == 'c':
                    os.system('echo > index.c && echo > index.h')
                elif lingua == 'node':
                    os.system('npm init')
                elif lingua == 'py': 
                    os.system('echo from arquivo import classe > index.py && echo > arquivo.py ')
                elif lingua == 'nodeelectron': 
                    os.system('npm init && npm install electron')
                elif lingua == 'nodediscord':
                    os.system('npm init && npm install discord')
                elif lingua == 'jsp5':
                    os.system('wget https://github.com/processing/p5.js/releases/download/0.7.3/p5.zip && unzip p5.zip && rm p5.zip')
            else:    print('Lingua não suportada')
                              
         
#print('usagem newproject.py 1 2')                
    else:
        print('um ou mais erro encontrado') 
try:
    main(''.join(sys.argv[1]),''.join(sys.argv[2])) 
except:                              
    print('program.py 1 2')
