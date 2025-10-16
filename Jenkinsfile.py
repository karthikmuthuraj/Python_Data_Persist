pipeline {
    agent any
    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32"
        PYTHONPATH = "C:\\Python312"
    }

    stages {
        stage('Build') {
            steps {
                bat 'python .\testPy.py'
            }
        }
    }    
}
