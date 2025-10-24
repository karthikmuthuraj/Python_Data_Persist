pipeline {
    agent any
    stages {
        stage('User Input Stage') {
            steps {
                script {
                    def userInput = input(
                        id: 'deploymentDetails',
                        message: 'Provide deployment details:',
                        parameters: [
                            [$class: 'StringParameterDefinition', name: 'environment', defaultValue: 'dev', description: 'Target environment'],
                            [$class: 'ChoiceParameterDefinition', name: 'version', choices: ['1.0', '1.1', '2.0'].join('\n'), description: 'Select application version']
                        ]
                    )
                    echo "Deploying to environment: ${userInput.environment}"
                    echo "Deploying version: ${userInput.version}"
                    // Use userInput.environment and userInput.version in subsequent steps
                }
            }
        }
        '''
         stage('Test Python Script') {
            steps {
                powershell 'python testPy.py'
            }
         }
        '''
    }    
}
