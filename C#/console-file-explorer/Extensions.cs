using System;
using System.IO;

namespace file_explorer
{
    static class Extensions
    {
        public static string Rahs(this FileSystemInfo fileSystemInfo)
        {
            string rahs = "";

            FileAttributes fileAttributes = fileSystemInfo.Attributes;

            rahs += (fileAttributes & FileAttributes.ReadOnly) == FileAttributes.ReadOnly ? "r" : "-";
            rahs += (fileAttributes & FileAttributes.Archive) == FileAttributes.Archive ? "a" : "-";
            rahs += (fileAttributes & FileAttributes.Hidden) == FileAttributes.Hidden ? "h" : "-";
            rahs += (fileAttributes & FileAttributes.System) == FileAttributes.System ? "s" : "-";
            
            return rahs;
        }

        public static DateTime OldestDate(this DirectoryInfo directoryInfo, DateTime oldestDate)
        {
            Search(directoryInfo.ToString(), ref oldestDate);
            
            void Search(string path, ref DateTime date)
            {
                foreach (string directory in Directory.GetDirectories(path))
                {
                    if (new DirectoryInfo(directory).CreationTime < oldestDate)
                    {
                        oldestDate = new DirectoryInfo(directory).CreationTime;
                    }
                    foreach (string file in Directory.GetFiles(directory))
                    {
                        if (new FileInfo(file).CreationTime < oldestDate)
                        {
                            oldestDate = new FileInfo(file).CreationTime;
                        }
                    }
                    Search(directory, ref oldestDate);
                }
            }

            return oldestDate;
        }
    }
}