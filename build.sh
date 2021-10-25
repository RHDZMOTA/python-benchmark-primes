
function build() {
  case "${1}" in
    --c-standalone )
      gcc -o standalonec standalone.c
      ;;
    --c )
      gcc -c -Wall -Werror -fpic isprime.c
      gcc -shared -o libisprime.so isprime.o
      gcc -L${PWD} -Wall -o benchmarkc benchmark.c -lisprime
      ;;
    --py-numba )
      python numba_source.py
      ;;
    --py-cython )
      python setup.py build_ext --inplace
      ;;
  esac
  shift
}

build "${@}"
