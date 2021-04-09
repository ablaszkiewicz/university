public class Main {
    public static void main(String[] args) {
        MyLinearClusterDetectorFactory factory = new MyLinearClusterDetectorFactory();
        LinearClusterDetector detector = factory.create(0.1);

//        detector.accept(100);
//        detector.accept(0);
//        detector.accept(7);
//        detector.accept(-89);
//        detector.accept(80);
//        detector.accept(86);
//        detector.accept(-100);
//        detector.accept(2);
//        detector.accept(81);

        int size = 1000000;

        for(int i=0; i < size; i++) {
            detector.accept(i);
        }

        for(int i=0; i < 10; i++) {
            detector.accept(Math.floor(Math.random() * size) + Math.random() * 0.1);
        }

        System.out.println(detector.clusterCount());
    }
}
