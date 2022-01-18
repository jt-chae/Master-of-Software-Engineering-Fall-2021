import java.util.Vector;
import java.util.concurrent.ArrayBlockingQueue;

public class MessageQueue {
    private static int n_ids;

    public static void main(String[] args) {
        int M_producers = 0;
        int N_consumers = 0;
        try {
            M_producers = Integer.parseInt(args[0]);
            N_consumers = Integer.parseInt(args[1]);
        } catch (Exception e) {
            System.err.println("Incorrect input");
            System.exit(1);
        }
        //Create vectors of producers and consumers lists
        Vector<Producer> Producers_list = new Vector<>();
        Vector<Consumer> Consumers_list = new Vector<>();
        ArrayBlockingQueue queue = new ArrayBlockingQueue(10);
        for (int i = 0; i < M_producers; i++) {
            Producer p1 = new Producer(queue, n_ids++);
            Producers_list.add(p1);
            new Thread(p1).start();
        }
        for (int i = 0; i < N_consumers; i++) {
            Consumer p1 = new Consumer(queue, n_ids++);
            Consumers_list.add(p1);
            new Thread(p1).start();
        }


//	ArrayBlockingQueue queue = new ArrayBlockingQueue(10);
//	Producer p1 = new Producer(queue, n_ids++);
//	//Change the main method so that two producer threads are created
//	Producer p2= new Producer(queue, n_ids++);
//	Consumer c1 = new Consumer(queue, n_ids++);
//	//Change the main method so that two consumer threads are created
//	Consumer c2 = new Consumer(queue, n_ids++);


//	new Thread(p1).start();
//	//Change the main method so that two producer threads are created
//	new Thread(p2).start();
//	new Thread(c1).start();
//	//Change the main method so that two consumer threads are created
//	new Thread(c2).start();

            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            for (int i = 0; i < M_producers; i++) {
                Producer p1 = Producers_list.get(i);
                p1.stop();
            }
//	p1.stop();
//	// tell thread 2 to stop
//	p2.stop();
        }
    }
