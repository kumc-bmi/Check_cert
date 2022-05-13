run: clean venv
	. venv/bin/activate && \
	which python3 && \
	mkdir -p ./server_fails && \
	# download which projects needs to export and its token && \
	python3 cert_scanner.py redcap.kumc.edu,heron.kumc.edu,nightheron.kumc.edu,webcamp.kumc.edu,informatics.kumc.edu,bmi-webcamp-dev.kumc.edu 'both'

venv:
	# "creating python3 virtual env"
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	python3 -m virtualenv venv
	python3 -m venv ./venv --upgrade
	. ./venv/bin/activate && \
	pip3 install --upgrade pip  && \
	pip3 install -r requirements.txt  && \
	pip3 freeze > requirements_pip_freeze.txt  && \
	which pip3 && which python3 && python3 --version

clean:
	# "deleting python3 virtual env"
	rm -rf ./venv &&\
	rm -rf ./server_fails
	
install_python3_cifs:
	sudo yum install -y python3-pip cifs-utils
	python3 -m pip3 install --user --upgrade pip
	python3 -m pip3 install --user virtualenv
