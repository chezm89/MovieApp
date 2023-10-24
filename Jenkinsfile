pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/chezm89/MovieApp', branch: 'main')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Check for Updates') {
      steps {
        git(url: 'https://github.com/chezm89/MovieApp', branch: 'main')
        sh '''git status
git pull
git push origin main'''
      }
    }

  }
}