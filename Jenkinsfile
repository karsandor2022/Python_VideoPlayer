pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-video-app"
        IMAGE_TAG = "latest"
        DOCKERHUB_REPO = "thecrafter22/python-video-app"   // <-- EDIT THIS
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
                sh "pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                // Placeholder for actual tests
                sh "echo 'No tests implemented yet'"
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
                sh """
                    docker compose down
                    docker compose up -d --build
                """
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