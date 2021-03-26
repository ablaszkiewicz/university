import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        int port = 6666;
        Server server = new Server(port);
        Thread serverThread = new Thread(server);
        serverThread.start();
        ArrayList<Thread> clientThreads = new ArrayList<Thread>();
        System.in.read();

        for(int i=0; i<1; i++) {
            Client client = new Client(port, "send" + i + ".txt");
            Thread clientThread = new Thread(client);
            clientThreads.add(clientThread);
            clientThread.start();
        }

        for(Thread thread : clientThreads) {
            thread.join();
        }
        System.out.println("Closed all client threads");
        server.close();
        serverThread.join();
    }
}
