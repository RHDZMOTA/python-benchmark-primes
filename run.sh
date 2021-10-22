
function run() {
  case "${1}" in
    --c )
      ./benchmarkc
      ;;
    --py-naive )
      python benchmark.py naive_impl is_prime 250001
      ;;
    --py-numba )
      python benchmark.py numba_impl is_prime 250001
      ;;
  esac
  shift
}

run "${@}"
