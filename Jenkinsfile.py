pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('testPy') {
            steps {
                sh 'python3 testPy.py'
            }
        }
    }
}