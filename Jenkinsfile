pipeline {

  agent { dockerfile true }

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

    // stage ('Docker Build') {
    //   agent { master }
    //   steps {
    //     sh 'docker build -t '
    //   }
    // }

    // stage ('Docker Run') {
    //   agent { master }
    //   steps {
    //     sh 'docker run -p 5000:5000'
    //   }
    // }
  }
}
