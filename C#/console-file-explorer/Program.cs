using System;
using System.Collections.Generic;
using System.IO;

namespace file_explorer
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine($"\nThe oldest date in this directory is {new DirectoryInfo(args[0]).OldestDate(DateTime.Now)}\n");
            
            RecursiveSearcher recursiveSearcher = new RecursiveSearcher(args[0]);
            recursiveSearcher.Search();

            SortedDictionary<string, int> elements = new CollectionBuilder(args[0]).Build();
            
            Serializer serializer = new Serializer();
            serializer.Serialize(elements);
            SortedDictionary<string, int> elementsDeserialized = serializer.Deserialize();
            
            foreach (KeyValuePair<string, int> pair in elementsDeserialized)
            {
                Console.WriteLine($"{pair.Key.Split('\\')[pair.Key.Split('\\').Length-1]} {pair.Value}");
            }
        }
    }
}