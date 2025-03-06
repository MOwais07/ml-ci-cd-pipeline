pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/ml-ci-cd-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('your-username/ml-app')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('your-username/ml-app').push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            emailext subject: "Deployment Status",
                     body: "The latest build and deployment were successful.",
                     to: "admin@example.com"
        }
    }
}