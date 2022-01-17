import java.net.*;
import java.io.*;

public class ClientTCP {
    static final int LISTENING_PORT = 3737;

    public static void main(String[] args) {
        String server;           // Name or IP address of server.
        Socket connection;       // Socket for communicating with server.
        PrintWriter outStream;   // Stream for sending a command to the server.
        BufferedReader inStream; // Stream for reading data from the connection.
        String command ;    // Command to send to the server.

        if (args.length == 0 || args.length > 2) {
            System.out.println("Usage:  java FileClient <server>");
            System.out.println("    or  java FileClient <server> <file>");
            return;
        }

            server = args[0];     // Get the server name
        if (args.length == 1)
            command = "INDEX";
        else
            command = "GET " + args[1];
        try{
            connection = new Socket(server, LISTENING_PORT); //open Socket
            inStream = new BufferedReader(new InputStreamReader(connection.getInputStream())); //buffer read inStream from connection
            outStream = new PrintWriter(connection.getOutputStream()); //write outStream
            outStream.println(command);
            outStream.flush(); // ESSENTIAL: Make sure command is dispatched to server!
        }catch(Exception e){
            System.out.println("Can't make connection to server at \"" + args[0] + "\".");
            System.out.println("Error:  " + e);
            return;
        }

        /* Read and process the server's response to the command. */
        try {
            if (args.length == 1) {
                // The command was "index".  Read and display lines
                // from the server until the end-of-stream is reached.
                System.out.println("File list from server:");
                while (true) {
                    String line = inStream.readLine();
                    if (line == null)
                        break;
                    System.out.println("   " + line);
                }
            }
            else { // The command was "get <file-name>".  Read the server's response message.
                // If the message is "OK", get the file.
                String message = inStream.readLine();
                if (! message.equalsIgnoreCase("OK")) {
                    System.out.println("File not found on server.");
                    System.out.println("Message from server: " + message);
                    return;
                }
                PrintWriter fileOut;  // For writing the received data to a file.
                File file = new File(args[1]); // Use second parameter as a file name.
                if (file.exists()) { // reminder if exists.
                    System.out.println("A file with that name already exists.");
                    return;
                }
                fileOut = new PrintWriter( new FileWriter(args[1]) );

                while (true) { // Copy lines from incoming to the file until
                    // the end of the incoming stream is encountered.
                    String line = inStream.readLine(); // Copy lines from incoming to the file
                    if (line == null) // until inStream ends.
                        break;
                    fileOut.println(line);
                }
                if (fileOut.checkError()) {
                    System.out.println("Some error occurred while writing the file.");
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
                connection.close();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }  // end main()
}
