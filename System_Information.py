import psutil
import time
import pyodbc

con = pyodbc.connect('Driver={SQL Server};'
                     'Server=Ekaksh\\SQLEXPRESS;'
                     'Database=System_Information;'
                     'Trusted_Connection=yes;')


cursor = con.cursor()

while 1 == 1:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3] 
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_recieved = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]

    cursor.execute('insert into Performance values(GETDATE(),'
                   +str(cpu_usage)+','
                   +str(memory_usage)+','
                   +str(cpu_interrupts)+','
                   +str(cpu_calls)+','
                   +str(memory_used)+','
                   +str(memory_free)+','
                   +str(bytes_sent)+','
                   +str(bytes_recieved)+','
                   +str(disk_usage)+ ')'
                   )
    
    con.commit()


    '''print(cpu_usage)
    print(memory_usage)
    print(cpu_interrupts)
    print(cpu_calls)
    print(memory_used)
    print(memory_free)
    print(bytes_sent)
    print(bytes_recieved)
    print(disk_usage)'''
    time.sleep(1)