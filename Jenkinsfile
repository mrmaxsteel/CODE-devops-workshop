pipeline {

  agent { 
    dockerfile {
      additionalBuildArgs  '--target builder'
    } 
  }

  environment {
    IMAGE_ID = 'flask-calculator-img'
    CONTAINER_NAME = 'flask-calculator-app'
  }

  stages {

    stage ('Run Unit Tests') {
      steps {
        sh 'py.test flask-test-kata/tests/unit -v --junitprefix=linux --junitxml unit_results.xml || true'
      }
      post {
        always {
          junit '**/unit_results.xml'
        }
      }
    }

    stage ('Run Integration Tests') {
      steps {
        sh 'py.test flask-test-kata/tests/integration -v --junitprefix=linux --junitxml integration_results.xml || true'
      }
      post {
        always {
          junit '**/integration_results.xml'
        }
      }
    }

    stage ('Docker Build & Run') {
      agent { label 'master' }
      // when {
      //   branch 'master'
      // }
      steps {  
        sh "sudo docker container rm --force ${env.CONTAINER_NAME} || true"
        sh "sudo docker build --rm -t ${env.IMAGE_ID} ${env.IMAGE_ID}:latest"
        sh "sudo docker tag ${env.IMAGE_ID} ."
        sh "sudo docker container run --name ${env.CONTAINER_NAME} -p 5000:5000 ${env.IMAGE_ID}:latest"
      }
    }
  }
}
