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

			// Read in request (it should be a string.)
			String request = in.readObject();

			// Sending response back to client
			String response = "Request recived!";
			out.writeObject(response);

			// Outputting recived Integer Object.
			System.out.println("Received request: " + request);
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
}
