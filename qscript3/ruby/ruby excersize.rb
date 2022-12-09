#which accept the radius of a circle from the user and compute the parameter and area
=begin
def areafunc
	radius=gets.to_f
	area=(22/7.to_f)*radius*radius
	parameter=2*(22/7.to_f)*radius
	puts 'area='+(area.to_s) +'and parameter=' +(parameter.to_s)
end
areafunc

# Write a Ruby program to check whether a string starts with "if"
def checkfunc
	string=gets.to_s	
	a=((string[0,2]))
	if a=='if'
		puts 'true'
		puts a
	else
		puts 'false'
		puts a
	end

end
checkfunc


#Write a program which accept the user's first and last name and print them in reverse order 
#with a space between them

def reverse_func
	print 'enter your first name'
	first_name=gets.chomp.to_s
	print 'enter your second name'
	last_name=gets.chomp.to_s
	puts "hello #{last_name} #{first_name}"
	
end
reverse_func


#Write a Ruby program to accept a filename from the user print the extension of that.

def filename
file = "/user/system/test.rb"
# file name
fbname = File.basename(file)  
puts "File name: "+fbname 
# basename
bname = File.basename(file),'.rb'
puts "Base name: "+bname 
# file extention
ffextn = File.extname(file)
puts "Extention: "+ffextn 
# path name
path_name= File.dirname(file) 
puts "Path name: "+path_name

end
filename



# print the following 'here document'.
subject='Sample string :
a string that you "don\'t" have to escape
This
is a ....... multi-line
heredoc string --------> example'

puts subject

puts(
<<-eos
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
eos
)


#Write a Ruby program to create a new string where "if" is added to the front of a given string. 
#If the string already begins with "if", return the string unchanged.
def string_check
string=gets.to_s
if string[0,2]=='if'
	return string
else
	add='if'
	string.insert(0,add)
	print string
end
end

string_check
=end




