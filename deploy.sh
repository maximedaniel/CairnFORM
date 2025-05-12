user_machine="pi@192.168.5.1"
tar -czvf CairnFORM.tar.gz *
scp CairnFORM.tar.gz $user_machine:/home/pi/
# add -v to docker compose down to remove all volumes too (required if .env file is modified)
ssh $user_machine << EOF
rm -fr /home/pi/CairnFORM
mkdir /home/pi/CairnFORM
tar -xzvf /home/pi/CairnFORM.tar.gz -C /home/pi/CairnFORM
EOF
rm -f CairnFORM.tar.gz