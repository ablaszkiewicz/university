using System.Xml.Serialization;

namespace xml_serialization
{
    [XmlRoot(ElementName = "engine")]
    public class Engine
    {
        private double displacement;
        private double horsePower;
        [XmlAttribute]
        private string model;

        [XmlAttribute]
        public string Model
        {
            get => model;
            set => model = value;
        }

        public double HorsePower
        {
            get => horsePower;
            set => horsePower = value;
        }

        public double Displacement
        {
            get => displacement;
            set => displacement = value;
        }

        public Engine()
        {
            
        }

        public Engine(double displacement, double horsePower, string model)
        {
            this.displacement = displacement;
            this.horsePower = horsePower;
            this.model = model;
        }
    }
}