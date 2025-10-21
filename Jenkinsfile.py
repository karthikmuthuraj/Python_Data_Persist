pipeline {
    agent any
    stages {
        stage('Test Python Script') {
            steps {
                cmd 'python testPy.py'
            }
        }
    }    
}
