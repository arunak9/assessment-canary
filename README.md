kubernetes canary deployment:

DESCRIPTION:

1. I'm creating strategy in kubernetes for canary deployment. Below are my assemptions:

2. I have 2 versions of applications(say stable and canary). The stable deployment is the application which is production and running from long time. Canary version is the new code that I want to deploy into production in kubernetes.
3. Currently, 3 replicas of stable version are running(deploy-stable.yaml).
4. The above stable version is being served by service of type NodePort(service-stable-canary.yaml).
5. Now if I want to deploy newer version|(canary), I can simply deploy deploy-canary.yaml  by using the below command.
     kubectl apply -f deploy-canary.yaml
6. So if I run the above step, 1 replica of canary and 3 replicas of stable will be running at a time which is served by the service.
7. Now, depends on your requirement you can change the replica count in respective deploy-(stable, canary).yaml so that respective number of pods will run at a time. 

ASSUMPTIONS:
1. I am running kubernetes cluster in minikube.
2. Based on the created files, 3 replicas of stable and 1 replica of canary will be running at a time if you apply as it is.
3. The application is served on port 30001. So if you want to access the application you need to open the browser and run as http://your-minikube-kubernetes-ip:30001. So that if you keep refreshing browser both the stable and canary versions will be served randomly.
4. The code for stable version is desplayed as "I am Aruna".
5. The code for canary version is displayed as "I am Aruna Sripriya".

Steps to replicate:
1. Create a minikube cluster in your laptop and Make sure it is up and running.
2. Clone this repo.
3. Run kubectl apply -f deploy-stable.yaml.
4. Run kubectl apply -f deploy-canary.yaml.
5. Run kubectl apply -f service-stable-canary.yaml.
6. Open the browser and enter http://your-minikube-kubernetes-ip:30001 and keep refreshing the browser. So that you will be served with stable and canary deployments randomly.
7. Based on your requirement, keep changing the replica count in stable and canary deployment files and follow step 2 and 3.

