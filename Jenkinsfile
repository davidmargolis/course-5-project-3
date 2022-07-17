#!/usr/bin/env groovy

def image

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        script {
          image = docker.build('dmm2168/course-5-project-3:latest')
        }
      }
    }

    stage('Test') {
      steps {
        script {
          image.withRun() {container ->
            sh """
              docker cp test_app.py ${container.id}:/ \
                && docker exec ${container.id} python -m unittest
            """
          }
        }
      }
    }

    stage('Cleanup') {
      steps {
        sh """
          docker inspect -f '{{.ID}}' my-container 2>/dev/null \
            && docker rm -f my-container \
            || true
        """
      }
    }

    stage('Deploy') {
      steps {
        script {
          image.run("--name my-container")
        }
      }
    }

    stage('Release') {
      steps {
        script {
          sh """
          docker login -u dmm2168 --password=c2a46d35-2300-4ffe-961a-4d9a36474221 \
            && docker push my-container:latest
          """
        }
      }
    }
  }
}