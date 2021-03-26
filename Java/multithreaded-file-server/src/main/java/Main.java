import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        int port = 6666;
        Thread serverThread = new Thread(new Server(port));
        serverThread.start();

        System.in.read();

        for(int i=0; i<1; i++) {
            Client client = new Client(port, "send" + i + ".txt");
            Thread clientThread = new Thread(client);
            clientThread.start();
        }
    }
}
