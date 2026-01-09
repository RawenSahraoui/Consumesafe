pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "oumaymariahi"
        BACKEND_IMAGE  = "oumaymariahi/consumesafe-backend"
        FRONTEND_IMAGE = "oumaymariahi/consumesafe-frontend"
        DOCKER_TAG     = "latest"

        // ID du credential Docker Hub dans Jenkins
        DOCKER_CRED = "74ac32e9-9f43-4cc6-a3a9-2bf40dfed8ec"
    }

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build Images") {
            steps {
                sh """
                  docker build -t $BACKEND_IMAGE:$DOCKER_TAG ./backend
                  docker build -t $FRONTEND_IMAGE:$DOCKER_TAG ./frontend
                """
            }
        }

        stage("Security Scan (Trivy)") {
            steps {
                sh """
                  trivy image --severity HIGH,CRITICAL $BACKEND_IMAGE:$DOCKER_TAG || true
                  trivy image --severity HIGH,CRITICAL $FRONTEND_IMAGE:$DOCKER_TAG || true
                """
            }
        }

        stage("Login Docker Hub") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKER_CRED,
                    usernameVariable: "DOCKER_USER",
                    passwordVariable: "DOCKER_PASS"
                )]) {
                    sh """
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    """
                }
            }
        }

        stage("Push Images") {
            steps {
                sh """
                  docker push $BACKEND_IMAGE:$DOCKER_TAG
                  docker push $FRONTEND_IMAGE:$DOCKER_TAG
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubecfg-file', variable: 'KUBECONFIG')]) {
                    sh '''
                    kubectl get nodes

                    kubectl apply -f k8s/deployments/backend-deployment.yaml
                    kubectl apply -f k8s/deployments/frontend-deployment.yaml
                    kubectl apply -f k8s/services/backend-service.yaml
                    kubectl apply -f k8s/services/frontend-service.yaml
                    '''
                }
            }
        }
    }   

    post {
        success {
            echo "Pipeline CI/CD terminé avec succès"
        }
        failure {
            echo "Pipeline échoué — vérifier les logs"
        }
    }
}
