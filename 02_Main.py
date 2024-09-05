#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py

import pandas as pd
from Calib import calibT1, calibVar01, calibVar02, calibVar03, calibTXcurrent, calibRXcurrent, calibIMTQ_temp, linealCalib
import struct


#Esto no es generico, con esto resuelvo el problema 
#puntual que me plantea el fabricante!
def mnamef(**kwargs):
    chuck   = kwargs["chuck"]
    pos     = kwargs["pos"]
    
    med_name_len = struct.unpack("B", chuck[pos-1:pos])
    value, = struct.unpack(str(med_name_len[0])+"s", chuck[pos:pos+med_name_len[0]])
    return value, med_name_len[0]

def getPacket(**kwargs):
    offset = 16 #El 16 es hardcode, no hay documentacion
    chuck   = kwargs["chuck"]
    pos     = kwargs["pos"]
    
    packet_len = struct.unpack("<H", chuck[pos-2:pos])
    value, = struct.unpack(str(packet_len[0])+"s", chuck[pos:pos+packet_len[0]])
    return value[offset:], pos+packet_len[0]  


def getUTC(**kwargs):
    #hardcode, se debe mejorar
    chuck   = kwargs["chuck"]
    pos     = kwargs["pos"]
    
    value, = struct.unpack("<L", chuck[139:139+4])
    return value, 4

frmDic = {"Frame command":{"len":1, "deco":"B"}, 
           "Frame length":{"len":4, "deco":"I"},
           "Datarate":{"len":4, "deco":"I"},    
           "Modulation name length":{"len":1, "deco":"B"},
           "Modulation name":{"len":0, "deco":mnamef},
           "RSSI":{"len":8, "deco":"<d"},
           "Freq":{"len":8, "deco":"<d"},
           "Packet length":{"len":2, "deco":"<H"},
           "Packet":{"len":0, "deco":getPacket},
           "UTCTime":{"len":4, "deco":getUTC},
           }

    


pktDic = {
    "frameType":    {"len":1, "deco":"B",   "pos":0},
    "packetNumber": {"len":1, "deco":"<h",  "pos":1},
    "OBCUpTime":    {"len":1, "deco":"<h",  "pos":3}, 
    "obcT1":        {"len":2, "deco":"<h",  "pos":8, "calib":{"afunction":calibT1, "args":{"gain":0.38991, "offset":-67.84}}},
    "TXcurrent":    {"len":2, "deco":"<h",  "pos":25,"rcalib":{"afunction":"calibTXcurrent", "args":{"gain":0.395, "offset":0}}},
    "RXcurrent":    {"len":2, "deco":"<h",  "pos":27,"rcalib":{"afunction":"calibRXcurrent", "args":{"gain":0.395, "offset":0}}},
    "TempBatt":     {"len":2, "deco":"<h",  "pos":51},
    "IMTQ_temp":    {"len":2, "deco":"<h",  "pos":88, "calib":{"afunction":calibIMTQ_temp, "args":{"gain":0.00390625, "offset":0}}},
    "tempP1":    {"len":2, "deco":"<h",  "pos":76, "calib":{"afunction":linealCalib, "args":{"gain":0.0078125, "offset":0}}},
}




def tlmyProcessor(tlmyDic, chuck):
    pos = 0
    rdic = {}
    for key, value in tlmyDic.items():
        deco = value["deco"]
        if "pos" in value:
            pos = value["pos"]
        if callable(deco):
            vval, _len = deco(chuck=chuck, pos=pos)
        else:
            _len = struct.calcsize(value["deco"])
            vval, = struct.unpack(deco, chuck[pos:pos+_len])

        if "calib" in value:
            calib = value["calib"]
            vval = calib["afunction"](value=vval, **calib["args"])
        elif "rcalib" in value:
            rcalib = value["rcalib"]
            fun_name = rcalib["afunction"]
            #La carga puede ser tambien dinamica!
            globals()[fun_name](value=vval, **rcalib["args"])
        else:
            pass    
        rdic[key] = vval 
        #1494015420 UC aprox
        #1444413440
        #print(key, ", value:", vval) 
        pos+=_len

    return rdic
            

if __name__ == '__main__':
    f = open('./resources/FS2017raw_tlmy_146bytes.bin', 'rb')
    pos = 0
    chuck = f.read(146)
    #while chuck:
    df = pd.DataFrame()
    i=0
    while chuck:
    #for i in range(4):
        tup_frame = tlmyProcessor(frmDic, chuck)
        #print(tup)
        
        if "Packet" in tup_frame:
            #print(tup["Packet"])
            tup_pkt = tlmyProcessor(pktDic, tup_frame["Packet"])
            #print("Packet=>", tup)
            
            for key, value in tup_pkt.items():
                df.loc[i,key] = value
            
        chuck = f.read(146)
        df.loc[i,"UTCTime"] = tup_frame["UTCTime"]
        i+=1
        

    f.close()
    df.to_csv("./resources/tlmy.csv")
    print(df)
