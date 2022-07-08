#!/usr/bin/env groovy

pipeline {
  stages {
    node {
      stage 'Initialize'
      checkout scm

      stage 'Build'
      def customImage = docker.build("course-5-project-3:latest")

      stage 'Test'
      testContainer.withRun('--name dmm2168/course-5-project-3-test') {c ->
        sh '''
          docker cp test_app.py test:/ \
            && docker exec test python -m unittest
        '''
      }

      stage 'Deploy'
      def containerID = docker.inspect('course-5-project-3', '.Id')
      if (containerID) {
        docker.stop(containerID)
      }
      customImage.run('--name course-5-project-3')

      stage 'Release'
      customImage.push()
    }
  }
}
