## Installing Kubernetes

`sudo snap install microk8s --classic`

`microk8s enable dns storage helm3`

## Installing Keda

```
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
kubectl create namespace keda
helm install keda kedacore/keda --namespace keda
```

## Installing Kafka

`kubectl create namespace kafka`
`microk8s helm3 install kafka --namespace kafka bitnami/kafka --set rbac.create=true`
`kubectl apply -f kube/testclient.yml`

## Creating your topic

`kubectl exec -it kafka-client -n kafka -- /bin/bash`
`kafka-topics --bootstrap-server kafka.kafka.svc.cluster.local:9092 --create --topic my-topic --replication-factor 1 --partitions 20`

## Creating your consumer deployment

`kubectl apply -f kube/consumer-deployment.yml`

## Creating your autoscaler

`kubectl apply -f kube/kafka-scaled-object.yml`

## Running a producer job

`kubectl apply -f kube/producer-job.yml`

## Checking lag

`kafka-consumer-groups --bootstrap-server kafka.kafka.svc.cluster.local:9092 --describe --group my-group`