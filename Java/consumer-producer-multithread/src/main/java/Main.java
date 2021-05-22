import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Warehouse warehouse = new Warehouse();

        ArrayList<Thread> producerThreads = new ArrayList<Thread>();
        producerThreads.add(new Thread(new Producer(warehouse)));
        producerThreads.add(new Thread(new Producer(warehouse)));
        producerThreads.add(new Thread(new Producer(warehouse)));
        producerThreads.add(new Thread(new Producer(warehouse)));
        producerThreads.add(new Thread(new Producer(warehouse)));
        producerThreads.add(new Thread(new Producer(warehouse)));

        ArrayList<Thread> consumerThreads = new ArrayList<Thread>();
        consumerThreads.add(new Thread(new Consumer(warehouse)));
//        consumerThreads.add(new Thread(new Consumer(warehouse)));
//        consumerThreads.add(new Thread(new Consumer(warehouse)));
//        consumerThreads.add(new Thread(new Consumer(warehouse)));
//        consumerThreads.add(new Thread(new Consumer(warehouse)));
//        consumerThreads.add(new Thread(new Consumer(warehouse)));

        for(Thread thread : producerThreads) {
            thread.start();
        }

        for(Thread thread : consumerThreads) {
            thread.start();
        }

        for(Thread thread : producerThreads) {
            thread.join();
        }

        for(Thread thread : consumerThreads) {
            thread.join();
        }
    }
}
