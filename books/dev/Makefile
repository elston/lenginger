export PROJECT = lendinger

all:
	@echo "Hello $(LOGNAME), nothing to do by default"

# ========= pull ==============
pull:
	@echo "---> pull python:3.6-slim"
	@docker pull python:3.4-slim

# =========== build ================


build_lending:
	@echo "---> build lending"	
	@docker-compose \
		-p $(PROJECT) \
		-f build.yml \
		build lending		


build_all:
	@make build_lending	


# ========= bootstrap ==============

bootstrap_lending:
	@echo "---> bootstrap lending"	
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run \
		--rm \
		lending \
		/usr/local/bin/bootstrap.sh
	@echo "---> end session lending"
	@make down	


bootstrap:
	@make bootstrap_lending	


# =========== shell ======================

.PHONY: shell_lending
shell_lending:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		run \
		--rm \
		--service-ports \
		--name $(PROJECT)_lending_1 \
		lending \
		/bin/bash	




# ============ misc ======================

down:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		down	

ps:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		ps

clear:
	@../../scripts/clear_untagged.sh


# target: images - show all images in project
.PHONY: images
images:
	@docker images |grep $(PROJECT)


# target: volumes - show all volumes in project
.PHONY: volumes
volumes:
	@docker volume ls |grep $(PROJECT)


# target: rmi - remove all images in project
.PHONY: rmi
rmi:
	@docker rmi `docker images |grep $(PROJECT) |xargs -L1 | awk '{print $1}'`


# target: rmvol - remove all volumes in project
.PHONY: rmvol
rmvol:
	@docker volume rm `docker volume ls |grep $(PROJECT) |xargs -L1 | awk "{print $2}"`
