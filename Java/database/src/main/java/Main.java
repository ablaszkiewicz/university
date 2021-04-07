import Entity.Mage;
import Entity.Tower;
import Repository.MageRepository;
import Repository.TowerRepository;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("testPu");

        Tower akoTower = new Tower("Architektura komputerów", 666);
        Tower waiTower = new Tower("Wytwarzanie aplikacji internetowych", 123);

        Mage tomaszMage = new Mage("Tomasz Dziubich", 578, akoTower);
        Mage krystynaMage = new Mage("Krystyna Dziubich", 145, waiTower);

        TowerRepository towerRepository = new TowerRepository(emf, Tower.class);
        towerRepository.add(akoTower);
        towerRepository.add(waiTower);

        MageRepository mageRepository = new MageRepository(emf, Mage.class);
        mageRepository.add(tomaszMage);
        mageRepository.add(krystynaMage);

//        List<Tower> towers = towerRepository.findAll();
//        System.out.println(towers);
//
//        List<Mage> mages = mageRepository.findAll();
//        System.out.println(mages);

        List<Mage> magesInTower = mageRepository.getMagesFromTower(akoTower);
        System.out.println(magesInTower);
    }
}
