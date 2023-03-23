h = {"hash?" => "yep, it\‚s a hash!", "the answer to everything" =>
42, :linux => "fun for coders."}
puts "Stringy string McString!".class
puts 1.class
puts nil.class
puts h.class
puts :symbol.class

puts "---------------------------"


# CONSTANST(selalu memakai kapital)

NAMA = "yodharishang"
puts NAMA

puts "---------------------------"



# Symbols (diawali karakcter :nama_symbol )
# 
ketua = "bajak laut"
ketua2 = :ketua 


puts ketua
puts ketua.object_id
puts ketua2
puts ketua2.object_id

puts "---------------------------"


# HASH 


hash = { :rishang => "rishang makan bakso", :yodha => "yodha makan rendang", :luke => "benerin kabel"}

puts hash[:rishang]
puts hash[:yodha]
puts hash[:luke]

puts "-------------------------------"
puts __LINE__
puts __FILE__
puts __ENCODING__

puts $0