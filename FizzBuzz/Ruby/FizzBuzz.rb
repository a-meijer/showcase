File.open("output.txt", "w")

for num in 1..100
    case
    when num % 3 == 0 then File.write("output.txt", "Fizz", mode: "a")
    when num % 5 == 0 then File.write("output.txt", "Buzz", mode: "a")
    when num % 15 == 0 then File.write("output.txt", "FizzBuzz", mode: "a")
    else File.write("output.txt", num, mode: "a")
    end
end