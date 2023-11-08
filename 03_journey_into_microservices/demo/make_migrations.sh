set -e -u

servers=`ls backend/ | grep '_microservice$'`
for d in $servers ; do
  echo "--------------------------------------- making migrations $d ---------------------------------------"
  d2=`echo "$d" | tr _ -`
  docker exec masterclass_${d2}_1 su - masterclass /bin/bash -c  "cd backend/${d}/ && python manage.py makemigrations"
done
