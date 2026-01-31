import time
import matplotlib.pyplot as plt

from matcher import generate_input, gale_shapley
import verifier

def measure_times():
    ns = [1,2,4,8,16,32,64,128,256,512]
    match_times = []
    verify_times = []

    for n in ns:
        filename = f"scale/file{n}.txt"
        generate_input(filename, n)
        
        start = time.perf_counter()
        output = gale_shapley(filename)
        end = time.perf_counter()
        match_times.append(end - start)
        
        start = time.perf_counter()
        verifier.verifier(*output)
        end = time.perf_counter()
        verify_times.append(end - start)
    
    return ns, match_times, verify_times

def plot_results(ns, match_times, verify_times):
    plt.plot(ns, match_times, marker='o', label="Gale-Shapley")
    plt.plot(ns, verify_times, marker='o', label="Verifier")

    plt.xlabel("Number of hospitals/students (n)")
    plt.ylabel("Running time (seconds)")
    plt.title("Scalability of Matching and Verification")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ns, match_times, verify_times = measure_times()
    plot_results(ns, match_times, verify_times)