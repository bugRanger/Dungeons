from threading import Thread

# TODO Перепроверить подход работы с потоком.
def thread(myfunc):
	def wrapper(*args, **kwargs):
		thread = Thread(target=myfunc, args=args, kwargs=kwargs)
		thread.start()
		return thread
	return wrapper
	
if __name__ == '__main__':
	@thread
	def message(text):
		print(text)
	message('it is thread')