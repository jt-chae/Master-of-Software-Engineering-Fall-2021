import java.io.*;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
/* Write a program that will count the number of lines in each file that is specified on the command line.
Assume that the files are text files.
Note that multiple files can be specified, as in "java LineCounts file1.txt file2.txt file3.txt".
Write each file name, along with the number of lines in that file, to standard output.
If an error occurs while trying to read from one of the files,
you should print an error message for that file,
but you should still process all the remaining files.
https://blog.csdn.net/lalaxumelala/article/details/79532159
244P M4.2 FrequencyCount.java
*/

public class NumLines {
    private static void numLines(String file_name) {
        BufferedReader inputStream = null;
        try {
            inputStream = new BufferedReader(new FileReader(file_name));
        } catch(Exception e) {
            System.out.println(" cannot be open. Error. Please check the file name.");
            return;
        }
        int counter;
        counter = 0;
        try {
            String l = inputStream.readLine(); //readLine() returns a line of text with the line
            while (l != null) {
                counter++;
                l = inputStream.readLine(); //readLine() returns a line of text with the line
            }
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        System.out.println(" - number of lines: " + counter);
               return;
    }

    //take arguments as input strings from command prompt
    public static void main(String[] args) {
        if (args.length == 0){
            System.out.println("Please input a valid argument to the cmd prompt, such as 'file1.txt'");
            return;
        }
        for (int i = 0; i < args.length; i++){
            System.out.print(args[i]);
            numLines(args[i]);
        }
    }
}
