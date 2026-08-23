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
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest'
            }
        }

    }
}