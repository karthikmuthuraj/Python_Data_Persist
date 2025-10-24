pipeline {
    agent any
    stages {
      stage('Select Environment to Deploy') {
        steps {
              script {
                env.selected_module = input  message: 'Select Module to Build',ok : 'Proceed',id :'tag_id',
                parameters:[choice(choices: ['CSV', 'JSN', 'RWL'], description: 'Select Module', name: 'Module_Keyword')]
                echo "Selected Module : ${env.selected_module}."
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
s