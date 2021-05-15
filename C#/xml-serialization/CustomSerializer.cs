using System;
using System.Collections.Generic;
using System.IO;
using System.Xml.Serialization;

namespace xml_serialization
{
    public class CustomSerializer
    {
        public static void SerializeToXML(List<Car> cars, string fileName)
        {
            string outputPath = Path.Combine(Directory.GetCurrentDirectory(), fileName);
            XmlSerializer xmlSerializer = new XmlSerializer(typeof(List<Car>), new XmlRootAttribute("cars"));
            StreamWriter streamWriter = new StreamWriter(outputPath);
            xmlSerializer.Serialize(streamWriter, cars);
            streamWriter.Close();
            Console.WriteLine($"Serialized to: {outputPath}");
        }

        public static List<Car> DeserializeFromXML(string fileName)
        {  
            List<Car> cars = new List<Car>();
            string path = Path.Combine(Directory.GetCurrentDirectory(), fileName);
            XmlSerializer xmlSerializer = new XmlSerializer(typeof(List<Car>), new XmlRootAttribute("cars"));
            FileStream fileStream = new FileStream(path, FileMode.Open);
            cars = (List<Car>) xmlSerializer.Deserialize(fileStream);
            fileStream.Close();
            return cars;
        }
    }
}