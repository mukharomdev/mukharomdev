def my_function( a )
	puts "Hello, #{a}"
	return a.length
end


len = my_function( "Giraffe" )
puts "My secret word is #{len} long"