pipeline {
    agent any
    stages {
        stage('Test Python Script') {
            steps {
                bat 'python testPy.py'
            }
        }
    }    
}
