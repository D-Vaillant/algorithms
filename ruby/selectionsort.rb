# Implementation of the selectionsort algorithm.
# 
#

def sort(arr)
    arr.each_with_index do |element, i|
        (i+1..arr.length-1).each do |j|
            if arr[j] < element
                element, arr[j] = arr[j], element
            end
            arr[i] = element
        end
    end
end

def main
    tester = [1, 2, 5, 6, 3, 2, 3, 6, 8, 7, 3, 1]
    
    sort tester
    print tester
    puts
end

main
