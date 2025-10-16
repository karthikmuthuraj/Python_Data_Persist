pipeline {
    agent any
        stages {
            stage('testPy') {
                steps {
                    bat 'python testPy.py'
                }
            }
        }    
}