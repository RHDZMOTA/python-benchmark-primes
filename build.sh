
function build() {
  case "${1}" in
    --c )
      gcc -o benchmarkc benchmark.c
      ;;
    --py-numba )
      python numba_source.py
      ;;
  esac
  shift
}

build "${@}"
