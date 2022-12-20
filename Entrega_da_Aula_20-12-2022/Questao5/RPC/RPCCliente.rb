require "xmlrpc/client"

server = XMLRPC::Client.new("localhost","/RPC2",8050)

begin
	print "Digite a idade:"
	data = gets
	
	result = server.call("categoria", data.to_i)
	puts result
	
rescue XMLRPC::FaultException => e
	puts "Error:"
	puts e.faultCode
	puts e.faultString

end
