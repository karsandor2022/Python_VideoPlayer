pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = "python-video-app"
        IMAGE_TAG = "latest"
        DOCKERHUB_REPO = "thecrafter22/python-video-app"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Pulling project from Git..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh "pip install --no-cache-dir -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh "echo 'No tests implemented yet'"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "Pushing Docker image to DockerHub..."
                sh """
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKERHUB_REPO}:${IMAGE_TAG}
                    docker push ${DOCKERHUB_REPO}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application using Docker Compose..."
                sh "docker compose down && docker compose up -d --build"
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Build failed. Check errors."
        }
    }
}
