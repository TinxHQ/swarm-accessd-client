pipeline {
  agent any
  environment {
    MAIL_RECIPIENTS = 'dev+tests-reports@wazo.community'
  }
  options {
    skipStagesAfterUnstable()
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Linters') {
      steps {
        sh 'tox -e linters'
      }
    }
    stage('Unit tests') {
      steps {
        sh 'tox -e py37'
      }
    }
    stage('Build and deploy') {
      steps {
        build job: 'build-package', parameters: [
          string(name: 'PACKAGE', value: "${env.JOB_NAME}"),
          string(name: 'VERSION', value: sh(script: 'wazo-version unstable', returnStdout: true).trim()),
          string(name: 'DEBIAN_REPOSITORY', value: 'private'),
          string(name: 'DEBIAN_DISTRIBUTION', value: 'nestbox-dev-buster'),
        ]
      }
    }
  }
  post {
    failure {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
    fixed {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
  }
}
