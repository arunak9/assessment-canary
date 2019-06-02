pipeline {
    agent any
    environment {
        DOCKER_STABLE_IMAGE_NAME = "arunak9/stable-deployment"
        DOCKER_CANARY_IMAGE_NAME = "arunak9/canary-deployment"
    }
    stages {
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app_stable = docker.build(DOCKER_STABLE_IMAGE_NAME)
                    app_canary = docker.build(DOCKER_CANARY_IMAGE_NAME)
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app_stable.push("${env.BUILD_NUMBER}")
                        app_stable.push("latest")
                        app_canary.push("${env.BUILD_NUMBER}")
                        app_canary.push("latest")
                    }
                }
            }
        }
        stage('CanaryDeploy') {
            when {
                branch 'master'
            }
            steps {
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'deploy-canary.yaml','deploy-stable.yaml','service-stable-canary.yaml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
}
