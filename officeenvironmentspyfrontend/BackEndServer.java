import java.io.*;
import java.net.*;

public class BackEndServer
{
    public static void main(String[] args) throws IOException, ClassNotFoundException
    {
	// Port number to bind server to.
	int portNum = 16192;

	// Socket for server to listen at.
	ServerSocket listener = new ServerSocket(portNum);

	while(true)
	    {
		try
		    {
			// Accept a client connection once Server recives one.
			Socket clientSocket = listener.accept();

			// Input and output streams. Output stream must be created first.
			ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
			ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());

			// Reading in Integer Object from input stream.
			int i = (Integer) in.readObject();

			// Sending response back to client
			String response = "Integer Object Received.";
			out.writeObject(response);

			// Outputting recived Integer Object.
			System.out.println("Received integer: " + i);
			out.close();
			in.close();
			clientSocket.close();
			break;
		    }
		finally
		    {		// Close server socket.
			listener.close();
		    }
	    }
    }
}
