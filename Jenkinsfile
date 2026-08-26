pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/python -m pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t devops-task-app:jenkins-${BUILD_NUMBER} .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f devops-task-app || true

                    docker run -d \
                        --name devops-task-app \
                        -p 8000:8000 \
                        devops-task-app:jenkins-${BUILD_NUMBER}
                '''
            }
        }

    }
}
