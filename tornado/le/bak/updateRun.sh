source /etc/profile
#!/bin/bash
ps -fe|grep processString |grep -v grep
if [ $? -ne 0 ]
then
echo "start process....."
else
echo "runing....."
fi