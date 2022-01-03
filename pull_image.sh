echo "Input version (*.*.*)"
read version
echo version=$version

aws ecr get-login --no-include-email --region ap-northeast-1 | sh

docker pull 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version
docker tag 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version hrm_frontend
docker rmi 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_frontend:$version

docker pull 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend:$version
docker tag 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend:$version hrm_backend
docker rmi 809967774165.dkr.ecr.ap-northeast-1.amazonaws.com/hrm_backend:$version
