using System.Xml.Serialization;

namespace xml_serialization
{
    [XmlType("car")]
    public class Car
    {
        private string model;
        private int year;
        private Engine motor;

        public string Model
        {
            get => model;
            set => model = value;
        }

        public int Year
        {
            get => year;
            set => year = value;
        }

        [XmlElement(ElementName = "engine")]
        public Engine Motor
        {
            get => motor;
            set => motor = value;
        }

        public Car()
        {
            
        }

        public Car(string model, Engine motor, int year)
        {
            this.model = model;
            this.motor = motor;
            this.year = year;
        }
    }
}