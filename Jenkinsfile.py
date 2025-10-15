pipeline {
    agent any
        stages {
            stage('testPy') {
                steps {
                    'python3 testPy.py'
                }
            }
        }    
}