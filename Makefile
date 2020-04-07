
dev_env:
	@echo "Seting up development environment"
	(cd algos;pip install -e .)

package:
	(cd algos;make package)

test_algos_local:
	(cd algos;make test)

test:
	docker-compose build algos
	docker-compose run algos /bin/sh -c 'pypy3 -m unittest -v'

clean:
	rm -rf *.out
	(cd algos;make clean)

build_UI_image:
	(cd ui; make clean; make build)
	docker-compose build --no-cache frontend
