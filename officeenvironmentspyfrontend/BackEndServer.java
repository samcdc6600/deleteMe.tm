import java.io.*;
import java.net.*;

public class BackEndServer
{
    public static void main(String[] args) throws IOException, ClassNotFoundException
    {
	// Port number to bind server to.
	final int portNum = 8192;

	while(true)
	    {
		// Socket for server to listen at.
		ServerSocket listener = new ServerSocket(portNum);
		try
		    {
			// Accept a client connection once Server recives one.
			Socket clientSocket = listener.accept();

			// Input and output streams. Output stream must be created first.
			ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
			ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());

			// Read in and handle request (it should be a string.)
			String response = handleRequest((String)in.readObject());
			// Sending response back to client
			out.writeObject(response);

			out.close();
			in.close();
			clientSocket.close();
		    }
		finally
		    {		// Close server socket.
			listener.close();
		    }
	    }
    }

    private static String handleRequest(final String request)
    {
	System.out.println(request);
	switch(request)
	    {
	    case "get office stats":
		return new String("these are the stats");
	    default:
		return new String("Error: request not valid");
	    }
    }
}
