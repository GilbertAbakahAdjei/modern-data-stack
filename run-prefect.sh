#!/usr/bin/env bash
up() {


  echo "Starting Prefect..."
  docker-compose -f docker-compose-prefect.yaml down -v
 
  docker-compose -f docker-compose-prefect.yaml up -d
  

}

down() {
 
  echo "Stopping Prefect..."
  docker-compose -f docker-compose-prefect.yaml down -v
  
}

case $1 in
  up)
    up
    ;;
  down)
    down
    ;;
  *)
    echo "Usage: $0 {up|down}"
    ;;
esac