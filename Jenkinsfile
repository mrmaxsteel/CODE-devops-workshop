pipeline {
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

    stage ('Run Unit & Integration Tests') {
      steps {
        // Run the Unit Tests
        sh """
          docker build \
            --target unit-tester .
        """
        // Run the Integration Tests
        sh """
          docker build \
            --target integration-tester \
            -t img-${GIT_COMMIT} .
        """
      }
      post {
        // Parse the test results so they appear in BlueOcean UI
        success {
          sh "docker run -t -d --rm --name ctr-${GIT_COMMIT} img-${GIT_COMMIT}"
          sh "docker cp ctr-${GIT_COMMIT}:/app/. results"
          sh "docker rm --force ctr-${GIT_COMMIT}"
          junit 'results/**/*_results.xml'
        }
      }
    }
    
    stage ('Docker Build') {
      steps {
       sh """
        docker build \
          --target production \
          -t flask-calculator-img:latest .
       """
      }
    }

    stage ('Deploy') {
      // Since no agent{} is specified, this stage will run on the Jenkins Master
      when {
        // Only deploy the application when on 'master' branch
        branch 'master'
      }
      steps {  
        // Remove any existing running containers
        sh 'docker container rm --force flask-calculator-app || true'
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
