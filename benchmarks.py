import os
import re
import sys
import time
import json
import subprocess
from multiprocessing import Process, Queue
from typing import List


TERMINATE_MESSAGE = "TERMINATE"
REGEX_NUMBERS = re.compile("\d*\.?\d+")
BENCH_PARALLELISM = os.environ.get(
    "BENCH_PARALLELISM",
    default="false"
).lower().startswith("true")


def worker_benchmark(tag: str, queue: Queue):
    cmd = f"bash run.sh --{tag}"
    res = subprocess.check_output(cmd, shell=True).decode("utf-8")
    payload = {
        "tag": tag,
        "res": res,
        "duration": REGEX_NUMBERS.findall(res)[-1]
    }
    queue.put(json.dumps(payload))


def worker_writer(output_path: str, queue: Queue):
    print("Starting writer worker.")
    output_file = os.path.join(output_path, f"benchmark-outputs-{time.time()}.json")
    while True:
        message = queue.get(block=True)
        if not message or not isinstance(message, str):
            continue
        if message == TERMINATE_MESSAGE:
            print("Closing writer worker.")
            break
        if not message.startswith("{"):
            continue
        with open(output_file, "a") as file:
            file.write(message + "\n")


class Benchmark:

    def __init__(self, tag: str):
        self.tag = tag

    def run(self, output_queue: Queue, executions: int, parallel: bool = BENCH_PARALLELISM) -> List[Process]:
        processes = []
        for _ in range(executions):
            p = Process(target=worker_benchmark, args=(self.tag, output_queue))
            p.start()
            if not parallel:
                p.join()
            processes.append(p)
        return processes


class Benchmarks:
    C = "c"
    PY_NAIVE = "py-naive"
    PY_CTYPES = "py-ctypes"
    PY_NUMBA = "py-numba"
    PY_CYTHON_NAIVE = "py-cython-naive"
    PY_CYTHON = "py-cython"

    def __init__(self, output_queue: Queue, executions: int):
        self.output_queue = output_queue
        self.executions = executions

    def tags(self) -> List[str]:
        return [
            self.C,
            self.PY_NAIVE,
            self.PY_CTYPES,
            self.PY_NUMBA,
            self.PY_CYTHON_NAIVE,
            self.PY_CYTHON
        ]

    def run_benchmark(self, tag: str) -> List[Process]:
        return Benchmark(tag=tag).run(
            output_queue=self.output_queue,
            executions=self.executions,
        )

    def run_all(self) -> List[Process]:
        return [
            process
            for tag in self.tags()
            for process in self.run_benchmark(tag=tag)
        ]


class Main:

    def __init__(self, execs: int):
        self.execs = execs
        self.output_queue = Queue()

    def run(self):
        # Configure writer process
        output_path = os.path.dirname(os.path.realpath(__file__))
        process_writer = Process(target=worker_writer, args=(output_path, self.output_queue))
        process_writer.start()
        # Run benchmarks
        benchmarks = Benchmarks(output_queue=self.output_queue, executions=self.execs)
        processes = benchmarks.run_all()
        for process in processes:
            process.join()
        # Close up resources
        self.output_queue.put(TERMINATE_MESSAGE)
        process_writer.join(timeout=3)


if __name__ == "__main__":
    _, execs = sys.argv
    Main(execs=int(execs)).run()
