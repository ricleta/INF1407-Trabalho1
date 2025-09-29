cd ../site-avaliacoes-jogos

echo "Building Docker image for the AvaliacoesSite..."

docker build -t avaliacoes-site:1.0 .

echo "Starting Docker container for the AvaliacoesSite..."

docker run -d -p 8000:8000 --name avaliacoes-container avaliacoes-site:1.0
