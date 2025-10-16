pipeline {
    agent any
        stages {
            stage('testPy') {
                steps {
                    bat 'pyrun.bat'
                }
            }
        }    
}