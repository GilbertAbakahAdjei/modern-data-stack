#!/usr/bin/env bash
up() {
  # echo "Starting Airbyte..."
  # docker-compose -f docker-compose-airbyte.yaml down -v
  # docker-compose -f docker-compose-airbyte.yaml up -d

  echo "Starting Prefect..."
  docker-compose -f docker-compose-prefect.yaml down -v
 
  docker-compose -f docker-compose-prefect.yaml up
  
  echo "Starting Metabase..."
  cd metabase
  docker-compose -f docker-compose-metabase.yaml down -v
  docker-compose -f docker-compose-metabase.yaml up -d
  cd ..

}

down() {
  # echo "Stopping Airbyte..."
  # docker-compose -f docker-compose-airbyte.yaml down -v
  echo "Stopping Prefect..."
  docker-compose -f docker-compose-prefect.yaml down -v
  echo "Stopping Metabase..."
  docker-compose -f metabase/docker-compose-metabase.yaml down -v
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