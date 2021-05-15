using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Linq;
using System.Xml.XPath;

namespace xml_serialization
{
    class Program
    {
        static List<Car> myCars = new List<Car>(){
            new Car("E250", new Engine(1.8, 204, "CGI"), 2009),
            new Car("E350", new Engine(3.5, 292, "CGI"), 2009),
            new Car("A6", new Engine(2.5, 187, "FSI"), 2012),
            new Car("A6", new Engine(2.8, 220, "FSI"), 2012),
            new Car("A6", new Engine(3.0, 295, "TFSI"), 2012),
            new Car("A6", new Engine(2.0, 175, "TDI"), 2011),
            new Car("A6", new Engine(3.0, 309, "TDI"), 2011),
            new Car("S6", new Engine(4.0, 414, "TFSI"), 2012),
            new Car("S8", new Engine(4.0, 513, "TFSI"), 2012)
        };
        
        static void Main(string[] args)
        {
            FindCarsOfModel("A6");
            SerializeAndDeserialize();
            XPathStatement();
            LinqSerialization();
            ModifyCarsCollection();
        }

        static void FindCarsOfModel(string searchedModel)
        {
            var anonymousCarQuery = myCars
                .Where(car => car.Model == searchedModel)
                .Select(car =>
                    new
                    {
                        engineType = car.Motor.Model == "TDI" ? "diesel" : "petrol",
                        hppl = car.Motor.HorsePower / car.Motor.Displacement,
                    });
            Console.Write("A6 cars:");
            foreach (var car in anonymousCarQuery)
            {
                Console.WriteLine(car.ToString());
            }
            Console.WriteLine("\nAverage hppl for types of engine:");
            var groupedQuery = anonymousCarQuery
                .GroupBy(car => car.engineType)
                .Select(car => $"{car.First().engineType}: {car.Average(subCar => subCar.hppl)}");
            foreach (var record in groupedQuery)
            {
                Console.WriteLine(record);
            }
            Console.WriteLine();
        }
        
        static void SerializeAndDeserialize()
        {
            CustomSerializer.SerializeToXML(myCars, "CarsCollection.xml");
            List<Car> cars = CustomSerializer.DeserializeFromXML("CarsCollection.xml");

            Console.WriteLine("\nCars from deserialized list:");
            foreach (var car in cars)
            {
                Console.WriteLine($"{car.Model}");
            }
            Console.WriteLine();
        }

        static void XPathStatement()
        {
            XElement rootNode = XElement.Load("CarsCollection.xml");
            var countAverageXPath = "sum(//car/engine[@Model!=\"TDI\"]/HorsePower) div count(//car/engine[@Model!=\"TDI\"]/HorsePower)";
            Console.WriteLine($"Średnia: {(double)rootNode.XPathEvaluate(countAverageXPath)}");

            var removeDuplicatesXPath = "//car[following-sibling::car/Model=Model]";
            IEnumerable<XElement> models = rootNode.XPathSelectElements(removeDuplicatesXPath);

            var fileName = "CarsCollectionNoDuplicates.xml";
            var currentDirectory = Directory.GetCurrentDirectory();
            var filePath = Path.Combine(currentDirectory, fileName);
            using (var writer = new StreamWriter(filePath))
            {
                foreach(var model in models)
                {
                    writer.WriteLine(model);   
                }
            }
        }
        
        static void LinqSerialization()
        {
            IEnumerable<XElement> nodes = myCars
                .Select(n =>
                    new XElement("car",
                        new XElement("model", n.Model),
                        new XElement("engine",
                            new XAttribute("model", n.Motor.Model),
                            new XElement("displacement", n.Motor.Displacement),
                            new XElement("horsePower", n.Motor.HorsePower)),
                        new XElement("year", n.Year)));
            XElement rootNode = new XElement("cars", nodes);
            rootNode.Save("CarsCollectionLinq.xml");
        }
        
        static void ModifyCarsCollection()
        {
            XElement template = XElement.Load("CarsCollection.xml");
            foreach(var car in template.Elements())
            {
                foreach(var carField in car.Elements())
                {
                    if(carField.Name == "engine")
                    {
                        foreach(var engineField in carField.Elements())
                        {
                            if(engineField.Name == "horsePower")
                            {
                                engineField.Name = "hp";
                            }
                        }
                    }
                    else if (carField.Name == "Model")
                    {
                        var yearField = car.Element("Year");
                        XAttribute attribute = new XAttribute("year", yearField.Value);
                        carField.Add(attribute);
                        yearField.Remove();
                    }
                }
            }
            template.Save("CarsCollectionModified.xml");
        }
    }
}