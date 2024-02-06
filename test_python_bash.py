import os

try:
    from pyfiglet import Figlet
    figlet = True
except:
    figlet = False


def print_msg(result, figlet):
    
    msg = {True: 'You are AMAZING!', False: 'Что-то не так!'}

    if figlet:
        f = Figlet(font='banner')
        print(f.renderText(msg[result]))
    else:
        print(msg[result])
        
try:
    os.system('mkdir test')
except Exception as e:
    print(e)

try:
    os.system('cp -rf python_bash.py test/python_bash.py')
    os.chdir('test')
    os.system('python python_bash.py')
   
    with open('01-ls.txt', 'r') as f:
        text = f.read()
        print_msg(text.split() == [os.getcwd(), 'python_bash.py'], figlet=figlet)

except Exception as e:
    print_msg(False, figlet)
    # print(e)
                
os.system('cd .. && rm -r test')
