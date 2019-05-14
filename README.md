# multipleParallelSshClients
## Instructions
1. Copy id_rsa and id_rsa.pub files to the current directory
1. Build the image: docker build .
1. Run the image: docker run --env user=myusernameonallhosts --env command="mycommandtorunonallhosts" --env hosts=host1,host2,hostn \<imageid\>
1. Note that it is required that the id_rsa.pub is added to ~myusernameonallhosts/.ssh/authorized_keys on all hosts

## Features
1. Same user id on all hosts
1. Same command on all hosts
1. Multiple hosts/connections
1. Parallel execution of command
1. SIGINT handler implemented (ctrl-c)
1. parallelSshClient package is used 
