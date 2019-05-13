FROM python:3 
RUN pip3 install parallel-ssh
ADD multipleParallelSsh.py .
ADD id_rsa .
ADD id_rsa.pub .
ADD authorized_keys .
RUN whoami
RUN ls -al
ENV hosts mane.bruuhi.com
ENV user vsrao
ENV command "date"
USER nobody
ENTRYPOINT python3 ./multipleParallelSsh.py -ch $hosts -u $user -c $command
