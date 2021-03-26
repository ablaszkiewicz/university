import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server implements Runnable {
    private int port;
    private int id;
    public Server(int port) {
        System.out.println("Created server on port: " + port);
        this.port = port;
    }
    @Override
    public void run() {
        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("Started server on port: " + port);
            while(!Thread.interrupted()) {
                try {
                    Socket socket = server.accept();
                    System.out.println("Someone connected");
                    Thread clientThread = new Thread(new ClientHandler(socket, "receive" + id + ".txt"));
                    id++;
                    clientThread.start();
                } catch (IOException ex) {
                    System.err.println(ex);
                }
            }
        } catch (IOException ex) {
            System.err.println(ex);
        }
    }
}
