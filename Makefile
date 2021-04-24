# To run this file use the following command:
# make TARGET_NAME FLASK_ENV=<VALUE>

all: stop delete start

dev:
	@echo "========================"
	@echo "Note: This app is run in ${FLASK_ENV} mode"
	@echo "========================"
	@python3 app.py

prod:
	@echo "========================"
	@echo "Note: This app is run in ${FLASK_ENV} mode"
	@echo "========================"
	@python3 app.py

start:
	@echo ""
	@echo "========================"
	@echo "Building image..."
	@echo "========================"
	@echo ""
	@sudo docker build --tag repo.treescale.com/abdurahmanshiine/vm-app-api:amd64 .

	@echo ""
	@echo "========================"
	@echo "Running container..."
	@echo "========================"
	@echo ""
	@sudo docker container run -dp 8888:8888 -v $(pwd):/app -e PORT='8888' -e FLASK_ENV='Development' --name api repo.treescale.com/abdurahmanshiine/vm-app-api:amd64

stop:
	@echo ""
	@echo "========================"
	@echo "Stopping container..."
	@echo "========================"
	@echo ""
	@-sudo docker stop api

delete: stop
	@echo ""
	@echo "========================"
	@echo "Deleting container..."
	@echo "========================"
	@echo ""
	@-sudo docker container rm api