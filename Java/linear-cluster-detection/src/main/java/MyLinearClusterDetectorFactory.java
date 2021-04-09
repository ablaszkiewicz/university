import java.util.ArrayList;

public class MyLinearClusterDetectorFactory implements LinearClusterDetectorFactory {
    int c = 0;
    double p = Double.NEGATIVE_INFINITY;

    @Override
    public LinearClusterDetector create(double spacing) {
        if(spacing <= 0) {
            throw new IllegalArgumentException("Invalid spacing!");
        }
        return new LinearClusterDetector() {
            private ArrayList<Tuple> intervals = new ArrayList<Tuple>();
            @Override
            public void accept(double number) {
                //System.out.println("\ngot number: " + number);
                int start = 0;
                int end = this.intervals.size() - 1;

                int middle = 0;

                while(start <= end) {
                    middle = (int) Math.floor((start + end) / 2);
                    //System.out.println("Current middle index: " + middle + ". Middle value: " + intervals.get(middle).GetMin() + " " + intervals.get(middle).GetMax());

                    // value is inside an interval
                    if (number <= intervals.get(middle).getMax() && number >= intervals.get(middle).getMin()) {
                        //System.out.println("inside an interval");
                        return;
                    }

                    // is on right of max
                    if (number > intervals.get(middle).getMax() && Math.abs(number - intervals.get(middle).getMax()) <= spacing) {
                        //System.out.println("on the right");
                        intervals.get(middle).setMax(number);

                        // overlapped with interval on right
                        if (middle + 1 < intervals.size() && intervals.get(middle).getMax() >= intervals.get(middle + 1).getMin() - spacing) {
                            intervals.get(middle).setMax(intervals.get(middle + 1).getMax());
                            intervals.remove(middle + 1);
                        }

                        return;
                    }

                    // is on left of min
                    if (number < intervals.get(middle).getMin() && Math.abs(number - intervals.get(middle).getMin()) <= spacing) {
                        //System.out.println("on the left");
                        intervals.get(middle).setMin(number);

                        // overlapped with interval on left
                        if (middle - 1 > 0 && intervals.get(middle).getMin() -spacing <= intervals.get(middle -1).getMax()) {
                            intervals.get(middle).setMin(intervals.get(middle - 1).getMax());
                            intervals.remove(middle - 1);
                        }

                        return;
                    }

                    if (number > intervals.get(middle).getMax()) {
                        start = middle + 1;
                    } else {
                        end = middle - 1;
                    }
                }
                    //System.out.println("Creating new tuple...");
                    intervals.add(start, new Tuple(number, number));
            }

            @Override
            public int clusterCount() {
                return intervals.size();
            }

            @Override
            public void print() {
                for(Tuple tuple : intervals) {
                    System.out.println(tuple.getMin() + " " + tuple.getMax());
                }
            }
        };
    }
}