jetzt := $(shell date)

build:
	python build.py deploy

clean:
	rm -r -v deploy

deploy: build
	git checkout gh-pages
	mv deploy/* .
	rmdir deploy
	git commit -a -m "updated $(jetzt)"
	git push
	git checkout master
