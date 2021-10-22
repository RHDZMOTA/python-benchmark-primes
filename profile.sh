
function profile() {
  case "${1}" in
    --py-naive )
      scalene \
        --profile-all \
        --reduced-profile \
        --profile-only 'benchmark.py,naive_impl.py' \
        benchmark.py naive_impl is_prime 250001
      ;;
    --py-numba )
      scalene \
        --profile-all \
        --reduced-profile \
        --profile-only 'benchmark.py,numba_impl.py,numba_source.py' \
        benchmark.py numba_impl is_prime 250001
      ;;
  esac
  shift
}

profile "${@}"
