using System;
using System.Collections.Generic;
using System.IO;

namespace file_explorer
{
    public class CollectionBuilder
    {
        private string path;
        
        public CollectionBuilder(string path)
        {
            this.path = path;
        }

        public SortedDictionary<string, int> Build()
        {
            SortedDictionary<string, int> files = new SortedDictionary<string, int>(new FileComparer());
            
            foreach (string directory in Directory.GetDirectories(path))
            {
                files.Add(directory, Directory.GetFiles(directory).Length + Directory.GetDirectories(directory).Length);
            }

            foreach (string file in Directory.GetFiles(path))
            {
                files.Add(file, (int)new FileInfo(file).Length);
            }

            return files;
        }
    }
}