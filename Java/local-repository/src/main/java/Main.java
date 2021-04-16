public class Main {
    public static void main(String[] args) {
        PiwoRepository piwoRepository = new PiwoRepository();
        PiwoController piwoController = new PiwoController(piwoRepository);

        try {

            System.out.println(piwoController.insert("Marek", 12));
            System.out.println(piwoController.insert("Marek", 12));

            System.out.println(piwoController.find("Marek"));
            System.out.println(piwoController.find("Marcin"));

            System.out.println(piwoController.delete("Marek"));
            System.out.println(piwoController.delete("Marcin"));

        } catch (IllegalArgumentException ex) {
            ex.printStackTrace();
        }
    }
}