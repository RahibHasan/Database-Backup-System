import  pymysql
import os



def __init__():
    print("## THIS SINGLE OR MULTIPLE DATABASE BACKUP SYSTEM POGRAM ##")
    backup_type=input("Which Type Backup Type Are You Interested , type Multiple is M & Single is S")
    set_backup_location=input("Enter Location which is backup File Stored")
    hostname=0;
    username=0;
    user_password=0;
    databasename=0;
 
    if backup_type is "M" :
        hostname = input("Enter Your Hostname  ")
        username = input("Enter Your Username  ")
        password = input("Enter Your User Password ")
        upload_file_location=input('Upload Your File Location')
        file_name=open(upload_file_location,'r')


        for single_database in file_name :

            single_database=single_database[:-1]
            create_cmd = "mysqldump -h " + hostname + " -u " + username + " -p" + password + " " + single_database + " > " + set_backup_location + "/" + single_database + ".sql"
            # print(create_cmd)
            os.system(create_cmd)
            # / media / hasan / Error / Database_backup_python_script/database_name.txt


    else:
        print("Single")
        hostname=input("Enter Your Hostname  ")
        username=input("Enter Your Username  ")
        password =input("Enter Your User Password ")
        databasename = input("Enter Your Dataabase Name")

        create_cmd="mysqldump -h " + hostname + " -u " + username + " -p" + password + " " + databasename + " > " + set_backup_location +"/"+databasename+".sql"
        # print(create_cmd)
        os.system(create_cmd)

__init__()


#
# db=pymysql.connect("localhost","root","root","hem");
# cursor=db.cursor();
# cursor.execute("select count(*) from fixtures")
# data=cursor.fetchone()
# print ("Database version : %s " % data)
# db.close()
