# do
# 	print "I like "
# 	print "code blocks!"
# end

# {
# 	print "Me too!"
# }

# using yield

def simpleFunction
yield
yield
end

simpleFunction { puts "Hello!" }


# using yield

def animals
yield "Tiger"
yield "Giraffe"
end

animals { |x| puts "Hello, #{x}"} 
animals { |x| puts "It's #{x.length} characters long!" }