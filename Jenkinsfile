pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
            }
        }
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
        stage('Run fronted tests') {
            steps {
                sh 'python fronted_testing.py'
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
