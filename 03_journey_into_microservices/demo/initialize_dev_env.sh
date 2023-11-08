services=`ls backend/ | grep '_microservice'`
for d in $services ; do
  echo "--------------------------------------- intializing $d ---------------------------------------"
  chmod 777 "backend/$d"
  cd "backend/$d"
  ./initialize_docker.sh
  cd ../../
done
