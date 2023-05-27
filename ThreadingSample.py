import threading


def testing():
    print("Line gets executed")
    time.sleep(2)

testing()
testing()
testing()
testing()
testing()

for i in range (0, 5):
    t = threading.Thread(target=testing)
    t.start()