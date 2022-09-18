import a2
import time
import pickle

# f = open("testcase.bin", "rb")
# test = pickle.lx oad(f)
# f = open("testcase2.bin", "rb")
# test2 = pickle.load(f)
f = open("testcase3.bin", "rb")
test3 = pickle.load(f)
f = open("check2.bin", "rb")
check = pickle.load(f)

out = []


def compare(out, check):
    if (len(out) != len(check)):
        return False
    for j in range(len(out)):
        if (len(out[j]) != len(check[j])):
            return False
        for i in range(len(out[j])):
            if abs(out[j][i][0] - check[j][i][0]) > 0.0001 or out[j][i][1] != check[j][i][1] or abs(out[j][i][2] - check[j][i][2]) > 0.0001:
                print(f"Your answer, ", out[j][i])
                print(f"Checker answer, ", check[j][i])
                return False
    return True


print("Checking Function")
if a2.listCollisions([1, 1, 1, 1, 1, 1],
                     [0, 1, 2, 3, 4, 5],
                     [1, 0, 1, 0, 1, 0],
                     8,
                     100) == [(1.0, 0, 1.0), (1.0, 2, 3.0), (1.0, 4, 5.0), (3.0, 1, 3.0), (3.0, 3, 5.0), (5.0, 2, 5.0)]:
    print("Starting Checker")
    # print("Checking Normal Cases...")
    # st = time.time()
    # for i in test:
    #     out.append(a2.listCollisions(i[0], i[1], i[2], i[3], i[4]))
    # print("Time taken: ", time.time()-st)
    # print()
    # print("Checking Large Cases...")
    # st = time.time()
    # for i in test2:
    #     out.append(a2.listCollisions(i[0], i[1], i[2], i[3], i[4]))
    # print("Time taken: ", time.time()-st)

    print()
    print("Checking Other Cases...")
    st = time.time()
    for i in test3:
        out.append(a2.listCollisions(i[0], i[1], i[2], i[3], i[4]))
    print("Time taken: ", time.time()-st)
    print()

    # f = open("check2.bin", "wb")
    # pickle.dump(out, f)
    if compare(out, check):
        print("Passed")
    else:
        print("Failed")
else:
    print("Function test failed")
