using System;
using System.IO;

namespace file_explorer
{
    public class RecursiveSearcher
    {
        private string path;
        
        public RecursiveSearcher(string path)
        {
            this.path = path;
        }

        public void Search()
        {
            Search(path);
        }
        private void Search(string searchPath, int depth = 0)
        {
            foreach (string directory in Directory.GetDirectories(searchPath))
            {
                for (int i = 0; i < depth; i++)
                {
                    Console.Write("\t");
                }
                Console.Write(directory.Split('\\')[directory.Split('\\').Length-1] + " ");
                Console.Write($"({new FileInfo(directory).Rahs()}) ");
                Console.WriteLine($"({Directory.GetFiles(directory).Length + Directory.GetDirectories(directory).Length})");
                foreach (string file in Directory.GetFiles(directory))
                {
                    for (int i = 0; i < depth+1; i++)
                    {
                        Console.Write("\t");
                    }
                    Console.Write(file.Split('\\')[file.Split('\\').Length-1] + " ");
                    Console.Write($"({new FileInfo(directory).Rahs()}) ");
                    Console.WriteLine($"{new FileInfo(file).Length}");
                }
                Search(directory, depth+1);
            }
        }
    }
}