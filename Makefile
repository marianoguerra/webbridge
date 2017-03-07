
.PHONY: build
build: clean
	cd site && nikola build && mv output/* ..

clean:
	rm -rf 2013 2017 *.html *.txt *.xml speakers sponsors signup news imgs favicon.ico contact es de assets categories location schedule site/__pycache__ site/output site/cache

serve:
	python -m SimpleHTTPServer
