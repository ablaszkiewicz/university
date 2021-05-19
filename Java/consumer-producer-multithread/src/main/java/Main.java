public class Main {
    public static void main(String[] args) throws InterruptedException {
        Warehouse warehouse = new Warehouse();

        Thread producerThread = new Thread(new Producer(warehouse));
        producerThread.start();
        Thread consumerThread = new Thread(new Consumer(warehouse));
        consumerThread.start();

        producerThread.join();
        consumerThread.join();
    }
}
