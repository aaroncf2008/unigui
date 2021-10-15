import subprocess

def cmdrun(string):     
    try:         
        res = subprocess.run(string,shell=True,check=True)         
        print(res.stdout)    
    except:         
        print("no worko")

cmdrun("firefox")