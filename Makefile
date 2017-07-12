
run fg default : 
	. venv.bottle/bin/activate && python hello_world.py

bg : 
	. venv.bottle/bin/activate && nohup python hello_world.py > hello_world.log 2>&1 & echo $$! | tee hello_world.pid

kill :
	kill `cat hello_world.pid`
	rm -fv hello_world.pid

status : 
	if [ -r hello_world.pid ] ; then \
		ps --pid `cat hello_world.pid` ; \
	else \
		echo no PID ; \
	fi

clean : 
	rm -fv hello_world.pid
