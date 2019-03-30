# Radiation Testing Budget

repo for laying out radiation tests, components to be tested, and the sequence of
those tests.

# Software To Be Used 
for reference on what should be done look at pdf in main directory of this repo

## GPU TESTS
(https://docs.nvidia.com/cuda/cuda-samples/index.html)

- vector addition loop 
- summation loop (atomics and shared memory) 
- FluidsGL (heavy CPU and GPU)

## MEMORY MONITORS

- flash checker = checksum and copy script needs to be written 
 - 100MB version in answers (https://unix.stackexchange.com/questions/37815/where-can-i-find-storage-integrity-write-read-test-tools)
- LPDDR4 checkers
 - GPU RAM usage (cudamemchecker or https://sourceforge.net/projects/cudagpumemtest/)
 - CPU RAM usage (https://en.wikipedia.org/wiki/Memtest86)
