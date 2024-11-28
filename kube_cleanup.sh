echo "Deleting services"
kubectl delete svc/register-microservice-service
kubectl delete svc/login-microservice-service
kubectl delete svc/add-microservice-service
kubectl delete svc/list-microservice-service
kubectl delete svc/remove-microservice-service
kubectl delete svc/status-microservice-service
kubectl delete svc/mysql

sleep 5 &  
echo "Deleting Deployments"

kubectl delete deployment/register-microservice
kubectl delete deployment/add-microservice
kubectl delete deployment/login-microservice
kubectl delete deployment/list-microservice
kubectl delete deployment/remove-microservice
kubectl delete deployment/status-microservice
kubectl delete deployment/mysql

sleep 5 &  
echo "Deleting Images"

docker rmi "lab4_register-service" 
docker rmi "lab4_login-service" 
docker rmi "lab4_status-service" 
docker rmi "lab4_list-service" 
docker rmi "lab4_add-service" 
docker rmi "lab4_remove-service" 
docker rmi "mysql:8.0" 

