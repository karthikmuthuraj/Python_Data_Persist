pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('testPy') {
            steps {
                sh 'python testPy.py'
            }
        }
    }
}