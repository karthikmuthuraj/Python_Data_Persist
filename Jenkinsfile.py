pipeline {
    agent any
    stages {
      stage('Select Environment to Deploy') {
        steps {
              script {
                env.selected_environment = input  message: 'Select Module to Build',ok : 'Proceed',id :'tag_id',
                parameters:[choice(choices: ['CSV', 'JSN', 'RWL'], description: 'Select Module', name: 'env')]
                echo "Deploying in ${env.selected_environment}."
                }
            }
        }
        
        // stage('Test Python Script') {
        //    steps {
        //        powershell 'python testPy.py'
        //    }
        // }
    }    
}
