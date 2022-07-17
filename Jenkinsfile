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
        script {
          containerID = docker.inspect("my-container", '.Id')
          if (containerID) {
            docker.stop(containerID) // also removes it
          }
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