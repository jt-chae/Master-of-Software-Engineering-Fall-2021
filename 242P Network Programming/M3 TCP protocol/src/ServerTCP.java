import java.net.*;
import java.io.*;
import java.util.Scanner;

public class ServerTCP {
    static final int PORT_NUMBER = 6868;

/**
a,The command can be the string "index".
responds by sending a list of names of all the files that are available on the server.

b,the command can be of the form "get <file>".
checks whether the requested file actually exists.
   If so, sends the word "ok" Then the contents of the file and closes the connection.
   Otherwise, sends the word "error" to the client and closes the connection. */

    private static void getFile(File fileDirectory, Socket clientSocket) { //open a socket
        Scanner inputStream;//open input stream to the socket to read data
        PrintWriter outputStream;//open output steam to the socket to transmit data from server to client.
        String userInput = null;// input from command.
        try {
            inputStream = new Scanner(clientSocket.getInputStream());
            outputStream = new PrintWriter(clientSocket.getOutputStream());
            userInput = inputStream.nextLine(); //read from input and store in userInput
            if (userInput.equalsIgnoreCase("index")) { //The command can be the string "index". equalsIgnoreCase() compares two strings, ignoring lower case and upper case differences.
                sendIndex(fileDirectory, outputStream); //responds by sending a list of names of all the files that are available on the server.
            }
            else if (userInput.toLowerCase().startsWith("get")){ //the command can be of the form "get <file>".
                String fileName = userInput.substring(3).trim(); //get filename from command
                userInput = userInput.replace("\0", "");
                sendFile(fileName, fileDirectory, outputStream);
            }
            else {
                outputStream.println("Invalid input.");
                outputStream.flush(); //this is important to flush even though not needed yet
                //The flush() method breaks the deadlock by forcing the buffered stream to send its data
                //even if the buffer isn’t yet full.
            }
            System.out.println("ok. Connected to " + clientSocket.getInetAddress()
                    + " using command " + userInput);
        }
        catch (Exception e) {
            System.out.println("error at " + clientSocket.getInetAddress()
                    + " using command " + userInput + " " + e);
        }
        finally {
            try {
                clientSocket.close(); // closes the socket
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    //called by getFile() method in response to an "index" command
    private static void sendIndex(File fileDirectory, PrintWriter outStream) throws Exception {
        String[] filesList = fileDirectory.list();
        for (int i = 0; i < filesList.length; i++)
            outStream.println(filesList[i]);
        outStream.flush(); //if you don't flush, data maybe incomplete
        outStream.close(); //close output stream
        if (outStream.checkError())
            throw new Exception("Error while transmitting data.");
    }

    //called by getFile()
    private static void sendFile(String fileName, File fileDirectory, PrintWriter outStream)
            throws Exception {
        File file = new File(fileDirectory, fileName);
        if ( (! file.exists()) || file.isDirectory() ) { //If the file doesn't exist or not in a directory
            outStream.println("error"); //sends the word "error" to the client and closes the connection
        } //server checks whether the requested file actually exists
        else {
            outStream.println("ok"); //if the requested file actually exists, sends the message "ok"
            BufferedReader fileIn = new BufferedReader(new FileReader(file));
            while (true) {
                // Read and send lines from the file until an end-of-file is encountered.
                String line = fileIn.readLine();
                if (line == null)
                    break;
                outStream.println(line); //send the contents of the file.
            }
        }
        outStream.flush();
        outStream.close(); //close output stream
        if (outStream.checkError())
            throw new Exception("Error transmitting data.");
    }

    public static void main(String[] args) {
        File fileDirectory;        // directory of files
        ServerSocket serverSocket; // Listen for connection requests
        Socket clientSocket;     // create A socket variable for communicating with a client.

        if (args.length == 0) { // if command-line argument=0，print format
            System.out.println("Please use correct format of input: <directory>");
            return;
        }

        fileDirectory = new File(args[0]); //Get the directory name from the command line and make it a file object
        if ( ! fileDirectory.exists() ) {
            System.out.println("This directory does not exist.");
            return;
        }
        if (! fileDirectory.isDirectory() ) {
            System.out.println("This is not a directory.");
            return;
        }

        try {
            serverSocket = new ServerSocket(PORT_NUMBER); //Listen for connection requests from clients.
            System.out.println("Listening on port " + PORT_NUMBER);
            while (true) {
                clientSocket = serverSocket.accept(); //For each connection
                getFile(fileDirectory, clientSocket); //call method to process connections.
            }
        }
        catch (Exception e) {
            System.out.println("Unexpected Error");
            System.out.println("Error:  " + e);
        } // The server runs until the program is terminated, ex.CONTROL-C.
    }
} // end main()