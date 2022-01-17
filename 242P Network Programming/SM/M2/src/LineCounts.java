import java.io.*;
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

public class LineCounts {
    private static void countLines(String fileName) {
        BufferedReader streamIn;  //stream reader from files
//        int lineCount = 0;        //line counter
        try { //textbook p37 Filters are connected to streams by their constructors
            streamIn = new BufferedReader(new FileReader(fileName));
        }catch(Exception e) {
            System.out.println("Can't open files.");
            return;
        }
        int lineCount = 0;
        try {
            String line = streamIn.readLine(); //Read the first line.
            while (line != null) {
                lineCount++;
                line = streamIn.readLine(); //Read the next line.
            }
        }catch (IOException e) {
            e.printStackTrace();
            return;
        }
        System.out.println(" has " + lineCount + " lines. ");
               return;
    }

    //get file names from command line and process each
    public static void main(String[] args) {
        if (args.length == 0){
            System.out.println("Command format: java LineCounts.java *.txt");
            return;
        }
        for (int i = 0; i < args.length; i++){
            System.out.print(args[i]);
            countLines(args[i]);
        }
    }
}
