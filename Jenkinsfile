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

    stage('Deploy') {
      steps {
        sh """
          $(docker inspect -f '{{.ID}}' my-container 2>/dev/null) \
            && docker rm -f my-container \
            || true
        """
        script {
          image.run("--name my-container")
        }
      }
    }

    stage('Release') {
      steps {
        script {
          image.push()
        }
      }
    }
  }
}