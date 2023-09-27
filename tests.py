from src.pytona import chronograph


@chronograph(filename="example.prof")
def count_alot():
    last = 1
    for i in range(100000):
        last += i

    return last

count_alot()


@chronograph
def yell_several_times():
    for _ in range(50):
        print("YELLING!")


yell_several_times()
