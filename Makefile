
dev_env:
	@echo "Seting up development environment"
	(cd algos;pip install -e .)

package:
	(cd algos;make package)

test:
	(cd algos;make test)

clean:
	rm -rf *.out
	(cd algos;make clean)
