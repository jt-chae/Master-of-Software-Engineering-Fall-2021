import java.net.*;
import java.io.*;
import java.util.Scanner;

//textbook page285 ex.9.4
//https://stackoverflow.com/questions/890966/what-is-string-args-parameter-in-main-method-java
public class ServerTCP {
    static final int LISTENING_PORT = 3737; //0-1023-49151-65535

/**
a,The command can be the string "index".
responds by sending a list of names of all the files that are available on the server.

b,the command can be of the form "get <file>".
checks whether the requested file actually exists.
   If so, sends the word "ok" Then the contents of the file and closes the connection.
   Otherwise, sends the word "error" to the client and closes the connection. */

    private static void getFile(File directory, Socket connection) {
        Scanner inStream;                                     // reading data from the client.
        PrintWriter outStream;                                // transmitting data to the client.
        String command = "Ready for getting command";         // input from command.
        try {
            inStream = new Scanner( connection.getInputStream() );
            outStream = new PrintWriter( connection.getOutputStream() );
            command = inStream.nextLine();
            if (command.equalsIgnoreCase("index")) { //The command can be the string "index".
                sendIndex(directory, outStream); //responds by sending a list of names of all the files that are available on the server.
            }
            else if (command.toLowerCase().startsWith("get")){ //the command can be of the form "get <file>".
                String fileName = command.substring(3).trim(); //get filename from command
                sendFile(fileName, directory, outStream);
            }
            else {
                outStream.println("Input is not valid.");
                outStream.flush();
            }
            System.out.println("OK    " + connection.getInetAddress()
                    + " " + command);
        }
        catch (Exception e) {
            System.out.println("ERROR " + connection.getInetAddress()
                    + " " + command + " " + e);
        }
        finally {
            try {
                connection.close(); // closes the connection.
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    //called by getFile() method in response to an "INDEX" command
    private static void sendIndex(File directory, PrintWriter outStream) throws Exception {
        String[] fileList = directory.list();
        for (int i = 0; i < fileList.length; i++)
            outStream.println(fileList[i]);
        outStream.flush();
        outStream.close();
        if (outStream.checkError())
            throw new Exception("Error while transmitting data.");
    }

    //called by getFile() command in response to "GET <fileName>"
    private static void sendFile(String fileName, File directory, PrintWriter outStream)
            throws Exception {
        File file = new File(directory,fileName);
        if ( (! file.exists()) || file.isDirectory() ) { //If the file doesn't exist or a directory
            outStream.println("ERROR"); //send the message "ERROR".
        }
        else {
            outStream.println("OK"); //Otherwise, send the message "OK"
            BufferedReader fileIn = new BufferedReader( new FileReader(file) );
            while (true) {
                // Read and send lines from the file until an end-of-file is encountered.
                String line = fileIn.readLine();
                if (line == null)
                    break;
                outStream.println(line); //send the contents of the file.
            }
        }
        outStream.flush();
        outStream.close();
        if (outStream.checkError())
            throw new Exception("Error while transmitting data.");
    }

    public static void main(String[] args) {
        File directory;        // directory of files
        ServerSocket listener; // Listen for connection requests
        Socket connection;     // A socket for communicating with a client.

        if (args.length == 0) { // if command-line argument=0，print format
            System.out.println("Format:  java ServerTCP.java <directory>");
            return;
        }

        directory = new File(args[0]); //Get the directory name from the command line and make it a file object
        if ( ! directory.exists() ) {
            System.out.println("This directory does not exist.");
            return;
        }
        if (! directory.isDirectory() ) {
            System.out.println("This file is not a directory.");
            return;
        }

        try {
            listener = new ServerSocket(LISTENING_PORT); //Listen for connection requests from clients.
            System.out.println("Listening on port " + LISTENING_PORT);
            while (true) {
                connection = listener.accept(); //For each connection
                getFile(directory,connection); //call method to process connections.
            }
        }
        catch (Exception e) {
            System.out.println("Server shut down unexpectedly.");
            System.out.println("Error:  " + e);
        } // The server runs until the program is terminated, ex.CONTROL-C.
    }
} // end main()