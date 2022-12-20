require 'socket'

class Client
   def initialize(socket)
      @socket = socket
      @request_object = send_request
      @response_object = listen_response

      @request_object.join 
      @response_object.join 
   end

   def send_request
      begin
         Thread.new do
                @socket.puts "45 35" 
         end
      rescue IOError => e
         puts e.message
         @socket.close
      end

   end

   def listen_response
      begin
         Thread.new do
                resp = @socket.recvfrom( 1024 )
                puts resp
         end
      rescue IOError => e
         puts e.message
         # e.backtrace
         @socket.close
      end
   end
end



socket = TCPSocket.open( "localhost", 1531 )
a = 0

1.step(500,1) do |i| 
        Client.new( socket )
end