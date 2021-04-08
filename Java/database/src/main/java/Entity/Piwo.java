package Entity;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

@Getter
@Setter
@EqualsAndHashCode
@Entity
@ToString
@NoArgsConstructor

public class Piwo {
    @Id
    private String name;

    private long cena;

    @ManyToOne
    private Browar browar;

    public Piwo(String name, long cena, Browar browar) {
        this.name = name;
        this.cena = cena;
        this.browar = browar;
    }
}
