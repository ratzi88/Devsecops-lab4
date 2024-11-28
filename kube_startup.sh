eval $(minikube docker-env)
echo "Move to Minikube's Docker environment"
sleep 2 &  
echo "Building images"
docker-compose build

sleep 2 &  
echo "Build the docker container"
kubectl apply -f kubernetes/deployments/config_map.yaml 
kubectl apply -f kubernetes/deployments/mysql_deploy.yaml
kubectl apply -f kubernetes/deployments/login_deploy.yaml
kubectl apply -f kubernetes/deployments/register_deploy.yaml
kubectl apply -f kubernetes/deployments/add_deploy.yaml
kubectl apply -f kubernetes/deployments/list_deploy.yaml
kubectl apply -f kubernetes/deployments/remove_deploy.yaml
kubectl apply -f kubernetes/deployments/status_deploy.yaml

echo "Ready for testing"