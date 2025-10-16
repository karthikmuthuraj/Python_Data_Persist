pipeline {
    agent any
        stages {
            stage('Build') {
                steps {
                    powershell 'python testPy.py'
                }
            }
        }    
}