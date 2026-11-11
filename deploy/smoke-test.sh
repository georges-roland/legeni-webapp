#!/bin/sh
set -e
PROJECT=$1
EXPECTED_VERSION=$2
NETWORK="${PROJECT}_default"
CONTAINER="${PROJECT}-web-1"

curl_net() {
    docker run --rm --network "$NETWORK" curlimages/curl:8.11.1 -sf --retry 10 --retry-connrefused --retry-delay 1 "$1"
}

echo "Verification de /ready sur $CONTAINER..."
curl_net "http://${CONTAINER}:5000/ready" | grep -q "true"

echo "Verification de la version $EXPECTED_VERSION sur /api/info..."
curl_net "http://${CONTAINER}:5000/api/info" | grep -q "$EXPECTED_VERSION"

echo "Smoke test OK pour $PROJECT ($EXPECTED_VERSION)"
