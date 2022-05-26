import pyqrcode
import pandas as pd

def main():
    df = pd.read_csv('meibo.csv')
    for row in df.itertuples():
        name = row.name
        id = row.id 
        # QRコード作成
        # code = pyqrcode.create(str(name), error='L', version=3, mode='binary')
        code = pyqrcode.create(content=id,error='H',version=3, mode='binary')
        code.png(str(name)+'.png', scale=7, module_color=[0, 0, 0, 128], background=[255, 255, 255])

main()
