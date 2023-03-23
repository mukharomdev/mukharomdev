# Class

class RubyClass
	def show
		print "hallo ini ruby class\n"
	end
end

rubyclass = RubyClass.new

print rubyclass.show()

=begin
# Self
penggunaan self sebagai variable
=end
class RubySelf
	def self.size
		return self + 1000
	end
end

rubyself = RubySelf.new
rubyself = 2

print rubyself.size() 