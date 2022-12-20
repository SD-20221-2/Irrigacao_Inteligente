require "xmlrpc/client"

server = XMLRPC::Client.new("localhost", "/RPC2", 5000)
begin
    print "Qual o nome do funcionário? "
    nome = gets
    print "Qual o cargo do funcionário? "
    cargo = gets.chomp
    print "Qual o salário do funcionário? "
    salario = gets
    result = server.call("salarioReajustado", cargo, salario.to_f)
    puts result
rescue XMLRPC::FaultException => e
    puts "Error:"
    puts e.faultCode
    puts e.faultString
end