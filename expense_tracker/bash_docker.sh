echo "FROM python:3" > Dockerfile
echo "RUN pip3 install django" >> Dockerfile
echo "COPY . ." >> Dockerfile
echo "RUN python manage.py migrate" >> Dockerfile
echo 'CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]' >> Dockerfile

# Build the Docker image
sudo docker build . -t expense_tracker

# Run the Docker container
container_id=$(sudo docker run -p 8001:8001 expense_tracker)

# Display the Container ID
echo "Docker container ID: $container_id"
