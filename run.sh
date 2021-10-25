
function run() {
  case "${1}" in
    --c-standalone )
      ./standalonec
      ;;
    --c )
      LD_LIBRARY_PATH=${PWD} ./benchmarkc
      ;;
    --py-naive )
      python benchmark.py naive_impl is_prime 250001
      ;;
    --py-ctypes )
      python benchmark.py ctypes_impl is_prime 250001
      ;;
    --py-numba )
      python benchmark.py numba_impl is_prime 250001
      ;;
    --py-cython-naive )
      python benchmark.py cython_naive_impl is_prime 250001
      ;;
    --py-cython )
      python benchmark.py cython_impl is_prime 250001
      ;;
  esac
  shift
}

run "${@}"
