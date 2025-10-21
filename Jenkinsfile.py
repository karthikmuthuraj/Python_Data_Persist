pipeline {
    agent any
    stages {
        stage('Test Python Script') {
            steps {
                powershell 'python testPy.py'
            }
        }
    }    
}
