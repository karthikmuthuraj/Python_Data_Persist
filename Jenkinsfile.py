pipeline {
    agent any
    stages {
        stage('Test') {
        def reg = input(
            message: 'What is the reg value?', 
            parameters: [
                [$class: 'ChoiceParameterDefinition', 
                    choices: 'Choice 1\nChoice 2\nChoice 3', 
                    name: 'input', 
                    description: 'A select box option']
            ])

        echo "Reg is ${reg}"
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
