pipeline {
    agent any
        stages {
            stage('testPy') {
                steps {
                    sh 'python3 testPy.py'
                }
            }
        }    
}