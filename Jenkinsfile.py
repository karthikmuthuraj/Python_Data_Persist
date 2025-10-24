pipeline {
    agent any
    stages {
        '''
        stage('User Input') {
            steps {
                script {
                    def userInput = input(message: 'Please enter a value:', ok: 'Proceed', submitter: 'admin')
                    echo "User entered: ${userInput}"
                }
            }
        }
        '''
        stage('Test Python Script') {
            steps {
                powershell 'python testPy.py'
            }
        }
    }    
}
