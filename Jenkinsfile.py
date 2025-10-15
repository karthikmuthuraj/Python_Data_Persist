pipeline {
    agent any
        stages {
            stage('testPy') {
                steps {
                    sh 'python testPy.py'
                }
            }
        }    
}