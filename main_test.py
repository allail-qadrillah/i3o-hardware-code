from firebase.api import RTDB
from time import sleep
from pzem.app import PZEM
from lcd.app import LCD

BIAYA_PER_KWH = 415

db = RTDB()
lcd = LCD()

def biaya_listrik(kwh):
    biaya = kwh * BIAYA_PER_KWH
    return int(round(biaya + ( biaya * 0.1), 3) * 1000)

# conecting 
lcd.progress_bar()
sleep(3)

def main():
  

    while True:
        try:
            pzem = PZEM()
            # display starting
            sisa_token = db.read('/harga_token')
            # lcd.display("Token: {sisa_token}", 1)
            # lcd.display("Power: {pzem.get_energy_kwh} kWh")

            if sisa_token > 0:
                value_kwh  = round(pzem.get_energy_kwh(), 3)
                pemakaian_listrik = biaya_listrik(value_kwh)
                token_baru = sisa_token - pemakaian_listrik

                if token_baru < 0:
                    db.update('/', { 'harga_token': 0})
                    continue
                
                # update sisa token
                else:
                    db.update('/', {'harga_token': token_baru})

            else: 
                db.update('/', {'harga_token': 0})
                print("TOKEN HABISS")


            db.update('/', {
                "arus": pzem.get_current(),
                "daya": round(pzem.get_energy_kwh(), 3),
                "tegangan": pzem.get_voltage(),
                "frekuensi": pzem.get_frekuensi()
            })    
            sleep(3)
        except ModbusInvalidResponseError as e:
            print("pzem mati") 
            continue
        

if __name__ == "__main__":
  main()