# Implementation of insertsort algorithm.
#
#

def sort(arr)
    arr[1..-1].each_with_index do |element, index|
        while index >=0 and arr[index] > element
          arr[index+1] = arr[index]
          index -= 1
      end
  end

  return arr
end

def main
    arr = [1, 5, 6, 8, 3, 3, 1]
    sort arr
    print arr, "\n"
end

main
