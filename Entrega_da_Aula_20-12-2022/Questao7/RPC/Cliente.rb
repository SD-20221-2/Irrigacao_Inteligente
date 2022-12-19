require "xmlrpc/client"

server = XMLRPC::Client.new("localhost", "/RPC2", 8000)
begin
  result = server.call("podeAposentar", 45, 30)
  puts result
rescue XMLRPC::FaultException => e
  puts "Error:"
  puts e.faultCode
  puts e.faultString
end