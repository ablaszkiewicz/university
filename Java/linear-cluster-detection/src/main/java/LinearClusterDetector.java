public interface LinearClusterDetector {
    void accept(double number);

    int clusterCount();

    void print();
}