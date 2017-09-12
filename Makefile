
run fg default : 
	. venv.bottle/bin/activate && python hello_world.py

bg : 
	date
	. venv.bottle/bin/activate && nohup python hello_world.py > hello_world.log 2>&1 & echo $$! | tee hello_world.pid
	date

kill :
	date
	kill `cat hello_world.pid` || true
	rm -fv hello_world.pid || true
	date

status diag : 
	@if [ -r hello_world.pid ] ; then \
		ps -F --pid `cat hello_world.pid` ; \
	else \
		echo no PID ; \
	fi

clean : 
	rm -fv hello_world.pid

refresh :
	make kill
	git pull
	make bg

