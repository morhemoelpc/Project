pipeline {
    agent any

    options {
        timestamps()
        buildDiscarder(strategy: logRotator(numToKeepStr: '5', artifactNumToKeepStr: '20'))
        triggers {
            cron('*/30 * * * *')
        }
    }

    stages {
        stage('Clone repository') {
            steps {
                git url: 'https://github.com/morhemoelpc/Project.git'
            }
        }
        stage('Run backend server') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('Run frontend server') {
            steps {
                bat 'start /min python web_app.py'
            }
        }
        stage('Run backend tests') {
            steps {
                sh 'python backend_testing.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                sh 'python frontend_testing.py'
            }
        }
        stage('Run combined tests') {
            steps {
                sh 'python combined_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }
}
