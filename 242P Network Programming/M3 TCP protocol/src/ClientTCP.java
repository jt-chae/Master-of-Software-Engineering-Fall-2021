import java.net.*;
import java.io.*;

public class ClientTCP {
    static final int PORT_NUMBER = 6868;

    public static void main(String[] args) {
        String hostName = args[0];     //"localhost" - Name or IP address of server.
        Socket networkSocket;       // Socket for communicating with server.
        PrintWriter out;   // Stream for sending a command to the server.
        BufferedReader in; // Stream for reading data from the client connection.
        String userInput ;    // Command to send to the server.

        if (args.length == 0 || args.length > 2) {
            System.out.println("Please use correct format of input.");
            System.out.println("To get a a list of names of all the files, enter <server>.");
            System.out.println("To get a file from the server, enter <server> <file>.");
            return;
        }

        if (args.length == 1)
            userInput = "index"; //if we don't pass in an argument, set the command to "index" automatically
        else
            userInput = "get " + args[1];
        try{
            networkSocket = new Socket(hostName, PORT_NUMBER); //open Socket
            in = new BufferedReader(new InputStreamReader(networkSocket.getInputStream())); //buffer read inStream from connection
            //in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(networkSocket.getOutputStream()); //write outStream
            out.println(userInput);
            out.flush(); // Make sure user input command is dispatched to server, flush even when not needed
        }catch(Exception e){
            System.out.println("Unable to make connection to server at \"" + args[0] + "\".");
            System.out.println("Error:  " + e);
            return;
        }

        /* Read and process the server's response to the command. */
        try {
            if (args.length == 1) {
                // The command here is "index". Read and display file names from the server until the end-of-stream is reached.
                System.out.println("List of files from server:");
                while (true) {
                    String line = in.readLine();
                    if (line == null)
                        break;
                    System.out.println("   " + line);
                }
            }
            else { // The command was "get <file-name>".  Read the server's response message.
                // If the message is "OK", get the file.
                String message = in.readLine();
                if (! message.equalsIgnoreCase("OK")) {
                    System.out.println("File not found on server.");
                    System.out.println("Message from server: " + message);
                    return;
                }
                PrintWriter fileOut;  // For writing the received data to a file.
                File file = new File(args[1]); // Use second parameter as a file name.
                if (file.exists()) { // reminder if exists.
                    System.out.println("File already exists in this directory. Please try a different file name.");
                    return;
                }
                fileOut = new PrintWriter(new FileWriter(args[1]) );

                while (true) { // Copy lines from incoming to the file until
                    // the end of the incoming stream is encountered.
                    String line = in.readLine(); // Copy lines from incoming to the file
                    if (line == null) // until inStream ends.
                        break;
                    fileOut.println(line);
                }
                if (fileOut.checkError()) {
                    System.out.println("An error occurred while writing the file.");
                    System.out.println("Output file might be empty or incomplete.");
                }
            }
        } catch (Exception e) {
            System.out.println(
                    "An error occurred while reading data from the server.");
            System.out.println("Error: " + e);
        }
        finally {
            try {
                networkSocket.close(); //close the socket
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
// reference used: https://docs.oracle.com/javase/tutorial/networking/sockets/readingWriting.html