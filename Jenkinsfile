pipeline {
  agent any

  environment {
    IMAGE_NAME = "flask-notes:01"
  }

  stages {

    stage('Checkout Code') {
      steps {
        checkout scm
        echo '✅ Checked out source code from repository.'
      }
    }

    stage('Setup Python') {
      steps {
        echo '⚙️ Setting up the Python environment...'
        // (Optional) If you really want to install Python locally, you could do so here.
        // For now we’ll just echo it like your GitHub Action did.
      }
    }

    stage('Install Dependencies') {
      steps {
        echo '📦 Installing dependencies...'
        // In real case:
        // sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        echo '🧪 Running tests...'
        // In real case:
        // sh 'pytest -q || echo "⚠️ No tests found (skipping)"'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo '🐳 Building Docker image...'
        sh '''
          docker build -t ${IMAGE_NAME} .
          echo "Sleeping for 10 seconds to simulate wait..."
          sleep 10
          docker ps
          sleep 5
          docker ps -a
        '''
      }
    }

    stage('Run Docker Container') {
      steps {
        echo '🚀 Running Docker container...'
        sh '''
          docker run -d -p 5000:5000 --name flasknotes ${IMAGE_NAME}
          echo "Container started successfully!"
          sleep 5
          docker ps
        '''
      }
    }

    stage('Cleanup') {
      steps {
        echo '🧹 Cleaning up Docker containers and images...'
        sh '''
          docker rm -f $(docker ps -aq) || true
          docker rmi -f $(docker images -aq) || true
        '''
      }
    }
  }

  post {
    success {
      echo '🎉 CI workflow completed successfully!'
    }
    failure {
      echo '❌ CI workflow failed. Check logs for details.'
    }
  }
}
