import Entity.Piwo;
import Entity.Browar;
import Repository.PiwoRepository;
import Repository.BrowarRepository;

import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("testPu");

        Browar kasztelanski = new Browar("Browar kasztelanski", 666);
        Browar specjalny = new Browar("Browar Specjalny", 123);

        Piwo kasztelan = new Piwo("kasztelan", 2, kasztelanski);
        Piwo specjal = new Piwo("specjal", 4, specjalny);

        BrowarRepository browarRepository = new BrowarRepository(emf, Browar.class);
        browarRepository.add(kasztelanski);
        browarRepository.add(specjalny);

        PiwoRepository piwoRepository = new PiwoRepository(emf, Piwo.class);
        piwoRepository.add(kasztelan);
        piwoRepository.add(specjal);

        System.out.println(piwoRepository.findAll());
        System.out.println(browarRepository.findAll());
        System.out.println(browarRepository.getBrowarsWithBeerCheaperThan(3));
    }
}
