pipeline {

  agent { label 'master' }

  environment {
    IMAGE_ID = 'flask-calculator-img'
    CONTAINER_NAME = 'flask-calculator-app'
  }

  stages {

    stage ('Run Unit & Integration Tests') {
      agent { 
        dockerfile true
      }
      steps {
        sh 'py.test flask-test-kata/tests/unit -v --junitprefix=linux --junitxml unit_results.xml || true'
        sh 'py.test flask-test-kata/tests/integration -v --junitprefix=linux --junitxml integration_results.xml || true'
      }
      post {
        always {
          junit '**/*_results.xml'
        }
      }
    }

    stage ('Docker Build & Run') {
      // when {
      //   branch 'master'
      // }
      steps {  
        sh 'docker container rm --force flask-calculator-app || true'
        sh 'docker build --rm -t flask-calculator-img .'
        sh 'docker tag flask-calculator-img flask-calculator-img:latest'
        sh 'docker container run --name flask-calculator-app -p 5000:5000 -d flask-calculator-img:latest'
      }
      post {
        success {
          echo 'The app can be tested by visiting: "http://`curl -s http://169.254.169.254/latest/meta-data/public-hostname`:5000"'
        }
      }
    }
  }
}
