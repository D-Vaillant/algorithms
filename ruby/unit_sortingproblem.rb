
R = Random.new

def main(size, runs)
  glass = True
  for j in (0..runs)
    a = generator(size)
    b = isIncorrect(a)
    if b:
        glass = False
    end
  end
  if glass:
      print("All arrays successfully sorted.")
  end
end

def generator(size)
  arr = (1..size).map { R.rand(1000) }

  return test.main(arr)
end

def isIncorrect(arr)
  
