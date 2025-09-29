#!/bin/bash

cd ../site-avaliacoes-jogos

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
IMAGE_NAME="avaliacoes-site"
IMAGE_TAG="1.0"
REGISTRY="ghcr.io"
# Replace with your GitHub username and repository name
GH_OWNER="ricleta"
GH_REPO="inf1407-trabalho1"

# --- Script ---
echo "Tagging image for GitHub Container Registry..."
docker tag "${IMAGE_NAME}:${IMAGE_TAG}" "${REGISTRY}/${GH_OWNER}/${GH_REPO}:${IMAGE_TAG}"

echo "Pushing image to ${REGISTRY}..."
docker push "${REGISTRY}/${GH_OWNER}/${GH_REPO}:${IMAGE_TAG}"