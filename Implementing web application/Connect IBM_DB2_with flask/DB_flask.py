import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=jjt02162;PWD=xVTBdOcHSV6GmZpV",'','')

sql= "SELECT * FROM EMPLOYEE"
stmt= ibm_db.exec_immediate(conn,sql)
dictionary= ibm_db.fetch_assoc(stmt)
print(dictionary)
Footer