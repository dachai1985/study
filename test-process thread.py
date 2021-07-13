import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('222222222222222222=', std)
    print('333333333333333333=', threading.current_thread().name)
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    print('1111111111111111111=', name)
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()