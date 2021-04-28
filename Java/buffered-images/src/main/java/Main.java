public class Main {
    public static void main(String[] args) {

        for(int i=0; i <= 16; i+= 4) {
            long time = System.currentTimeMillis();
            ImageLoader imageLoader = new ImageLoader(args[0], args[1], i == 0 ? 1 : i);
            imageLoader.execute();
            System.out.println("Execution time for " + (i == 0 ? 1 : i) + " threads is " + (System.currentTimeMillis() - time) + " ms");
        }
    }
}
