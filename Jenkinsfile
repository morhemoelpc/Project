pipeline {
    agent any
    options {
        timestamps()
        buildDiscarder(strategy: logRotator(numToKeepStr: '5', artifactNumToKeepStr: '20'))
    }
    stages {
        stage('SCM Poll') {
            triggers {
                pollSCM('*/30 * * * *')
            }
            steps {
                git url: 'https://github.com/morhemoelpc/Project.git'
            }
        }
        stage('Run Backend Server') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('Run Frontend Server') {
            steps {
                bat 'start /min python web_app.py'
            }
        }
        stage('Backend Testing') {
            steps {
                python 'backend_testing.py'
            }
        }
        stage('Frontend Testing') {
            steps {
                python 'frontend_testing.py'
            }
        }
        stage('Combined Testing') {
            steps {
                python 'combined_testing.py'
            }
        }
        stage('Clean Environment') {
            steps {
                python 'clean_environment.py'
            }
        }
    }
}