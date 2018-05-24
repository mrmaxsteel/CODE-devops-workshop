pipeline {
  // Run this pipeline on the Jenkins Master (unless otherwise specified)
  agent { label 'master' }

  stages {
    stage ('Build') {
      steps {
        sh """
          docker build \
            --pull \
            --no-cache \
            --target builder .
        """
      }
    }

    stage ('Unit Tests') {
      steps {
        sh """
          docker build \
            --target unit-tests .
        """
      }
    }

    stage ('Integration Tests') {
      steps {
        sh """
          docker build \
            --target integration-tests \
            -t img-${GIT_COMMIT} .
        """
      }
    }

    stage ('Parse Test Results') {
      steps {
        sh "docker run --name ctr-${GIT_COMMIT} img-${GIT_COMMIT}"
        sh "docker cp ctr-${GIT_COMMIT}:/app results"
      }
      post {
        // Parse the test results so they appear in BlueOcean UI
        always {
          sh "docker rm --force ctr-${GIT_COMMIT} || true"
          junit 'results/**/*_results.xml'
        }
      }
    }

    stage ('Docker Build & Run') {
      // Since no agent{} is specified, this stage will run on the Jenkins Master
      when {
        // Only run the application when on 'master' branch
        branch 'master'
      }
      steps {
        // Remove any existing running containers
        sh 'docker container rm --force flask-calculator-app || true'
        // Re-build the Docker Image and tag it as 'latest'
        sh 'docker build --rm -t flask-calculator-img --target production .'
        sh 'docker tag flask-calculator-img flask-calculator-img:latest'
        // Run the new Docker Image
        sh 'docker container run --name flask-calculator-app -p 5000:5000 -d flask-calculator-img:latest'
      }
      post {
        success {
          sh "echo The app can be tested by visiting: http://`curl -s http://169.254.169.254/latest/meta-data/public-hostname`:5000"
        }
      }
    }
  }
}
