import glob
from pandas import DataFrame
import os
from progressbar import ProgressBar
pbar = ProgressBar()


for line in open("output.txt","r").readlines(): 
    taslar = line.split("#$") 

tumtakimlar=[]

all_files = glob.glob('*\*.td')

for file in pbar(all_files):
    tatak=os.path.basename(file)

    icerikfile = []
    icerikfile.append(tatak)
    with open(file, errors="ignore") as f:
        lines=f.read()
        for tas in taslar:
            if tas=="":
                continue
            else:    
                tas_string=tas+" "
                result=lines.find(tas_string)
                        
                if result>0:
                    paket=tas_string.strip()
                    icerikfile.append(paket)
    if len(icerikfile)<=3:
        continue
    else:
                        
        while len(icerikfile)<7:
            icerikfile.append("")
                
    tumtakimlar.append(icerikfile)
print(tumtakimlar)

df = DataFrame (tumtakimlar,columns=['turcar kodu','tas1','tas2','tas3','tas4','tas5','tas6',])
file_name = 'takimdata.xlsx'
df.to_excel(file_name)
