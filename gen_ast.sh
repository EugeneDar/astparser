export TERM=xterm-mono

#clang++ -Xclang -ast-dump -fsyntax-only data/simple_heap_allocation.cpp > input/simple_heap_allocation
#clang++ -Xclang -ast-dump -fsyntax-only data/simple.cpp

for file in `find data -type f -name "*"`
do
  prefix="data"
  path="$file"
  path="${path##data}"
  input_file="data${path}"
  output_file="input${path}"
  echo $input_file $output_file
  clang++ -Xclang -ast-dump -fsyntax-only ${input_file} > ${output_file}
done