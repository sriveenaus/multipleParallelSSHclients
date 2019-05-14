FROM python:3 
RUN pip3 install parallel-ssh
ADD multipleParallelSsh.py .
ADD id_rsa .
ADD id_rsa.pub .
ENV hosts host1,host2,host3
ENV user vrao
ENV command 'uname'
ENTRYPOINT python3 ./multipleParallelSsh.py -ch $hosts -u $user -c $command
