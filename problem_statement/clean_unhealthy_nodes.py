# lst = ['10.0.132.198']
# import os
# import subprocess
# for i in lst:
#     cmd = "ssh -i /Users/amardip.kumar/Documents/project_doc/cointreau-prod.pem hadoop@{0}".format(i)
#     subprocess.call(cmd)
#     import pdb;pdb.set_trace()
#     os.system("du -sch /mnt/yarn/usercache/cointreau/appcache/*")



# import paramiko

# cert = paramiko.RSAKey.from_private_key_file("/Users/amardip.kumar/Documents/project_doc/cointreau-prod.pem")
# c = paramiko.SSHClient()
# c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print "connecting..."
# c.connect(hostname = "10.0.132.198", username = "hadoop", pkey = cert )
# print "connected!!!"
# # stdin, stdout, stderr = c.exec_command('pwd')
# stdin, stdout, stderr = c.exec_command('sudo rm -rf /mnt/yarn/usercache/cointreau/appcache/*')
# import pdb;pdb.set_trace()
# c.close()


def mydecorater(orgn):
    def new_fun():
        print("hello")
        orgn()
        #original_fun()
        print("bye")
    return new_fun

@mydecorater   
def original_fun():
    print("Original funcation")
original_fun()



