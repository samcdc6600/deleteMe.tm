import java.io.*;
import java.net.*;


public class FrontEndClient
{
    public static void main(String arg[]) throws IOException, ClassNotFoundException
    {
	int portNum = 8192;

	Socket socket = new Socket("ec2-52-90-192-10.compute-1.amazonaws.com", portNum);

	// Integer Object to send to Server.
	Integer num = 50;

	ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
	ObjectInputStream in = new ObjectInputStream(socket.getInputStream());

	out.writeObject(num);

	String response = (String) in.readObject();

	System.out.println("Server message: " + response);
    }
}
