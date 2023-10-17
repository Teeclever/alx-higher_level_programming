exec:
	chmod +x *.py models/*.py tests/test_models/*.py

pycode:
	pycodestyle models/*.py tests/test_models/*.py

quicktest_all:
	for f in $$(seq 1 18); do \
		echo "############################## Quick testing $${f}-main.py ##############################"; \
		"./$${f}-main.py"; \
	done
	echo "############################## Quick testing 100-main.py ##############################";
	./100-main.py;

unittest_all:
	python3 -m unittest discover tests

unittest_base:
	python3 -m unittest tests/test_models/test_base.py

unittest_rectangle:
	python3 -m unittest tests/test_models/test_rectangle.py

unittest_square:
	python3 -m unittest tests/test_models/test_square.py

clean:
	rm *.json *.csv