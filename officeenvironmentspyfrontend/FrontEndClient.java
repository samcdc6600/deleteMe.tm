import java.io.*;
import java.net.*;


public class FrontEndClient
{
    public static void main(String args[]) throws IOException, ClassNotFoundException
    {
	if(args.length != 0)
	    {			// We have been given a message to send. Now construct it!
		String msg = new String("");
		for(String msgComp: args)
		    msg += msgComp + " ";


		final int portNum = 8192; // Open socket.
		Socket socket = new Socket("ec2-52-90-192-10.compute-1.amazonaws.com", portNum);
		// Create input and output streams for socket. Output must be created first.
		ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
		ObjectInputStream in = new ObjectInputStream(socket.getInputStream());

		out.writeObject(msg); // Send our message out over the wire (maybe we'll get tapped by a vampire.)
		// Get reply
		String response = (String) in.readObject();
		// Output reply
		final String rWDir = new String("/tmp/");
		final String responseFileName = new String(rWDir + "serverData.csv");
		writeFile(responseFileName, response);
		System.out.println("cats");
	    }
	else
	    {
		System.err.println("Error: 0 arguments given but at least 1 required!");
	    }
    }

    public static void writeFile(final String fileName, final String data)
    {
	try
	    {
		FileWriter fileObject = new FileWriter(fileName);
		fileObject.write(data);
		fileObject.close();
	    }
	catch(IOException e)
	    {
		System.out.println("Recived exception: " + e);
		e.printStackTrace();
	    }
    }
}
