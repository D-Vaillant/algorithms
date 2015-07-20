# Implementation of the bubblesort algorithm.
#
#

def sort(arr)
    (0..(arr.length-1)).each do |i|
        r = (i..(arr.length-1))
        r.reverse_each do |j| 
          if arr[j] < arr[j-1]
             arr[j-1], arr[j] = arr[j], arr[j-1]
          end
        end
    end
end

def main
    test = [5, 7, 2, 5, 7, 8, 2, 1, 4, 1, -2]
    
    print test, "\n"
    sort(test)
    print test, "\n"
end

main
