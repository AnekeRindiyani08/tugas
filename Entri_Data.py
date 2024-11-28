import mysql.connector
from mysql.connector import errors

mydbs=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="dbsritail051"
)
mycursor=mydbs.cursor()
mysql_isert_Kol = """ INSERT INTO tblmaster VALUES(%s,%s,%s,%s,%s,%s)"""

#variable input Entry_Record
Kode_brg=input("Kode Barang = ")
Nama=input("Nama Barang = ")
Satuan=input("Satuan            ")
Stok=input("Stok              = ")
Harga=input("Harga            = ")
Keterangan=input("Keterangan          = ")

Entry_record= (Kode_brg,Nama,Satuan,Stok,Harga,Keterangan)
mycursor.execute(mysql_isert_Kol,Entry_record)
mydbs.commit()
print("Data Berhasil Disimpan")