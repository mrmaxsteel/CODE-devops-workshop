pipeline {

  agent { dockerfile true }

  stages {

    stage ('Run Unit Tests') {
      steps {
        sh 'py.test flask-test-kata/tests/unit -v'
      }
    }

    stage ('Run Integration Tests') {
      steps {
        sh 'py.test flask-test-kata/tests/integration -v'
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
