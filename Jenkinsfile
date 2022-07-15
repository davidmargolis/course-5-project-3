#!/usr/bin/env groovy

pipeline {
  stages {
    stage 'Build' {
      def image = docker.build 'dmm2168/course-5-project-3:latest'
    }

    stage 'Test' {
      image.withRun() {container ->
        sh """
          docker cp test_app.py ${container.id} \
            && docker exec ${container.id} python -m unittest
        """
      }
    }

    stage 'Deploy' {
      environment {
        CONTAINER_NAME = "my-container"
      }

      def containerID = docker.inspect("$CONTAINER_NAME", '.Id')
      if (containerID) {
        docker.stop containerID // also removes it
      }
      image.run "--name $CONTAINER_NAME"
    }

    stage 'Release' {
      image.push
    }
  }
}