pipeline {

  agent { label 'master' }

  environment {
    IMAGE_ID = 'flask-calculator-img'
    CONTAINER_NAME = 'flask-calculator-app'
  }

  stages {

    stage ('Run Unit Tests') {
      agent { 
        dockerfile {
          additionalBuildArgs  '--target builder'
        } 
      }
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
      agent { 
        dockerfile {
          reuseNode true
        } 
      }
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
      // when {
      //   branch 'master'
      // }
      steps {  
        sh "docker container rm --force ${env.CONTAINER_NAME} || true"
        sh "docker build --rm -t ${env.IMAGE_ID} ${env.IMAGE_ID}:latest ."
        sh "docker tag ${env.IMAGE_ID} ."
        sh "docker container run --name ${env.CONTAINER_NAME} -p 5000:5000 ${env.IMAGE_ID}:latest"
      }
    }
  }
}
