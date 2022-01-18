package SimpleThreads;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Vector;

public class SimpleThreads {
    // Function to print out a message with the name of the current thread
    static void threadMessage(String message) {
        String threadName = Thread.currentThread().getName(); //these are built-in in Java
        System.out.format("%s: %s%n", //set the format of outputs
                threadName, //variable name of thread
                message); //variable message output
    }

    private static class MessageLoop implements Runnable { // indicates this class is a thread when you use Runnable
        public void run() { //this thread prints out Hello World
            threadMessage("Message thread starting"); //call the function threadMessage from line 9
            try {
                while (true) {
                    // Pause for 4 seconds
                    Thread.sleep(2000);
                    // Print a message
                    threadMessage("Hello world");
                }
            } catch (InterruptedException e) {
                threadMessage("Thread exiting");
            }
        }
    }

    private static class MainThread implements Runnable {
        //this vector list is to keep track of all the threads that we run
        //because we are running multiple threads at once
        public List<Thread> messageThreads = new Vector<Thread>();

        public void createMessageThread() {
            Thread t = new Thread(new MessageLoop()); //create a new thread with a message with thread to print "hello w
            messageThreads.add(t); //add this thread to the vector list to keep track
            t.start(); //start the thread to get it running
        }

        public void endThread(Thread t) //this is a function to end a thread
            throws InterruptedException{ //indicates that this thread can be interrupted while running
            t.interrupt(); //interrupt is a built-in function
            t.join(); //wait for the thread to finish/end
        }

        public void run(){ //this function is the main function that takes inputs from users
            threadMessage("Main thread starting");

            createMessageThread();

            Scanner reader = new Scanner(System.in);  // Reading from System.in

            try {
                boolean threadsAreAlive = true; //keep track of weather all the threads are still alive
                while (threadsAreAlive) {
                    threadMessage("Enter an option: ");
                    threadMessage("a: Create a new message thread");
                    threadMessage("b: Stop a given thread (e.g. \"b 2\" kills thread 2)");
                    threadMessage("c: Stop all threads and exit this program");
                    String s = reader.nextLine(); //create a variable to store the input read from user
                    if (s.length() <= 0) { //if there is no input, continue
                        continue;
                    }
                    Character c = s.charAt(0); //create a character variable from the input string

                    if (c == 'a') {
                        threadMessage("Creating new message thread");
                        createMessageThread();
                    }
                    if (c == 'b') {
                        threadMessage("Choose a thread to end");
                        //choose a number from 0 to the end of the vector list of threads we created above
                        threadMessage("Enter a number from 0 to " + (messageThreads.size() - 1));
                        //get the input from the user on which thread to kill
                        Integer i = reader.nextInt();
                        //Let the user know which thread is being killed
                        threadMessage("Ending thread " + i);
                        endThread(messageThreads.get(i)); //call the function endThread to kill the thread
                        messageThreads.remove(i); //remove i from our vector list of thread above
                    }
                    if (c == 'c') {
                        threadMessage("Ending all threads");
                        for (int i = 0; i < messageThreads.size(); i++) {
                            endThread(messageThreads.get(i)); //immediately quits b/c no threads are left
                        }
                    }

                    threadsAreAlive = false; //quits all threads
                    //check if any threads are alive still, if not, the loop will end
                    for (int i = 0; i < messageThreads.size(); i++) {
                        if (messageThreads.get(i).isAlive()) {
                            threadsAreAlive = true;
                        }
                    }
                }
                threadMessage("All threads ended - exiting");
            } catch (InterruptedException e) {
                threadMessage("Thread interrupted - exiting");
            }

            reader.close(); //object that we used to get the input from the user
        }
    }

    public static void main(String args[]) //the main function of this entire that starts main thread
            throws InterruptedException {
        Thread t = new Thread(new MainThread());
        t.start(); //start main thread
    }
}
// Reference: https://docs.oracle.com/javase/tutorial/essential/concurrency/simple.html