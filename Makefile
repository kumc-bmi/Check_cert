run: venv_clean venv
	. venv/bin/activate && \
	which python3 && \
	mkdir -p ./server_fails && \
	# download which projects needs to export and its token && \
	python3 Main_Code_Extraaction.py '12.0.8' '12.0.8' 'Both'

venv:
	# "creating python3 virtual env"
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	python3 -m virtualenv venv
	python3 -m venv ./venv --upgrade
	. ./venv/bin/activate && \
	pip3 install --upgrade pip  && \
	pip3 install -r requirements.txt  && \
	pip3 freeze >  requirements_pip_freeze.txt  && \
	which pip3 && which python3 && python3 --version

venv_clean:
	# "deleting python3 virtual env"
	rm -rf ./venv
