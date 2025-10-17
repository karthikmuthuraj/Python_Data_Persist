pipeline {
    agent any
    environment {
        PATH = 'C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python.exe'
    }

    stages {
        stage('Build') {
            steps {
                bat 'pyrun.bat'
            }
        }
    }    
}
