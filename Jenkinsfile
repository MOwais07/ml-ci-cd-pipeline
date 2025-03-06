pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials' // Your Jenkins Docker Hub credentials ID
        DOCKER_IMAGE_NAME = 'mowais07/mlop-ci-cd-pipeline' // Your Docker image name
        DOCKER_TAG = 'latest' // Tag for the Docker image
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Checkout the latest code from GitHub repository
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile
                    echo "Building Docker image..."
                    sh 'docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub using Jenkins credentials
                    echo "Logging into Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    echo "Pushing Docker image to Docker Hub..."
                    sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            // Cleanup after build - optionally remove local images after push
            echo "Cleaning up..."
            sh 'docker rmi ${DOCKER_IMAGE_NAME}:${DOCKER_TAG}'
        }

        success {
            echo "Docker image successfully pushed to Docker Hub."
        }

        failure {
            echo "Docker image push failed."
        }
    }
}