.PHONY = analisis
SHELL := /bin/bash

analisis:
	sudo apt install python3-pip
	pip3 install flask
	pip3 install flask_cors
	pip3 install sympy
	pip3 install numpy	
	pip3 install matplotlib
	pip3 install threading
