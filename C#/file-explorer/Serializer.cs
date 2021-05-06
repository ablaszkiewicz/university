using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace file_explorer
{
    public class Serializer
    {
        public void Serialize(SortedDictionary<string, int> elements)
        {
            FileStream fs = new FileStream("DataFile.dat", FileMode.Create);
            BinaryFormatter formatter = new BinaryFormatter();
            formatter.Serialize(fs, elements);
            fs.Close();
        }

        public SortedDictionary<string, int> Deserialize()
        {
            SortedDictionary<string, int> elements = null;
            FileStream fs = new FileStream("DataFile.dat", FileMode.Open);
            BinaryFormatter formatter = new BinaryFormatter();
            elements = (SortedDictionary<string, int>) formatter.Deserialize(fs);
            fs.Close();
            
            return elements;
        }
    }
}