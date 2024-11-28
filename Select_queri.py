import mysql.connector
from koneksi import mydbs
mycursor=dbs.cursor()
mysql_select_master="select * from tblmaaster"
mycursor.execute(mysql_select_tblmaster)
records=mycursor.fetchall()
print("Total number of rows in table:",mycursor.rowcount)
print("\nprinting each row")
for row in records
    print("kode barang = ",row[0],)
    print("nama barang = ",row[1])
    print("satuan      = ",row[2])
    print("stok barang = ",row[3])
    print("satuan      = ",row[4])
    print("keterangan  = ",row[5], "\n")
    print("=" * 40)
    
