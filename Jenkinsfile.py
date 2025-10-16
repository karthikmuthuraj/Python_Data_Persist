pipeline {
    agent any
        stages {
            stage('Build') {
                steps {
                    bat  "pyrun.bat"
                }
            }
        }    
}
