PY?=python
PELICAN?=pelican
PELICANOPTS=
PORT=8000

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
OUTPUTDIRZIP=$(BASEDIR)/output_zip
PUBLISHCONF=$(BASEDIR)/publishconf.py
DATESTAMP=$(shell /bin/date "+%Y_%m_%d_%H_%M_%S")


SSH_HOST=0x7c00.me
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/blog_zip
SSH_DEPLOY_CMD='/usr/local/tools/blog_deploy.sh'

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make upload                         upload the web site to vps         '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html: clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)


upload: html
	cd $(OUTPUTDIR) && zip -r $(OUTPUTDIRZIP)/blog_$(DATESTAMP).zip ./*
	scp -P $(SSH_PORT) $(OUTPUTDIRZIP)/blog_$(DATESTAMP).zip $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

deploy:
	ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_HOST) $(SSH_DEPLOY_CMD)