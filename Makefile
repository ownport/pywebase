test-unittest:
	@ echo '***************************'
	@ echo '*       Unittests         *'
	@ echo '***************************'

test-doctest:
	@ echo '***************************'
	@ echo '*       Doctests          *'
	@ echo '***************************'

test-all:
	make test-unittest
	make test-doctest

todo:
	@ echo 
	@ echo "*** TODOs for manage.py ***"
	@ echo 
	@ awk '/# TODO/ { gsub(/^ /, ""); print }' manage.py
	@ echo 
	@ echo "*** TODOs for packages/pywebase.py ***"
	@ echo 
	@ awk '/# TODO/ { gsub(/^ /, ""); print }' packages/pywebase.py
	@ echo 
	
