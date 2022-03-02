import paramiko
import os

# execute command from local pc
output_stream = os.popen('ls -lh /home/ubuntu')
print("="*50, "LOCAL", "="*50)
print(output_stream.read())

# ssh connection to remote server
server = "172.16.4.80"
ssh = paramiko.SSHClient()
ssh_key = '/home/ubuntu/.ssh/id_rsa.pub'
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username="ubuntu", key_filename=ssh_key)

# execute command from remote pc and print out
command = "ls -lh /home/ubuntu/"
print("="*50, "REMOTE", "="*50)
stdin, stdout, stderr = ssh.exec_command(command)
print(stdout.read().decode())
err = stderr.read().decode()
if err:
    print(err)

